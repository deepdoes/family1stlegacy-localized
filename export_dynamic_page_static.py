#!/usr/bin/env python3
"""
export_dynamic_page_static.py
Creates public/dynamic.html and public/dynamic/index.html so Vercel's static asset server
serves the dynamic Next.js React page on https://family1stlegacy.com/dynamic without 404.
"""

import os
import shutil

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
PUBLIC_DIR = os.path.join(BASE, "public")
PUBLIC_DYNAMIC_DIR = os.path.join(PUBLIC_DIR, "dynamic")

def export_dynamic():
    os.makedirs(PUBLIC_DYNAMIC_DIR, exist_ok=True)

    # Copy rendered Next.js HTML or create public/dynamic/index.html
    next_server_app = os.path.join(BASE, ".next", "server", "app")
    dynamic_rendered_html = os.path.join(next_server_app, "dynamic.html")

    target_html = os.path.join(PUBLIC_DYNAMIC_DIR, "index.html")
    target_root_dynamic = os.path.join(PUBLIC_DIR, "dynamic.html")

    if os.path.exists(dynamic_rendered_html):
        shutil.copy2(dynamic_rendered_html, target_html)
        shutil.copy2(dynamic_rendered_html, target_root_dynamic)
        print("  ✓ Exported Next.js compiled dynamic.html to public/dynamic/index.html & public/dynamic.html")
    else:
        print("  ⚠ Compiled dynamic.html not found in .next/server/app")

if __name__ == "__main__":
    print("=== Exporting Dynamic Route to Public Directory for Vercel Static Serving ===")
    export_dynamic()
    print("=== Done! ===")
