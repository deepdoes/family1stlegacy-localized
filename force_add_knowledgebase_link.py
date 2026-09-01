#!/usr/bin/env python3
"""
force_add_knowledgebase_link.py
Forces the addition of Knowledgebase & Articles to the Company footer list in index.html and ALL HTML files!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def force_update():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        is_es = "_es." in fname
        kb_text = "Base de Conocimiento y Artículos" if is_es else "Knowledgebase &amp; Articles"
        blog_link = "index_es.html#blog" if is_es else ("#blog" if fname == "index.html" else "index.html#blog")

        new_item = f'<li><a href="{blog_link}">{kb_text}</a></li>'

        if "Knowledgebase &amp; Articles" not in content and "Knowledgebase & Articles" not in content and "Base de Conocimiento" not in content:
            # Match Real Questions link and insert Knowledgebase right after
            content = re.sub(
                r'(<li><a href="[^"]*#reviews"[^>]*>.*?</a></li>)',
                r'\1\n            ' + new_item,
                content,
                flags=re.DOTALL
            )
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added '{kb_text}' to Company footer column in {fname}")
        else:
            # Ensure index.html specifically has #blog
            if fname == "index.html" and 'href="#blog"' not in content:
                content = content.replace('<li><a href="#reviews">Real Questions &amp; Guidance</a></li>', '<li><a href="#reviews">Real Questions &amp; Guidance</a></li>\n            <li><a href="#blog">Knowledgebase &amp; Articles</a></li>')
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  ✓ Added Knowledgebase to index.html footer")

def main():
    print("=== Force Inserting Knowledgebase to Footer Company Column ===")
    force_update()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
