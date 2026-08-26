#!/usr/bin/env python3
"""
replace_theme_matched_nav_effects.py
Replaces old nav motion CSS with the refined theme-matched CSS across all HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

THEME_MATCHED_CSS = """/* ─────────────────────────────────────────────────────────────
   THEME-MATCHED NAVIGATION HOVER & ACTIVE MOTION EFFECTS
───────────────────────────────────────────────────────────── */
.nav-links > li > a:not(.nav-cta),
.nav-dropdown-toggle {
  position: relative;
  transition: color 0.25s ease, transform 0.25s ease !important;
}

/* Mouse Hover on Transparent Dark Hero Header: Vibrant Emerald Green */
#nav:not(.stuck) .nav-links > li > a:not(.nav-cta):hover,
#nav:not(.stuck) .nav-dropdown-wrap:hover .nav-dropdown-toggle {
  transform: translateY(-2px);
  color: #20C997 !important;
  text-shadow: 0 0 12px rgba(32, 201, 151, 0.4);
}

/* Mouse Hover on Sticky White Header: Rich Royal Purple */
#nav.stuck .nav-links > li > a:not(.nav-cta):hover,
#nav.stuck .nav-dropdown-wrap:hover .nav-dropdown-toggle {
  transform: translateY(-2px);
  color: #4A2D7A !important;
}

/* Glowing Underline Bar on Hover & Active */
.nav-links > li > a:not(.nav-cta)::after,
.nav-dropdown-toggle::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  width: 0;
  height: 2.5px;
  background: linear-gradient(90deg, #1D9E75, #F5D061);
  border-radius: 4px;
  transform: translateX(-50%);
  transition: width 0.3s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.3s ease;
  opacity: 0;
  box-shadow: 0 2px 8px rgba(32, 201, 151, 0.6);
}

.nav-links > li > a:not(.nav-cta):hover::after,
.nav-dropdown-wrap:hover .nav-dropdown-toggle::after,
.nav-links > li > a.nav-active:not(.nav-cta)::after,
.nav-links > li > a.pill-active:not(.nav-cta)::after {
  width: 85% !important;
  opacity: 1 !important;
}

/* Active Menu Item States */
#nav:not(.stuck) .nav-links > li > a.nav-active:not(.nav-cta),
#nav:not(.stuck) .nav-links > li > a.pill-active:not(.nav-cta) {
  color: #F5D061 !important;
  font-weight: 700 !important;
}

#nav.stuck .nav-links > li > a.nav-active:not(.nav-cta),
#nav.stuck .nav-links > li > a.pill-active:not(.nav-cta) {
  color: #4A2D7A !important;
  font-weight: 700 !important;
}

/* Submenu Mouseover State: Rich Purple Glass & Emerald Accent Line */
.nav-dropdown a {
  position: relative;
  transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
  border-left: 3px solid transparent !important;
}

.nav-dropdown a:hover {
  transform: translateX(4px) !important;
  background: rgba(74, 45, 122, 0.1) !important;
  color: #4A2D7A !important;
  font-weight: 600 !important;
  border-left: 3px solid #1D9E75 !important;
  padding-left: 22px !important;
}"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match previous block
    pattern = r'/\* ─+ \s* (?:PREMIUM|THEME-MATCHED) NAVIGATION HOVER & ACTIVE MOTION EFFECTS \s* ─+ \*/.*?(?=\.nav-dropdown-toggle svg\.chevron|\Z)'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, THEME_MATCHED_CSS + "\n\n", content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Replaced with theme-matched nav motion CSS in {filename}")

def main():
    print("=== Replacing Nav Motion CSS Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
