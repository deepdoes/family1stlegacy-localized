#!/usr/bin/env python3
"""
apply_item6_option_b_footer.py
Standardizes the 3rd link under "Company" in the footer across ALL English pages to read:
"Real Questions & Guidance"
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def is_english_file(fname):
    if not fname.endswith(".html") or fname.startswith("v1"):
        return False
    for lang in ["_es.", "_pt.", "_rw.", "_sw."]:
        if lang in fname:
            return False
    return True

def apply_item6():
    english_files = [f for f in os.listdir(BASE) if is_english_file(f)]
    
    for fname in sorted(english_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Update 3rd Company footer link (Client Stories or Q&A)
        # Matches <li><a href="...#reviews">...</a></li> within the Company footer list
        pattern = r'(<div class="f-col-head">Company</div>\s*<ul class="f-links">.*?<li><a href="([^"]*#reviews)">).*?(</a></li>)'
        
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, r'\1Real Questions &amp; Guidance\3', content, flags=re.DOTALL)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated Company footer link to 'Real Questions & Guidance' in {fname}")
        else:
            print(f"  ⚠ Company footer link pattern not found in {fname}")

def main():
    print("=== Applying Option B Footer Standardization Across All English Pages ===")
    apply_item6()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
