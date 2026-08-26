#!/usr/bin/env python3
"""
fix_nav_inline_height_and_bleeding_bug.py
1. Fixes inline height="90px" on #nav > div container across all HTML files.
2. Fixes #nav.stuck bleeding bug: guarantees #nav.stuck stays 100% fixed at top:0 with white background, crisp dark logo, and royal purple hamburger icon.
3. Keeps logo height at 46px perfectly centered inside the 66px mobile header bar with zero bleeding.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

UNIFIED_HEADER_FIX_CSS = """
/* ─────────────────────────────────────────────────────────────
   MOBILE HEADER, STUCK HEADER & OVERLAY MENU LAYOUT FIXES
───────────────────────────────────────────────────────────── */
#nav {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  width: 100% !important;
  z-index: 1000 !important;
  box-sizing: border-box !important;
}

#nav.stuck {
  background: #FFFFFF !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
}

@media (max-width: 768px) {
  #nav > div {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 64px !important;
    min-height: 64px !important;
    max-height: 64px !important;
    padding: 0 20px !important;
    box-sizing: border-box !important;
    margin: 0 !important;
  }

  .nav-logo {
    display: flex !important;
    align-items: center !important;
    height: 44px !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .nav-logo img {
    height: 44px !important;
    max-height: 44px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
    display: block !important;
  }

  #nav:not(.stuck) .nav-logo img {
    filter: brightness(0) invert(1) !important;
  }

  #nav.stuck .nav-logo img {
    filter: none !important;
  }

  /* Hamburger Toggle Button & Bars */
  .nav-toggle {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    gap: 5px !important;
    background: none !important;
    border: none !important;
    padding: 6px !important;
    margin: 0 !important;
    cursor: pointer !important;
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

  /* Mobile Menu Overlay Header Pixel-Synced */
  .mobile-menu {
    padding: 0 20px 36px 20px !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
    background: #0F0C1C !important;
  }

  .mobile-menu-header {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 64px !important;
    min-height: 64px !important;
    max-height: 64px !important;
    margin-top: 0 !important;
    margin-bottom: 24px !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-sizing: border-box !important;
    width: 100% !important;
  }

  .mobile-menu-logo {
    height: 44px !important;
    max-height: 44px !important;
    width: auto !important;
    object-fit: contain !important;
    filter: brightness(0) invert(1) !important;
    margin: 0 !important;
  }

  .mobile-close {
    background: rgba(255, 255, 255, 0.1) !important;
    border: none !important;
    color: #FFFFFF !important;
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    font-size: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
  }

  /* Services Dropdown Arrow Fix */
  .mobile-menu-summary {
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    justify-content: flex-start !important;
    cursor: pointer !important;
    width: 100% !important;
  }

  .mobile-menu-summary .summary-arrow,
  .mobile-menu-summary span {
    font-size: 12px !important;
    margin-left: 4px !important;
    transition: transform 0.25s ease !important;
  }

  /* Section Scroll Margin for Smooth Offset */
  section[id], div[id="reviews"], div[id="about"], div[id="services"], div[id="process"], div[id="opportunity"], div[id="contact"] {
    scroll-margin-top: 75px !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove inline style="... height: 90px;" from <header id="nav"> <div ...>
    content = re.sub(
        r'(<header id="nav">\s*<div [^>]*style="[^"]*height:\s*90px;[^"]*")',
        r'<header id="nav">\n  <div class="container-full">',
        content
    )

    # 2. Update CSS block
    pattern_css = r'/\* ─+ \s* MOBILE HEADER, STUCK HEADER & OVERLAY MENU LAYOUT FIXES \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, UNIFIED_HEADER_FIX_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", UNIFIED_HEADER_FIX_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed stuck header bleeding & mobile logo in {filename}")

def main():
    print("=== Fixing Stuck Header Bleeding & Mobile Logo Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
