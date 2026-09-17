#!/usr/bin/env python3
"""
fix_spanish_who_we_are_title.py
Fixes the 4-line title wrapping on index_es.html:
- Changes <h2 class="t-h1"> from 4 lines down to 2 clean, elegant lines:
  "Ponemos a la familia primero.<br/>Siempre."
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "index_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

OLD_TITLE = '<h2 class="t-h1" data-delay="1" data-reveal="">Ponemos a la familia<br/>primero. Siempre.</h2>'
NEW_TITLE = '<h2 class="t-h1" data-delay="1" data-reveal="" style="font-size: clamp(28px, 3.2vw, 42px); line-height: 1.2; margin-bottom: 24px;">Ponemos a la familia primero.<br/>Siempre.</h2>'

html = html.replace(OLD_TITLE, NEW_TITLE)

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Fixed title line breaks on index_es.html")
