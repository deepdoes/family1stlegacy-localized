#!/usr/bin/env python3
"""
add_spanish_services_dropdown.py
Adds the interactive Services dropdown menu (Servicios ˅) to the top navigation bar
across all Spanish HTML files, matching the English header.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SPANISH_DROPDOWN_HTML = """<li class="has-dropdown">
          <a href="index_es.html#services" class="nav-dropdown-toggle">Servicios <svg class="chevron" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></a>
          <ul class="nav-dropdown">
            <li><a href="family_protection_es.html" class="no-pill">Seguro de Vida</a></li>
            <li><a href="retirement_planning_es.html" class="no-pill">Planificación de Jubilación</a></li>
            <li><a href="education_planning_es.html" class="no-pill">Planificación Educativa</a></li>
            <li><a href="estate_planning_es.html" class="no-pill">Planificación del Patrimonio y Legado</a></li>
            <li><a href="financial_strategy_es.html" class="no-pill">Estrategia Financiera</a></li>
            <li><a href="business_strategies_es.html" class="no-pill">Estrategias para Negocios</a></li>
          </ul>
        </li>"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Targets: <li><a href="#services">Servicios</a></li> OR <li><a href="index_es.html#services">Servicios</a></li>
    old_item_1 = '<li><a href="#services">Servicios</a></li>'
    old_item_2 = '<li><a href="index_es.html#services">Servicios</a></li>'
    old_item_3 = '<li><a href="#services" class="nav-active">Servicios</a></li>'

    if 'class="has-dropdown"' in content and 'Seguro de Vida' in content:
        print(f"  ✓ Already has Spanish dropdown: {filename}")
        return

    if old_item_1 in content:
        content = content.replace(old_item_1, SPANISH_DROPDOWN_HTML)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Added Servicios dropdown to {filename}")
    elif old_item_2 in content:
        content = content.replace(old_item_2, SPANISH_DROPDOWN_HTML)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Added Servicios dropdown to {filename}")
    elif old_item_3 in content:
        content = content.replace(old_item_3, SPANISH_DROPDOWN_HTML)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Added Servicios dropdown to {filename}")
    else:
        # Regex replacement for any variant
        pattern = r'<li><a href="[^"]*#services"[^>]*>Servicios</a></li>'
        if re.search(pattern, content):
            content = re.sub(pattern, SPANISH_DROPDOWN_HTML, content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Regex added Servicios dropdown to {filename}")
        else:
            print(f"  ⚠️ Could not find Servicios nav item in {filename}")

def main():
    print("=== Adding Servicios Dropdown Menu to All Spanish Pages ===")
    es_files = [f for f in os.listdir(BASE) if f.endswith("_es.html")]
    for fname in sorted(es_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
