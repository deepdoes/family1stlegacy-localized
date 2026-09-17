#!/usr/bin/env python3
"""
apply_section8_business_updates.py
Applies Section 8 (Business Strategies Page) updates to business_strategies_es.html:
- 8.1 Buy-sell agreement paragraph with legal-tax qualification
- 8.2 Business Legal & Tax Disclaimer footer note
- Section 1 Global Shared Components (Trust badges, contact sentence, disclosure, office hours)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "business_strategies_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 8.1 Buy-sell paragraph
BUY_SELL_NEW = "Sin un plan claro, la salida, fallecimiento o incapacidad de un propietario puede crear confusión entre socios, familiares, empleados y prestamistas. Un acuerdo buy-sell financiado puede ayudar a proporcionar una forma estructurada para que los propietarios restantes compren la participación de un propietario a un precio justo, al mismo tiempo que ayuda a proteger los intereses de la familia. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal."

# 8.2 Business legal & tax disclaimer
DISCLAIMER_NEW = "Aviso legal y fiscal para negocios: Las estrategias empresariales pueden implicar consideraciones legales y fiscales. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal."

html = re.sub(
    r'(<h2[^>]*>¿Qué sucede con el negocio si cambia la propiedad\?.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + BUY_SELL_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# Insert Disclaimer before FAQ or at end of content section
if "Aviso legal y fiscal para negocios" not in html:
    html = html.replace(
        '<section id="faq"',
        f'<div class="container" style="margin-top:40px; margin-bottom:40px;"><p style="font-size:12px; color:#64748B; font-style:italic;">{DISCLAIMER_NEW}</p></div>\n<section id="faq"'
    )

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Synchronized Section 8 on business_strategies_es.html")
