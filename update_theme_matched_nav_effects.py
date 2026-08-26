#!/usr/bin/env python3
"""
update_theme_matched_nav_effects.py
Refines mouseover and active states across main menu and submenus to perfectly match
Family First Legacy's brand theme (Emerald Green #1D9E75, Warm Gold #F5D061, Royal Purple #4A2D7A).

Fixes:
1. Submenu hover state made vibrant with rich purple glass backdrop (rgba(74, 45, 122, 0.1)), bold purple text, and an emerald left border indicator line.
2. Main menu hover state color changed to vibrant Emerald Green (#20C997) on dark hero and Deep Royal Purple (#4A2D7A) on sticky white header.
3. Active tab color updated to Warm Gold (#F5D061) on dark hero and Royal Purple (#4A2D7A) on white header.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

REFINED_NAV_CSS = """
/* ─────────────────────────────────────────────────────────────
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
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace previous nav motion block if present, or inject before </style>
    pattern = r'/\* ─+ \s* PREMIUM NAVIGATION HOVER & ACTIVE MOTION EFFECTS \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, REFINED_NAV_CSS, content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Refined theme-matched nav motion CSS in {filename}")
    elif "</style>" in content:
        content = content.replace("</style>", REFINED_NAV_CSS + "\n</style>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Injected theme-matched nav motion CSS into {filename}")

def main():
    print("=== Updating Theme-Matched Nav Motion Effects Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
