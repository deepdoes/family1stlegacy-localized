#!/usr/bin/env python3
"""
organize_v1_folder.py
Creates a clean dedicated /v1 folder in the project root and populates it with
a full standalone copy of all original static HTML pages and assets.
This allows browsing the V1 site smoothly at http://localhost:8080/v1/
with all internal links intact. Also cleans up loose *_v1.html files from root.
"""

import os
import shutil
import glob

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
V1_DIR = os.path.join(BASE, "v1")

def main():
    print("=== Creating Clean /v1 Subdirectory ===")
    os.makedirs(V1_DIR, exist_ok=True)

    # Copy all HTML files to /v1
    html_files = glob.glob(os.path.join(BASE, "*.html"))
    for fpath in html_files:
        fname = os.path.basename(fpath)
        if not fname.endswith("_v1.html"):
            dst = os.path.join(V1_DIR, fname)
            shutil.copy2(fpath, dst)

    # Copy images folder to /v1/images
    images_src = os.path.join(BASE, "images")
    images_dst = os.path.join(V1_DIR, "images")
    if os.path.exists(images_src):
        if os.path.exists(images_dst):
            shutil.rmtree(images_dst)
        shutil.copytree(images_src, images_dst)

    # Clean up loose *_v1.html files from root
    loose_v1 = glob.glob(os.path.join(BASE, "*_v1.html"))
    for f in loose_v1:
        os.remove(f)
        print(f"  ✓ Cleaned up loose root file: {os.path.basename(f)}")

    print("  ✓ Full V1 site organized in /v1 directory!")
    print("=== Done! ===")

if __name__ == "__main__":
    main()
