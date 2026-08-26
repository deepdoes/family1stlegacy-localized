#!/usr/bin/env python3
"""
implement_clean_top_header_bottom_nav.py
1. Hides top hamburger icon on mobile (@media max-width: 768px) -> Top header displays clean logo only.
2. Bottom floating bar handles full navigation via 'Menu' / 'Menú' tab.
3. Mobile overlay menu (.mobile-menu) opens cleanly when 'Menu' is tapped, with close button (✕) at top right.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CLEAN_MOBILE_HEADER_AND_NAV_CSS = """
/* ─────────────────────────────────────────────────────────────
   CLEAN MOBILE TOP HEADER (LOGO ONLY) & BOTTOM APP BAR SYSTEM
───────────────────────────────────────────────────────────── */

@media (max-width: 768px) {
  /* Top Header: Clean Brand Logo Only (No redundant top hamburger icon) */
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

  /* Hide top hamburger toggle icon on mobile for clean, modern UX */
  .nav-toggle, button.nav-toggle {
    display: none !important;
  }

  /* Full-Screen Light Glass Overlay (Opened via Bottom Bar 'Menu' tab) */
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
    padding: 0 20px 36px 20px !important;
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
    width: 34px !important;
    height: 34px !important;
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

  /* Floating Bottom Nav - Un-highlighted Consult Button */
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

  /* Services Sheet & Item Text Visibility */
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
    color: #1A0C2E !important;
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

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean previous blocks
    blocks_to_remove = [
        r'/\* ─+ \s* MASTER MOBILE UI, GLASSMORPHISM & HAMBURGER SYSTEM \s* ─+ \*/.*?(?=</style>|\Z)',
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

    # Inject clean master CSS
    if "</style>" in content:
        content = content.replace("</style>", CLEAN_MOBILE_HEADER_AND_NAV_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Updated mobile UI (Clean Logo Header + Bottom App Nav) in {filename}")

def main():
    print("=== Implementing Clean Mobile Header & Bottom App Nav Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
