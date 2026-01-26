#!/usr/bin/env python3
"""
Upload centered images for all superpowers to GitHub and update CMS.
"""
import os
import sys
import json
import time
import shutil
import subprocess
from pathlib import Path
from urllib.parse import urljoin
import requests

# Paths
SCRIPT_DIR = Path(__file__).parent
CONTENT_DIR = SCRIPT_DIR.parent.parent.parent
SUPERPOWERS_DIR = CONTENT_DIR / "aimee-skills-description"
REPO_PATH = CONTENT_DIR / "agents" / "framer-to-blog-agent" / "web-assets-hosting"

# GitHub
REPO_URL = "https://github.com/aibilitycz/web-assets-hosting.git"
RAW_BASE_URL = "https://raw.githubusercontent.com/aibilitycz/web-assets-hosting/main"

# Framer MCP
FRAMER_MCP_URL = "https://mcp.unframer.co/sse?id=9b3f53d2ebdb0edfc9c452a48a08e46cd6c90ffbe2d45617a3fe648e05e5e8b9&secret=wfy450OF24dufMIDRDPSqRCq55FJIuzX"
COLLECTION_ID = "TL6Az7H8N"
CENTERED_IMAGE_FIELD_ID = "dF_Fz0sHM"

def get_framer_endpoint() -> str:
    """Get Framer MCP endpoint URL."""
    try:
        response = requests.get(FRAMER_MCP_URL, stream=True, timeout=10)
        for line in response.iter_lines():
            if not line:
                continue
            line_text = line.decode('utf-8')
            if line_text.startswith("data: "):
                endpoint_url = line_text[6:]
                if not endpoint_url.startswith("http"):
                    endpoint_url = urljoin("https://mcp.unframer.co", endpoint_url)
                return endpoint_url
        return None
    except Exception as e:
        print(f"❌ Error getting Framer endpoint: {e}")
        return None

def get_existing_items() -> dict:
    """Get all existing CMS items and their IDs from local file."""
    ids_file = SCRIPT_DIR / "item_ids.json"
    if ids_file.exists():
        with open(ids_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def ensure_repo() -> bool:
    """Ensure GitHub repo exists locally."""
    if not REPO_PATH.exists():
        print(f"📥 Cloning repository to {REPO_PATH}...")
        try:
            subprocess.run(["git", "clone", REPO_URL, str(REPO_PATH)], check=True)
            print("  ✅ Repository cloned")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error cloning repo: {e}")
            return False
    return True

def upload_image_to_github(image_path: Path, target_filename: str) -> str:
    """Upload image to GitHub and return URL."""
    target_path = REPO_PATH / target_filename
    
    # Copy image to repo
    shutil.copy(image_path, target_path)
    
    # Git operations
    original_cwd = os.getcwd()
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", target_filename], check=True)
        
        # Check if there are changes to commit
        status = subprocess.run(
            ["git", "status", "--porcelain"], 
            capture_output=True, 
            text=True
        ).stdout
        
        if status:
            subprocess.run(
                ["git", "commit", "-m", f"Add centered image {target_filename}"], 
                check=True
            )
            subprocess.run(["git", "push", "origin", "main"], check=True)
        
        return f"{RAW_BASE_URL}/{target_filename}"
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Git error: {e}")
        return None
    finally:
        os.chdir(original_cwd)

def update_cms_item(item_id: str, image_url: str) -> bool:
    """Update CMS item with centered image."""
    endpoint = get_framer_endpoint()
    if not endpoint:
        return False
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "upsertCMSItem",
            "arguments": {
                "collectionId": COLLECTION_ID,
                "itemId": item_id,
                "fieldData": {
                    CENTERED_IMAGE_FIELD_ID: {
                        "type": "image",
                        "value": image_url
                    }
                }
            }
        }
    }
    
    try:
        res = requests.post(endpoint, json=payload, timeout=60)
        if res.status_code in [200, 202]:
            return True
        else:
            print(f"  ❌ HTTP Error: {res.status_code}")
            return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Upload all centered images and update CMS."""
    print("🚀 Starting centered images upload\n")
    
    # Get existing items
    print("📋 Getting existing CMS items...")
    existing_items = get_existing_items()
    print(f"   Found {len(existing_items)} existing items\n")
    
    if not existing_items:
        print("❌ Could not get existing items. Exiting.")
        return
    
    # Ensure GitHub repo
    if not ensure_repo():
        print("❌ Could not set up GitHub repository. Exiting.")
        return
    
    print()
    
    # Find all image-center.png files
    folders = [f for f in SUPERPOWERS_DIR.iterdir() 
               if f.is_dir() and not f.name.startswith('.')]
    
    success_count = 0
    skipped_count = 0
    failed_count = 0
    
    for folder in sorted(folders):
        folder_name = folder.name
        slug = folder_name.replace('_', '-').lower()
        
        # Check if item exists in CMS
        if slug not in existing_items:
            print(f"⚠️  {slug} not found in CMS, skipping")
            skipped_count += 1
            continue
        
        # Check if centered image exists
        center_image = folder / "image-center.png"
        if not center_image.exists():
            print(f"⚠️  {slug} - no centered image found, skipping")
            skipped_count += 1
            continue
        
        item_id = existing_items[slug]
        print(f"🖼️  Processing: {slug}")
        
        # Upload to GitHub
        github_filename = f"superpower-{folder_name}-center.png"
        print(f"   📤 Uploading to GitHub as {github_filename}...")
        image_url = upload_image_to_github(center_image, github_filename)
        
        if not image_url:
            print(f"   ❌ Failed to upload to GitHub")
            failed_count += 1
            continue
        
        print(f"   ✅ Uploaded: {image_url}")
        
        # Update CMS
        print(f"   📝 Updating CMS...")
        if update_cms_item(item_id, image_url):
            print(f"   ✅ CMS updated\n")
            success_count += 1
        else:
            print(f"   ❌ Failed to update CMS\n")
            failed_count += 1
        
        time.sleep(0.5)
    
    print(f"{'='*60}")
    print(f"✅ Successfully updated: {success_count}")
    print(f"⚠️  Skipped: {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
