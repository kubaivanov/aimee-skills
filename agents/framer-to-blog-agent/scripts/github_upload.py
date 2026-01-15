#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_PATH = SCRIPT_DIR.parent / "web-assets-hosting"
REPO_URL = "https://github.com/aibilitycz/web-assets-hosting.git"
RAW_BASE_URL = "https://raw.githubusercontent.com/aibilitycz/web-assets-hosting/main"

def upload_to_github(image_path: str) -> str:
    image_path = Path(image_path)
    if not image_path.exists():
        print(f"Error: Image {image_path} not found.")
        sys.exit(1)

    filename = image_path.name
    target_path = REPO_PATH / filename

    # Ensure repo exists
    if not REPO_PATH.exists():
        print(f"Cloning repository to {REPO_PATH}...")
        subprocess.run(["git", "clone", REPO_URL, str(REPO_PATH)], check=True)

    # Copy image to repo
    import shutil
    shutil.copy(image_path, target_path)

    # Git operations
    original_cwd = os.getcwd()
    try:
        os.chdir(REPO_PATH)
        subprocess.run(["git", "add", filename], check=True)
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
        if status:
            subprocess.run(["git", "commit", "-m", f"Add blog image {filename}"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print(f"Successfully pushed {filename} to GitHub.")
        else:
            print(f"File {filename} already exists on GitHub with no changes.")
        
        return f"{RAW_BASE_URL}/{filename}"
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operations: {e}")
        sys.exit(1)
    finally:
        os.chdir(original_cwd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: github_upload.py <image_path>")
        sys.exit(1)
    
    url = upload_to_github(sys.argv[1])
    print(f"URL: {url}")
