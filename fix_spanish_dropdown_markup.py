#!/usr/bin/env python3
"""
fix_spanish_dropdown_markup.py
Fixes class name to 'nav-dropdown-wrap' and SVG stroke attributes for the Servicios dropdown
across all Spanish HTML files.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CORRECT_SPANISH_DROPDOWN_HTML = """<li class="nav-dropdown-wrap">
          <a href="index_es.html#services" class="nav-dropdown-toggle">Servicios <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg></a>
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

    # Replace any previous has-dropdown or malformed dropdown block
    pattern = r'<li class="(?:has-dropdown|nav-dropdown-wrap)">\s*<a href="[^"]*#services"[^>]*>Servicios.*?</ul>\s*</li>'
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, CORRECT_SPANISH_DROPDOWN_HTML, content, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Fixed Servicios dropdown markup in {filename}")
    else:
        print(f"  ⚠️ Could not find dropdown pattern in {filename}")

def main():
    print("=== Fixing Servicios Dropdown Markup Across All Spanish Pages ===")
    es_files = [f for f in os.listdir(BASE) if f.endswith("_es.html")]
    for fname in sorted(es_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
