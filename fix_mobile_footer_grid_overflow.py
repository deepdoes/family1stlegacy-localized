#!/usr/bin/env python3
"""
fix_mobile_footer_grid_overflow.py
Fixes mobile footer layout and eliminates horizontal page scrolling across ALL HTML files:
1. Adds responsive media query for .footer-grid:
   - On screens <= 900px: converts 4-column layout into 2 columns or 1 single stacked column.
   - On screens <= 640px: single stacked column (1fr), ensuring 100% text fit without clipping.
2. Applies strict `overflow-x: hidden !important` on html and body to guarantee zero horizontal scrolling on mobile.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MOBILE_FOOTER_CSS = """
/* ── Mobile Footer Grid & Horizontal Scroll Fix ── */
html, body {
  overflow-x: hidden !important;
  max-width: 100vw !important;
}

@media (max-width: 900px) {
  .footer-grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 32px 24px !important;
  }
  .f-brand {
    grid-column: 1 / -1 !important;
  }
}

@media (max-width: 640px) {
  .footer-grid {
    grid-template-columns: 1fr !important;
    gap: 28px !important;
  }
  .footer-bottom {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 16px !important;
  }
  .fb-left {
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 8px !important;
  }
}
"""

def update_all_html_files():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False
        if "Mobile Footer Grid & Horizontal Scroll Fix" not in content:
            content = content.replace("</head>", f"<style>{MOBILE_FOOTER_CSS}</style>\n</head>")
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Fixed mobile footer grid & horizontal scroll in {fname}")

def main():
    print("=== Fixing Mobile Footer Grid Layout & Horizontal Scroll Across All Pages ===")
    update_all_html_files()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
