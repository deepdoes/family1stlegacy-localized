#!/usr/bin/env python3
"""
fix_language_selector_tabs.py
Removes the redundant cycling language modal button (.nav-lang) across all HTML files
so that ONLY the clean dropdown pill (.lang-switcher / "ES v") remains.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove <li> containing .nav-lang
    content = re.sub(r'<li>\s*<a [^>]*class="[^"]*nav-lang[^"]*"[^>]*>.*?</a>\s*</li>', '', content, flags=re.DOTALL)
    # Also remove standalone <a class="nav-lang..."> if not in <li>
    content = re.sub(r'<a [^>]*class="[^"]*nav-lang[^"]*"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

    # 2. Add CSS rule to force hide .nav-lang
    if '.nav-lang { display: none !important; }' not in content:
        content = content.replace('</head>', '<style>.nav-lang { display: none !important; }</style>\n</head>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed language selector on {os.path.basename(filepath)}")

def main():
    print("=== Removing redundant language selector tabs across all HTML files ===")
    files = glob.glob(os.path.join(BASE, "*.html"))
    for f in files:
        fix_file(f)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
