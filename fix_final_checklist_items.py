#!/usr/bin/env python3
"""
fix_final_checklist_items.py
Fixes remaining audit items across all HTML files:
1. Replaces "100% Private" with "Privacy Respected" / "No-Cost Consultation".
2. Replaces "2,000+" in index_es, index_pt, index_rw, index_sw with "Thousands of Families".
3. Replaces "Estate Preservation" with "Estate & Legacy Planning".
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_all():
    print("=== Fixing Final Verification Checklist Items Across All Pages ===")
    
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    
    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Replace 100% Private
        content = content.replace("100% Private", "Privacy Respected")
        content = content.replace("100% private", "Privacy Respected")
        content = content.replace("100% Privado", "Privacidad Respetada")
        content = content.replace("100% privado", "Privacidad Respetada")

        # 2. Replace 2,000+ claim in index files
        content = content.replace("2,000+", "Thousands of")
        content = content.replace("2000+", "Thousands of")
        content = content.replace("2.000+", "Miles de")

        # 3. Replace Estate Preservation -> Estate & Legacy Planning
        content = content.replace("Estate Preservation", "Estate & Legacy Planning")
        content = content.replace("Preservación del Patrimonio", "Planificación de Patrimonio y Herencia")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Cleaned checklist items in {fname}")

def main():
    fix_all()

if __name__ == "__main__":
    main()
