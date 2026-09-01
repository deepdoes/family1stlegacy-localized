#!/usr/bin/env python3
"""
clean_top_nav_duplicate_kb.py
Removes the accidental duplicate 'Knowledgebase & Articles' item from the top header navigation bar (<ul class="nav-links">)
across all HTML files, ensuring the top header contains only ONE clean 'Knowledgebase' link!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def cleanup():
    files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove duplicate top nav items
        targets = [
            '<li><a href="index.html#blog">Knowledgebase & Articles</a></li>\n',
            '<li><a href="index.html#blog">Knowledgebase &amp; Articles</a></li>\n',
            '<li><a href="index_es.html#blog">Base de Conocimiento y Artículos</a></li>\n',
            '<li><a href="index_es.html#blog">Base de conocimiento y artículos</a></li>\n',
            '            <li><a href="index.html#blog">Knowledgebase & Articles</a></li>',
            '            <li><a href="index.html#blog">Knowledgebase &amp; Articles</a></li>',
            '            <li><a href="index_es.html#blog">Base de Conocimiento y Artículos</a></li>',
            '            <li><a href="index_es.html#blog">Base de conocimiento y artículos</a></li>',
        ]

        updated = False
        # Only clean inside <header id="nav"> ... </header>
        header_match = re.search(r'<header id="nav">.*?</header>', content, flags=re.DOTALL)
        if header_match:
            header_html = header_match.group(0)
            new_header = header_html
            for t in targets:
                if t in new_header:
                    new_header = new_header.replace(t, '')
                    updated = True
            
            if updated:
                content = content.replace(header_html, new_header)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  ✓ Cleaned top navbar duplicate link in {fname}")

def main():
    print("=== Cleaning Duplicate Top Navbar Links ===")
    cleanup()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
