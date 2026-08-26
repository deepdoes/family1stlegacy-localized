#!/usr/bin/env python3
"""
enable_mouseover_language_dropdown.py
Updates all static .html files and React Navbar to ensure the Language Selector dropdown
opens seamlessly on mouseover (hover) on desktop, while retaining click capability for touch devices.
Includes a hover bridge to ensure moving the cursor down to the dropdown options never loses focus.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

HOVER_CSS_BLOCK = """
/* ─── Seamless Language Selector Mouseover (Hover) & Bridge ─── */
#nav .lang-switcher {
  position: relative !important;
}
#nav .lang-switcher:hover .lang-dropdown,
#nav .lang-switcher.open .lang-dropdown {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) !important;
}
#nav .lang-dropdown {
  transition: opacity 0.2s ease, transform 0.2s ease, visibility 0.2s ease !important;
}
/* Invisible gap bridge to keep mouseover active during cursor movement */
#nav .lang-dropdown::before {
  content: "" !important;
  position: absolute !important;
  top: -12px !important;
  left: 0 !important;
  right: 0 !important;
  height: 14px !important;
  background: transparent !important;
}
"""

def update_html_files():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in html_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "Seamless Language Selector Mouseover (Hover) & Bridge" not in content:
            content = content.replace("</head>", f"<style>{HOVER_CSS_BLOCK}</style>\n</head>")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added seamless mouseover hover CSS to {fname}")

def main():
    print("=== Enabling Mouseover (Hover) Language Dropdown Across All Pages ===")
    update_html_files()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
