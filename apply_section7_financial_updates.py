#!/usr/bin/env python3
"""
apply_section7_financial_updates.py
Applies Section 7 (Financial Strategy Page) updates to financial_strategy_es.html:
- 7.1 Hero text
- 7.2 Four labels (removes 100% control, 0% market loss, 3-8% probate fee)
- 7.3 The Rule of 72 paragraph
- 7.4 Debt Management paragraph
- 7.5 Legacy Transfer paragraph
- 7.6 All 9 Financial Strategy FAQs
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "financial_strategy_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 7.1 Hero
HERO_P1 = "Un progreso financiero sólido generalmente viene de decisiones claras, no de adivinanzas. Las familias pueden beneficiarse de aprender a manejar deudas, construir ahorros, proteger lo que han trabajado por conseguir y planificar pensando en el futuro."
HERO_P2 = "¿Tus decisiones financieras te están ayudando a avanzar hacia el futuro que deseas?"

html = re.sub(
    r'(<div class="service-hero-content">.*?<p class="service-hero-sub">).*?(</p>)',
    r'\1' + HERO_P1 + '<br/><br/>' + HERO_P2 + r'\2',
    html,
    flags=re.DOTALL
)

# 7.2 Four labels
L1 = "CLARIDAD FINANCIERA — ¿Sabes adónde va tu dinero?"
L2 = "ESTRATEGIA DE DEUDA — ¿Podrían los intereses estar frenando tu progreso?"
L3 = "PRINCIPIOS DE CRECIMIENTO — ¿Está el tiempo trabajando a favor de tu dinero?"
L4 = "REVISIÓN SIN COSTO — Construye un plan con claridad y sin presión."

html = re.sub(r'FINANCIAL CLARITY.*?(?=</div>|</span>|</p>)', L1, html)
html = re.sub(r'DEBT STRATEGY.*?(?=</div>|</span>|</p>)', L2, html)
html = re.sub(r'GROWTH PRINCIPLES.*?(?=</div>|</span>|</p>)', L3, html)
html = re.sub(r'NO-COST REVIEW.*?(?=</div>|</span>|</p>)', L4, html)

# Remove old statistics numeric claims (100%, 0%, 3-8%, Day 1)
html = re.sub(r'<div class="stat-number">100%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">0%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">3-8%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">Day 1</div>', '<div class="stat-number">✓</div>', html)

# 7.3 Rule of 72
RULE_NEW = "Comprender cómo funciona el interés compuesto puede ayudar a las familias a ver el poder del tiempo. La Regla del 72 es una manera sencilla de estimar cuánto tiempo podría tardar el dinero en duplicarse a una determinada tasa anual de rendimiento. Cuando entiendes cómo funciona el crecimiento, puedes tomar mejores decisiones sobre ahorro, inversión, deuda y planificación a largo plazo."

# 7.4 Debt Management
DEBT_NEW = "No todas las deudas son iguales, pero la deuda con intereses altos puede frenar silenciosamente el progreso de una familia. Una buena estrategia financiera te ayuda a comprender lo que debes, reducir deudas innecesarias con el tiempo y crear espacio para el ahorro y las metas futuras. La meta es sencilla: ayudar a que tu dinero apoye tu futuro en lugar de ir únicamente al pago de deudas."

# 7.5 Legacy Transfer
LEGACY_NEW = "Un verdadero legado no se trata solo de lo que dejas atrás. También se trata de las oportunidades, los valores y la dirección que creas para las personas que amas. Ayudamos a las familias a explorar estrategias que pueden apoyar a futuras generaciones, proteger lo que han trabajado duro para construir y transmitir sus valores con mayor claridad."

html = re.sub(
    r'(<h2[^>]*>La Regla del 72.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + RULE_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>Manejo de deudas.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + DEBT_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>Transferencia de legado.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + LEGACY_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 7.6 All 9 Financial Strategy FAQs
FAQS = [
    ("¿Qué es la Regla del 72?", "Es una forma sencilla de estimar cuánto tiempo puede tardar el dinero en duplicarse. Divide 72 entre una tasa anual de rendimiento; por ejemplo, al 7%, el dinero podría duplicarse en aproximadamente 10 años."),
    ("¿Cómo pueden ayudar con el manejo de deuda?", "La deuda puede frenar silenciosamente el progreso. Ayudamos a las familias a comprender sus deudas, mejorar el flujo de efectivo y explorar pasos prácticos para reducir la deuda con el tiempo."),
    ("¿Qué significa “convertirte en tu propio banco”?", "Es un concepto, no un banco literal. Generalmente se refiere a usar el valor en efectivo de una póliza de seguro de vida correctamente estructurada como una posible fuente de fondos para necesidades futuras, dependiendo del diseño de la póliza."),
    ("¿Cómo puedo ayudar a proteger mis activos de las caídas del mercado?", "Cuando el mercado baja, el dinero invertido directamente en el mercado puede perder valor. Algunas FIA y pólizas IUL están diseñadas para ayudar a reducir la exposición a pérdidas directas del mercado mediante estrategias vinculadas a índices. La meta es ayudar a proteger lo que has trabajado duro para construir, manteniendo al mismo tiempo cierta oportunidad de crecimiento futuro, dependiendo de los términos del producto o la póliza."),
    ("¿Qué es una estrategia de jubilación con eficiencia fiscal?", "Dependiendo del diseño de la póliza y de la ley fiscal vigente, en algunas situaciones se puede acceder al valor en efectivo de manera fiscalmente favorable. Acceder al valor en efectivo puede afectar los beneficios de la póliza y puede tener implicaciones fiscales. Consulta a un profesional fiscal calificado."),
    ("¿Por qué es importante el interés compuesto?", "El interés compuesto ayuda a que tu dinero crezca tanto sobre la cantidad original como sobre el crecimiento ya obtenido. Con el tiempo, esto puede convertirse en una de las bases para construir patrimonio, porque pequeños pasos constantes pueden crecer hasta convertirse en algo significativo."),
    ("¿Necesito una estrategia financiera si no soy una persona adinerada?", "Sí. Una estrategia financiera no es solo para personas adineradas. Puede ayudar a las familias a reducir deudas, construir ahorros, proteger lo que han trabajado por conseguir y tomar decisiones con mayor confianza."),
    ("¿Qué es el riesgo de secuencia de rendimientos?", "El momento importa durante la jubilación. El riesgo de secuencia de rendimientos ocurre cuando se producen pérdidas de mercado al principio de la jubilación mientras ya han comenzado los retiros, lo que puede afectar cuánto tiempo duran los ahorros."),
    ("¿Cómo se compara un IUL con una Roth IRA?", "Ambos pueden ofrecer ventajas fiscales, pero funcionan de manera diferente. Una Roth IRA tiene límites de ingresos y contribuciones establecidos por el IRS. Un IUL es un seguro de vida con valor en efectivo y beneficio por fallecimiento, y no sigue las mismas reglas de contribución de una Roth IRA; en cambio, sigue las reglas de la póliza y las normas fiscales aplicables.")
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

print("  ✓ Synchronized Section 7 on financial_strategy_es.html")
