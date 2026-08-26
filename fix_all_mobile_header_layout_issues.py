#!/usr/bin/env python3
"""
fix_all_mobile_header_layout_issues.py
Fixes all 4 mobile header issues:
1. Increases mobile logo height to a well-proportioned 48px.
2. Aligns mobile header logo & mobile menu overlay logo pixel-for-pixel (66px header bar with 24px padding).
3. Fixes Services dropdown arrow positioning so '▼' sits directly next to 'Services' instead of far right.
4. Fixes sticky scroll header layout (#nav.stuck) so logo & hamburger icon stay neatly inside the 66px white background with zero bleeding.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

REFINED_MOBILE_HEADER_CSS = """
/* ─────────────────────────────────────────────────────────────
   MOBILE HEADER, STUCK HEADER & OVERLAY MENU LAYOUT FIXES
───────────────────────────────────────────────────────────── */

@media (max-width: 768px) {
  /* 1. Header Bar Container (Default & Stuck) */
  #nav {
    padding: 0 !important;
    height: auto !important;
    transition: background 0.3s ease, box-shadow 0.3s ease !important;
  }

  #nav > div {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 66px !important;
    min-height: 66px !important;
    padding: 0 24px !important;
    box-sizing: border-box !important;
  }

  #nav.stuck {
    background: rgba(255, 255, 255, 0.98) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
  }

  /* Logo Sizing: 48px height */
  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
  }

  .nav-logo img {
    height: 48px !important;
    max-height: 48px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
    transition: filter 0.3s ease !important;
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
    z-index: 100 !important;
  }

  .nav-toggle span {
    display: block !important;
    width: 24px !important;
    height: 2px !important;
    border-radius: 2px !important;
    transition: background 0.3s ease !important;
  }

  #nav:not(.stuck) .nav-toggle span {
    background: #FFFFFF !important;
  }

  #nav.stuck .nav-toggle span {
    background: #0F0C1C !important;
  }

  /* 2. Mobile Menu Overlay & Header Alignment */
  .mobile-menu {
    padding: 0 24px 36px 24px !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
    background: #0F0C1C !important;
  }

  .mobile-menu-header {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 66px !important;
    min-height: 66px !important;
    margin-top: 0 !important;
    margin-bottom: 24px !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-sizing: border-box !important;
    width: 100% !important;
  }

  .mobile-menu-logo {
    height: 48px !important;
    max-height: 48px !important;
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

  /* 3. Services Dropdown Arrow Fix */
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

  /* 4. Section Scroll Margin for Smooth Offset */
  section[id], div[id="reviews"], div[id="about"], div[id="services"], div[id="process"], div[id="opportunity"], div[id="contact"] {
    scroll-margin-top: 80px !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace previous mobile header block if present, or inject before </style>
    pattern = r'/\* ─+ \s* (?:COMPACT MOBILE HEADER & SCROLL MARGIN CLIPPING FIX|MOBILE HEADER, STUCK HEADER & OVERLAY MENU LAYOUT FIXES) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, REFINED_MOBILE_HEADER_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", REFINED_MOBILE_HEADER_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed mobile header layout & alignment in {filename}")

def main():
    print("=== Fixing All Mobile Header Layout Issues Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
