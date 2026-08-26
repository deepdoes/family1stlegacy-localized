#!/usr/bin/env python3
"""
fix_row13_placement.py
1. Removes any stray paragraphs appended below footers across all HTML files.
2. Places Row 13 text cleanly inside education_planning.html (and language variants)
   in the exact section where 0% floor is explained in detail (FAQ question "Is cash value growth guaranteed?").
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

NEW_ROW13_TEXT = "Some IUL policies include a 0% floor on index-linked interest crediting, which can help provide protection from negative index performance. Policy charges and terms still apply, and we can help you understand how the policy works for your goals."

def clean_footer_stray_text(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern for any text inserted after </html> or </footer>
    pattern_stray = r'<div class="container" style="margin:24px auto;">.*?Some IUL policies include a 0% floor.*?</div>'
    content = re.sub(pattern_stray, '', content, flags=re.DOTALL)

    pattern_stray2 = r'<div class="container" style="margin:24px auto;">.*?Financial-aid treatment can vary.*?</div>'
    content = re.sub(pattern_stray2, '', content, flags=re.DOTALL)

    # If education_planning page, update FAQ "Is cash value growth guaranteed?" or IUL section
    if "education_planning" in filename:
        # Update FAQ answer where 0% floor is explained
        faq_target = r'(<button class="faq-q"[^>]*>\s*Is cash value growth guaranteed\?\s*<div class="faq-icon"></div>\s*</button>\s*<div class="faq-a"><p>).*?(</p></div>)'
        if re.search(faq_target, content, flags=re.DOTALL):
            content = re.sub(faq_target, r'\1' + NEW_ROW13_TEXT + r'\2', content, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Cleaned stray footer text & placed Row 13 in {filename}")

def main():
    print("=== Cleaning Stray Below-Footer Paragraphs & Placing Row 13 Text Properly ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        clean_footer_stray_text(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
