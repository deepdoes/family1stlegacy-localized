#!/usr/bin/env python3
"""
fix_spanish_svg_and_dropdown_style.py
Adds explicit inline width/height/stroke styles directly onto the chevron SVG and nav-dropdown elements
across all Spanish HTML files to guarantee zero SVG scaling overflow in any browser.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

EXACT_SPANISH_DROPDOWN_HTML = """<li class="nav-dropdown-wrap" style="position:relative;">
          <a href="index_es.html#services" class="nav-dropdown-toggle">Servicios <svg class="chevron" viewBox="0 0 24 24" style="width:10px; height:10px; min-width:10px; min-height:10px; stroke:currentColor; fill:none; stroke-width:2.5px; display:inline-block; vertical-align:middle; margin-left:4px;"><path d="M6 9l6 6 6-6"/></svg></a>
          <ul class="nav-dropdown">
            <li><a href="family_protection_es.html" class="no-pill">Seguro de Vida</a></li>
            <li><a href="retirement_planning_es.html" class="no-pill">Planificación de Jubilación</a></li>
            <li><a href="education_planning_es.html" class="no-pill">Planificación Educativa</a></li>
            <li><a href="estate_planning_es.html" class="no-pill">Planificación del Patrimonio y Legado</a></li>
            <li><a href="financial_strategy_es.html" class="no-pill">Estrategia Financiera</a></li>
            <li><a href="business_strategies_es.html" class="no-pill">Estrategias para Negocios</a></li>
          </ul>
        </li>"""

def fix_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<li class="nav-dropdown-wrap"[^>]*>.*?<ul class="nav-dropdown">.*?</ul>\s*</li>'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, EXACT_SPANISH_DROPDOWN_HTML, content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Applied inline SVG constraints to {filename}")
    else:
        print(f"  ⚠️ Could not find dropdown pattern in {filename}")

def main():
    print("=== Applying Inline SVG and Dropdown Styles to Spanish Pages ===")
    es_files = [f for f in os.listdir(BASE) if f.endswith("_es.html")]
    for fname in sorted(es_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
