#!/usr/bin/env python3
"""
Fix QA format in Superpowers CMS - replace Q:/A: with -q/-a format.
"""
import json
import time
from pathlib import Path
from urllib.parse import urljoin
import requests

# Paths
SCRIPT_DIR = Path(__file__).parent

# Framer MCP
FRAMER_MCP_URL = "https://mcp.unframer.co/sse?id=9b3f53d2ebdb0edfc9c452a48a08e46cd6c90ffbe2d45617a3fe648e05e5e8b9&secret=wfy450OF24dufMIDRDPSqRCq55FJIuzX"
COLLECTION_ID = "TL6Az7H8N"
QA_FIELD_ID = "UOOGkwDUE"

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

def get_cms_items() -> list:
    """Get all CMS items."""
    endpoint = get_framer_endpoint()
    if not endpoint:
        return []
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "getCMSItems",
            "arguments": {
                "collectionId": COLLECTION_ID,
                "limit": 100
            }
        }
    }
    
    try:
        res = requests.post(endpoint, json=payload, timeout=60)
        if res.status_code == 200:
            result = res.json()
            if "result" in result and "content" in result["result"]:
                data = json.loads(result["result"]["content"][0]["text"])
                return data.get("items", [])
        return []
    except Exception as e:
        print(f"❌ Error getting CMS items: {e}")
        return []

def fix_qa_format(qa_text: str) -> tuple:
    """Fix QA format and return (fixed_text, changed)."""
    if not qa_text:
        return qa_text, False
    
    original = qa_text
    
    # Replace Q: with -q (with space after)
    qa_text = qa_text.replace("Q:", "-q")
    
    # Replace A: with -a (with space after)
    qa_text = qa_text.replace("A:", "-a")
    
    changed = (qa_text != original)
    return qa_text, changed

def update_cms_item(item_id: str, qa_text: str) -> bool:
    """Update CMS item with fixed QA text."""
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
                    QA_FIELD_ID: {
                        "type": "string",
                        "value": qa_text
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
    """Fix QA format for all items."""
    print("🚀 Starting QA format fix\n")
    
    # Get all items
    print("📋 Getting CMS items...")
    items = get_cms_items()
    print(f"   Found {len(items)} items\n")
    
    if not items:
        print("❌ Could not get CMS items. Exiting.")
        return
    
    success_count = 0
    skipped_count = 0
    failed_count = 0
    
    for item in items:
        item_id = item.get("id")
        slug = item.get("slug")
        field_data = item.get("fieldData", {})
        
        # Get QA field
        qa_field = field_data.get(QA_FIELD_ID)
        if not qa_field or not qa_field.get("value"):
            print(f"⚠️  {slug} - no QA content, skipping")
            skipped_count += 1
            continue
        
        qa_text = qa_field["value"]
        
        # Check if needs fixing
        if "Q:" not in qa_text and "A:" not in qa_text:
            print(f"✓  {slug} - already in correct format, skipping")
            skipped_count += 1
            continue
        
        print(f"🔧 Processing: {slug}")
        
        # Fix format
        fixed_text, changed = fix_qa_format(qa_text)
        
        if not changed:
            print(f"  ✓ No changes needed")
            skipped_count += 1
            continue
        
        # Update CMS
        print(f"  📝 Updating CMS...")
        if update_cms_item(item_id, fixed_text):
            print(f"  ✅ Updated\n")
            success_count += 1
        else:
            print(f"  ❌ Failed\n")
            failed_count += 1
        
        time.sleep(0.5)
    
    print(f"{'='*60}")
    print(f"✅ Successfully updated: {success_count}")
    print(f"✓  Already correct/skipped: {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
