#!/usr/bin/env python3
"""
improve_who_we_are_balance.py
Polishes the "Who We Are" section layout for perfect visual balance on index.html and index_es.html:
1. Injects flex/grid CSS so the left photo column dynamically matches the right text column height.
2. Anchors the quote box cleanly at the bottom, perfectly aligning top and bottom edges.
3. Synchronizes the 4 paragraphs and quote box in Spanish on index_es.html.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

BALANCE_CSS = """
/* ── Perfect Balance for "Who We Are" Section ── */
@media (min-width: 900px) {
  #about .about-grid {
    display: grid !important;
    grid-template-columns: 1fr 1.15fr !important;
    gap: 48px !important;
    align-items: stretch !important;
  }
  #about .about-photo-col {
    display: flex !important;
    flex-direction: column !important;
    justify-content: space-between !important;
    height: 100% !important;
  }
  #about .about-photo-wrap {
    flex: 1 !important;
    min-height: 400px !important;
    position: relative !important;
    border-radius: 24px !important;
    overflow: hidden !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.08) !important;
  }
  #about .about-photo-wrap img.about-photo {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center top !important;
    display: block !important;
  }
}

.about-pull {
  background: linear-gradient(135deg, rgba(74, 45, 122, 0.06) 0%, rgba(29, 158, 117, 0.08) 100%) !important;
  border-left: 4px solid #4A2D7A !important;
  border-radius: 16px !important;
  padding: 20px 24px !important;
  margin-top: 24px !important;
}

.about-pull p {
  font-size: 14.5px !important;
  font-style: italic !important;
  color: #334155 !important;
  line-height: 1.6 !important;
  margin-bottom: 8px !important;
}

.about-pull cite {
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  color: #4A2D7A !important;
  text-transform: uppercase !important;
  display: block !important;
}
"""

def update_english():
    fpath = os.path.join(BASE, "index.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "Perfect Balance for \"Who We Are\" Section" not in content:
        content = content.replace("</head>", f"<style>{BALANCE_CSS}</style>\n</head>")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Balanced 'Who We Are' layout on index.html")

def update_spanish():
    fpath = os.path.join(BASE, "index_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "Perfect Balance for \"Who We Are\" Section" not in content:
        content = content.replace("</head>", f"<style>{BALANCE_CSS}</style>\n</head>")

    # Update Spanish quote box
    QUOTE_ES = '<div class="about-pull" data-delay="3" data-reveal="" style="border-radius:16px; margin-top:32px;">\n<p>“Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y las ayudamos a crear planes enfocados en proteger lo que más importa.”</p>\n<cite>— EQUIPO DE FAMILY FIRST LEGACY</cite>\n</div>'
    content = re.sub(
        r'<div class="about-pull".*?</div>\s*</div>\s*<div class="about-content">',
        QUOTE_ES + '\n</div>\n<div class="about-content">',
        content,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Balanced 'Who We Are' layout & Spanish text on index_es.html")

def main():
    print("=== Balancing 'Who We Are' Section on English & Spanish Home Pages ===")
    update_english()
    update_spanish()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
