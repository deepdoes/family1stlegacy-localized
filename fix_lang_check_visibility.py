#!/usr/bin/env python3
"""
fix_lang_check_visibility.py
Ensures that the checkmark (✓) in the language dropdown menu is ONLY displayed
on the active selected language link (.active .lang-check), hiding it on inactive languages.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

GOOD_LANG_CHECK_CSS = """<style id="lang-check-active-fix">
/* ─── Show Checkmark ONLY on Active Language ─── */
#nav .lang-dropdown a .lang-check,
.lang-dropdown a .lang-check {
  display: none !important;
  margin-left: auto !important;
  font-size: 13px !important;
  color: #4A2D7A !important;
}
#nav .lang-dropdown a.active .lang-check,
.lang-dropdown a.active .lang-check {
  display: inline-block !important;
}
</style>"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove old style tag if previously inserted
    content = re.sub(r'<style id="lang-check-active-fix">.*?</style>', '', content, flags=re.DOTALL)

    # Insert updated style block in head
    content = content.replace('</head>', GOOD_LANG_CHECK_CSS + '\n</head>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Fixed lang-check active checkmark visibility in {os.path.basename(filepath)}")

def main():
    print("=== Fixing Language Dropdown Checkmark Visibility across all HTML files ===")
    files = glob.glob(os.path.join(BASE, "*.html"))
    for f in files:
        fix_file(f)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
