#!/usr/bin/env python3
"""
Process all superpowers from aimee-skills-description and upload to Framer CMS.
"""
import os
import sys
import re
import json
import subprocess
import shutil
import time
from pathlib import Path
from urllib.parse import urljoin
import requests
import markdown

# Paths
SCRIPT_DIR = Path(__file__).parent
CONTENT_DIR = SCRIPT_DIR.parent.parent.parent  # Go up to "Aibility Content"
SUPERPOWERS_DIR = CONTENT_DIR / "aimee-skills-description"
FRAMER_AGENT_DIR = CONTENT_DIR / "agents" / "framer-to-blog-agent"
REPO_PATH = FRAMER_AGENT_DIR / "web-assets-hosting"
REPO_URL = "https://github.com/aibilitycz/web-assets-hosting.git"
RAW_BASE_URL = "https://raw.githubusercontent.com/aibilitycz/web-assets-hosting/main"
IDS_FILE = SCRIPT_DIR / "item_ids.json"

# Framer MCP
FRAMER_MCP_URL = "https://mcp.unframer.co/sse?id=9b3f53d2ebdb0edfc9c452a48a08e46cd6c90ffbe2d45617a3fe648e05e5e8b9&secret=wfy450OF24dufMIDRDPSqRCq55FJIuzX"
COLLECTION_ID = "TL6Az7H8N"

# Field IDs
FIELD_IDS = {
    "background_image": "efZuAZ_c3",
    "title": "jtPj6Nc64",
    "description": "h8htm_KbK",
    "content": "xVDmxEEkn",
    "cta_vpravo": "I1CXmhJ0u",
    "cta_headline_dolu": "Ebf3o42yN",
    "qa_content": "CeGDUIWQ7",
    "qa_headline": "ep9cARdMx",
    "description_cta_dolu": "KpOorLlkM",
    "cta_button_dolu": "BJqJPmFwM"
}

def upload_image_to_github(image_path: Path, unique_name: str) -> str:
    """Upload image to GitHub with unique name."""
    if not image_path.exists():
        print(f"⚠️  Image not found: {image_path}")
        return None
    
    # Ensure repo exists
    if not REPO_PATH.exists():
        print(f"Cloning repository to {REPO_PATH}...")
        subprocess.run(["git", "clone", REPO_URL, str(REPO_PATH)], check=True)
    
    # Copy with unique name
    target_path = REPO_PATH / unique_name
    shutil.copy(image_path, target_path)
    
    # Git operations
    original_cwd = os.getcwd()
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", unique_name], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
        if status:
            subprocess.run(["git", "commit", "-m", f"Add superpower image {unique_name}"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"  ✓ Uploaded image: {unique_name}")
        else:
            print(f"  ✓ Image already exists: {unique_name}")
        
        return f"{RAW_BASE_URL}/{unique_name}"
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Error uploading image: {e}")
        return None
    finally:
        os.chdir(original_cwd)

def parse_markdown(content: str) -> dict:
    """Parse superpower markdown into structured data."""
    result = {
        "title": "",
        "description": "",
        "content": "",
        "cta_vpravo": "",
        "cta_headline_dolu": "",
        "qa_content": "",
        "qa_headline": "",
        "description_cta_dolu": "",
        "cta_button_dolu": ""
    }
    
    # Extract title (H1)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        result["title"] = title_match.group(1).strip()
    
    # Split by FAQ section
    faq_match = re.search(r'^#\s+Často kladené otázky.*?\n', content, re.MULTILINE)
    if faq_match:
        main_content = content[:faq_match.start()]
        faq_content = content[faq_match.end():]
    else:
        main_content = content
        faq_content = ""
    
    # Extract description (intro paragraphs before first ***)
    desc_end = re.search(r'^\*\*\*', main_content, re.MULTILINE)
    if desc_end:
        desc_text = main_content[:desc_end.start()].strip()
        # Remove title if present
        desc_text = re.sub(r'^#\s+.*?\n', '', desc_text, flags=re.MULTILINE)
        # Remove CTA links from description
        desc_text = re.sub(r'\[[^\]]+→\s*\]', '', desc_text)
        desc_text = re.sub(r'\n{3,}', '\n\n', desc_text)
        result["description"] = desc_text.strip()
    
    # Extract CTA vpravo (first [CTA →] link after first ***)
    cta_match = re.search(r'\[([^\]]+→)\s*\]', main_content)
    if cta_match:
        result["cta_vpravo"] = cta_match.group(1).strip()
    
    # Extract main content (from second *** to "Naučte se" section)
    # Find all *** separators
    separators = list(re.finditer(r'^\*\*\*', main_content, re.MULTILINE))
    if len(separators) >= 2:
        # Content starts after second ***
        content_start = separators[1].end()
        # Find "Naučte se" section
        nauc_se_match = re.search(r'^\*\*\*\s*\n\s*##\s+Naučte se', main_content[content_start:], re.MULTILINE)
        if nauc_se_match:
            content_end = content_start + nauc_se_match.start()
            main_body = main_content[content_start:content_end].strip()
        else:
            # No "Naučte se" section, take everything
            main_body = main_content[content_start:].strip()
        
        # Remove CTA links from content
        main_body = re.sub(r'^\s*\[[^\]]+→\s*\]\s*$', '', main_body, flags=re.MULTILINE)
        main_body = re.sub(r'\[[^\]]+→\s*\]', '', main_body)
        main_body = re.sub(r'\n{3,}', '\n\n', main_body)
        result["content"] = main_body.strip()
    
    # Extract CTA headline dolu ("Naučte se... s Aimee")
    cta_headline_match = re.search(r'##\s+(Naučte se[^\n]+)', main_content)
    if cta_headline_match:
        result["cta_headline_dolu"] = cta_headline_match.group(1).strip()
    
    # Extract Description CTA dolu (paragraph after "Naučte se... s Aimee" heading)
    cta_section_match = re.search(r'##\s+Naučte se[^\n]+\n\n(.+?)(?:\n\n\[|\n\*\*\*)', main_content, re.DOTALL)
    if cta_section_match:
        result["description_cta_dolu"] = cta_section_match.group(1).strip()
    
    # Extract CTA button dolu (last [CTA →] link in main content)
    cta_buttons = re.findall(r'\[([^\]]+→)\s*\]', main_content)
    if len(cta_buttons) > 1:
        result["cta_button_dolu"] = cta_buttons[-1].strip()
    elif len(cta_buttons) == 1:
        # If only one, it might be the bottom one
        result["cta_button_dolu"] = cta_buttons[0].strip()
    
    # Parse FAQ
    if faq_content:
        result["qa_headline"] = "Často kladené otázky (FAQ)"
        # Convert FAQ format (-q and -a) to HTML
        faq_html = []
        current_q = None
        current_a = None
        
        for line in faq_content.split('\n'):
            line = line.strip()
            if line.startswith('-q'):
                # Save previous Q&A if exists
                if current_q and current_a:
                    faq_html.append(f"<p><strong>{current_q}</strong></p>")
                    faq_html.append(f"<p>{current_a}</p>")
                current_q = line[3:].strip()
                current_a = None
            elif line.startswith('-a'):
                current_a = line[3:].strip()
            elif current_a and line:
                # Continue answer on next line
                current_a += " " + line
            # Empty lines are ignored, continue collecting answer
        
        # Add last Q&A
        if current_q:
            faq_html.append(f"<p><strong>{current_q}</strong></p>")
            if current_a:
                faq_html.append(f"<p>{current_a}</p>")
        
        result["qa_content"] = "\n".join(faq_html)
    
    return result

def remove_cta_links(text: str) -> str:
    """Remove CTA links like [Naučte se... →] from text."""
    # Remove lines that are only CTA links
    text = re.sub(r'^\s*\[[^\]]+→\s*\]\s*$', '', text, flags=re.MULTILINE)
    # Remove inline CTA links
    text = re.sub(r'\[[^\]]+→\s*\]', '', text)
    # Clean up multiple empty lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def markdown_to_html(md_text: str) -> str:
    """Convert markdown to HTML."""
    if not md_text.strip():
        return ""
    
    # Remove CTA links from text before converting
    md_text = remove_cta_links(md_text)
    
    # Convert markdown
    html = markdown.markdown(md_text, extensions=['extra', 'nl2br'])
    
    # Clean up separators (***)
    html = re.sub(r'<hr\s*/?>', '', html)
    
    # Clean up empty paragraphs
    html = re.sub(r'<p>\s*</p>', '', html)
    
    return html

def create_cms_item(slug: str, parsed_data: dict, image_url: str) -> dict:
    """Create CMS item fieldData structure."""
    field_data = {}
    
    if image_url:
        field_data[FIELD_IDS["background_image"]] = {"type": "image", "value": image_url}
    
    if parsed_data["title"]:
        field_data[FIELD_IDS["title"]] = {"type": "string", "value": parsed_data["title"]}
    
    if parsed_data["description"]:
        desc_html = markdown_to_html(parsed_data["description"])
        field_data[FIELD_IDS["description"]] = {"type": "formattedText", "value": desc_html}
    
    if parsed_data["content"]:
        content_html = markdown_to_html(parsed_data["content"])
        field_data[FIELD_IDS["content"]] = {"type": "formattedText", "value": content_html}
    
    if parsed_data["cta_vpravo"]:
        field_data[FIELD_IDS["cta_vpravo"]] = {"type": "string", "value": parsed_data["cta_vpravo"]}
    
    if parsed_data["cta_headline_dolu"]:
        field_data[FIELD_IDS["cta_headline_dolu"]] = {"type": "string", "value": parsed_data["cta_headline_dolu"]}
    
    if parsed_data["qa_content"]:
        field_data[FIELD_IDS["qa_content"]] = {"type": "formattedText", "value": parsed_data["qa_content"]}
    
    if parsed_data["qa_headline"]:
        field_data[FIELD_IDS["qa_headline"]] = {"type": "string", "value": parsed_data["qa_headline"]}
    
    if parsed_data["description_cta_dolu"]:
        field_data[FIELD_IDS["description_cta_dolu"]] = {"type": "string", "value": parsed_data["description_cta_dolu"]}
    
    if parsed_data["cta_button_dolu"]:
        field_data[FIELD_IDS["cta_button_dolu"]] = {"type": "string", "value": parsed_data["cta_button_dolu"]}
    
    return {
        "collectionId": COLLECTION_ID,
        "slug": slug,
        "draft": True,
        "fieldData": field_data
    }

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

def load_item_ids() -> dict:
    """Load existing item IDs from file."""
    if IDS_FILE.exists():
        with open(IDS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_item_ids(item_ids: dict):
    """Save item IDs to file."""
    with open(IDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(item_ids, f, indent=2, ensure_ascii=False)

def upsert_to_framer(cms_data: dict, retry_count: int = 0):
    """Upload CMS item to Framer."""
    # Get fresh endpoint for each request
    endpoint = get_framer_endpoint()
    if not endpoint:
        if retry_count < 2:
            time.sleep(1)
            return upsert_to_framer(cms_data, retry_count + 1)
        print(f"  ❌ Could not get Framer endpoint after retries")
        return False
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "upsertCMSItem",
            "arguments": cms_data
        }
    }
    
    try:
        res = requests.post(endpoint, json=payload, timeout=60)
        response_text = res.text
        
        if res.status_code == 200:
            result = res.json()
            if "error" in result:
                print(f"  ❌ MCP Error: {json.dumps(result['error'], indent=2, ensure_ascii=False)}")
                return False
            if "result" in result:
                item_id = result.get('result', {}).get('item', {}).get('id', 'unknown')
                slug = result.get('result', {}).get('item', {}).get('slug', 'unknown')
                print(f"  ✅ Created: {slug} (ID: {item_id})")
                return True, item_id
            # If no result but no error, might still be OK
            print(f"  ⚠️  Response OK but no result field")
            return True, None
        elif res.status_code == 202:
            # 202 Accepted - might be async, but we'll assume success
            print(f"  ✅ Accepted for processing (202)")
            return True, None
        else:
            print(f"  ❌ HTTP Error: {res.status_code}")
            print(f"  Response: {response_text[:500]}")
            return False, None
    except Exception as e:
        print(f"  ❌ Exception: {e}")
        import traceback
        traceback.print_exc()
        return False, None

def process_superpower(folder_path: Path):
    """Process a single superpower folder."""
    folder_name = folder_path.name
    print(f"\n📦 Processing: {folder_name}")
    
    # Find markdown file
    md_files = list(folder_path.glob("*.md"))
    if not md_files:
        print(f"  ⚠️  No markdown file found")
        return False
    
    md_file = md_files[0]
    
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse content
    parsed = parse_markdown(content)
    
    if not parsed["title"]:
        print(f"  ⚠️  No title found")
        return False
    
    # Upload image
    image_path = folder_path / "image.png"
    image_url = None
    if image_path.exists():
        unique_name = f"superpower-{folder_name}.png"
        image_url = upload_image_to_github(image_path, unique_name)
    
    # Create slug from folder name
    slug = folder_name.replace('_', '-').lower()
    
    # Create CMS data
    cms_data = create_cms_item(slug, parsed, image_url)
    
    # Upload to Framer
    print(f"  📤 Uploading to Framer...")
    success, item_id = upsert_to_framer(cms_data)
    
    # Small delay to avoid rate limiting
    time.sleep(0.5)
    
    if success:
        print(f"  ✅ Successfully created: {slug}")
        return True, item_id
    else:
        print(f"  ❌ Failed to create: {slug}")
        return False, None

def main():
    """Process all superpowers."""
    if not SUPERPOWERS_DIR.exists():
        print(f"❌ Superpowers directory not found: {SUPERPOWERS_DIR}")
        sys.exit(1)
    
    # Load existing item IDs
    item_ids = load_item_ids()
    print(f"📋 Loaded {len(item_ids)} existing items from item_ids.json\n")
    
    # Get all folders (skip files and .DS_Store)
    all_folders = [f for f in SUPERPOWERS_DIR.iterdir() 
                   if f.is_dir() and not f.name.startswith('.')]
    
    # Filter to only unprocessed folders
    unprocessed_folders = []
    for folder in sorted(all_folders):
        slug = folder.name.replace('_', '-').lower()
        if slug not in item_ids:
            unprocessed_folders.append(folder)
        else:
            print(f"⏭️  Skipping {folder.name} (already processed)")
    
    if not unprocessed_folders:
        print(f"\n✅ All items are already processed!")
        return
    
    print(f"\n🚀 Found {len(unprocessed_folders)} unprocessed superpowers to process\n")
    
    success_count = 0
    failed = []
    
    for folder in unprocessed_folders:
        success, item_id = process_superpower(folder)
        if success:
            success_count += 1
            # Save item ID if we got one
            if item_id:
                slug = folder.name.replace('_', '-').lower()
                item_ids[slug] = item_id
                save_item_ids(item_ids)
        else:
            failed.append(folder.name)
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully processed: {success_count}/{len(unprocessed_folders)}")
    if failed:
        print(f"❌ Failed: {len(failed)}")
        for name in failed:
            print(f"   - {name}")

if __name__ == "__main__":
    main()
