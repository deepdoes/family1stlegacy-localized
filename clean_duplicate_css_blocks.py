#!/usr/bin/env python3
"""
clean_duplicate_css_blocks.py
Consolidates all mobile header, glassmorphism, hamburger icon, and drawer sheet CSS blocks
into ONE clean, non-duplicated master CSS block across all HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MASTER_MOBILE_UI_CSS = """
/* ─────────────────────────────────────────────────────────────
   MASTER MOBILE UI, GLASSMORPHISM & HAMBURGER SYSTEM
───────────────────────────────────────────────────────────── */

@media (max-width: 768px) {
  /* 1. Closed Header Bar (#nav) */
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

  /* Unbreakable 3-Line Hamburger Icon (24px width x 16px height) */
  .nav-toggle {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 24px !important;
    height: 16px !important;
    min-height: 16px !important;
    max-height: 16px !important;
    padding: 0 !important;
    margin: 0 !important;
    margin-left: auto !important;
    background: transparent !important;
    border: none !important;
    cursor: pointer !important;
    flex-shrink: 0 !important;
    z-index: 100 !important;
    box-sizing: border-box !important;
  }

  .nav-toggle span {
    display: block !important;
    width: 24px !important;
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

  /* 2. Open Mobile Menu Overlay (.mobile-menu) */
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

  /* Close Button Positioned at EXACT SAME Pixel Location as Hamburger Icon */
  .mobile-close {
    background: rgba(74, 45, 122, 0.08) !important;
    border: 1px solid rgba(74, 45, 122, 0.12) !important;
    color: #4A2D7A !important;
    width: 32px !important;
    height: 32px !important;
    border-radius: 50% !important;
    font-size: 16px !important;
    font-weight: bold !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    margin: 0 !important;
    margin-left: auto !important;
    flex-shrink: 0 !important;
    transition: all 0.2s ease !important;
  }

  .mobile-close:hover {
    background: rgba(74, 45, 122, 0.15) !important;
    transform: scale(1.05) !important;
  }

  /* 3. Floating Bottom Nav (Un-highlighted Consult Button) */
  .mobile-bottom-nav {
    position: fixed !important;
    bottom: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: calc(100% - 28px) !important;
    max-width: 440px !important;
    height: 64px !important;
    background: rgba(255, 255, 255, 0.92) !important;
    backdrop-filter: blur(20px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.8) !important;
    border-radius: 32px !important;
    box-shadow: 0 12px 36px rgba(74, 45, 122, 0.15), 0 2px 8px rgba(0, 0, 0, 0.05) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-around !important;
    padding: 0 8px !important;
    z-index: 899 !important;
    box-sizing: border-box !important;
  }

  .mbn-item, .mbn-cta {
    color: #5A6A85 !important;
    background: none !important;
    border: none !important;
    box-shadow: none !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    padding: 4px 8px !important;
    border-radius: 12px !important;
    transition: color 0.2s ease !important;
  }

  .mbn-item svg, .mbn-cta svg {
    width: 20px !important;
    height: 20px !important;
    stroke: #5A6A85 !important;
    fill: none !important;
    margin-bottom: 2px !important;
    transition: stroke 0.2s ease !important;
  }

  .mbn-item span, .mbn-cta span {
    color: #5A6A85 !important;
    font-size: 11px !important;
  }

  .mbn-item.active, .mbn-item:hover, .mbn-cta:hover {
    color: #1D9E75 !important;
  }

  .mbn-item.active svg, .mbn-item:hover svg, .mbn-cta:hover svg {
    stroke: #1D9E75 !important;
  }

  .mbn-item.active span, .mbn-item:hover span, .mbn-cta:hover span {
    color: #1D9E75 !important;
  }

  /* 4. Services Sheet & Item Text Visibility Fix */
  .mobile-services-sheet, .mobile-menu-sheet {
    position: fixed !important;
    bottom: 86px !important;
    left: 50% !important;
    transform: translateX(-50%) translateY(20px) scale(0.95) !important;
    width: calc(100% - 28px) !important;
    max-width: 440px !important;
    background: rgba(255, 255, 255, 0.96) !important;
    backdrop-filter: blur(24px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.9) !important;
    border-radius: 24px !important;
    padding: 20px !important;
    box-shadow: 0 20px 50px rgba(74, 45, 122, 0.18), 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    z-index: 900 !important;
    box-sizing: border-box !important;
    color: #1A0C2E !important;
  }

  .mss-header, .mms-header {
    color: #4A2D7A !important;
    border-bottom: 1px solid rgba(74, 45, 122, 0.08) !important;
    padding-bottom: 12px !important;
    margin-bottom: 14px !important;
  }

  .mss-item {
    background: rgba(74, 45, 122, 0.04) !important;
    border: 1px solid rgba(74, 45, 122, 0.08) !important;
    color: #1A0C2E !important;
    font-weight: 600 !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    padding: 12px 14px !important;
    border-radius: 14px !important;
    text-decoration: none !important;
    margin-bottom: 8px !important;
    transition: all 0.2s ease !important;
  }

  .mss-item span, .mss-item p, .mss-item div {
    color: #1A0C2E !important; /* Sharp dark text visibility */
  }

  .mss-item:hover, .mss-item:active {
    background: rgba(29, 158, 117, 0.08) !important;
    border-color: rgba(29, 158, 117, 0.3) !important;
    color: #1D9E75 !important;
  }

  .mss-item:hover span {
    color: #1D9E75 !important;
  }

  .mss-icon {
    background: rgba(29, 158, 117, 0.12) !important;
    color: #1D9E75 !important;
    width: 32px !important;
    height: 32px !important;
    border-radius: 10px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
  }
}
"""

def clean_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove all previous mobile UI CSS blocks to prevent duplicates
    blocks_to_remove = [
        r'/\* ─+ \s* UNBREAKABLE HAMBURGER ICON, EXACT CLOSE POSITION & LIGHT SHEETS \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* PERFECT HAMBURGER ICON & CLEAN LIGHT GLASS OVERLAY SYSTEM \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* LIGHT / WHITE GLASSMORPHISM & HAMBURGER CLOSE FIX \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* PERFECT MOBILE HEADER & HAMBURGER POSITIONING FIX \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* PIXEL-SYNCED MOBILE HEADER & OVERLAY LOGO POSITIONING \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* BULLETPROOF RESPONSIVE LOGO & STUCK HEADER SYSTEM \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* MOBILE HEADER, STUCK HEADER & OVERLAY MENU LAYOUT FIXES \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* COMPACT MOBILE HEADER & SCROLL MARGIN CLIPPING FIX \s* ─+ \*/.*?(?=</style>|\Z)'
    ]

    for pat in blocks_to_remove:
        content = re.sub(pat, '', content, flags=re.DOTALL)

    # Inject single master CSS block right before </style>
    if "</style>" in content:
        content = content.replace("</style>", MASTER_MOBILE_UI_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Consolidated clean CSS in {filename}")

def main():
    print("=== Consolidating Master Mobile UI CSS Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        clean_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
