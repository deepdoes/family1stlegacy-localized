#!/usr/bin/env python3
"""
match_drawer_sheets_layout_and_prominent_hover.py
1. Unifies layout of #mobileMenuSheet and #mobileServicesSheet so both use identical clean rounded card items.
2. Prominent desktop hover effect with deeper emerald green background tint (rgba(29,158,117,0.14)), border, and shadow.
3. Mobile touch feedback (:active) with scale(0.98) micro-press.
4. Persistent active state (.active) with a 4px Emerald Green left accent bar.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MATCHED_SHEETS_CSS = """
/* ─────────────────────────────────────────────────────────────
   UNIFIED DRAWER SHEETS LAYOUT, PROMINENT HOVER & TOUCH FEEDBACK
───────────────────────────────────────────────────────────── */

/* Services Sheet & Menu Sheet Card Items (100% Matched Layout) */
.mss-grid a, .mobile-services-sheet a,
.mms-links a:not(.mms-cta-btn) {
  color: #1A0C2E !important;
  font-weight: 600 !important;
  font-size: 14.5px !important;
  background: rgba(74, 45, 122, 0.04) !important;
  border: 1px solid rgba(74, 45, 122, 0.08) !important;
  border-radius: 14px !important;
  padding: 12px 16px !important;
  margin-bottom: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  text-decoration: none !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
  box-sizing: border-box !important;
  width: 100% !important;
}

.mss-grid a svg, .mobile-services-sheet a svg {
  width: 20px !important;
  height: 20px !important;
  stroke: #1D9E75 !important;
  fill: none !important;
  flex-shrink: 0 !important;
  margin-right: 12px !important;
  transition: stroke 0.25s ease !important;
}

/* Prominent Mouseover / Hover State (Desktop) */
.mss-grid a:hover, .mobile-services-sheet a:hover,
.mms-links a:not(.mms-cta-btn):hover {
  background: rgba(29, 158, 117, 0.14) !important;
  border-color: rgba(29, 158, 117, 0.4) !important;
  color: #1D9E75 !important;
  font-weight: 700 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.15) !important;
}

.mss-grid a:hover svg, .mobile-services-sheet a:hover svg {
  stroke: #1D9E75 !important;
}

/* Instant Touch Feedback on Mobile (:active) */
.mss-grid a:active, .mobile-services-sheet a:active,
.mms-links a:not(.mms-cta-btn):active {
  background: rgba(29, 158, 117, 0.22) !important;
  border-color: #1D9E75 !important;
  color: #1D9E75 !important;
  transform: scale(0.98) !important;
}

/* Persistent Active Page Highlight (Mobile & Desktop) */
.mss-grid a.active, .mobile-services-sheet a.active,
.mms-links a.active:not(.mms-cta-btn) {
  background: rgba(29, 158, 117, 0.14) !important;
  border-color: rgba(29, 158, 117, 0.4) !important;
  color: #1D9E75 !important;
  font-weight: 700 !important;
  border-left: 4px solid #1D9E75 !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace or inject CSS block
    pattern_css = r'/\* ─+ \s* (?:UNIFIED DRAWER SHEETS LAYOUT, PROMINENT HOVER & TOUCH FEEDBACK|SERVICES SHEET & BOTTOM NAV LIGHT COLOR THEME FIX) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, MATCHED_SHEETS_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", MATCHED_SHEETS_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Matched drawer sheet layouts & added prominent hover/touch in {filename}")

def main():
    print("=== Matching Drawer Sheet Layouts & Adding Prominent Hover/Touch Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
