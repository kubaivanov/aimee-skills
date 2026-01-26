#!/usr/bin/env python3
"""
Check which folders are missing required files (markdown or image).
"""
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTENT_DIR = SCRIPT_DIR.parent.parent.parent
SUPERPOWERS_DIR = CONTENT_DIR / "aimee-skills-description"

def check_folders():
    """Check all folders for required files."""
    if not SUPERPOWERS_DIR.exists():
        print(f"❌ Superpowers directory not found: {SUPERPOWERS_DIR}")
        return
    
    folders = [f for f in SUPERPOWERS_DIR.iterdir() 
               if f.is_dir() and not f.name.startswith('.')]
    
    missing_md = []
    missing_image = []
    complete = []
    
    for folder in sorted(folders):
        md_files = list(folder.glob("*.md"))
        image_path = folder / "image.png"
        
        if not md_files:
            missing_md.append(folder.name)
        elif not image_path.exists():
            missing_image.append(folder.name)
        else:
            complete.append(folder.name)
    
    print(f"📊 File Status Check\n")
    print(f"Total folders: {len(folders)}\n")
    
    if missing_md:
        print(f"❌ Missing markdown files ({len(missing_md)}):")
        for name in missing_md:
            print(f"   - {name}")
        print()
    
    if missing_image:
        print(f"⚠️  Missing image.png ({len(missing_image)}):")
        for name in missing_image:
            print(f"   - {name}")
        print()
    
    print(f"✅ Complete ({len(complete)}):")
    for name in complete[:10]:  # Show first 10
        print(f"   - {name}")
    if len(complete) > 10:
        print(f"   ... and {len(complete) - 10} more")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Complete: {len(complete)}")
    print(f"  Missing markdown: {len(missing_md)}")
    print(f"  Missing image: {len(missing_image)}")

if __name__ == "__main__":
    check_folders()
