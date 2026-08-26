#!/usr/bin/env python3
"""
make_v1_backups.py
Creates V1 copies of all English static HTML files (e.g. index_v1.html, family_protection_v1.html)
so that the user can compare http://localhost:8080/index_v1.html (Original V1)
with http://localhost:8080/index.html (Updated Version) side-by-side.
"""

import os
import shutil
import glob

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def main():
    print("=== Creating V1 Backups for Comparison ===")
    english_files = [
        "index.html",
        "family_protection.html",
        "retirement_planning.html",
        "education_planning.html",
        "estate_planning.html",
        "financial_strategy.html",
        "business_strategies.html",
        "opportunity.html",
        "privacy.html",
        "terms.html",
        "blog_family_protection.html",
        "blog_retirement.html",
        "blog_education.html",
        "blog_financial_strategy.html",
        "blog_legacy.html",
        "blog_living_benefits.html"
    ]

    for fname in english_files:
        src = os.path.join(BASE, fname)
        if os.path.exists(src):
            v1_fname = fname.replace(".html", "_v1.html")
            dst = os.path.join(BASE, v1_fname)
            shutil.copy2(src, dst)
            print(f"  ✓ Created V1 backup: {v1_fname}")

    print("=== Done! ===")

if __name__ == "__main__":
    main()
