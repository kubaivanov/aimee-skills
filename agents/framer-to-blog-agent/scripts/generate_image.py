#!/usr/bin/env python3
"""
Gemini Image Generator via OpenRouter API
Generate images with text prompts and optional reference images.
"""

import argparse
import base64
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "google/gemini-3-pro-image-preview"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

SCRIPT_DIR = Path(__file__).parent
IMAGES_DIR = SCRIPT_DIR.parent / "images"


def slugify(text: str, max_length: int = 50) -> str:
    """Convert text to a valid filename slug."""
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    slug = slug[:max_length].rstrip('-')
    return slug or "image"


def is_url(path: str) -> bool:
    """Check if the given path is a URL."""
    try:
        result = urlparse(path)
        return result.scheme in ('http', 'https')
    except Exception:
        return False


def load_image_as_base64(path: str) -> Tuple[str, str]:
    """Load an image from URL or local path and return base64 encoded data."""
    if is_url(path):
        response = requests.get(path, timeout=30)
        response.raise_for_status()
        image_data = response.content
        content_type = response.headers.get('content-type', '')
        if 'png' in content_type or path.lower().endswith('.png'):
            media_type = 'image/png'
        elif 'gif' in content_type or path.lower().endswith('.gif'):
            media_type = 'image/gif'
        elif 'webp' in content_type or path.lower().endswith('.webp'):
            media_type = 'image/webp'
        else:
            media_type = 'image/jpeg'
    else:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError(f"Image not found: {path}")
        
        with open(file_path, 'rb') as f:
            image_data = f.read()
        
        ext = file_path.suffix.lower()
        media_types = {
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.webp': 'image/webp',
        }
        media_type = media_types.get(ext, 'image/jpeg')
    
    return base64.b64encode(image_data).decode('utf-8'), media_type


def extract_image_from_response(result: dict, debug: bool = False) -> Optional[bytes]:
    """Extract image data from OpenRouter response format."""
    if debug:
        print("\n=== DEBUG: Full API Response ===")
        print(json.dumps(result, indent=2, default=str)[:4000])
        print("================================\n")
    
    if "choices" not in result or len(result["choices"]) == 0:
        return None
    
    message = result["choices"][0].get("message", {})
    
    # OpenRouter returns images in message["images"] array
    images = message.get("images", [])
    if images:
        for image in images:
            image_url = image.get("image_url", {}).get("url", "")
            if image_url.startswith("data:"):
                _, base64_data = image_url.split(",", 1)
                return base64.b64decode(base64_data)
            elif image_url.startswith("http"):
                resp = requests.get(image_url, timeout=60)
                resp.raise_for_status()
                return resp.content
    
    # Fallback: check content field
    content = message.get("content", "")
    
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict):
                if item.get("type") == "image_url":
                    image_url = item.get("image_url", {}).get("url", "")
                    if image_url.startswith("data:"):
                        _, base64_data = image_url.split(",", 1)
                        return base64.b64decode(base64_data)
    
    elif isinstance(content, str) and content.strip():
        if content.startswith("data:image"):
            _, base64_data = content.split(",", 1)
            return base64.b64decode(base64_data)
        
        match = re.search(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', content)
        if match:
            return base64.b64decode(match.group(1))
    
    return None


def generate_image(prompt: str, reference_image: Optional[str] = None, debug: bool = False) -> Optional[bytes]:
    """Generate an image using Gemini via OpenRouter API."""
    if not OPENROUTER_API_KEY:
        print("Error: OPENROUTER_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
        sys.exit(1)
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/gemini-image-gen",
        "X-Title": "Gemini Image Generator"
    }
    
    content = []
    
    # Add reference image if provided
    if reference_image:
        print(f"Loading reference image: {reference_image}")
        try:
            image_base64, media_type = load_image_as_base64(reference_image)
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{media_type};base64,{image_base64}"
                }
            })
        except Exception as e:
            print(f"Error loading reference image: {e}")
            sys.exit(1)
    
    # Build the prompt
    if reference_image:
        generation_prompt = f"Generate an image based on this reference. Description: {prompt}"
    else:
        generation_prompt = prompt
    
    content.append({
        "type": "text",
        "text": generation_prompt
    })
    
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": content}],
        "modalities": ["image", "text"],
    }
    
    print(f"Generating image with prompt: \"{prompt}\"")
    print(f"Using model: {MODEL}")
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=180)
        if debug:
            print(f"HTTP Status: {response.status_code}")
        response.raise_for_status()
        result = response.json()
        return extract_image_from_response(result, debug=debug)
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text[:1000]}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None


def save_image(image_data: bytes, prompt: str) -> Path:
    """Save image data to the images directory with a prompt-based filename."""
    IMAGES_DIR.mkdir(exist_ok=True)
    
    slug = slugify(prompt)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{slug}_{timestamp}.png"
    
    filepath = IMAGES_DIR / filename
    
    with open(filepath, 'wb') as f:
        f.write(image_data)
    
    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Generate images with Gemini 3 via OpenRouter API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "a sunset over mountains"
  %(prog)s "transform this into anime style" --ref photo.jpg
  %(prog)s "add a dragon to this scene" --ref https://example.com/image.png
  %(prog)s "a cute robot" --debug
        """
    )
    
    parser.add_argument(
        "prompt",
        help="Text description for image generation"
    )
    
    parser.add_argument(
        "--ref", "-r",
        dest="reference",
        help="Reference image (local path or URL)"
    )
    
    parser.add_argument(
        "--output", "-o",
        dest="output",
        help="Custom output path (default: auto-generated in images/)"
    )
    
    parser.add_argument(
        "--debug", "-d",
        action="store_true",
        help="Show debug output including full API response"
    )
    
    args = parser.parse_args()
    
    # Generate the image
    image_data = generate_image(args.prompt, args.reference, debug=args.debug)
    
    if image_data:
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(image_data)
        else:
            output_path = save_image(image_data, args.prompt)
        
        print(f"\n✓ Image saved to: {output_path}")
    else:
        print("\n✗ Failed to generate image")
        sys.exit(1)


if __name__ == "__main__":
    main()
