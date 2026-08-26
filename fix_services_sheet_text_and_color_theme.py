#!/usr/bin/env python3
"""
fix_services_sheet_text_and_color_theme.py
Fixes color contrast and text visibility in the Services Popover Sheet and Bottom Navigation Bar:
1. .mss-title: Set to #4A2D7A (Deep Royal Purple) instead of yellow/gold.
2. .mss-grid a: Set text to #1A0C2E (Dark Charcoal Purple) with #1D9E75 Emerald SVG icons and light purple border background.
3. Active service link on service subpages: Highlighted in Emerald Green (#1D9E75).
4. Bottom Bar (.mbn-item / .mbn-cta): Un-highlighted Consult button; only active tab is Emerald Green.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SHEET_AND_BOTTOM_BAR_THEME_CSS = """
/* ─────────────────────────────────────────────────────────────
   SERVICES SHEET & BOTTOM NAV LIGHT COLOR THEME FIX
───────────────────────────────────────────────────────────── */

/* 1. Services Sheet Header Title */
.mss-title, .mms-title {
  color: #4A2D7A !important;
  font-family: var(--font-head, sans-serif) !important;
  font-size: 16px !important;
  font-weight: 700 !important;
  letter-spacing: 0.5px !important;
  text-transform: uppercase !important;
}

/* 2. Services Sheet Links (.mss-grid a) - Crisp Dark Text Visibility */
.mss-grid a, .mobile-services-sheet a {
  color: #1A0C2E !important; /* Sharp dark text visibility */
  font-weight: 600 !important;
  font-size: 14px !important;
  background: rgba(74, 45, 122, 0.04) !important;
  border: 1px solid rgba(74, 45, 122, 0.08) !important;
  border-radius: 12px !important;
  padding: 12px 14px !important;
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
  margin-bottom: 8px !important;
}

.mss-grid a svg, .mobile-services-sheet a svg {
  width: 20px !important;
  height: 20px !important;
  stroke: #1D9E75 !important;
  fill: none !important;
  flex-shrink: 0 !important;
}

.mss-grid a:hover, .mss-grid a.active, .mobile-services-sheet a:hover, .mobile-services-sheet a.active {
  background: rgba(29, 158, 117, 0.1) !important;
  border-color: rgba(29, 158, 117, 0.3) !important;
  color: #1D9E75 !important;
}

/* 3. Bottom Bar (.mobile-bottom-nav) Colors */
.mobile-bottom-nav {
  background: rgba(255, 255, 255, 0.94) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
  border: 1px solid rgba(255, 255, 255, 0.8) !important;
  box-shadow: 0 12px 36px rgba(74, 45, 122, 0.15), 0 2px 8px rgba(0, 0, 0, 0.05) !important;
}

.mbn-item, .mbn-cta {
  color: #5A6A85 !important;
  background: none !important;
  border: none !important;
  box-shadow: none !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-decoration: none !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  padding: 4px 8px !important;
  border-radius: 12px !important;
  transition: color 0.2s ease !important;
}

.mbn-item svg, .mbn-cta svg {
  width: 20px !important;
  height: 20px !important;
  stroke: #5A6A85 !important;
  fill: none !important;
  margin-bottom: 2px !important;
  transition: stroke 0.2s ease !important;
}

.mbn-item span, .mbn-cta span {
  color: #5A6A85 !important;
  font-size: 11px !important;
}

/* Highlight ONLY active tab in Emerald Green */
.mbn-item.active, .mbn-item:hover, .mbn-cta:hover {
  color: #1D9E75 !important;
}

.mbn-item.active svg, .mbn-item:hover svg, .mbn-cta:hover svg {
  stroke: #1D9E75 !important;
}

.mbn-item.active span, .mbn-item:hover span, .mbn-cta:hover span {
  color: #1D9E75 !important;
}

/* 4. Full Menu Drawer Sheet (.mobile-menu-sheet) Links */
.mms-links a {
  color: #1A0C2E !important;
  border-bottom: 1px solid rgba(74, 45, 122, 0.06) !important;
  font-weight: 600 !important;
  padding: 12px 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  text-decoration: none !important;
}

.mms-links a:hover {
  color: #1D9E75 !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace or inject CSS block
    pattern_css = r'/\* ─+ \s* (?:SERVICES SHEET & BOTTOM NAV LIGHT COLOR THEME FIX|SERVICES SHEET & ITEM TEXT VISIBILITY FIX) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, SHEET_AND_BOTTOM_BAR_THEME_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", SHEET_AND_BOTTOM_BAR_THEME_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed Services sheet text & bottom nav theme in {filename}")

def main():
    print("=== Fixing Services Sheet & Bottom Nav Theme Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
