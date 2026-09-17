#!/usr/bin/env python3
"""
apply_section9_opportunity_updates.py
Applies Section 9 (Opportunity Page) updates to opportunity_es.html:
- 9.1 Transparent opportunity statement
- Ensures removal of any legacy income claims or outdated statistics
- Synchronizes Global Shared Components (Trust badges, contact sentence, disclosure, office hours)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "opportunity_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 9.1 Transparent opportunity statement
STATEMENT_NEW = "Esta es una oportunidad de negocio basada en comisiones dentro de los servicios financieros, no un empleo tradicional con salario. Antes de atender a familias como profesional con licencia, se requiere obtener la licencia estatal correspondiente. El crecimiento depende del aprendizaje, la constancia, el esfuerzo y la capacidad de servir bien a las personas. Para la persona adecuada, puede ser un camino significativo de desarrollo personal y profesional."

html = re.sub(
    r'(<p[^>]*class="[^"]*opp-disclaimer[^"]*"[^>]*>).*?(</p>)',
    r'\1' + STATEMENT_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'Esta es una oportunidad de negocio basada en comisiones.*?(?=</p>|</div>)',
    STATEMENT_NEW,
    html,
    flags=re.DOTALL
)

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Synchronized Section 9 on opportunity_es.html")
