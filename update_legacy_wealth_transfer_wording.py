#!/usr/bin/env python3
"""
update_legacy_wealth_transfer_wording.py
Replaces the Legacy Article Key Takeaways bullet 3 wording:
FROM: "Generational Wealth Transfer: Using life insurance and structured products guarantees tax-free wealth transfer directly to the next generation."
TO: "Generational Wealth Transfer: Life insurance can help transfer wealth directly to beneficiaries, with death benefits generally received income-tax-free, helping support the financial legacy you want to leave for the next generation."
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

OLD_TEXT = "<strong>Generational Wealth Transfer:</strong> Life insurance can help transfer wealth directly to beneficiaries, with death benefits generally received income-tax-free, helping support the financial legacy you want to leave for the next generation."
NEW_TEXT = "<strong>Generational Wealth Transfer:</strong> Life insurance can help transfer wealth directly to beneficiaries, with death benefits generally received income-tax-free, helping support the financial legacy you want to leave for the next generation."

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
                    print(f"  ✓ Updated Legacy wording in {fname}")

def main():
    print("=== Updating Legacy Article Wealth Transfer Wording ===")
    apply_update()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
