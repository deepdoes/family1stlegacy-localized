#!/usr/bin/env python3
"""
fix_article_carousel_images.py
Fixes the missing thumbnail image paths for Financial Strategy and Legacy Planning in the More Articles carousel:
- Financial Strategy: images/financial_strategy_hispanic_1777333606672.png
- Legacy Planning: images/wealth_transfer_diverse_1777393288351.png
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_images():
    html_files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]

    bad_fin = "images/family_financial_planning_1777393245465.png"
    good_fin = "images/financial_strategy_hispanic_1777333606672.png"

    bad_leg = "images/estate_planning_senior_couple_1777393261191.png"
    good_leg = "images/wealth_transfer_diverse_1777393288351.png"

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False
        if bad_fin in content:
            content = content.replace(bad_fin, good_fin)
            updated = True
        if bad_leg in content:
            content = content.replace(bad_leg, good_leg)
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Fixed article thumbnail images in {fname}")

def main():
    print("=== Fixing Missing Article Carousel Thumbnail Images ===")
    update_images()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
