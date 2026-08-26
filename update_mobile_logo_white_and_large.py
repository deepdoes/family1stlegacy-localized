#!/usr/bin/env python3
"""
update_mobile_logo_white_and_large.py
Updates mobile logo across all HTML pages:
1. Makes .mobile-menu-logo 50% bigger (65px height) and pure white (filter: brightness(0) invert(1)) for high contrast on the dark mobile menu overlay.
2. Increases header logo height on mobile screens to 65px (50% larger).
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MOBILE_LOGO_CSS = """
/* ─────────────────────────────────────────────────────────────
   MOBILE LOGO 50% LARGER & PURE WHITE ENHANCEMENT
───────────────────────────────────────────────────────────── */
.mobile-menu-logo {
  height: 65px !important;
  max-height: 70px !important;
  width: auto !important;
  object-fit: contain !important;
  filter: brightness(0) invert(1) !important;
}

@media (max-width: 768px) {
  .nav-logo img {
    height: 65px !important;
    max-height: 70px !important;
    width: auto !important;
    object-fit: contain !important;
  }
  #nav:not(.stuck) .nav-logo img {
    filter: brightness(0) invert(1) !important;
  }
  .mobile-menu-logo {
    height: 65px !important;
    max-height: 70px !important;
    width: auto !important;
    object-fit: contain !important;
    filter: brightness(0) invert(1) !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace existing block if already injected or append before </style>
    pattern = r'/\* ─+ \s* MOBILE LOGO 50% LARGER & PURE WHITE ENHANCEMENT \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, MOBILE_LOGO_CSS, content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Updated mobile logo CSS in {filename}")
    elif "</style>" in content:
        content = content.replace("</style>", MOBILE_LOGO_CSS + "\n</style>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Injected mobile logo CSS into {filename}")

def main():
    print("=== Updating Mobile Logo Size & Color Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
