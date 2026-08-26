#!/usr/bin/env python3
"""
inject_nav_dropdown_css_spanish.py
Injects the complete nav-dropdown CSS rules into all Spanish HTML files
so that Servicios dropdown renders as a floating white card with a 10px chevron.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

NAV_DROPDOWN_CSS = """
/* Navigation Dropdown styling */
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
.nav-dropdown {
  position: absolute !important;
  top: 100% !important;
  left: 50% !important;
  transform: translateX(-50%) translateY(10px) !important;
  width: 260px !important;
  background: rgba(255, 255, 255, 0.98) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  border: 1px solid rgba(74, 45, 122, 0.08) !important;
  border-radius: 12px !important;
  box-shadow: 0 10px 30px rgba(74, 45, 122, 0.12) !important;
  padding: 8px 0 !important;
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
  padding: 8px 20px !important;
  color: var(--dark) !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  text-decoration: none !important;
  transition: background 0.2s, color 0.2s !important;
  border-radius: 0 !important;
  text-align: left !important;
}
.nav-dropdown a:hover {
  background: rgba(74, 45, 122, 0.04) !important;
  color: var(--purple) !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if ".nav-dropdown-wrap {" in content:
        print(f"  ✓ CSS already present in {filename}")
        return

    if "</style>" in content:
        content = content.replace("</style>", NAV_DROPDOWN_CSS + "\n</style>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Injected nav-dropdown CSS into {filename}")

def main():
    print("=== Injecting Nav Dropdown CSS Into All Spanish Pages ===")
    es_files = [f for f in os.listdir(BASE) if f.endswith("_es.html")]
    for fname in sorted(es_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
