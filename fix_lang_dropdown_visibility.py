#!/usr/bin/env python3
"""
fix_lang_dropdown_visibility.py
Fixes the CSS for #nav .lang-dropdown across all HTML files so that it is hidden by default
(opacity: 0; visibility: hidden; pointer-events: none) and only appears when hovered or clicked (.open / :hover).
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

BAD_CSS = """#nav .lang-dropdown {
  position: absolute !important;
  top: calc(100% + 10px) !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E8E4EF !important;
  border-radius: 16px !important;
  padding: 8px !important;
  min-width: 195px !important;
  box-shadow: 0 16px 40px rgba(32,18,56,0.18) !important;
  z-index: 10000 !important;
}"""

GOOD_CSS = """#nav .lang-dropdown {
  position: absolute !important;
  top: calc(100% + 10px) !important;
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
  transform: translateY(-8px) !important;
  transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important;
}
#nav .lang-switcher:hover .lang-dropdown,
#nav .lang-switcher.open .lang-dropdown {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
}"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace bad CSS block if present
    if BAD_CSS in content:
        content = content.replace(BAD_CSS, GOOD_CSS)
    else:
        # Generic regex replace for #nav .lang-dropdown rule
        content = re.sub(
            r'#nav\s+\.lang-dropdown\s*\{([^}]*)\}',
            r'#nav .lang-dropdown {\1; opacity:0 !important; visibility:hidden !important; pointer-events:none !important; transform:translateY(-8px) !important; transition:opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important; }\n#nav .lang-switcher:hover .lang-dropdown, #nav .lang-switcher.open .lang-dropdown { opacity:1 !important; visibility:visible !important; pointer-events:auto !important; transform:translateY(0) !important; }',
            content
        )

    # Add inline override style tag to head just in case
    override_style = """
<style>
#nav .lang-dropdown { opacity: 0 !important; visibility: hidden !important; pointer-events: none !important; transform: translateY(-8px) !important; transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important; }
#nav .lang-switcher:hover .lang-dropdown, #nav .lang-switcher.open .lang-dropdown { opacity: 1 !important; visibility: visible !important; pointer-events: auto !important; transform: translateY(0) !important; }
</style>
"""
    if 'opacity: 0 !important; visibility: hidden !important;' not in content:
        content = content.replace('</head>', override_style + '\n</head>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed lang-dropdown visibility CSS in {os.path.basename(filepath)}")

def main():
    print("=== Fixing #nav .lang-dropdown hover/toggle CSS across all HTML files ===")
    files = glob.glob(os.path.join(BASE, "*.html"))
    for f in files:
        fix_file(f)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
