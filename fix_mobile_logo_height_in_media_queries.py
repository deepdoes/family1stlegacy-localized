#!/usr/bin/env python3
"""
fix_mobile_logo_height_in_media_queries.py
Replaces old 40px/45px mobile logo rules in media queries across all HTML files with
height: 65px !important and filter: brightness(0) invert(1) !important.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Update .mobile-menu-logo { height: 40px !important; } -> 65px + white filter
    content = re.sub(
        r'\.mobile-menu-logo\s*\{\s*height:\s*\d+px\s*!important;\s*\}',
        '.mobile-menu-logo { height: 65px !important; filter: brightness(0) invert(1) !important; object-fit: contain !important; }',
        content
    )
    
    # Update .mobile-menu-logo { height: 38px; } -> 65px + white filter
    content = re.sub(
        r'\.mobile-menu-logo\s*\{\s*height:\s*38px;\s*\}',
        '.mobile-menu-logo { height: 65px !important; filter: brightness(0) invert(1) !important; object-fit: contain !important; }',
        content
    )

    # Update .nav-logo img { height: 45px !important; width: auto !important; } -> 65px
    content = re.sub(
        r'\.nav-logo\s+img\s*\{\s*height:\s*45px\s*!important;',
        '.nav-logo img { height: 65px !important;',
        content
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Updated mobile logo in {filename}")

def main():
    print("=== Fixing Mobile Logo Height & Filter in Media Queries Across All HTML Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
