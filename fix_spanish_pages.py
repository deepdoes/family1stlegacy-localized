#!/usr/bin/env python3
"""
fix_spanish_pages.py
Phase 1+3 fixes for all _es.html Spanish pages:
  - Set lang="es" on <html>
  - Set page-specific Spanish <title>
  - Set page-specific Spanish <meta description>
  - Add hreflang alternate tags (en + es)
  - Fix broken hero headlines (word-by-word machine translation artifacts)
"""

import re
import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# --- Page metadata: (filename_es, title_es, description_es, filename_en) ---
PAGES = {
    "index_es.html": {
        "en": "index.html",
        "title": "Family First Legacy | Protegiendo lo que mas importa",
        "description": "Family First Legacy ayuda a las familias a construir seguridad financiera, proteger a sus seres queridos y crear legados duraderos a traves de seguros de vida, planificacion para la jubilacion y estrategias de creacion de riqueza.",
    },
    "family_protection_es.html": {
        "en": "family_protection.html",
        "title": "Proteccion Familiar | Family First Legacy",
        "description": "Descubra como los seguros de vida pueden proteger a su familia ante lo inesperado. Ofrecemos coberturas a medida de las principales aseguradoras de EE. UU. para garantizar la tranquilidad de sus seres queridos.",
    },
    "retirement_planning_es.html": {
        "en": "retirement_planning.html",
        "title": "Planificacion de Jubilacion | Family First Legacy",
        "description": "Cree una estrategia de jubilacion adaptada a su horizonte temporal y metas financieras. Le ayudamos a asegurar ingresos libres de impuestos y proteger su principal para disfrutar de sus anos dorados.",
    },
    "education_planning_es.html": {
        "en": "education_planning.html",
        "title": "Planificacion Educativa | Family First Legacy",
        "description": "Invierta en el futuro de sus hijos con estrategias de ahorro para la educacion que crecen libres de impuestos, no afectan la ayuda financiera y pueden usarse para cualquier sueno que elijan.",
    },
    "estate_planning_es.html": {
        "en": "estate_planning.html",
        "title": "Planificacion Patrimonial | Family First Legacy",
        "description": "Preserve y transmita su legado a las generaciones futuras. Le ayudamos a estructurar su patrimonio para que su familia reciba proteccion y riqueza mucho despues de que usted haya partido.",
    },
    "financial_strategy_es.html": {
        "en": "financial_strategy.html",
        "title": "Estrategia Financiera | Family First Legacy",
        "description": "Desarrolle una estrategia financiera integral que combine seguros de vida, crecimiento con ventajas fiscales y diversificacion de activos para construir riqueza generacional de forma segura.",
    },
    "privacy_es.html": {
        "en": "privacy.html",
        "title": "Politica de Privacidad | Family First Legacy",
        "description": "Lea nuestra politica de privacidad para entender como Family First Legacy recopila, utiliza y protege su informacion personal de conformidad con las leyes aplicables.",
    },
    "terms_es.html": {
        "en": "terms.html",
        "title": "Terminos de Servicio | Family First Legacy",
        "description": "Conozca los terminos y condiciones que rigen el uso del sitio web y los servicios de Family First Legacy.",
    },
    "blog_education_es.html": {
        "en": "blog_education.html",
        "title": "Blog: Planificacion Educativa | Family First Legacy",
        "description": "Lea nuestros articulos sobre como financiar la educacion de sus hijos con estrategias inteligentes, libres de impuestos y mas flexibles que un plan 529.",
    },
    "blog_family_protection_es.html": {
        "en": "blog_family_protection.html",
        "title": "Blog: Proteccion Familiar | Family First Legacy",
        "description": "Consejos expertos sobre seguros de vida, beneficios en vida y como asegurar el futuro financiero de su familia ante cualquier eventualidad.",
    },
    "blog_financial_strategy_es.html": {
        "en": "blog_financial_strategy.html",
        "title": "Blog: Estrategia Financiera | Family First Legacy",
        "description": "Articulos sobre IUL, rentas vitalicias, diversificacion de activos y como construir riqueza generacional con estrategias financieras inteligentes.",
    },
    "blog_legacy_es.html": {
        "en": "blog_legacy.html",
        "title": "Blog: Legado y Patrimonio | Family First Legacy",
        "description": "Aprenda a planificar su legado, proteger su patrimonio y asegurarse de que sus valores y riqueza se transmitan a las generaciones futuras.",
    },
    "blog_retirement_es.html": {
        "en": "blog_retirement.html",
        "title": "Blog: Planificacion de Jubilacion | Family First Legacy",
        "description": "Estrategias para una jubilacion segura y libre de impuestos. Descubra como diversificar mas alla del 401(k) y crear ingresos garantizados para sus anos dorados.",
    },
}

# --- Hero headline fixes for index_es.html ---
INDEX_ES_FIXES = [
    # Slide 1: Family Protection - "OMS" is WHO (World Health Organization) - wrong!
    (
        'Proteger a la gente<br/>OMS<em>Lo más importante</em>',
        'Protegemos a las personas<br/>que<em>más te importan</em>'
    ),
    (
        'Proteger a la gente<br/>OMS<em>Lo m\u00e1s importante</em>',
        'Protegemos a las personas<br/>que<em>m\u00e1s te importan</em>'
    ),
    # Slide 2: Retirement
    (
        'Tus años dorados,<br/><em>Totalmente financiado</em>',
        'Tus a\u00f1os dorados,<br/><em>totalmente asegurados</em>'
    ),
    (
        'Tus a\u00f1os dorados,<br/><em>Totalmente financiado</em>',
        'Tus a\u00f1os dorados,<br/><em>totalmente asegurados</em>'
    ),
    # Slide 3: Education
    (
        'Invierta en sus<br/><em>Futuro brillante</em>',
        'Invierte en su<br/><em>futuro brillante</em>'
    ),
    # Slide 4: Legacy
    (
        'Deja un legado<br/>Eso<em>Dura generaciones</em>',
        'Deja un legado<br/>que<em>dure generaciones</em>'
    ),
    # Slide 5: Business
    (
        'Proteger el negocio<br/>Tú<em>Construido</em>',
        'Protege el negocio<br/>que<em>construiste</em>'
    ),
    (
        'Proteger el negocio<br/>T\u00fa<em>Construido</em>',
        'Protege el negocio<br/>que<em>construiste</em>'
    ),
]

def fix_head(content, page_key):
    info = PAGES[page_key]
    en_file = info["en"]
    title_es = info["title"]
    desc_es = info["description"]

    # 1. Fix lang="en" -> lang="es"
    content = re.sub(r'<html\s+lang="en"', '<html lang="es"', content, count=1)
    content = re.sub(r'<html>', '<html lang="es">', content, count=1)

    # 2. Fix <title>
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{title_es}</title>',
        content, count=1, flags=re.DOTALL
    )

    # 3. Fix <meta name="description">
    content = re.sub(
        r'<meta\s+(?:name="description"\s+content="[^"]*"|content="[^"]*"\s+name="description")[^/]*/?>',
        f'<meta name="description" content="{desc_es}"/>',
        content, count=1
    )

    # 4. Add hreflang tags after </title> if not already present
    if 'hreflang' not in content:
        hreflang_block = (
            f'\n<link rel="alternate" hreflang="en" href="https://family1stlegacy.com/{en_file}"/>'
            f'\n<link rel="alternate" hreflang="es" href="https://family1stlegacy.com/{page_key}"/>'
            f'\n<link rel="alternate" hreflang="x-default" href="https://family1stlegacy.com/{en_file}"/>'
        )
        content = content.replace('</title>', f'</title>{hreflang_block}', 1)

    return content


def process_file(filename):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print(f"  NOT FOUND: {filename}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)
    content = fix_head(content, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  OK: {filename} ({original_len} -> {len(content)} bytes)")


def fix_index_es_headlines():
    filepath = os.path.join(BASE, "index_es.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fixed = 0
    for broken, replacement in INDEX_ES_FIXES:
        if broken in content:
            content = content.replace(broken, replacement)
            print(f"  Fixed: '{broken[:50]}...'")
            fixed += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Total headline fixes applied to index_es.html: {fixed}")


def main():
    print("=== Phase 1: Fix head metadata across all _es.html pages ===")
    for filename in PAGES:
        process_file(filename)

    print("\n=== Phase 3: Fix broken hero headlines in index_es.html ===")
    fix_index_es_headlines()

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
