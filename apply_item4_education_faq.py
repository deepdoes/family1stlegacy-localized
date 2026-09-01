#!/usr/bin/env python3
"""
apply_item4_education_faq.py
Updates the FAQ answer for "How can life insurance help with education planning?" in education_planning.html:
New Answer: "Some permanent life insurance policies, such as IUL, may build cash value that can be accessed through policy loans or withdrawals for education or other future needs, depending on the policy. Accessing cash value can affect policy benefits, so it’s important to understand how your policy works. We can help you explore whether this option fits your family’s goals."
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
TARGET_FILE = os.path.join(BASE, "education_planning.html")

NEW_FAQ_ANSWER = "Some permanent life insurance policies, such as IUL, may build cash value that can be accessed through policy loans or withdrawals for education or other future needs, depending on the policy. Accessing cash value can affect policy benefits, so it’s important to understand how your policy works. We can help you explore whether this option fits your family’s goals."

def apply_item4():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    faq_pattern = r'(<button class="faq-q"[^>]*>\s*How can life insurance help with education planning\?\s*<div class="faq-icon"></div>\s*</button>\s*<div class="faq-a"><p>).*?(</p></div>)'
    
    if re.search(faq_pattern, content, flags=re.DOTALL):
        content = re.sub(faq_pattern, r'\1' + NEW_FAQ_ANSWER + r'\2', content, flags=re.DOTALL)
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ Updated FAQ answer in education_planning.html")
    else:
        print("  ⚠ FAQ question pattern not found in education_planning.html")

def main():
    print("=== Applying Item #4 Education Planning FAQ Update ===")
    apply_item4()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
