#!/usr/bin/env python3
"""
sync_public_folder_for_deployment.py
Copies all updated root .html files into public/ and copies v1/ into public/v1/
so that Vercel serves:
1. Main updated site: domain.com/index.html, domain.com/education_planning.html, etc.
2. Previous V1 site: domain.com/v1/index.html, domain.com/v1/education_planning.html, etc.
"""

import os
import shutil

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
PUBLIC_DIR = os.path.join(BASE, "public")
PUBLIC_V1_DIR = os.path.join(PUBLIC_DIR, "v1")

def sync():
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    os.makedirs(PUBLIC_V1_DIR, exist_ok=True)

    # 1. Copy all root .html files into public/
    root_html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in root_html_files:
        src = os.path.join(BASE, fname)
        dst = os.path.join(PUBLIC_DIR, fname)
        shutil.copy2(src, dst)
    print(f"  ✓ Synced {len(root_html_files)} main HTML files into public/")

    # 2. Copy all v1 .html files into public/v1/
    v1_src_dir = os.path.join(BASE, "v1")
    v1_html_files = [f for f in os.listdir(v1_src_dir) if f.endswith(".html")]
    for fname in v1_html_files:
        src = os.path.join(v1_src_dir, fname)
        dst = os.path.join(PUBLIC_V1_DIR, fname)
        shutil.copy2(src, dst)
    print(f"  ✓ Synced {len(v1_html_files)} V1 HTML files into public/v1/")

    # 3. Ensure images directory is inside public/v1/ images as well if needed
    src_img = os.path.join(BASE, "images")
    dst_img = os.path.join(PUBLIC_DIR, "images")
    if os.path.exists(src_img) and not os.path.exists(dst_img):
        shutil.copytree(src_img, dst_img)

if __name__ == "__main__":
    print("=== Syncing public/ and public/v1/ for Vercel Deployment ===")
    sync()
    print("=== Done! ===")
