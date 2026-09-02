#!/usr/bin/env python3
"""
update_legacy_section3_probate_wording.py
Replaces the Legacy Article Section 3 probate statement:
FROM: "When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free."
TO: "When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free."
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

OLD_TEXT = "When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free."
NEW_TEXT = "When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free."

def apply_update():
    for root, dirs, files in os.walk(BASE):
        if ".next" in root or "node_modules" in root:
            continue
        for fname in files:
            if fname.endswith(".html") or fname.endswith(".py"):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if OLD_TEXT in content:
                    content = content.replace(OLD_TEXT, NEW_TEXT)
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  ✓ Updated Legacy Section 3 probate wording in {fname}")

def main():
    print("=== Updating Legacy Article Section 3 Probate Wording ===")
    apply_update()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
