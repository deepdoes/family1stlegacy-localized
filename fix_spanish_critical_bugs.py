#!/usr/bin/env python3
"""
fix_spanish_critical_bugs.py
Fixes critical bugs found in the Spanish pages audit:

1. Wrong phone number: (214) 555-0100 -> (469) 608-1595 across ALL _es and _pt _rw _sw files
2. Wrong display URL: familia1stlegacy.com -> family1stlegacy.com in ALL _es files
3. Untranslated form placeholders in ALL _es files
4. 'Switch Language' tooltip -> 'Cambiar idioma' in ALL _es files
5. 'Vía de Servício' typo -> 'Área de Servicio' in ALL _es files
6. 'Parque Sara y David' -> 'Sara y David Park' in index_es.html
7. 'Family First Legacy Equipo' -> 'El Equipo de Family First Legacy'
8. lowercase 'ponemos familia' -> 'Ponemos a la Familia'
"""

import os
import glob

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# --- Fixes to apply to ALL _es.html files ---
ES_FIXES = [
    # Wrong phone number (fake placeholder -> real number)
    ("214-555-0100", "469-608-1595"),
    ("12145550100", "14696081595"),
    ("(214) 555-0100", "(469) 608-1595"),
    ("2145550100", "4696081595"),
    # Wrong display URL in footer
    ("familia1stlegacy.com", "family1stlegacy.com"),
    # Untranslated form placeholders
    ('placeholder="Enter your email address"', 'placeholder="Ingrese su correo electrónico"'),
    ('placeholder="Tell us about your goals or questions…"', 'placeholder="Cuéntenos sus objetivos o preguntas…"'),
    ('placeholder="Tell us about your goals or questions..."', 'placeholder="Cuéntenos sus objetivos o preguntas…"'),
    # 'Switch Language' tooltip
    ('title="Switch Language"', 'title="Cambiar idioma"'),
    # Typo: Servício -> Servicio
    ("Vía de Servício", "Área de Servicio"),
    ("Vía de Servicio", "Área de Servicio"),
]

# --- Fixes specific to index_es.html ---
INDEX_ES_SPECIFIC_FIXES = [
    # Reviewer name machine-translated
    ("Parque Sara y David", "Sara y David Park"),
    # Team attribution
    ("— Family First Legacy Equipo", "— El Equipo de Family First Legacy"),
    # Lowercase heading
    ("ponemos familia Primero. Siempre.", "Ponemos a la Familia Primero. Siempre."),
    # Fix: "Totalmente financiado" -> "totalmente asegurados" (already handled by fix_spanish_pages.py for <br/> version)
    # Cover plain text version too
    ("Totalmente financiado", "totalmente asegurados"),
]


def fix_file(filepath, fixes):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    applied = []
    for old, new in fixes:
        if old in content:
            content = content.replace(old, new)
            applied.append(old[:50])

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  OK: {os.path.basename(filepath)} — Fixed: {len(applied)} issues")
        for a in applied:
            print(f"    - '{a}'")
    else:
        print(f"  CLEAN: {os.path.basename(filepath)} — No changes needed")


def main():
    print("=== Fixing critical bugs in all _es.html files ===\n")

    es_files = sorted(glob.glob(os.path.join(BASE, "*_es.html")))
    for filepath in es_files:
        fix_file(filepath, ES_FIXES)

    print("\n=== Fixing index_es.html specific issues ===\n")
    index_es = os.path.join(BASE, "index_es.html")
    fix_file(index_es, INDEX_ES_SPECIFIC_FIXES)

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
