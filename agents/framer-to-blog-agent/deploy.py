#!/usr/bin/env python3
import os
import sys
import json
import re
from pathlib import Path
import subprocess

# Add scripts directory to path
SCRIPT_DIR = Path(__file__).parent / "scripts"
sys.path.append(str(SCRIPT_DIR))

import generate_image
import github_upload
import markdown as md_lib

def extract_metadata(content, is_markdown=False):
    metadata = {}
    clean_body = content
    
    if is_markdown:
        # Try to extract YAML frontmatter if exists, but don't require it
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            yaml_content = match.group(1)
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip().lower()] = value.strip()
            clean_body = content[match.end():]
        
        # Smart defaults for Markdown
        if not metadata.get('title'):
            # Find first H1
            title_match = re.search(r'^#\s+(.*)', clean_body, re.MULTILINE)
            if title_match:
                metadata['title'] = title_match.group(1).strip()
            else:
                # Fallback to filename
                metadata['title'] = "Článek bez názvu"
        
        if not metadata.get('slug'):
            metadata['slug'] = generate_image.slugify(metadata['title'])
            
        if not metadata.get('category'):
            metadata['category'] = "Business"
            
        if not metadata.get('description'):
            # Take first 200 characters of text (skipping titles)
            text_only = re.sub(r'^#+.*', '', clean_body, flags=re.MULTILINE).strip()
            metadata['description'] = text_only[:200].replace('\n', ' ') + "..."
            
        if not metadata.get('date'):
            from datetime import datetime
            metadata['date'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")
            
        if not metadata.get('featured'):
            metadata['featured'] = 'false'

        return metadata, clean_body
    else:
        # Original HTML logic (keeping for backward compatibility)
        patterns = {
            'title': r'<!--\s*Title:\s*(.*?)\s*-->',
            'slug': r'<!--\s*Slug:\s*(.*?)\s*-->',
            'category': r'<!--\s*Category:\s*(.*?)\s*-->',
            'description': r'<!--\s*Description:\s*(.*?)\s*-->',
            'image_prompt': r'<!--\s*ImagePrompt:\s*(.*?)\s*-->',
            'date': r'<!--\s*Date:\s*(.*?)\s*-->',
            'featured': r'<!--\s*Featured:\s*(.*?)\s*-->'
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                metadata[key] = match.group(1).strip()
        
        # Remove comments from body
        clean_body = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()
        
        return metadata, clean_body

def get_category_id(category_name):
    categories = {
        "Nástroje": "RwPb_GhT4",
        "Tutoriál": "BRGN6RAJs",
        "Case Study": "ViXT0FDf0",
        "Business": "ErKWS9XfT",
        "Etika": "AZtKTmohl",
        "HR": "NdjRdNX15"
    }
    return categories.get(category_name, "ErKWS9XfT") # Default to Business

def run_deployment(article_path):
    article_path = Path(article_path)
    if not article_path.exists():
        print(f"Error: Article {article_path} not found.")
        return

    is_markdown = article_path.suffix.lower() == '.md'
    print(f"Processing article: {article_path.name} ({'Markdown' if is_markdown else 'HTML'})")
    
    with open(article_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    metadata, clean_body = extract_metadata(raw_content, is_markdown)
    
    if is_markdown:
        # Convert body to HTML
        final_html = md_lib.markdown(clean_body)
    else:
        final_html = clean_body

    if not metadata.get('title'):
        print("Error: Article Title not found in metadata.")
        return

    # 1. Generate Image
    image_prompt = metadata.get('image_prompt')
    if not image_prompt:
        # Aibility Master Prompt Template from AIBILITY-BLOG-STYLE.md
        image_prompt = (
            f"A person working with digital tools in a modern office, soft dreamy aesthetic, "
            f"pastel purple and cyan tones, slightly blurred background, professional but warm atmosphere, "
            f"photorealistic style, person seen from side or back, context: {metadata['title']}"
        )
    
    print(f"Generating image for prompt: {image_prompt}")
    # Use a reference image if available (defaulting to 01-lide-ve-startupu.png as it's the primary reference)
    ref_image = Path(__file__).parent / "reference-images" / "01-lide-ve-startupu.png"
    if not ref_image.exists():
        # Fallback to the other one if 01 doesn't exist
        ref_image = Path(__file__).parent / "reference-images" / "02-zena-programuje.png"
    
    # We will try with reference image, but the generate_image script should handle failures
    # or we can pass None if we want to be safe. 
    # Let's try to use 01-lide-ve-startupu.png as it's recommended in the style guide.
    image_data = generate_image.generate_image(image_prompt, reference_image=str(ref_image) if ref_image.exists() else None)
    if not image_data:
        print("Error: Image generation failed.")
        return
    
    image_file = generate_image.save_image(image_data, image_prompt)
    print(f"Image saved to: {image_file}")

    # 2. Upload to GitHub
    print("Uploading image to GitHub...")
    github_url = github_upload.upload_to_github(str(image_file))
    print(f"GitHub URL: {github_url}")

    # 3. Prepare JSON for Framer
    deployment_data = {
        "collectionId": "A7DWNZVX_",
        "slug": metadata.get('slug', generate_image.slugify(metadata['title'])),
        "draft": True,
        "fieldData": {
            "Y5mUV0Wqc": {"type": "string", "value": metadata['title']},
            "BDcsuTyuW": {"type": "boolean", "value": metadata.get('featured', 'false').lower() == 'true'},
            "JQ1tvXCfV": {"type": "image", "value": github_url},
            "UwWgFCEaO": {"type": "date", "value": metadata.get('date', "2026-01-14T00:00:00.000Z")},
            "NdkymNRAq": {"type": "enum", "value": get_category_id(metadata.get('category'))},
            "EArw6OEAr": {"type": "formattedText", "value": final_html},
            "LN_y5s38h": {"type": "string", "value": metadata.get('description', '')}
        }
    }

    output_json = article_path.with_suffix('.json')
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(deployment_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Deployment JSON prepared: {output_json}")
    print("\n--- NEXT STEP FOR CURSOR ---")
    print(f"Please run the 'upsertCMSItem' tool using the data from {output_json.name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./deploy.py <article.html>")
        sys.exit(1)
    
    run_deployment(sys.argv[1])
