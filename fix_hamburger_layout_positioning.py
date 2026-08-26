#!/usr/bin/env python3
"""
fix_hamburger_layout_positioning.py
Enforces margin-right: auto on .nav-logo and margin-left: auto on .nav-toggle
within a flexbox .nav-bar container across all HTML pages, guaranteeing that the logo
stays on the far left and the hamburger icon stays on the far right.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

HAMBURGER_FIX_CSS = """
/* ─────────────────────────────────────────────────────────────
   PERFECT MOBILE HEADER & HAMBURGER POSITIONING FIX
───────────────────────────────────────────────────────────── */
@media (max-width: 768px) {
  #nav {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 64px !important;
    z-index: 1000 !important;
  }

  #nav > div {
    width: 100% !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
    height: 64px !important;
  }

  .nav-bar {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
    height: 64px !important;
    box-sizing: border-box !important;
  }

  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin-right: auto !important;
    height: 44px !important;
  }

  .nav-logo img, .nav-logo-img {
    height: 44px !important;
    max-height: 44px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
    display: block !important;
  }

  .nav-toggle {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 5px !important;
    margin-left: auto !important;
    background: none !important;
    border: none !important;
    padding: 8px !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
  }

  .nav-toggle span {
    display: block !important;
    width: 24px !important;
    height: 2.5px !important;
    border-radius: 2px !important;
    transition: background 0.3s ease !important;
  }

  #nav:not(.stuck) .nav-toggle span {
    background: #FFFFFF !important;
  }

  #nav.stuck .nav-toggle span {
    background: #4A2D7A !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern_css = r'/\* ─+ \s* (?:PERFECT MOBILE HEADER & HAMBURGER POSITIONING FIX|BULLETPROOF RESPONSIVE LOGO & STUCK HEADER SYSTEM) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, HAMBURGER_FIX_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", HAMBURGER_FIX_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed hamburger icon positioning in {filename}")

def main():
    print("=== Fixing Hamburger Icon Positioning Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
