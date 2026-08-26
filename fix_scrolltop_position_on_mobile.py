#!/usr/bin/env python3
"""
fix_scrolltop_position_on_mobile.py
Lifts the #scrolltop back-to-top purple arrow button to bottom: 90px on mobile viewports
so it sits cleanly above the floating bottom app bar with zero overlap.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SCROLLTOP_FIX_CSS = """
  /* Back to Top Arrow Button Mobile Position (Sits cleanly above bottom bar) */
  #scrolltop {
    bottom: 90px !important;
    right: 18px !important;
    z-index: 890 !important;
  }
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject inside @media (max-width: 768px) block or inside MASTER_MOBILE_UI_CSS
    if "/* 4. Services Sheet & Item Text Visibility Fix */" in content:
        content = content.replace(
            "/* 4. Services Sheet & Item Text Visibility Fix */",
            SCROLLTOP_FIX_CSS + "\n  /* 4. Services Sheet & Item Text Visibility Fix */"
        )
    elif "</style>" in content:
        content = content.replace(
            "</style>",
            "@media (max-width: 768px) {\n" + SCROLLTOP_FIX_CSS + "\n}\n</style>",
            1
        )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Lifted #scrolltop arrow button above bottom bar in {filename}")

def main():
    print("=== Fixing #scrolltop Arrow Button Position Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
