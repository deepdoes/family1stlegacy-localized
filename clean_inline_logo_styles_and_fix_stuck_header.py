#!/usr/bin/env python3
"""
clean_inline_logo_styles_and_fix_stuck_header.py
Removes inline style="height: 90px; margin-top: 4px;" from .nav-logo img tags across all HTML files
and applies clean, responsive class-based sizing:
- Desktop default: 70px height (55px when stuck)
- Mobile default & stuck: 44px height (perfectly aligned with 64px header bar, zero bleeding)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CLEAN_LOGO_CSS = """
/* ─────────────────────────────────────────────────────────────
   BULLETPROOF RESPONSIVE LOGO & STUCK HEADER SYSTEM
───────────────────────────────────────────────────────────── */
.nav-logo-img {
  height: 70px;
  width: auto;
  object-fit: contain;
  display: block;
  transition: height 0.3s ease, filter 0.3s ease;
}

#nav:not(.stuck) .nav-logo-img {
  filter: brightness(0) invert(1);
}

#nav.stuck .nav-logo-img {
  height: 56px;
  filter: none !important;
}

@media (max-width: 768px) {
  #nav {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    height: 64px !important;
    min-height: 64px !important;
    z-index: 1000 !important;
  }

  #nav > div, #nav > div > div {
    height: 64px !important;
    min-height: 64px !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
  }

  #nav.stuck {
    background: #FFFFFF !important;
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.1) !important;
  }

  .nav-logo-img {
    height: 44px !important;
    max-height: 44px !important;
    margin: 0 !important;
  }

  #nav:not(.stuck) .nav-logo-img {
    filter: brightness(0) invert(1) !important;
  }

  #nav.stuck .nav-logo-img {
    filter: none !important;
  }

  #nav.stuck .nav-toggle span {
    background: #4A2D7A !important;
  }

  .mobile-menu-header {
    height: 64px !important;
    padding: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
  }

  .mobile-menu-logo {
    height: 44px !important;
    max-height: 44px !important;
    filter: brightness(0) invert(1) !important;
    margin: 0 !important;
  }
}
"""

def fix_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Clean inline style from .nav-logo img
    content = re.sub(
        r'<img\s+src="images/FamilyFirstLogo\.png"\s+alt="Family First Legacy"\s+style="[^"]*"',
        '<img src="images/FamilyFirstLogo.png" alt="Family First Legacy" class="nav-logo-img"',
        content
    )

    # 2. Update CSS block
    pattern_css = r'/\* ─+ \s* BULLETPROOF RESPONSIVE LOGO & STUCK HEADER SYSTEM \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, CLEAN_LOGO_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", CLEAN_LOGO_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Cleaned inline logo styles & fixed stuck header in {filename}")

def main():
    print("=== Cleaning Inline Logo Styles & Fixing Stuck Header Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
