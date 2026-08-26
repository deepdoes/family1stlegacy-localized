#!/usr/bin/env python3
"""
update_nextjs_globals_css.py
Appends all master responsive styles, mobile app bottom nav bar, rounded drawer sheet card styles,
call pill button, and scrolltop offsets to src/app/globals.css.
"""

import os

GLOBALS_CSS = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy/src/app/globals.css"

MASTER_ADDITIONS = """

/* ─── MASTER RESPONSIVE & MOBILE NAVIGATION ADDITIONS ─── */

/* 1. Header Call Button Pill */
.mobile-nav-call-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  background: #1D9E75 !important;
  color: #FFFFFF !important;
  font-family: var(--font-body) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  padding: 6px 10px !important;
  border-radius: 100px !important;
  text-decoration: none !important;
  box-shadow: 0 2px 8px rgba(29, 158, 117, 0.3) !important;
  line-height: 1 !important;
  flex: 0 0 auto !important;
  width: auto !important;
  max-width: fit-content !important;
  transition: all 0.2s ease !important;
}
.mobile-nav-call-btn svg {
  width: 12px !important;
  height: 12px !important;
  fill: none !important;
  stroke: #FFFFFF !important;
  stroke-width: 2.2 !important;
  flex-shrink: 0 !important;
}
.mobile-nav-call-btn:hover, .mobile-nav-call-btn:active {
  background: #158360 !important;
  transform: scale(0.98) !important;
}

/* 2. Floating Mobile Bottom App Bar */
.mobile-bottom-nav {
  position: fixed !important;
  bottom: 14px !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: calc(100% - 28px) !important;
  max-width: 440px !important;
  height: 64px !important;
  background: rgba(26, 12, 46, 0.94) !important;
  backdrop-filter: blur(20px) !important;
  -webkit-backdrop-filter: blur(20px) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  border-radius: 100px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-around !important;
  padding: 0 6px !important;
  z-index: 9999 !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
}
.mbn-item {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 4px !important;
  color: rgba(255, 255, 255, 0.65) !important;
  text-decoration: none !important;
  font-size: 10px !important;
  font-weight: 500 !important;
  background: none !important;
  border: none !important;
  cursor: pointer !important;
  padding: 6px 12px !important;
  border-radius: 16px !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
  -webkit-tap-highlight-color: transparent !important;
}
.mbn-item svg {
  width: 20px !important;
  height: 20px !important;
  fill: none !important;
  stroke: rgba(255, 255, 255, 0.65) !important;
  stroke-width: 1.8 !important;
  transition: all 0.2s ease !important;
}
.mbn-item:hover, .mbn-item:active {
  color: #FFFFFF !important;
  transform: scale(0.95) !important;
}
.mbn-item:hover svg, .mbn-item:active svg {
  stroke: #1D9E75 !important;
}
.mbn-item.active {
  color: #FFFFFF !important;
}
.mbn-item.active svg {
  stroke: #1D9E75 !important;
}
.mbn-cta {
  background: linear-gradient(135deg, #1D9E75, #4A2D7A) !important;
  color: #FFFFFF !important;
  padding: 8px 16px !important;
  border-radius: 100px !important;
  font-weight: 600 !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.4) !important;
}
.mbn-cta svg {
  stroke: #FFFFFF !important;
}

/* 3. Mobile Back-To-Top Elevation */
@media (max-width: 768px) {
  #scrolltop {
    bottom: 90px !important;
  }
}

/* 4. Desktop / Mobile Responsive Separation */
@media (min-width: 769px) {
  .mobile-bottom-nav,
  .mobile-services-sheet,
  .mobile-menu-sheet,
  .mobile-sheet-overlay,
  .mobile-nav-call-btn,
  .nav-toggle {
    display: none !important;
  }
  .nav-links {
    margin-left: auto !important;
  }
}

@media (max-width: 768px) {
  .nav-links {
    display: none !important;
  }
  .nav-toggle {
    display: block !important;
  }
}
"""

def update():
    with open(GLOBALS_CSS, "r", encoding="utf-8") as f:
        content = f.read()

    if "MASTER RESPONSIVE & MOBILE NAVIGATION ADDITIONS" not in content:
        content += MASTER_ADDITIONS
        with open(GLOBALS_CSS, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ Appended master responsive CSS additions to globals.css")
    else:
        print("  ✓ Master responsive CSS already present in globals.css")

if __name__ == "__main__":
    update()
