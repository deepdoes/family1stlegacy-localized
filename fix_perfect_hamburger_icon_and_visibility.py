#!/usr/bin/env python3
"""
fix_perfect_hamburger_icon_and_visibility.py
1. Fixes hamburger icon line spacing (gap: 4px, height: 2px, 22px width) so it looks like a crisp classic 3-line hamburger icon.
2. Fixes menu closing bug so hamburger icon never disappears when closing the menu.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

PERFECT_HAMBURGER_CSS = """
/* ─────────────────────────────────────────────────────────────
   PERFECT HAMBURGER ICON & CLEAN LIGHT GLASS OVERLAY SYSTEM
───────────────────────────────────────────────────────────── */

/* 1. Sleek, Modern Hamburger Icon (22px width x 14px total height) */
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
  margin-left: auto !important;
  cursor: pointer !important;
  flex-shrink: 0 !important;
  z-index: 100 !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
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

/* 2. Full-Screen Light Glass Overlay (Covers #nav completely when open) */
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
  padding: 0 24px 36px 24px !important;
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

/* 3. Header Inside Mobile Menu Overlay */
.mobile-menu-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  height: 64px !important;
  min-height: 64px !important;
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
  transition: all 0.2s ease !important;
}

.mobile-close:hover {
  background: rgba(74, 45, 122, 0.15) !important;
  transform: scale(1.05) !important;
}

.mobile-menu a, .mobile-menu-summary {
  color: #1A0C2E !important;
  font-weight: 600 !important;
}

.mobile-menu a:hover, .mobile-menu-summary:hover {
  color: #1D9E75 !important;
}

.mobile-menu-sublinks a {
  color: #4A5568 !important;
}

.mobile-menu-sublinks a:hover {
  color: #1D9E75 !important;
}

/* 4. Light Glass Floating Bottom Bar & Sheet Styles */
.mobile-bottom-nav {
  position: fixed !important;
  bottom: 14px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: calc(100% - 28px) !important;
  max-width: 440px !important;
  height: 64px !important;
  background: rgba(255, 255, 255, 0.9) !important;
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

.mbn-item {
  color: #5A6A85 !important;
  background: none !important;
  border: none !important;
}

.mbn-item svg {
  stroke: #5A6A85 !important;
}

.mbn-item.active, .mbn-item:hover {
  color: #1D9E75 !important;
}

.mbn-item.active svg, .mbn-item:hover svg {
  stroke: #1D9E75 !important;
}

.mbn-cta {
  background: linear-gradient(135deg, #1D9E75 0%, #178361 100%) !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.35) !important;
}

.mbn-cta svg, .mbn-cta span {
  stroke: #FFFFFF !important;
  color: #FFFFFF !important;
}

.mobile-services-sheet, .mobile-menu-sheet {
  position: fixed !important;
  bottom: 86px !important;
  left: 50% !important;
  transform: translateX(-50%) translateY(20px) scale(0.95) !important;
  width: calc(100% - 28px) !important;
  max-width: 440px !important;
  background: rgba(255, 255, 255, 0.95) !important;
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

.mss-close, .mms-close {
  background: rgba(74, 45, 122, 0.08) !important;
  color: #4A2D7A !important;
}

.mss-item {
  background: rgba(74, 45, 122, 0.04) !important;
  border: 1px solid rgba(74, 45, 122, 0.06) !important;
  color: #1A0C2E !important;
}

.mss-item:hover, .mss-item:active {
  background: rgba(29, 158, 117, 0.08) !important;
  border-color: rgba(29, 158, 117, 0.3) !important;
  color: #1D9E75 !important;
}

.mss-icon {
  background: rgba(29, 158, 117, 0.12) !important;
  color: #1D9E75 !important;
}

.mms-item {
  color: #1A0C2E !important;
  border-bottom: 1px solid rgba(74, 45, 122, 0.06) !important;
}

.mms-item:hover {
  color: #1D9E75 !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS block
    pattern_css = r'/\* ─+ \s* (?:LIGHT / WHITE GLASSMORPHISM & HAMBURGER CLOSE FIX|PERFECT HAMBURGER ICON & CLEAN LIGHT GLASS OVERLAY SYSTEM) \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, PERFECT_HAMBURGER_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", PERFECT_HAMBURGER_CSS + "\n</style>", 1)

    # 2. Clean up any previous body.mobile-menu-active JS snippets
    content = content.replace("; document.body.classList.add('mobile-menu-active')", "")
    content = content.replace("; document.body.classList.remove('mobile-menu-active')", "")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed hamburger icon & menu toggle in {filename}")

def main():
    print("=== Fixing Hamburger Icon & Menu Toggle Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
