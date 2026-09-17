#!/usr/bin/env python3
"""
fix_all_unclosed_styles.py
Finds and fixes any unclosed `<style>` tags right before `</head>` across ALL HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content

    # Fix unclosed <style> before </head>
    content = re.sub(r'<style>\s*</head>', '</head>', content)
    content = re.sub(r'<style>\n+</head>', '</head>', content)
    
    # Ensure every <style> has matching </style>
    style_starts = content.count("<style")
    style_ends = content.count("</style>")
    if style_starts > style_ends:
        diff = style_starts - style_ends
        content = content.replace("</head>", ("</style>\n" * diff) + "</head>")

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Fixed unclosed <style> in {os.path.basename(fpath)}")

def main():
    print("=== Fixing Unclosed <style> Tags Across All Pages ===")
    for root, dirs, files in os.walk(BASE):
        if ".next" in root or "node_modules" in root or ".git" in root:
            continue
        for fname in files:
            if fname.endswith(".html"):
                fix_file(os.path.join(root, fname))
    print("=== Done! ===")

if __name__ == "__main__":
    main()
