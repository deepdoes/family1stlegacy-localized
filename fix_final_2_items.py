#!/usr/bin/env python3
"""
fix_final_2_items.py
Fixes:
1. estate_planning_es.html line 9914: PLANIFICACIÓN FISCAL -> PLANIFICACIÓN CON CONCIENCIA FISCAL
2. blog_living_benefits_es.html: English footer newsletter -> Spanish footer newsletter
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_estate():
    fpath = os.path.join(BASE, "estate_planning_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("PLANIFICACIÓN FISCAL", "PLANIFICACIÓN CON CONCIENCIA FISCAL")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Fixed estate_planning_es.html proof card 3 label")

def fix_blog4():
    fpath = os.path.join(BASE, "blog_living_benefits_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("Stay in the know.", "Mantente informado.")
    html = html.replace("Enter your email address", "Ingresa tu correo electrónico")
    html = html.replace(">Subscribe<", ">SUSCRIBIRME<")
    html = html.replace("Subscribe\n", "SUSCRIBIRME\n")
    html = html.replace("Monthly insights on family protection, financial planning, and preparing for the future. Unsubscribe anytime.", "Información mensual sobre protección familiar, planificación financiera y preparación para el futuro. Puedes cancelar tu suscripción en cualquier momento.")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Fixed blog_living_benefits_es.html footer newsletter")

def main():
    fix_estate()
    fix_blog4()

if __name__ == "__main__":
    main()
