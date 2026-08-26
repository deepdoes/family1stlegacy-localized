#!/usr/bin/env python3
"""
update_menu_label_to_qa.py
Updates the menu navigation label for Section 05 across all HTML files:
- English pages: Change 'Stories' / 'Real Questions & Guidance' -> 'Q&A'
- Spanish pages: Change 'Historias' / 'Preguntas Reales' -> 'Preguntas'
Applies to Desktop Header, Mobile Overlay Menu, Footer, Mobile Bottom Drawer Sheet, and Floating Bottom Bar.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    is_spanish = "_es.html" in filename

    if is_spanish:
        # Replace Spanish nav links
        content = content.replace('>Historias<', '>Preguntas<')
        content = content.replace('>Preguntas Reales & Guía<', '>Preguntas<')
        content = content.replace('>Preguntas Reales y Guía<', '>Preguntas<')
        content = content.replace('>Preguntas Reales<', '>Preguntas<')
        content = content.replace('<span>Historias</span>', '<span>Preguntas</span>')
    else:
        # Replace English nav links
        content = content.replace('>Stories<', '>Q&A<')
        content = content.replace('>Real Questions & Guidance<', '>Q&A<')
        content = content.replace('>Real Questions. Clear Guidance.<', '>Q&A<')
        content = content.replace('<span>Stories</span>', '<span>Q&A</span>')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Updated menu label in {filename}")

def main():
    print("=== Updating Navigation Label to Q&A / Preguntas Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
