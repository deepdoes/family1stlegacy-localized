#!/usr/bin/env python3
"""
apply_section4_retirement_updates.py
Applies Section 4 (Retirement Planning Page) updates to retirement_planning_es.html:
- 4.1 Hero text
- 4.2 Four labels (removes old numeric statistics)
- 4.3 What If Market Drops paragraph
- 4.4 Is IRS Part of Plan paragraph
- 4.5 What If Retirement Lasts Longer paragraph
- 4.6 All 10 Retirement FAQs
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "retirement_planning_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 4.1 Hero
HERO_P1 = "Has trabajado duro para construir tu futuro. Ahora, la jubilación puede requerir más que simplemente ahorrar dinero: puede necesitar un plan para los ingresos, los impuestos, los cambios del mercado y la posibilidad de vivir más tiempo de lo esperado."
HERO_P2 = "¿Simplemente estás ahorrando para la jubilación, o te estás preparando para la vida que deseas vivir?"

html = re.sub(
    r'(<div class="service-hero-content">.*?<p class="service-hero-sub">).*?(</p>)',
    r'\1' + HERO_P1 + '<br/><br/>' + HERO_P2 + r'\2',
    html,
    flags=re.DOTALL
)

# 4.2 Four labels
L1 = "INGRESOS DE JUBILACIÓN — ¿Podrían tus ahorros durar tanto como tú?"
L2 = "CAMBIOS DEL MERCADO — ¿Qué sucede si el mercado baja cerca de tu jubilación?"
L3 = "PLANIFICACIÓN CON CONCIENCIA FISCAL — ¿Sabes cuánto podrías conservar realmente?"
L4 = "REVISIÓN SIN COSTO — Haz preguntas antes de tomar decisiones de jubilación"

html = re.sub(r'RETIREMENT INCOME.*?(?=</div>|</span>|</p>)', L1, html)
html = re.sub(r'MARKET CHANGES.*?(?=</div>|</span>|</p>)', L2, html)
html = re.sub(r'TAX-AWARE PLANNING.*?(?=</div>|</span>|</p>)', L3, html)
html = re.sub(r'NO-COST REVIEW.*?(?=</div>|</span>|</p>)', L4, html)

# Remove old statistics numeric claims (3.5%, 20+, 15%, 0 taxes)
html = re.sub(r'<div class="stat-number">3\.5%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">20\+</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">15%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">0%</div>', '<div class="stat-number">✓</div>', html)

# 4.3 What If Market Drops
DROPS_NEW = "Las subidas y bajadas del mercado pueden afectar tus ahorros, especialmente cuando estás cerca de la jubilación o ya estás realizando retiros. Una anualidad fija indexada es un contrato de seguro que puede ofrecer protección del capital frente a un rendimiento negativo del índice, junto con la posibilidad de recibir créditos de interés vinculados al índice. La acreditación está sujeta a términos del contrato, como límites, tasas de participación o márgenes, y los retiros pueden estar sujetos a cargos por rescate o consecuencias fiscales."

# 4.4 Is IRS Part of Plan
IRS_NEW = "El dinero que ves en un 401(k) tradicional puede no estar completamente disponible para gastar. Los retiros generalmente están sujetos a impuestos más adelante, lo que significa que los impuestos pueden afectar cuánto ingreso de jubilación conservas realmente. Una planificación que tome en cuenta los impuestos puede ayudarte a comprender tus opciones antes de que comience la jubilación."

# 4.5 What If Retirement Lasts Longer
LONGER_NEW = "Vivir más tiempo es una bendición, pero también significa que tus ingresos quizá deban durar más. Planificar con anticipación puede ayudarte a considerar los ingresos futuros, los costos de atención médica y estrategias diseñadas para apoyar tu estilo de vida durante el mayor tiempo posible."

html = re.sub(
    r'(<h2[^>]*>¿Qué pasa si el mercado baja.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + DROPS_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>¿Forma parte el IRS.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + IRS_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>¿Qué pasa si la jubilación dura más.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + LONGER_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 4.6 All 10 Retirement FAQs
FAQS = [
    ("¿Por qué no debería depender completamente de un 401(k) o una IRA?", "Porque la jubilación puede necesitar más de una sola fuente. Un 401(k) o una IRA pueden ser útiles, pero los cambios del mercado y los impuestos pueden afectar lo que realmente conservas."),
    ("¿Qué es una anualidad fija indexada (FIA)?", "Una anualidad fija indexada es un contrato de seguro diseñado para ayudar a proteger tu capital frente a un rendimiento negativo del índice, al mismo tiempo que ofrece el potencial de crecimiento de intereses vinculados a un índice. Las características y los términos varían según el contrato, y podemos ayudarte a comprender cómo podría encajar en tus metas de jubilación."),
    ("¿Perderé mi dinero si el mercado de valores cae?", "Depende de dónde esté colocado tu dinero. Las inversiones directas en el mercado pueden perder valor, mientras que algunas anualidades y estrategias de seguro de vida están diseñadas para ayudar a reducir la exposición directa al mercado."),
    ("¿Qué es la “sorpresa fiscal” en la planificación de jubilación?", "El saldo que ves puede no ser la cantidad que conservas. El dinero de un 401(k) tradicional o una IRA generalmente tiene impuestos diferidos, no está libre de impuestos, por lo que los retiros suelen estar sujetos a impuestos más adelante."),
    ("¿Puede una anualidad proporcionar ingresos de por vida?", "Sí. Para algunas familias, contar con ingresos de jubilación confiables es la meta. Algunas anualidades ofrecen características de ingresos diseñadas para proporcionar pagos de por vida, dependiendo del contrato."),
    ("¿Qué es la “tasa de retiro seguro”?", "Es una guía, no una garantía. Ayuda a estimar cuánto puede retirar una persona de sus ahorros de jubilación cada año."),
    ("¿Cómo puede el IUL ayudar con la planificación de jubilación?", "Puede añadir flexibilidad. El IUL es ante todo un seguro de vida, pero puede acumular valor en efectivo al que se puede acceder para necesidades futuras, dependiendo del diseño de la póliza."),
    ("¿Las anualidades son solo para personas adineradas?", "No. Algunas anualidades pueden comenzar con cantidades más modestas, dependiendo de la compañía y del producto."),
    ("¿Cómo afectan los impuestos a mis beneficios del Seguro Social?", "El Seguro Social puede no estar completamente libre de impuestos. Dependiendo de tus ingresos combinados, una parte de tus beneficios puede estar sujeta a impuestos."),
    ("¿Es demasiado tarde para comenzar a planificar la jubilación?", "No. Incluso si faltan 5 o 10 años para jubilarte, revisar tus opciones puede ayudarte a proteger lo que has ahorrado, comprender las opciones de ingresos y tomar decisiones más informadas.")
]

for q, a in FAQS:
    html = re.sub(
        rf'(<div class="faq-question">{re.escape(q)}</div>\s*<div class="faq-answer">).*?(</div>)',
        rf'\1{a}\2',
        html,
        flags=re.DOTALL
    )

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Synchronized Section 4 on retirement_planning_es.html")
