#!/usr/bin/env python3
"""
add_mobile_app_bottom_nav_and_fix_top_gap.py
1. Fixes the large top gap above the logo in the mobile menu overlay across all HTML pages.
2. Injects a modern floating app-like bottom navigation bar on mobile screens.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

BOTTOM_NAV_CSS = """
/* ─────────────────────────────────────────────────────────────
   APP-LIKE FIXED BOTTOM MOBILE NAVIGATION BAR & LOGO GAP FIX
───────────────────────────────────────────────────────────── */
.mobile-menu {
  padding: 24px 24px 36px 24px !important;
  justify-content: flex-start !important;
  overflow-y: auto !important;
}

.mobile-menu-header {
  margin-top: 4px !important;
  margin-bottom: 20px !important;
  padding-bottom: 14px !important;
}

.mobile-bottom-nav {
  display: none;
}

@media (max-width: 768px) {
  .mobile-bottom-nav {
    display: flex !important;
    position: fixed !important;
    bottom: 14px !important;
    left: 14px !important;
    right: 14px !important;
    height: 62px !important;
    background: rgba(15, 12, 28, 0.92) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.16) !important;
    border-radius: 32px !important;
    z-index: 899 !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    align-items: center !important;
    justify-content: space-around !important;
    padding: 0 6px !important;
  }
  
  .mbn-item {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 3px !important;
    color: rgba(255, 255, 255, 0.75) !important;
    text-decoration: none !important;
    background: none !important;
    border: none !important;
    padding: 6px 10px !important;
    cursor: pointer !important;
    font-family: var(--font-body, sans-serif) !important;
    transition: all 0.2s ease !important;
  }
  
  .mbn-item svg {
    width: 20px !important;
    height: 20px !important;
    stroke: currentColor !important;
    transition: transform 0.2s ease !important;
  }
  
  .mbn-item span {
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 0.2px !important;
  }
  
  .mbn-item:hover, .mbn-item.active {
    color: #F5D061 !important;
  }
  
  .mbn-item:hover svg {
    transform: translateY(-2px) !important;
  }
  
  .mbn-cta {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 2px !important;
    background: linear-gradient(135deg, #1D9E75, #4A2D7A) !important;
    color: #FFFFFF !important;
    text-decoration: none !important;
    padding: 7px 14px !important;
    border-radius: 20px !important;
    box-shadow: 0 4px 14px rgba(29, 158, 117, 0.5) !important;
    transition: transform 0.2s ease !important;
  }
  
  .mbn-cta svg {
    width: 18px !important;
    height: 18px !important;
    stroke: #FFFFFF !important;
  }
  
  .mbn-cta span {
    font-size: 10px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
  }

  body {
    padding-bottom: 76px !important;
  }
}
"""

EN_BOTTOM_NAV_HTML = """
<!-- APP-LIKE FIXED BOTTOM NAVIGATION FOR MOBILE -->
<nav class="mobile-bottom-nav">
  <a href="index.html#hero" class="mbn-item active">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Home</span>
  </a>
  <a href="index.html#services" class="mbn-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Services</span>
  </a>
  <a href="#contact" class="mbn-cta">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consult</span>
  </a>
  <a href="index.html#reviews" class="mbn-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Stories</span>
  </a>
  <button class="mbn-item" onclick="document.querySelector('.mobile-menu').classList.add('open')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menu</span>
  </button>
</nav>
"""

ES_BOTTOM_NAV_HTML = """
<!-- APP-LIKE FIXED BOTTOM NAVIGATION FOR MOBILE -->
<nav class="mobile-bottom-nav">
  <a href="index_es.html#hero" class="mbn-item active">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 01-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Inicio</span>
  </a>
  <a href="index_es.html#services" class="mbn-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Servicios</span>
  </a>
  <a href="#contact" class="mbn-cta">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consulta</span>
  </a>
  <a href="index_es.html#reviews" class="mbn-item">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Historias</span>
  </a>
  <button class="mbn-item" onclick="document.querySelector('.mobile-menu').classList.add('open')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menú</span>
  </button>
</nav>
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Inject CSS if not present
    if "APP-LIKE FIXED BOTTOM MOBILE NAVIGATION BAR" not in content:
        if "</style>" in content:
            content = content.replace("</style>", BOTTOM_NAV_CSS + "\n</style>", 1)

    # 2. Inject Bottom Nav HTML if not present
    if "mobile-bottom-nav" not in content:
        nav_html = ES_BOTTOM_NAV_HTML if "_es.html" in filename else EN_BOTTOM_NAV_HTML
        if "</body>" in content:
            content = content.replace("</body>", nav_html + "\n</body>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Added mobile bottom nav & top gap fix to {filename}")

def main():
    print("=== Adding Mobile Bottom App Nav & Fixing Top Gap Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
