#!/usr/bin/env python3
"""
pixel_sync_mobile_logo_position.py
Pixel-syncs the mobile logo position between the closed #nav header and the open .mobile-menu overlay header:
- Header Bar side padding: 20px
- Header Bar height: 64px
- Logo height: 44px
- Logo margin/padding: 0
Guarantees 1:1 pixel alignment when opening and closing the mobile menu.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

PIXEL_SYNC_HEADER_CSS = """
/* ─────────────────────────────────────────────────────────────
   PIXEL-SYNCED MOBILE HEADER & OVERLAY LOGO POSITIONING
───────────────────────────────────────────────────────────── */

@media (max-width: 768px) {
  /* Closed State Header Bar (#nav) */
  #nav {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    height: 64px !important;
    z-index: 1000 !important;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }

  #nav > div {
    width: 100% !important;
    padding: 0 20px !important;
    margin: 0 !important;
    box-sizing: border-box !important;
    height: 64px !important;
    display: flex !important;
    align-items: center !important;
  }

  .nav-bar {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
    height: 64px !important;
    padding: 0 !important;
    margin: 0 !important;
    box-sizing: border-box !important;
  }

  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    margin-right: auto !important;
    padding: 0 !important;
    height: 44px !important;
  }

  .nav-logo img, .nav-logo-img {
    height: 44px !important;
    max-height: 44px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
    padding: 0 !important;
    display: block !important;
  }

  .nav-toggle {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: flex-end !important;
    width: 38px !important;
    height: 38px !important;
    padding: 0 !important;
    gap: 4px !important;
    background: transparent !important;
    border: none !important;
    margin: 0 !important;
    margin-left: auto !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
    z-index: 100 !important;
  }

  .nav-toggle span {
    display: block !important;
    width: 22px !important;
    height: 2px !important;
    min-height: 2px !important;
    max-height: 2px !important;
    border-radius: 2px !important;
    margin: 0 !important;
    padding: 0 !important;
    flex-shrink: 0 !important;
    transition: background 0.3s ease !important;
  }

  #nav:not(.stuck) .nav-toggle span {
    background: #FFFFFF !important;
  }

  #nav.stuck .nav-toggle span {
    background: #1A0C2E !important;
  }

  /* Open State Mobile Menu Overlay (.mobile-menu) */
  .mobile-menu {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    background: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    padding: 0 20px 36px 20px !important; /* EXACT 20px MATCH WITH #nav > div */
    margin: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
    z-index: 1100 !important;
    color: #1A0C2E !important;
    opacity: 0 !important;
    pointer-events: none !important;
    transition: opacity 0.3s ease, visibility 0.3s ease !important;
    visibility: hidden !important;
    box-sizing: border-box !important;
  }

  .mobile-menu.open {
    opacity: 1 !important;
    pointer-events: auto !important;
    visibility: visible !important;
  }

  .mobile-menu-header {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 64px !important;
    min-height: 64px !important;
    max-height: 64px !important;
    margin-top: 0 !important;
    margin-bottom: 20px !important;
    padding: 0 !important;
    border-bottom: 1px solid rgba(74, 45, 122, 0.08) !important;
    box-sizing: border-box !important;
    width: 100% !important;
  }

  .mobile-menu-logo {
    height: 44px !important;
    max-height: 44px !important;
    width: auto !important;
    object-fit: contain !important;
    filter: none !important;
    margin: 0 !important;
    padding: 0 !important;
    display: block !important;
  }

  .mobile-close {
    background: rgba(74, 45, 122, 0.08) !important;
    border: 1px solid rgba(74, 45, 122, 0.12) !important;
    color: #4A2D7A !important;
    width: 36px !important;
    height: 36px !important;
    border-radius: 50% !important;
    font-size: 18px !important;
    font-weight: bold !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    margin: 0 !important;
    margin-left: auto !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern_css = r'/\* ─+ \s* (?:PIXEL-SYNCED MOBILE HEADER & OVERLAY LOGO POSITIONING|PERFECT HAMBURGER ICON & CLEAN LIGHT GLASS OVERLAY SYSTEM|PERFECT MOBILE HEADER & HAMBURGER POSITIONING FIX) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, PIXEL_SYNC_HEADER_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", PIXEL_SYNC_HEADER_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Pixel-synced mobile logo in {filename}")

def main():
    print("=== Pixel-Syncing Mobile Logo Position Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
