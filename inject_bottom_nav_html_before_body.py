#!/usr/bin/env python3
"""
inject_bottom_nav_html_before_body.py
Guarantees mobile-bottom-nav HTML is placed before </body> across all active HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

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
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
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

def fix_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    nav_html = ES_BOTTOM_NAV_HTML if "_es.html" in filename else EN_BOTTOM_NAV_HTML

    # If nav tag isn't inside content HTML:
    if '<nav class="mobile-bottom-nav">' not in content:
        if "</body>" in content:
            content = content.replace("</body>", nav_html + "\n</body>", 1)
        elif "</html>" in content:
            content = content.replace("</html>", nav_html + "\n</html>", 1)
        
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Injected nav HTML into {filename}")
    else:
        print(f"  ✓ Nav HTML already in {filename}")

def main():
    print("=== Ensuring Mobile Bottom Nav HTML in All Files ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
