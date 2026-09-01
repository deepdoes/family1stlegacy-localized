#!/usr/bin/env python3
"""
apply_item3_family_protection_wording.py
Updates wording in family_protection.html (Service Box: "What If You Were Alive — But Your Paycheck Stopped?"):
From: "It can affect your ability to work, stop or reduce your paycheck, and put pressure on your family’s daily life."
To: "It can affect your ability to work, reduce or interrupt your income, and put pressure on your family’s daily life."
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
TARGET_FILE = os.path.join(BASE, "family_protection.html")

OLD_TEXT = "It can affect your ability to work, stop or reduce your paycheck, and put pressure on your family’s daily life."
NEW_TEXT = "It can affect your ability to work, reduce or interrupt your income, and put pressure on your family’s daily life."

def apply_item3():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if OLD_TEXT in content:
        content = content.replace(OLD_TEXT, NEW_TEXT)
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Updated wording in family_protection.html")
    else:
        print(f"  ⚠ OLD_TEXT not found in family_protection.html")

def main():
    print("=== Applying Item #3 Family Protection Wording Update ===")
    apply_item3()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
