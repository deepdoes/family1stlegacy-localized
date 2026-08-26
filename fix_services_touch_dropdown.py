#!/usr/bin/env python3
"""
fix_services_touch_dropdown.py
1. Removes click href navigation (href="#services" / href="index.html#services") on the Services menu item.
2. Ensures mouseover (hover) on desktop opens the Services dropdown submenu.
3. Ensures touch/tap on touchscreen devices toggles the Services dropdown submenu without jumping/scrolling to #services.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

TOUCH_CSS_BLOCK = """
/* ─── Services Navigation Touch & Mouseover Dropdown ─── */
.nav-dropdown-wrap {
  position: relative !important;
}
.nav-dropdown-wrap:hover .nav-dropdown,
.nav-dropdown-wrap.open .nav-dropdown {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateX(-50%) translateY(0) !important;
}
.nav-dropdown-wrap:hover .nav-dropdown-toggle svg.chevron,
.nav-dropdown-wrap.open .nav-dropdown-toggle svg.chevron {
  transform: rotate(180deg) !important;
}
.nav-dropdown-wrap::before {
  content: "" !important;
  position: absolute !important;
  top: 100% !important;
  left: -20px !important;
  right: -20px !important;
  height: 20px !important;
  z-index: 999 !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace href="...#services" on class="nav-dropdown-toggle"
    pattern = r'<a\s+href="[^"]*#services"\s+class="nav-dropdown-toggle">'
    replacement = '<a href="javascript:void(0)" class="nav-dropdown-toggle" onclick="event.preventDefault(); event.stopPropagation(); this.parentElement.classList.toggle(\'open\');">'
    
    content = re.sub(pattern, replacement, content)

    # Also handle spanish / translated link variations if any
    pattern_generic = r'<a\s+href="javascript:void\(0\)"\s+class="nav-dropdown-toggle">'
    if not re.search(pattern_generic, content):
        content = re.sub(
            r'<a\s+href="[^"]*services[^"]*"\s+class="nav-dropdown-toggle">',
            replacement,
            content
        )

    # Add touch CSS block if not present
    if "Services Navigation Touch & Mouseover Dropdown" not in content:
        content = content.replace("</head>", f"<style>{TOUCH_CSS_BLOCK}</style>\n</head>")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Updated Services touch & hover dropdown in {filename}")

def main():
    print("=== Fixing Services Dropdown Touch & Mouseover Behavior Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
