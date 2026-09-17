#!/usr/bin/env python3
"""
apply_section5_education_updates.py
Applies Section 5 (Education Planning Page) updates to education_planning_es.html:
- 5.1 Hero text
- 5.2 Four labels (removes old numeric statistics)
- 5.3 What If Your Child's Path Changes paragraph
- 5.4 Education Planning Should Fit Real Life paragraph
- 5.5 Your Child's Future Matters paragraph
- 5.6 All 10 Education FAQs
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "education_planning_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 5.1 Hero
HERO_P1 = "Los costos de educación continúan aumentando y la deuda estudiantil puede convertirse en una carga pesada antes de que la próxima generación siquiera comience. Quieres ayudar a tus hijos a seguir su futuro — universidad, carrera, negocio u otro camino — pero también necesitas proteger el tuyo."
HERO_P2 = "Puedes pedir prestado para la universidad, pero no para la jubilación."

html = re.sub(
    r'(<div class="service-hero-content">.*?<p class="service-hero-sub">).*?(</p>)',
    r'\1' + HERO_P1 + '<br/><br/>' + HERO_P2 + r'\2',
    html,
    flags=re.DOTALL
)

# 5.2 Four labels
L1 = "COSTOS EDUCATIVOS EN AUMENTO — ¿Estás preparado antes de que llegue la factura?"
L2 = "PLANIFICACIÓN FLEXIBLE — ¿Qué pasa si cambia el camino de tu hijo?"
L3 = "DEUDA ESTUDIANTIL — ¿Podría la planificación reducir futuros préstamos?"
L4 = "EQUILIBRIO CON LA JUBILACIÓN — ¿Puedes ayudarles sin perjudicar tu propio futuro?"

html = re.sub(r'RISING EDUCATION COSTS.*?(?=</div>|</span>|</p>)', L1, html)
html = re.sub(r'FLEXIBLE PLANNING.*?(?=</div>|</span>|</p>)', L2, html)
html = re.sub(r'STUDENT DEBT.*?(?=</div>|</span>|</p>)', L3, html)
html = re.sub(r'RETIREMENT BALANCE.*?(?=</div>|</span>|</p>)', L4, html)

# Remove old statistics numeric claims ($100k, 5%, $1.7T, $0 FAFSA)
html = re.sub(r'<div class="stat-number">\$100k</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">5%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">\$1\.7T</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">\$0</div>', '<div class="stat-number">✓</div>', html)

# 5.3 What If Your Child's Path Changes
PATH_NEW = "Un plan 529 puede ser una herramienta valiosa de ahorro educativo, pero está diseñado principalmente para gastos educativos calificados. Si tu hijo recibe una beca, elige un camino profesional diferente, inicia un negocio o decide no asistir a la universidad, tu familia puede necesitar más flexibilidad. Antes de elegir un solo camino, ayuda comprender cómo funciona cada estrategia educativa y qué sucede si la vida no sale exactamente como se planeó."

# 5.4 Education Planning Should Fit Real Life
FIT_NEW = "El seguro de vida permanente que acumula valor en efectivo puede ofrecer acceso flexible mediante préstamos o retiros de la póliza. Dependiendo del diseño de la póliza, el valor en efectivo puede utilizarse para gastos educativos, vivienda, oportunidades de negocio, necesidades de jubilación u otras metas futuras si cambia el camino de tu hijo. Ayudamos a las familias a comprender cómo funciona esta estrategia antes de decidir si se ajusta a sus metas."

# 5.5 Your Child's Future Matters
MATTERS_NEW = "Muchos padres están dispuestos a sacrificarse por sus hijos. Ese amor es poderoso. Pero ayudar a tu hijo no debería significar poner en riesgo tu propia jubilación. Una estrategia educativa bien pensada puede ayudarte a apoyar los sueños de tu hijo sin perder de vista el plan familiar a largo plazo."

html = re.sub(
    r'(<h2[^>]*>¿Qué pasa si cambia el camino de tu hijo.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + PATH_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>La planificación educativa debe adaptarse.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + FIT_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>El futuro de tu hijo importa.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + MATTERS_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 5.6 All 10 Education FAQs
FAQS = [
    ("¿Cuáles son las limitaciones de un plan 529 tradicional?", "Un plan 529 puede ser útil, pero la vida no siempre sigue un solo plan. Está diseñado principalmente para gastos educativos calificados, y los retiros no calificados pueden estar sujetos a impuestos o penalidades sobre las ganancias si cambian los planes de tu hijo."),
    ("¿Cómo puede ayudar el seguro de vida con la planificación educativa?", "Algunas pólizas de seguro de vida permanente, como el IUL, pueden acumular valor en efectivo al que se puede acceder mediante préstamos o retiros de la póliza para la educación u otras necesidades futuras, dependiendo de la póliza. Acceder al valor en efectivo puede afectar los beneficios de la póliza, por lo que es importante comprender cómo funciona. Podemos ayudarte a explorar si esta opción se ajusta a las metas de tu familia."),
    ("¿Un plan 529 afecta la ayuda financiera?", "El tratamiento para la ayuda financiera puede variar según quién sea el propietario de la cuenta, el tipo de activo y las reglas actuales de FAFSA. Las familias deben revisar la orientación federal vigente sobre ayuda estudiantil antes de elegir una estrategia."),
    ("¿Qué pasa si mi hijo decide no asistir a la universidad?", "Ahí es donde la flexibilidad importa. Dependiendo del diseño de la póliza, el seguro de vida con valor en efectivo puede ayudar a apoyar otras metas, como un negocio, vivienda o futuras necesidades familiares."),
    ("¿Está garantizado el crecimiento del valor en efectivo?", "Algunas pólizas IUL incluyen un piso del 0% en la acreditación de intereses vinculados al índice, lo que puede ayudar a brindar protección frente a un rendimiento negativo del índice. Los cargos y términos de la póliza siguen aplicando, y podemos ayudarte a comprender cómo funciona la póliza para tus metas."),
    ("¿Cuándo debo comenzar a ahorrar para la educación de mi hijo?", "Empezar antes generalmente le da a tu familia más tiempo y más opciones. Comenzar temprano puede darle a tu dinero más tiempo para crecer y ayudarte a planificar con menos presión."),
    ("¿Pueden contribuir los abuelos?", "Sí. Los abuelos también pueden formar parte del futuro del niño. Pueden ayudar a financiar una estrategia que apoye la educación, oportunidades futuras o etapas importantes de la vida."),
    ("¿Qué sucede si el mercado baja antes de que venza la matrícula?", "El momento puede importar cuando se necesita dinero para la educación. Las cuentas basadas en el mercado pueden bajar cuando cae el mercado, mientras que algunas pólizas IUL están diseñadas para ayudar a proteger intereses vinculados al índice que ya fueron acreditados, dependiendo de los términos de la póliza."),
    ("¿Puedo usar un IUL para educación privada K–12?", "En algunos casos, sí. Dependiendo del diseño de la póliza, se puede acceder al valor en efectivo para ayudar con la matrícula privada K–12 u otros gastos relacionados con la educación."),
    ("¿Es complicado establecer una póliza de seguro de vida para un hijo?", "No siempre. En muchos casos, el proceso puede ser sencillo, y comenzar temprano puede dar a las familias más opciones y flexibilidad para el futuro.")
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

print("  ✓ Synchronized Section 5 on education_planning_es.html")
