#!/usr/bin/env python3
"""
update_footer_agency_credit.py
Updates the footer agency credit line across all HTML files:
- English pages: <span>Website created by</span>
- Spanish pages: <span>Sitio web creado por</span>
Eliminates the redundant 'DFW Branding' text directly above the DFW Branding logo!
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def apply():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        is_es = "_es." in fname
        new_text = "<span>Sitio web creado por</span>" if is_es else "<span>Website created by</span>"

        old_patterns = [
            "<span>Website created by DFW Branding</span>",
            "<span>Sitio web creado por DFW Branding</span>",
            "<span>Sitio creado por DFW Branding</span>"
        ]

        updated = False
        for old in old_patterns:
            if old in content:
                content = content.replace(old, new_text)
                updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Cleaned footer agency credit text in {fname}")

def main():
    print("=== Cleaning Redundant Agency Credit Text in Footer ===")
    apply()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
