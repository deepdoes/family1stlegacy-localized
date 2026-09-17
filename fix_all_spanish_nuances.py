#!/usr/bin/env python3
"""
fix_all_spanish_nuances.py
Fixes exact string mismatches across all 16 Spanish HTML files to guarantee 100% test pass.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_files():
    html_files = [f for f in os.listdir(BASE) if f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in html_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Key Takeaways header in blog pages
        content = content.replace("⚡ Key Takeaways", "⚡ Puntos clave")
        content = content.replace("Key Takeaways", "Puntos clave")

        # 2. Newsletter button and placeholder
        content = content.replace('placeholder="Ingresa tu correo electrónico electrónico"', 'placeholder="Ingresa tu correo electrónico"')
        content = content.replace('>Suscribir<', '>SUSCRIBIRME<')
        content = content.replace('>Suscribirse<', '>SUSCRIBIRME<')
        content = content.replace('>SUSCRIBIRSE<', '>SUSCRIBIRME<')

        # 3. Estate Planning proof cards (estate_planning_es.html)
        if fname == "estate_planning_es.html":
            content = content.replace("LOS BENEFICIOS DEL TRABAJO PUEDEN DEJAR BRECHAS", "TUS DESEOS IMPORTAN")
            content = content.replace("SI LOS INGRESOS SE DETIENEN", "TRANSFERENCIAS MÁS SENCILLAS")
            content = content.replace("EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO", "PLANIFICACIÓN CON CONCIENCIA FISCAL")
            content = content.replace("REVISIÓN SIN COSTO", "TRANQUILIDAD")

        # 4. Home page proof section (index_es.html)
        if fname == "index_es.html":
            content = content.replace("YOUR FAMILY. OUR FOCUS.", "TU FAMILIA. NUESTRO ENFOQUE.")
            content = content.replace("Tu Familia. Nuestro Enfoque.", "TU FAMILIA. NUESTRO ENFOQUE.")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Processed {fname}")

if __name__ == "__main__":
    print("=== Fixing Spanish nuances and exact master strings ===")
    fix_files()
    print("=== Done! ===")
