#!/usr/bin/env python3
"""
Check which CMS items are not processed yet.
"""
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTENT_DIR = SCRIPT_DIR.parent.parent.parent
SUPERPOWERS_DIR = CONTENT_DIR / "aimee-skills-description"
IDS_FILE = SCRIPT_DIR / "item_ids.json"

def get_processed_slugs() -> set:
    """Get all processed slugs from item_ids.json."""
    if not IDS_FILE.exists():
        return set()
    
    with open(IDS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return set(data.keys())

def get_all_folders() -> list:
    """Get all superpower folders."""
    if not SUPERPOWERS_DIR.exists():
        return []
    
    folders = [f for f in SUPERPOWERS_DIR.iterdir() 
               if f.is_dir() and not f.name.startswith('.')]
    return sorted(folders)

def folder_to_slug(folder_name: str) -> str:
    """Convert folder name to slug."""
    return folder_name.replace('_', '-').lower()

def main():
    """Check which items are not processed."""
    processed_slugs = get_processed_slugs()
    folders = get_all_folders()
    
    print(f"📊 CMS Processing Status\n")
    print(f"Total folders: {len(folders)}")
    print(f"Processed items: {len(processed_slugs)}\n")
    
    unprocessed = []
    processed = []
    
    for folder in folders:
        slug = folder_to_slug(folder.name)
        if slug in processed_slugs:
            processed.append(folder.name)
        else:
            unprocessed.append(folder.name)
    
    print(f"✅ Processed ({len(processed)}):")
    for name in processed:
        print(f"   - {name}")
    
    print(f"\n❌ Not processed ({len(unprocessed)}):")
    for name in unprocessed:
        print(f"   - {name}")
    
    return unprocessed

if __name__ == "__main__":
    unprocessed = main()
    print(f"\n{'='*60}")
    print(f"Summary: {len(unprocessed)} items need processing")
