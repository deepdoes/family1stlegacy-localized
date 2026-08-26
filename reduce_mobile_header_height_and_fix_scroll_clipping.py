#!/usr/bin/env python3
"""
reduce_mobile_header_height_and_fix_scroll_clipping.py
1. Significantly reduces mobile header height to a compact 54px bar with 38px logo and 8px 18px padding.
2. Fixes section heading clipping bug when tapping Q&A (or any nav link) by adding scroll-margin-top: 70px and header-offset smooth scroll calculation.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

COMPACT_HEADER_AND_SCROLL_CSS = """
/* ─────────────────────────────────────────────────────────────
   COMPACT MOBILE HEADER & SCROLL MARGIN CLIPPING FIX
───────────────────────────────────────────────────────────── */
section[id], div[id="reviews"], div[id="about"], div[id="services"], div[id="process"], div[id="opportunity"], div[id="contact"] {
  scroll-margin-top: 85px !important;
}

@media (max-width: 768px) {
  section[id], div[id="reviews"], div[id="about"], div[id="services"], div[id="process"], div[id="opportunity"], div[id="contact"] {
    scroll-margin-top: 70px !important;
  }

  /* Compact Mobile Header (54px height) */
  #nav {
    padding: 0 !important;
  }
  #nav > div {
    padding: 8px 18px !important;
    align-items: center !important;
    height: 54px !important;
    min-height: 54px !important;
    box-sizing: border-box !important;
  }
  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  .nav-logo img {
    height: 38px !important;
    max-height: 38px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
  }
  
  /* Mobile menu overlay header pixel-synced with compact 54px header */
  .mobile-menu {
    padding: 8px 18px 32px 18px !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
  }
  .mobile-menu-header {
    margin-top: 0 !important;
    margin-bottom: 20px !important;
    padding-bottom: 12px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    height: 54px !important;
    box-sizing: border-box !important;
    width: 100% !important;
  }
  .mobile-menu-logo {
    height: 38px !important;
    max-height: 38px !important;
    width: auto !important;
    object-fit: contain !important;
    filter: brightness(0) invert(1) !important;
    margin: 0 !important;
  }
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace or inject CSS
    pattern_css = r'/\* ─+ \s* COMPACT MOBILE HEADER & SCROLL MARGIN CLIPPING FIX \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, COMPACT_HEADER_AND_SCROLL_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", COMPACT_HEADER_AND_SCROLL_CSS + "\n</style>", 1)

    # 2. Update JS handleMbnClick for header-offset smooth scrolling
    old_js = r'function handleMbnClick\(e, targetId, homePage\)\s*\{.*?\n\}'
    new_js = """function handleMbnClick(e, targetId, homePage) {
  if (e) e.preventDefault();
  closeMobileSheets();
  
  const currentPath = window.location.pathname;
  const isHomePage = currentPath.endsWith(homePage) || 
                     (homePage.includes('index') && (currentPath.endsWith('/') || currentPath.includes('index')));

  if (isHomePage) {
    const el = document.getElementById(targetId);
    if (el) {
      const headerOffset = window.innerWidth <= 768 ? 65 : 85;
      const elementPosition = el.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  } else {
    window.location.href = homePage + '#' + targetId;
  }
}"""
    if re.search(old_js, content, flags=re.DOTALL):
        content = re.sub(old_js, new_js, content, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Reduced mobile header height & fixed scroll clipping in {filename}")

def main():
    print("=== Reducing Mobile Header Height & Fixing Scroll Clipping Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
