#!/usr/bin/env python3
"""
apply_section3_family_protection_updates.py
Applies Section 3 (Family Protection Page) updates to family_protection_es.html:
- 3.1 Hero text
- 3.2 Four proof labels (removes old numeric statistics)
- 3.3 Bills Don't Wait paragraph
- 3.4 What If You Were Alive paragraph
- 3.5 A Diagnosis Can Change paragraph
- 3.6 Work Coverage Can Feel Safe paragraph
- 3.7 All 10 Family Protection FAQs
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "family_protection_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 3.1 Hero
HERO_NEW = "La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesiten. Te ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para ajustarse a tus necesidades, tu presupuesto y tu vida."

html = re.sub(
    r'(<div class="service-hero-content">.*?<p class="service-hero-sub">).*?(</p>)',
    r'\1' + HERO_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 3.2 Four proof labels
L1 = "LOS BENEFICIOS DEL TRABAJO PUEDEN DEJAR BRECHAS — Conoce qué protege a tu familia antes de que la vida cambie"
L2 = "SI LOS INGRESOS SE DETIENEN — ¿Podría tu familia seguir pagando las facturas el próximo mes?"
L3 = "EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO — Planifica antes de que tus seres queridos lo necesiten"
L4 = "REVISIÓN SIN COSTO — Pregunta ahora. Decide con claridad y sin presión."

html = re.sub(r'WORK BENEFITS CAN LEAVE GAPS.*?(?=</div>|</span>|</p>)', L1, html)
html = re.sub(r'IF INCOME STOPS.*?(?=</div>|</span>|</p>)', L2, html)
html = re.sub(r'PROBATE CAN DELAY MONEY.*?(?=</div>|</span>|</p>)', L3, html)
html = re.sub(r'NO-COST REVIEW.*?(?=</div>|</span>|</p>)', L4, html)

# Remove old statistics numeric claims (60%, 1-in-4, 9-24m)
html = re.sub(r'<div class="stat-number">60%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">1 in 4</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">9-24m</div>', '<div class="stat-number">✓</div>', html)

# 3.3 Bills Don't Wait
BILLS_NEW = "Después de una pérdida, tu familia puede necesitar dinero de inmediato para gastos funerarios, renta o hipoteca, alimentos y las necesidades de los hijos. Sin embargo, algunos bienes pueden demorarse durante el proceso sucesorio. Un seguro de vida con el beneficiario adecuado puede ayudar a proporcionar fondos directamente a tus seres queridos mientras otros bienes todavía están siendo gestionados."

# 3.4 What If You Were Alive
ALIVE_NEW = "Una enfermedad de larga duración puede afectar más que tu salud. Puede afectar tu capacidad para trabajar, reducir o interrumpir tus ingresos y ejercer presión sobre la vida diaria de tu familia. Algunas pólizas de seguro de vida pueden incluir cláusulas de beneficios acelerados o beneficios en vida que permiten a los titulares elegibles acceder a una parte del beneficio por fallecimiento después de un evento cubierto que califique. La disponibilidad, las condiciones de elegibilidad, los montos de los beneficios, los cargos y el efecto sobre el beneficio por fallecimiento restante dependen de los términos de la póliza y de la cláusula adicional."

# 3.5 A Diagnosis Can Change
DIAG_NEW = "Un ataque cardíaco, un derrame cerebral, cáncer u otra enfermedad grave puede traer gastos médicos, tiempo sin trabajar y presión financiera al mismo tiempo. Algunas pólizas de seguro de vida con beneficios en vida pueden ayudar a proporcionar fondos durante una enfermedad crítica cubierta, dando a tu familia más espacio para concentrarse en el cuidado, la recuperación y las necesidades diarias."

# 3.6 Work Coverage Can Feel Safe
WORK_NEW = "Muchas familias dependen de los beneficios del empleador sin saber exactamente qué tienen, cuánto cubren o qué sucede si cambia el empleo. La cobertura del trabajo puede ser un buen comienzo, pero tu familia también puede necesitar una protección más estable que no dependa únicamente de tu empleador. Una revisión sencilla puede ayudarte a comprender tu protección antes de que la vida te obligue a hacerte esa pregunta."

# Update section paragraphs
html = re.sub(
    r'(<h2[^>]*>Las facturas no esperan.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + BILLS_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>¿Qué pasaría si siguieras con vida.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + ALIVE_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>Un diagnóstico puede cambiar.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + DIAG_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>La cobertura del trabajo puede parecer segura.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + WORK_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 3.7 All 10 Family Protection FAQs
FAQS = [
    ("¿Cuál es el objetivo principal del seguro de Protección Familiar?", "El seguro de Protección Familiar está diseñado para ayudar a que tu familia pueda continuar financieramente si el principal proveedor de ingresos fallece inesperadamente. Puede ayudar con gastos de vida, deudas y metas futuras para que tus seres queridos no tengan que cargar con todo solos."),
    ("¿El seguro de vida de mi empleador ofrece suficiente protección?", "La cobertura del empleador puede ser un buen comienzo, pero quizá no sea suficiente para todas las necesidades de tu familia. También puede cambiar o terminar cuando cambia tu empleo, por lo que una revisión puede ayudarte a entender qué protección tienes realmente."),
    ("¿Qué son los beneficios en vida?", "Algunas pólizas de seguro de vida pueden incluir cláusulas de beneficios acelerados o beneficios en vida que permiten a titulares elegibles acceder a una parte del beneficio por fallecimiento después de un evento cubierto que califique. La disponibilidad, las condiciones de elegibilidad, los montos, los cargos y el efecto sobre el beneficio por fallecimiento restante dependen de los términos de la póliza y la cláusula adicional."),
    ("¿Cuánto seguro de vida necesito?", "No tienes que adivinar. La cantidad adecuada depende de tus ingresos, deudas, responsabilidades familiares y metas futuras, y una revisión sencilla puede ayudarte a entender qué podría ajustarse a tu familia."),
    ("¿Cuál es la diferencia entre seguro a término y seguro permanente?", "El seguro a término ofrece protección durante un período específico, como 10, 20 o 30 años. El seguro de vida permanente puede ofrecer cobertura a largo plazo y puede acumular valor en efectivo, dependiendo de la póliza."),
    ("¿Puede el seguro de vida ayudar a evitar el proceso sucesorio?", "Cuando se designan correctamente los beneficiarios adecuados, los beneficios del seguro de vida generalmente se pagan directamente a ellos. Esto puede ayudar a que los seres queridos reciban fondos de manera más directa cuando más los necesitan."),
    ("¿Los beneficios del seguro de vida están sujetos a impuestos?", "En muchas situaciones, los beneficios por fallecimiento del seguro de vida generalmente se pagan a los beneficiarios libres del impuesto sobre la renta. El tratamiento fiscal puede depender de la situación, por lo que las familias deben consultar a un profesional fiscal calificado."),
    ("¿Pueden los padres que se quedan en casa obtener seguro de vida?", "Sí. Un padre o una madre que se queda en casa aporta un valor real mediante el cuidado de los hijos, las comidas, el transporte y el apoyo diario. El seguro de vida puede ayudar a la familia a cubrir esas necesidades si esa persona ya no está, y algunas pólizas permanentes pueden acumular valor en efectivo para necesidades futuras."),
    ("¿Necesito un examen médico?", "No siempre. Algunas opciones de seguro de vida pueden estar disponibles sin examen médico, dependiendo de la compañía, el producto, el historial de salud y la elegibilidad. No dejes que el temor a un examen te impida preguntar."),
    ("¿Cuándo es el mejor momento para contratar un seguro de vida?", "Generalmente, antes de que la vida te obligue a hacerte la pregunta. Con el tiempo aumenta la edad y la salud puede cambiar, lo que puede afectar el costo, la elegibilidad y las opciones disponibles. Empezar antes puede darle a tu familia más opciones.")
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

print("  ✓ Synchronized Section 3 on family_protection_es.html")
