#!/usr/bin/env python3
"""
add_top_right_call_button_and_fix_consult_hover.py
1. Fixes mouseover effect on Consult button (.mbn-cta) on bottom floating nav bar so it matches .mbn-item.
2. Injects sleek top-right Click-to-Call button (469) 608-1595 into top navigation bar across all HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CALL_BTN_AND_CONSULT_HOVER_CSS = """
/* ─────────────────────────────────────────────────────────────
   TOP-RIGHT CLICK-TO-CALL BUTTON & CONSULT MOUSEOVER FIX
───────────────────────────────────────────────────────────── */

/* 1. Top-Right Click-to-Call Button */
.mobile-nav-call-btn {
  display: none !important;
}

@media (max-width: 768px) {
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

  /* Dark Hero State */
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

  /* Sticky Light Header State (#nav.stuck) */
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

/* 2. Consult Button & All Bottom Nav Items Mouseover / Touch Fix */
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
"""

CALL_BTN_HTML = """<a href="tel:+14696081595" class="mobile-nav-call-btn" aria-label="Call Family First Legacy"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg><span>(469) 608-1595</span></a>"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject Call Button into .nav-bar if not present
    if "mobile-nav-call-btn" not in content:
        content = content.replace(
            '<button class="nav-toggle"',
            CALL_BTN_HTML + '\n      <button class="nav-toggle"'
        )

    # 2. Inject or update CSS block
    pattern_css = r'/\* ─+ \s* TOP-RIGHT CLICK-TO-CALL BUTTON & CONSULT MOUSEOVER FIX \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, CALL_BTN_AND_CONSULT_HOVER_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", CALL_BTN_AND_CONSULT_HOVER_CSS + "\n</style>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Added call button & fixed consult hover in {filename}")

def main():
    print("=== Adding Top-Right Call Button & Fixing Consult Hover Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
