#!/usr/bin/env python3
"""
fix_nav_dropdown_width_all_pages.py
Increases the width of the navigation Services dropdown to fit longer text titles
such as 'Planificación del Patrimonio y Legado' perfectly without wrapping or overflowing.
Applies min-width: 290px, width: max-content, and white-space: nowrap across all HTML pages.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

ENHANCED_NAV_DROPDOWN_CSS = """
/* Navigation Dropdown styling — Spacious Responsive Width */
.nav-dropdown-wrap {
  position: relative;
}
.nav-dropdown-toggle {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.nav-dropdown-toggle svg.chevron {
  width: 10px !important;
  height: 10px !important;
  stroke: currentColor;
  stroke-width: 3px;
  fill: none;
  transition: transform 0.25s ease;
  display: inline-block;
  margin-top: 1px;
}
.nav-dropdown-wrap:hover .nav-dropdown-toggle svg.chevron {
  transform: rotate(180deg);
}
.nav-dropdown-wrap::before {
  content: '';
  position: absolute;
  top: 100%;
  left: -20px;
  right: -20px;
  height: 20px;
  z-index: 999;
}
.nav-dropdown {
  position: absolute !important;
  top: calc(100% + 4px) !important;
  left: 50% !important;
  transform: translateX(-50%) translateY(10px) !important;
  min-width: 310px !important;
  width: max-content !important;
  background: rgba(255, 255, 255, 0.98) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid rgba(74, 45, 122, 0.12) !important;
  border-radius: 14px !important;
  box-shadow: 0 12px 36px rgba(74, 45, 122, 0.16) !important;
  padding: 10px 0 !important;
  list-style: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  transition: opacity 0.25s ease, transform 0.25s ease, visibility 0.25s !important;
  z-index: 1000 !important;
  margin: 0 !important;
}
.nav-dropdown-wrap:hover .nav-dropdown {
  opacity: 1 !important;
  visibility: visible !important;
  transform: translateX(-50%) translateY(0) !important;
}
.nav-dropdown li {
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
}
.nav-dropdown a {
  display: block !important;
  padding: 10px 22px !important;
  color: var(--dark) !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  white-space: nowrap !important;
  text-decoration: none !important;
  transition: background 0.2s, color 0.2s !important;
  border-radius: 0 !important;
  text-align: left !important;
}
.nav-dropdown a:hover {
  background: rgba(74, 45, 122, 0.05) !important;
  color: var(--purple) !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "</style>" in content:
        # Check if already injected
        if "min-width: 310px !important;" in content:
            print(f"  ✓ Already updated in {filename}")
            return
        
        content = content.replace("</style>", ENHANCED_NAV_DROPDOWN_CSS + "\n</style>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Updated nav-dropdown width in {filename}")

def main():
    print("=== Updating Nav Dropdown Width Across All HTML Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
