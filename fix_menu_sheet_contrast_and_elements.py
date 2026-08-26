#!/usr/bin/env python3
"""
fix_menu_sheet_contrast_and_elements.py
Fixes text contrast, logo visibility, language pills, and consultation CTA button inside #mobileMenuSheet:
1. .mms-logo: Set to filter: none (original sharp dark purple logo on light white background).
2. .mms-links a: Set to #1A0C2E (crisp dark charcoal purple text).
3. .mms-lang a.active: Emerald green background (#1D9E75) with white bold text.
4. .mms-lang a:not(.active): Light purple background with dark purple text (#4A2D7A).
5. .mms-cta-btn: Gradient background (#1D9E75 to #4A2D7A) with bright white bold text (#FFFFFF).
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MENU_SHEET_CONTRAST_FIX_CSS = """
/* ─────────────────────────────────────────────────────────────
   MENU DRAWER SHEET CONTRAST & ELEMENT STYLING FIX
───────────────────────────────────────────────────────────── */

/* 1. Logo inside Menu Sheet Header */
.mms-header .mms-logo, img.mms-logo {
  height: 38px !important;
  max-height: 38px !important;
  width: auto !important;
  object-fit: contain !important;
  filter: none !important; /* Original dark purple logo on light sheet background */
}

/* 2. Menu Links inside Drawer Sheet */
.mms-links a:not(.mms-cta-btn) {
  color: #1A0C2E !important; /* Crisp dark charcoal text */
  font-weight: 600 !important;
  font-size: 15px !important;
  border-bottom: 1px solid rgba(74, 45, 122, 0.06) !important;
  padding: 12px 4px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  text-decoration: none !important;
  transition: color 0.2s ease !important;
}

.mms-links a:not(.mms-cta-btn):hover {
  color: #1D9E75 !important;
}

/* 3. Language Switcher Pills (.mms-lang) */
.mms-lang {
  display: flex !important;
  gap: 10px !important;
  margin: 16px 0 12px 0 !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

.mms-lang a {
  flex: 1 !important;
  text-align: center !important;
  padding: 10px 14px !important;
  border-radius: 10px !important;
  font-weight: 700 !important;
  font-size: 14px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
  box-sizing: border-box !important;
}

.mms-lang a.active {
  background: #1D9E75 !important;
  color: #FFFFFF !important;
  border: 1px solid #1D9E75 !important;
  box-shadow: 0 4px 12px rgba(29, 158, 117, 0.25) !important;
}

.mms-lang a:not(.active) {
  background: rgba(74, 45, 122, 0.05) !important;
  color: #4A2D7A !important;
  border: 1px solid rgba(74, 45, 122, 0.12) !important;
}

.mms-lang a:not(.active):hover {
  background: rgba(29, 158, 117, 0.08) !important;
  color: #1D9E75 !important;
}

/* 4. Free Consultation Button (.mms-cta-btn) */
.mms-cta-btn, a.mms-cta-btn {
  background: linear-gradient(135deg, #1D9E75 0%, #4A2D7A 100%) !important;
  color: #FFFFFF !important;
  font-weight: 700 !important;
  font-size: 15px !important;
  text-align: center !important;
  justify-content: center !important;
  padding: 14px 20px !important;
  border-radius: 14px !important;
  box-shadow: 0 6px 20px rgba(74, 45, 122, 0.25) !important;
  margin-top: 8px !important;
  letter-spacing: 0.3px !important;
  text-decoration: none !important;
  display: flex !important;
  align-items: center !important;
  width: 100% !important;
  box-sizing: border-box !important;
  border: none !important;
}

.mms-cta-btn:hover {
  box-shadow: 0 8px 24px rgba(74, 45, 122, 0.35) !important;
  transform: translateY(-1px) !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace or inject CSS block
    pattern_css = r'/\* ─+ \s* (?:MENU DRAWER SHEET CONTRAST & ELEMENT STYLING FIX|SERVICES SHEET & BOTTOM NAV LIGHT COLOR THEME FIX) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, MENU_SHEET_CONTRAST_FIX_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", MENU_SHEET_CONTRAST_FIX_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed Menu sheet element contrast in {filename}")

def main():
    print("=== Fixing Menu Sheet Element Contrast Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
