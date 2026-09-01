#!/usr/bin/env python3
"""
apply_item5_fia_faq.py
Updates the FAQ answer for "What is a Fixed Indexed Annuity (FIA)?" in retirement_planning.html:
New Answer: "A fixed indexed annuity is an insurance contract designed to help protect your principal from negative index performance while offering the potential for index-linked interest growth. Features and terms vary by contract, and we can help you understand how it may fit your retirement goals."
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
TARGET_FILE = os.path.join(BASE, "retirement_planning.html")

NEW_ANSWER = "A fixed indexed annuity is an insurance contract designed to help protect your principal from negative index performance while offering the potential for index-linked interest growth. Features and terms vary by contract, and we can help you understand how it may fit your retirement goals."

def apply_item5():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update HTML FAQ item
    faq_pattern = r'(<button class="faq-q"[^>]*>\s*What is a Fixed Indexed Annuity \(FIA\)\?\s*<div class="faq-icon"></div>\s*</button>\s*<div class="faq-a"><p>).*?(</p></div>)'
    if re.search(faq_pattern, content, flags=re.DOTALL):
        content = re.sub(faq_pattern, r'\1' + NEW_ANSWER + r'\2', content, flags=re.DOTALL)

    # 2. Update JSON-LD schema answer
    schema_pattern = r'("@name":\s*"What is a Fixed Indexed Annuity \(FIA\)\?",\s*"acceptedAnswer":\s*\{\s*"@type":\s*"Answer",\s*"text":\s*").*?("\s*\}|")'
    content = re.sub(
        r'("name":\s*"What is a Fixed Indexed Annuity \(FIA\)\?",\s*"acceptedAnswer":\s*\{\s*"@type":\s*"Answer",\s*"text":\s*").*?("\s*\})',
        r'\1' + NEW_ANSWER + r'\2',
        content,
        flags=re.DOTALL
    )

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Updated FIA FAQ answer in retirement_planning.html")

def main():
    print("=== Applying Item #5 Retirement Planning FIA FAQ Update ===")
    apply_item5()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
