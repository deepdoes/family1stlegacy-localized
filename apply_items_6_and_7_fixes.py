#!/usr/bin/env python3
"""
apply_items_6_and_7_fixes.py
1. Applies CSS fix for Item #6:
   - Sets .footer-grid grid-template-columns: 2fr 1.1fr 1.35fr 1.1fr;
   - Sets .f-links a { white-space: nowrap; }
   This prevents "Real Questions & Guidance" from breaking into 2 lines on hover.

2. Applies Fix for Item #7:
   - Removes the duplicate <p><strong>Last Updated: ...</strong></p> inside the card body of privacy.html, terms.html, and localized versions.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

FOOTER_CSS_FIX = """
/* ─── Footer Grid & Link Hover Overflow Fix ─── */
.footer-grid { grid-template-columns: 2fr 1.1fr 1.35fr 1.1fr !important; gap: 40px !important; }
.f-links a { white-space: nowrap !important; }
"""

def fix_css_in_files():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "Footer Grid & Link Hover Overflow Fix" not in content:
            content = content.replace("</head>", f"<style>{FOOTER_CSS_FIX}</style>\n</head>")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added footer hover CSS fix to {fname}")

def fix_duplicate_dates():
    legal_files = [
        "privacy.html", "terms.html",
        "privacy_es.html", "terms_es.html",
        "privacy_pt.html", "terms_pt.html",
        "privacy_rw.html", "terms_rw.html",
        "privacy_sw.html", "terms_sw.html"
    ]

    dup_pattern = r'<p>\s*<strong>\s*Last Updated:\s*[^<]+</strong>\s*</p>\s*'
    dup_pattern_es = r'<p>\s*<strong>\s*(Última actualización|Última Atualização|Kuheruka kuvugururwa|Mwisho Kusasishwa):\s*[^<]+</strong>\s*</p>\s*'

    for fname in legal_files:
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove duplicate <p><strong>Last Updated...</strong></p> inside card body
        new_content = re.sub(dup_pattern, '', content, flags=re.IGNORECASE)
        new_content = re.sub(dup_pattern_es, '', new_content, flags=re.IGNORECASE)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  ✓ Removed duplicate Last Updated date in {fname}")
        else:
            print(f"  ⚠ Duplicate date line not found or already removed in {fname}")

def main():
    print("=== Applying Items #6 and #7 Fixes ===")
    fix_css_in_files()
    fix_duplicate_dates()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
