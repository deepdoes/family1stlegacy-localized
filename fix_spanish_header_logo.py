#!/usr/bin/env python3
"""
fix_spanish_header_logo.py
Standardizes the header logo markup and CSS across all Spanish files to match the English master 1:1:
1. Logo height: 70px on top transparent header (#nav:not(.stuck)).
2. Logo height: 56px on sticky header (#nav.stuck).
3. Brightness/invert filter: crisp white on dark hero, original logo on stuck white navbar.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

LOGO_CSS = """
/* ── Standardized Header Logo Polish (Matches English Master 1:1) ── */
.nav-logo-img {
  height: 70px !important;
  max-height: 70px !important;
  width: auto !important;
  object-fit: contain !important;
  display: block !important;
  transition: height 0.3s ease, filter 0.3s ease !important;
}

#nav:not(.stuck) .nav-logo-img {
  filter: brightness(0) invert(1) !important;
}

#nav.stuck .nav-logo-img {
  height: 56px !important;
  max-height: 56px !important;
  filter: none !important;
}
"""

def fix_logos():
    spanish_files = [f for f in os.listdir(BASE) if f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in sorted(spanish_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove old CSS block if present
        content = re.sub(r'/\* ── Standardized Header Logo Polish.*?\*/\s*\.nav-logo-img.*?}#nav\.stuck \.nav-logo-img {.*?}', '', content, flags=re.DOTALL)

        # Standardize <a class="nav-logo">
        new_nav_logo = '<a class="nav-logo" href="index_es.html">\n  <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" class="nav-logo-img">\n</a>'
        
        content = re.sub(
            r'<a[^>]*class="nav-logo"[^>]*>.*?</a>',
            new_nav_logo,
            content,
            flags=re.DOTALL
        )

        # Inject LOGO_CSS
        content = content.replace("</head>", f"<style>{LOGO_CSS}</style>\n</head>")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Standardized header logo to 70px (56px stuck) in {fname}")

def main():
    print("=== Matching Spanish Header Logo Size 1:1 with English Master ===")
    fix_logos()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
