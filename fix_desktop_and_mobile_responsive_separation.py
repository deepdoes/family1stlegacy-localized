#!/usr/bin/env python3
"""
fix_desktop_and_mobile_responsive_separation.py
Enforces strict media query separation between Desktop (>768px) and Mobile (<=768px):
Desktop (>768px):
- .nav-logo margin-right: 0
- .nav-links margin-left: auto (pushed to the right, cleanly separated from logo)
- Hides ALL mobile elements (.nav-toggle, .mobile-bottom-nav, .mobile-services-sheet, .mobile-menu-sheet, .mobile-sheet-overlay, .mobile-menu, .mobile-nav-call-btn)

Mobile (<=768px):
- Hides desktop .nav-links & .nav-toggle
- Displays clean logo on left, Click-to-Call (469) 608-1595 on right
- Displays floating bottom app bar
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MASTER_RESPONSIVE_CSS = """
/* ─────────────────────────────────────────────────────────────
   STRICT DESKTOP vs MOBILE RESPONSIVE SEPARATION
───────────────────────────────────────────────────────────── */

/* DESKTOP VIEW (Width > 768px) */
@media (min-width: 769px) {
  #nav {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 1000 !important;
    padding: 0 !important;
  }

  #nav > div {
    width: 100% !important;
    padding: 0 48px !important;
    box-sizing: border-box !important;
    height: 90px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    transition: height 0.3s ease !important;
  }

  #nav.stuck > div {
    height: 70px !important;
  }

  .nav-bar {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
    height: 100% !important;
  }

  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin-right: 0 !important;
    padding: 0 !important;
  }

  .nav-logo-img {
    height: 70px !important;
    width: auto !important;
    object-fit: contain !important;
    transition: height 0.3s ease !important;
  }

  #nav.stuck .nav-logo-img {
    height: 54px !important;
  }

  .nav-links {
    display: flex !important;
    align-items: center !important;
    gap: 4px !important;
    list-style: none !important;
    margin: 0 !important;
    margin-left: auto !important; /* Pushes menu items to the right */
  }

  /* Hide ALL mobile-only elements on Desktop */
  .nav-toggle,
  button.nav-toggle,
  .mobile-bottom-nav,
  .mobile-services-sheet,
  .mobile-menu-sheet,
  .mobile-sheet-overlay,
  .mobile-menu,
  .mobile-nav-call-btn {
    display: none !important;
  }
}

/* MOBILE VIEW (Width <= 768px) */
@media (max-width: 768px) {
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

  /* Hide desktop links and hamburger button on mobile */
  .nav-links, .nav-toggle, button.nav-toggle {
    display: none !important;
  }

  /* Mobile Call Button */
  .mobile-nav-call-btn {
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    padding: 6px 12px !important;
    border-radius: 20px !important;
    font-family: var(--font-head, sans-serif) !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    margin-left: auto !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08) !important;
  }

  #nav:not(.stuck) .mobile-nav-call-btn {
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    color: #FFFFFF !important;
  }

  #nav:not(.stuck) .mobile-nav-call-btn svg {
    width: 14px !important;
    height: 14px !important;
    stroke: #20C997 !important;
    fill: none !important;
  }

  #nav.stuck .mobile-nav-call-btn {
    background: rgba(29, 158, 117, 0.1) !important;
    border: 1px solid rgba(29, 158, 117, 0.25) !important;
    color: #1D9E75 !important;
  }

  #nav.stuck .mobile-nav-call-btn svg {
    width: 14px !important;
    height: 14px !important;
    stroke: #1D9E75 !important;
    fill: none !important;
  }

  .mobile-nav-call-btn:hover, .mobile-nav-call-btn:active {
    transform: scale(1.03) !important;
    background: #1D9E75 !important;
    color: #FFFFFF !important;
    border-color: #1D9E75 !important;
  }

  .mobile-nav-call-btn:hover svg, .mobile-nav-call-btn:active svg {
    stroke: #FFFFFF !important;
  }

  /* Full-Screen Light Glass Overlay */
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

  /* Floating Bottom Nav */
  .mobile-bottom-nav {
    position: fixed !important;
    bottom: 14px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: calc(100% - 28px) !important;
    max-width: 440px !important;
    height: 64px !important;
    background: rgba(255, 255, 255, 0.94) !important;
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
    transition: all 0.2s ease !important;
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
    transition: color 0.2s ease !important;
  }

  .mbn-item:hover, .mbn-cta:hover,
  .mbn-item:active, .mbn-cta:active,
  .mbn-item.active {
    color: #1D9E75 !important;
  }

  .mbn-item:hover svg, .mbn-cta:hover svg,
  .mbn-item:active svg, .mbn-cta:active svg,
  .mbn-item.active svg {
    stroke: #1D9E75 !important;
  }

  .mbn-item:hover span, .mbn-cta:hover span,
  .mbn-item:active span, .mbn-cta:active span,
  .mbn-item.active span {
    color: #1D9E75 !important;
  }

  /* Back to Top Arrow Button Mobile Position */
  #scrolltop {
    bottom: 90px !important;
    right: 18px !important;
    z-index: 890 !important;
  }
}

@media (max-width: 380px) {
  .mobile-nav-call-btn span {
    display: none !important;
  }
  .mobile-nav-call-btn {
    padding: 8px !important;
    border-radius: 50% !important;
  }
}
"""

def clean_and_update(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove all previous mobile UI CSS blocks to prevent conflicts
    blocks_to_remove = [
        r'/\* ─+ \s* STRICT DESKTOP vs MOBILE RESPONSIVE SEPARATION \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* TOP-RIGHT CLICK-TO-CALL BUTTON & CONSULT MOUSEOVER FIX \s* ─+ \*/.*?(?=</style>|\Z)',
        r'/\* ─+ \s* CLEAN MOBILE TOP HEADER \(LOGO ONLY\) & BOTTOM APP BAR SYSTEM \s* ─+ \*/.*?(?=</style>|\Z)',
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

    # Inject master responsive CSS right before </style>
    if "</style>" in content:
        content = content.replace("</style>", MASTER_RESPONSIVE_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed desktop & mobile responsive separation in {filename}")

def main():
    print("=== Fixing Desktop vs Mobile Responsive Separation Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        clean_and_update(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
