#!/usr/bin/env python3
"""
Update existing superpowers in Framer CMS with fixed content (no CTAs in text).
"""
import os
import sys
import re
import json
import time
from pathlib import Path
from urllib.parse import urljoin
import requests
import markdown

# Paths
SCRIPT_DIR = Path(__file__).parent
CONTENT_DIR = SCRIPT_DIR.parent.parent.parent  # Go up to "Aibility Content"
SUPERPOWERS_DIR = CONTENT_DIR / "aimee-skills-description"

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

RAW_BASE_URL = "https://raw.githubusercontent.com/aibilitycz/web-assets-hosting/main"

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
    
    # Extract CTA vpravo (first [CTA →] link) - remove arrow
    cta_match = re.search(r'\[([^\]]+?)→?\s*\]', main_content)
    if cta_match:
        cta_text = cta_match.group(1).strip().rstrip('→').strip()
        result["cta_vpravo"] = cta_text
    
    # Extract main content (from second *** to "Naučte se" section)
    separators = list(re.finditer(r'^\*\*\*', main_content, re.MULTILINE))
    if len(separators) >= 2:
        content_start = separators[1].end()
        nauc_se_match = re.search(r'^\*\*\*\s*\n\s*##\s+Naučte se', main_content[content_start:], re.MULTILINE)
        if nauc_se_match:
            content_end = content_start + nauc_se_match.start()
            main_body = main_content[content_start:content_end].strip()
        else:
            main_body = main_content[content_start:].strip()
        
        # Remove CTA links from content
        main_body = re.sub(r'^\s*\[[^\]]+→\s*\]\s*$', '', main_body, flags=re.MULTILINE)
        main_body = re.sub(r'\[[^\]]+→\s*\]', '', main_body)
        main_body = re.sub(r'\n{3,}', '\n\n', main_body)
        result["content"] = main_body.strip()
    
    # Extract CTA headline dolu
    cta_headline_match = re.search(r'##\s+(Naučte se[^\n]+)', main_content)
    if cta_headline_match:
        result["cta_headline_dolu"] = cta_headline_match.group(1).strip()
    
    # Extract Description CTA dolu
    cta_section_match = re.search(r'##\s+Naučte se[^\n]+\n\n(.+?)(?:\n\n\[|\n\*\*\*)', main_content, re.DOTALL)
    if cta_section_match:
        result["description_cta_dolu"] = cta_section_match.group(1).strip()
    
    # Extract CTA button dolu (last [CTA →] link) - remove arrow
    cta_buttons = re.findall(r'\[([^\]]+?)→?\s*\]', main_content)
    if len(cta_buttons) > 1:
        cta_text = cta_buttons[-1].strip().rstrip('→').strip()
        result["cta_button_dolu"] = cta_text
    elif len(cta_buttons) == 1:
        cta_text = cta_buttons[0].strip().rstrip('→').strip()
        result["cta_button_dolu"] = cta_text
    
    # Parse FAQ
    if faq_content:
        result["qa_headline"] = "Často kladené otázky (FAQ)"
        faq_html = []
        current_q = None
        current_a = None
        
        for line in faq_content.split('\n'):
            line = line.strip()
            if line.startswith('-q'):
                if current_q and current_a:
                    faq_html.append(f"<p><strong>{current_q}</strong></p>")
                    faq_html.append(f"<p>{current_a}</p>")
                current_q = line[3:].strip()
                current_a = None
            elif line.startswith('-a'):
                current_a = line[3:].strip()
            elif current_a and line:
                current_a += " " + line
        
        if current_q:
            faq_html.append(f"<p><strong>{current_q}</strong></p>")
            if current_a:
                faq_html.append(f"<p>{current_a}</p>")
        
        result["qa_content"] = "\n".join(faq_html)
    
    return result

def remove_cta_links(text: str) -> str:
    """Remove CTA links from text."""
    text = re.sub(r'^\s*\[[^\]]+→\s*\]\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\[[^\]]+→\s*\]', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def markdown_to_html(md_text: str) -> str:
    """Convert markdown to HTML."""
    if not md_text.strip():
        return ""
    
    md_text = remove_cta_links(md_text)
    html = markdown.markdown(md_text, extensions=['extra', 'nl2br'])
    html = re.sub(r'<hr\s*/?>', '', html)
    html = re.sub(r'<p>\s*</p>', '', html)
    return html

def update_cms_item(item_id: str, parsed_data: dict, image_url: str) -> dict:
    """Create update fieldData structure."""
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
        "itemId": item_id,
        "fieldData": field_data
    }

def upsert_to_framer(cms_data: dict) -> bool:
    """Upload CMS item to Framer."""
    endpoint = get_framer_endpoint()
    if not endpoint:
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
        if res.status_code in [200, 202]:
            return True
        else:
            print(f"  ❌ HTTP Error: {res.status_code}")
            return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    """Update all superpowers."""
    print("🔍 Getting existing CMS items...")
    existing_items = get_existing_items()
    print(f"   Found {len(existing_items)} existing items")
    
    if not existing_items:
        print("❌ Could not get existing items. Exiting.")
        return
    
    folders = [f for f in SUPERPOWERS_DIR.iterdir() 
               if f.is_dir() and not f.name.startswith('.')]
    
    print(f"\n🚀 Processing {len(folders)} superpowers\n")
    
    success_count = 0
    
    for folder in sorted(folders):
        folder_name = folder.name
        slug = folder_name.replace('_', '-').lower()
        
        if slug not in existing_items:
            print(f"⚠️  {slug} not found in CMS, skipping")
            continue
        
        item_id = existing_items[slug]
        print(f"📦 Updating: {slug} (ID: {item_id})")
        
        # Find markdown file
        md_files = list(folder.glob("*.md"))
        if not md_files:
            print(f"  ⚠️  No markdown file found")
            continue
        
        # Read and parse
        with open(md_files[0], 'r', encoding='utf-8') as f:
            content = f.read()
        
        parsed = parse_markdown(content)
        
        # Get image URL
        image_url = f"{RAW_BASE_URL}/superpower-{folder_name}.png"
        
        # Create update data
        cms_data = update_cms_item(item_id, parsed, image_url)
        
        # Upload
        if upsert_to_framer(cms_data):
            print(f"  ✅ Updated")
            success_count += 1
        else:
            print(f"  ❌ Failed")
        
        time.sleep(0.5)
    
    print(f"\n{'='*60}")
    print(f"✅ Successfully updated: {success_count}/{len(folders)}")

if __name__ == "__main__":
    main()
