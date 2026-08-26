#!/usr/bin/env python3
"""
apply_row14_fafsa_compliance.py
Replaces all categorical 529 / FAFSA comparison statements in education_planning.html
(and its language variants) with the compliant Row 14 text:

"Financial-aid treatment can vary based on account ownership, the type of asset, and current FAFSA rules. Families should review current federal student-aid guidance before choosing a strategy."
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

NEW_ROW14_TEXT = "Financial-aid treatment can vary based on account ownership, the type of asset, and current FAFSA rules. Families should review current federal student-aid guidance before choosing a strategy."

def update_fafsa_in_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update FAQ answer for "Does a 529 plan affect financial aid?"
    faq_pattern = r'(<button class="faq-q"[^>]*>\s*Does a 529 plan affect financial aid\?\s*<div class="faq-icon"></div>\s*</button>\s*<div class="faq-a"><p>).*?(</p></div>)'
    if re.search(faq_pattern, content, flags=re.DOTALL):
        content = re.sub(faq_pattern, r'\1' + NEW_ROW14_TEXT + r'\2', content, flags=re.DOTALL)

    # 2. Replace any schema / text references in education_planning files claiming FAFSA non-counting
    content = re.sub(
        r'doesn\'t count against FAFSA financial aid calculations',
        NEW_ROW14_TEXT,
        content
    )
    content = re.sub(
        r'doesn\'t count heavily against financial aid \(FAFSA\)',
        'offers flexible education planning options',
        content
    )
    content = re.sub(
        r'A parent-owned 529 plan is generally treated as a parental asset on the FAFSA and can be considered when determining eligibility for need-based financial aid\.',
        NEW_ROW14_TEXT,
        content
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Applied Row 14 FAFSA compliance update to {filename}")

def main():
    print("=== Applying Row 14 FAFSA Compliance to Education Planning Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.startswith("education_planning") and f.endswith(".html")]
    for fname in sorted(html_files):
        update_fafsa_in_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
