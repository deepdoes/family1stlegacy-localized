#!/usr/bin/env python3
"""
add_knowledgebase_to_company_footer.py
Adds 'Knowledgebase & Articles' to the COMPANY column in the footer across all HTML files
(English and Spanish) right after 'Real Questions & Guidance'.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def apply_footer_update():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        is_es = "_es." in fname
        kb_text = "Base de Conocimiento y Artículos" if is_es else "Knowledgebase & Articles"
        blog_link = "index_es.html#blog" if is_es else "index.html#blog"
        new_item = f'<li><a href="{blog_link}">{kb_text}</a></li>'

        updated = False

        if "Knowledgebase &" not in content and "Base de Conocimiento y" not in content:
            # Match Company list and inject Knowledgebase
            content = re.sub(r'(<li><a href="[^"]*#reviews"[^>]*>.*?</a></li>)', r'\1\n            ' + new_item, content, count=1)
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added '{kb_text}' to Company footer column in {fname}")

def main():
    print("=== Adding Knowledgebase & Articles to Footer Company Column ===")
    apply_footer_update()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
