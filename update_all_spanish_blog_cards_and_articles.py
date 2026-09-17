#!/usr/bin/env python3
"""
update_all_spanish_blog_cards_and_articles.py
1. Updates all 6 Knowledgebase article cards on index_es.html to match client's pre-approved Spanish text and links to blog_living_benefits_es.html for Card 4.
2. Ensures all 6 Spanish blog article pages (blog_*_es.html) have updated trust badges in sidebars.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_homepage_blog_cards():
    fpath = os.path.join(BASE, "index_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Card 1 (Family Protection)
    html = re.sub(
        r'(<div class="bc-cat">PROTECCIÓN FAMILIAR</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_family_protection\.html|blog_family_protection_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿Tu familia depende solo de los beneficios del trabajo?\2El seguro de vida del empleador puede ser un beneficio útil. Para muchas familias trabajadoras y profesionales, puede ser el primer tipo de protección que reciben. Como viene a través del trabajo, puede parecer sencillo, conveniente y fácil de confiar.\3blog_family_protection_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    # Card 2 (Retirement)
    html = re.sub(
        r'(<div class="bc-cat">JUBILACIÓN</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_retirement\.html|blog_retirement_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿Podrían los impuestos reducir los ingresos de jubilación con los que cuentas?\2Un 401(k) puede ser una herramienta valiosa para la jubilación. Para muchas familias trabajadoras, es uno de los primeros lugares donde comienzan a ahorrar para el futuro, especialmente cuando el empleador ofrece aportaciones equivalentes.\3blog_retirement_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    # Card 3 (Education)
    html = re.sub(
        r'(<div class="bc-cat">EDUCACIÓN</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_education\.html|blog_education_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿Qué pasa si el camino de tu hijo cambia después de haber ahorrado?\2Todo padre desea dar a sus hijos un buen comienzo. Para muchas familias, eso significa comenzar a ahorrar temprano, reducir la necesidad de préstamos estudiantiles y darles a sus hijos más opciones para el futuro.\3blog_education_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    # Card 4 (Living Benefits - Fix link!)
    html = re.sub(
        r'(<div class="bc-cat">BENEFICIOS EN VIDA</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_living_benefits\.html|blog_living_benefits_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no?\2La mayoría de las familias saben que la vida puede cambiar cuando alguien fallece. Pero muchas no están preparadas para otra realidad dolorosa: a veces una persona sobrevive a la enfermedad, pero los ingresos de la familia no sobreviven con ella.\3blog_living_benefits_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    # Card 5 (Financial Strategy)
    html = re.sub(
        r'(<div class="bc-cat">ESTRATEGIA FINANCIERA</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_financial_strategy\.html|blog_financial_strategy_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿El tiempo está trabajando a favor de tu dinero, o en contra?\2La mayoría de las familias trabajan duro. Pagan sus cuentas, cuidan de sus hijos, apoyan a sus seres queridos y tratan de ahorrar lo que pueden. Pero incluso con buenas intenciones, muchas veces se pasa por alto una pregunta importante:\3blog_financial_strategy_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    # Card 6 (Estate Planning)
    html = re.sub(
        r'(<div class="bc-cat">PLANIFICACIÓN PATRIMONIAL Y DE LEGADO</div>\s*<h3 class="bc-title">).*?(</h3>\s*<p class="bc-excerpt">).*?(</p>\s*<div class="bc-footer">\s*<a href=")(?:blog_legacy\.html|blog_legacy_es\.html)(" class="bc-link">).*?(</a>)',
        r'\1¿Tu familia tendrá que esperar el dinero que necesita?\2Cuando fallece un ser querido, la familia enfrenta más que el dolor de la pérdida. También puede enfrentar necesidades financieras inmediatas.\3blog_legacy_es.html\4LEER ARTÍCULO →\5',
        html,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Updated Knowledgebase cards & Living Benefits link on index_es.html")

def update_spanish_blog_sidebars():
    blog_files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in sorted(blog_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        content = content.replace("24hr Response Guarantee", "Respuesta en 24 horas")
        content = content.replace("Respuesta garantizada en 24h", "Respuesta en 24 horas")
        content = content.replace("100% Privacy Protected", "Tu privacidad nos importa")
        content = content.replace("Privacidad 100% protegida", "Tu privacidad nos importa")
        content = content.replace("Su privacidad importa", "Tu privacidad nos importa")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Verified sidebar trust badges on {fname}")

def main():
    print("=== Updating Spanish Knowledgebase Cards & Blog Articles ===")
    update_homepage_blog_cards()
    update_spanish_blog_sidebars()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
