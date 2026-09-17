#!/usr/bin/env python3
"""
restore_perfect_who_we_are_layout.py
Restores the original, un-clipped, perfectly proportioned "Who We Are" layout on index.html and index_es.html:
1. Removes the experimental stretch CSS that clipped the floating pill badges and cropped the advisors' faces.
2. Ensures floating badges (.about-badge top right, .about-photo-tag bottom right) are 100% visible and un-clipped.
3. Synchronizes index_es.html structure 1:1 with index.html master.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def clean_file(fname, is_spanish=False):
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove experimental CSS
    content = re.sub(r'/\* ── Perfect Balance for "Who We Are" Section ── \*/.*?</style>', '', content, flags=re.DOTALL)

    if is_spanish:
        # Match English structure 1:1 for Spanish
        SPANISH_PHOTO_COL = """<div class="about-photo-col">
        <div class="about-photo-wrap" data-reveal="left">
          <img class="about-photo" src="images/about.jpg" alt="Equipo de Family First Legacy" loading="lazy">
          <div class="about-badge">
            <div class="ab-dot"></div>
            <div class="ab-text">Sirviendo a familias en todo el país</div>
          </div>
          <div class="about-photo-tag">
            <div class="apt-num" style="font-size:14px; font-weight:800; color:#fff;">TU FAMILIA.</div>
            <div class="apt-label" style="font-weight:700; color:var(--amber-lt);">NUESTRO ENFOQUE.</div>
          </div>
        </div>
        <div class="about-pull" data-reveal data-delay="3" style="border-radius:16px; margin-top:32px;">
          <p>“Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y las ayudamos a crear planes enfocados en proteger lo que más importa.”</p>
          <cite>— EQUIPO DE FAMILY FIRST LEGACY</cite>
        </div>
      </div>"""

        # Replace photo col in Spanish index_es.html
        content = re.sub(
            r'<div class="about-photo-col">.*?</div>\s*<div class="about-content">',
            SPANISH_PHOTO_COL + '\n\n      <div class="about-content">',
            content,
            flags=re.DOTALL
        )

        # Ensure quote box is NOT duplicated in about-content
        content = re.sub(
            r'(<div class="about-content">.*?<a href="#contact" class="btn btn-green".*?</a>)\s*<div class="about-pull".*?</div>',
            r'\1',
            content,
            flags=re.DOTALL
        )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Restored clean 'Who We Are' section on {fname}")

def main():
    print("=== Restoring Original Clean 'Who We Are' Layout ===")
    clean_file("index.html", is_spanish=False)
    clean_file("index_es.html", is_spanish=True)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
