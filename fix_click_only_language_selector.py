#!/usr/bin/env python3
"""
fix_click_only_language_selector.py
Removes mouseover/hover triggers on .lang-switcher so that the language selector
dropdown menu opens ONLY on click (when .open class is toggled), eliminating the discrepancy.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove #nav .lang-switcher:hover .lang-dropdown from CSS
    content = content.replace('#nav .lang-switcher:hover .lang-dropdown,', '')
    content = content.replace('#nav .lang-switcher:hover .lang-dropdown', '')
    content = content.replace('.lang-switcher:hover .lang-dropdown,', '')
    content = content.replace('.lang-switcher:hover .lang-dropdown', '')

    # 2. Update inline style tag in head if present
    old_style = """<style>
#nav .lang-dropdown { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; transform: translateY(-8px) !important; transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important; }
#nav .lang-switcher:hover .lang-dropdown, #nav .lang-switcher.open .lang-dropdown { opacity: 1 !important; visibility: visible !important; pointer-events: auto !important; transform: translateY(0) !important; }
</style>"""

    new_style = """<style>
#nav .lang-dropdown { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; transform: translateY(-8px) !important; transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important; }
#nav .lang-switcher.open .lang-dropdown { opacity: 1 !important; visibility: visible !important; pointer-events: auto !important; transform: translateY(0) !important; }
</style>"""

    if old_style in content:
        content = content.replace(old_style, new_style)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed click-only language dropdown in {os.path.basename(filepath)}")

def main():
    print("=== Updating Language Selector to CLICK-ONLY across all HTML files ===")
    files = glob.glob(os.path.join(BASE, "*.html"))
    for f in files:
        fix_file(f)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
