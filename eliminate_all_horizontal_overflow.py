#!/usr/bin/env python3
"""
eliminate_all_horizontal_overflow.py
Injects a comprehensive, bulletproof anti-horizontal overflow stylesheet across ALL 70 HTML files:
1. Prevents any sub-container (.blog-slider-track, flexboxes, padded divs) from expanding the viewport past 100vw.
2. Ensures all carousel wrappers (.blog-slider-wrap) strictly clip horizontal overflow (`max-width: 100% !important; overflow-x: auto !important`).
3. Sets `overflow-x: hidden !important; width: 100% !important; max-width: 100vw !important;` on `html` and `body`.
4. Adjusts container padding on mobile screens (max-width: 768px) to 20px so zero elements protrude off screen.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

ANTI_OVERFLOW_CSS = """
/* ── Bulletproof Global Anti-Horizontal Overflow System ── */
html {
  overflow-x: hidden !important;
  width: 100% !important;
  max-width: 100vw !important;
}

body {
  overflow-x: hidden !important;
  width: 100% !important;
  max-width: 100vw !important;
  position: relative !important;
}

*, *::before, *::after {
  box-sizing: border-box !important;
}

.container, .article-container-wrap, .article-hero-container, .article-grid-container {
  max-width: 100% !important;
  box-sizing: border-box !important;
}

.blog-slider-wrap, .more-articles-wrap {
  width: 100% !important;
  max-width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
}

@media (max-width: 768px) {
  #nav > div {
    padding-left: 20px !important;
    padding-right: 20px !important;
  }
  .container {
    padding-left: 16px !important;
    padding-right: 16px !important;
  }
  section {
    max-width: 100vw !important;
    overflow-x: hidden !important;
  }
}
"""

def apply_anti_overflow():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False
        if "Bulletproof Global Anti-Horizontal Overflow System" not in content:
            content = content.replace("</head>", f"<style>{ANTI_OVERFLOW_CSS}</style>\n</head>")
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Applied anti-horizontal overflow system to {fname}")

def main():
    print("=== Applying Anti-Horizontal Overflow System Across All HTML Files ===")
    apply_anti_overflow()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
