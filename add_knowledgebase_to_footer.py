#!/usr/bin/env python3
"""
add_knowledgebase_to_footer.py
Adds 'Knowledgebase & Articles' to the COMPANY column in the footer across all HTML files
(English and Spanish) so that visitors can easily navigate to educational guides from the footer!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_footers():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        is_es = "_es." in fname
        link_text = "Base de conocimiento y artículos" if is_es else "Knowledgebase & Articles"
        home_target = "index_es.html#blog" if is_es else "index.html#blog"

        new_link_html = f'<li><a href="{home_target}">{link_text}</a></li>'

        # Target after Real Questions & Guidance link
        target_en = '<li><a href="index.html#reviews">Real Questions & Guidance</a></li>'
        target_es = '<li><a href="index_es.html#reviews">Preguntas reales y orientación</a></li>'

        updated = False
        if "Knowledgebase & Articles" not in content and "Base de conocimiento" not in content:
            if target_en in content:
                content = content.replace(target_en, f'{target_en}\n          {new_link_html}')
                updated = True
            elif target_es in content:
                content = content.replace(target_es, f'{target_es}\n          {new_link_html}')
                updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added '{link_text}' to footer in {fname}")

def main():
    print("=== Adding Knowledgebase & Articles to Footer Across All Pages ===")
    update_footers()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
