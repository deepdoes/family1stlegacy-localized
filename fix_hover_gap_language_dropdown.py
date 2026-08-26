#!/usr/bin/env python3
"""
fix_hover_gap_language_dropdown.py
Enables mouseover (hover) opening for the language selector dropdown,
AND adds an invisible bridge pseudo-element (::before) to eliminate the gap so the dropdown
never disappears when moving the mouse downward to select a language.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

GOOD_HOVER_CSS = """<style id="lang-dropdown-hover-fix">
/* ─── Language Selector Hover + Gap Bridge Fix ─── */
#nav .lang-switcher {
  position: relative !important;
  display: inline-flex !important;
  align-items: center !important;
  padding-bottom: 8px !important; /* Invisible hover buffer */
  margin-bottom: -8px !important;
}

#nav .lang-dropdown {
  position: absolute !important;
  top: 100% !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E8E4EF !important;
  border-radius: 16px !important;
  padding: 8px !important;
  min-width: 195px !important;
  box-shadow: 0 16px 40px rgba(32,18,56,0.18) !important;
  z-index: 10000 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translateY(-4px) !important;
  transition: opacity 0.22s ease, transform 0.22s ease, visibility 0.22s ease !important;
}

/* Invisible bridge so moving cursor downwards keeps hover active */
#nav .lang-dropdown::before {
  content: '' !important;
  position: absolute !important;
  top: -14px !important;
  left: 0 !important;
  right: 0 !important;
  height: 14px !important;
  background: transparent !important;
}

/* Show menu on mouseover / hover AND on click (.open) */
#nav .lang-switcher:hover .lang-dropdown,
#nav .lang-switcher.open .lang-dropdown,
#nav .lang-dropdown:hover {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
}
</style>"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove old style tag if previously inserted
    content = re.sub(r'<style id="lang-dropdown-hover-fix">.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>\s*#nav \.lang-dropdown \{ opacity: 0 !important;.*?</style>', '', content, flags=re.DOTALL)

    # Insert updated style block in head
    content = content.replace('</head>', GOOD_HOVER_CSS + '\n</head>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed hover & gap bridge in {os.path.basename(filepath)}")

def main():
    print("=== Fixing Language Dropdown Hover & Gap Bridge across all HTML files ===")
    files = glob.glob(os.path.join(BASE, "*.html"))
    for f in files:
        fix_file(f)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
