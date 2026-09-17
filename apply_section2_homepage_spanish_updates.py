#!/usr/bin/env python3
"""
apply_section2_homepage_spanish_updates.py
Comprehensive script applying Section 2 & 2A (Home Page) updates to index_es.html:
- 2.1 Career Opportunity hero text
- 2.2 Proof section (TU FAMILIA. NUESTRO ENFOQUE.)
- 2.3 Guidance for Every Stage paragraph
- 2.4 - 2.9 Service rows & service cards text (Life Insurance, Retirement, Estate, Education, Financial Strategy, Business)
- 2.10 - 2.12 How It Works steps
- 2.13 All 10 Home FAQs
- 2A Section headlines & callout headings
- PRESERVES top navigation ("Planificación Educativa", etc.) and main-site footer ("Preguntas reales y orientación").
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "index_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 2.1 Career Opportunity hero
OPP_HERO_NEW = "Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer hasta trabajar a tiempo completo, con capacitación, mentoría y apoyo durante el proceso. Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más les importa."

html = re.sub(
    r'En Family First Legacy, creemos que la educación financiera.*?(?=</p>)',
    OPP_HERO_NEW,
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'At Family First Legacy, we believe financial education can help families.*?(?=</p>)',
    OPP_HERO_NEW,
    html,
    flags=re.DOTALL
)

# 2.2 Proof section
html = re.sub(r'YOUR FAMILY\.\s*OUR FOCUS\.', 'TU FAMILIA. NUESTRO ENFOQUE.', html)
html = re.sub(r'100%\s*Licensed Professionals', '100% Profesionales con licencia', html)
html = re.sub(r'DFW &amp; US\s*—\s*Serving Families Nationwide', 'DFW y EE. UU. — Sirviendo a familias en todo el país', html)
html = re.sub(r'DFW & US\s*—\s*Serving Families Nationwide', 'DFW y EE. UU. — Sirviendo a familias en todo el país', html)

# 2.3 Guidance for Every Stage
GUIDANCE_NEW = "Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a comprender tus opciones y construir una estrategia que se adapte a cada etapa de tu vida."
html = re.sub(
    r'<div class="services-top-right"[^>]*>\s*<div class="st-accent"></div>\s*<p>.*?</p>',
    f'<div class="services-top-right" data-delay="2" data-reveal="">\n<div class="st-accent"></div>\n<p>{GUIDANCE_NEW}</p>',
    html,
    flags=re.DOTALL
)

# Service texts
LIFE_TXT = "Tu familia cuenta contigo todos los días. Te explicamos de manera sencilla el seguro de vida a término, el seguro de vida entera y el seguro de vida universal indexado (IUL), para que puedas elegir una cobertura que apoye a las personas que amas, tu presupuesto y tus metas futuras."
RETIREMENT_TXT = "La jubilación no debería sentirse como una incertidumbre. Ya sea que estés comenzando a ahorrar o revisando un plan que ya tienes, te ayudamos a comprender tus opciones y crear un plan pensado para apoyar el futuro que deseas."
ESTATE_TXT = "Tu legado es más que dinero: son las personas, los valores y el futuro que te importan. Te ayudamos a comprender maneras de organizar tus bienes y a trabajar junto con tus profesionales legales y fiscales para crear un plan enfocado en lo que más importa."
EDU_TXT = "Todo padre desea brindar a sus hijos más oportunidades para el futuro. Ya sea que elijan la universidad, una escuela técnica u otro camino, te ayudamos a comprender las opciones de ahorro para la educación y a crear un plan que apoye sus metas sin perder de vista tu propia jubilación."
FINANCIAL_TXT = "Tu dinero debe tener un propósito, no simplemente quedarse guardado. Te ayudamos a comprender maneras de ahorrar, prepararte para el futuro y explorar opciones diseñadas para ayudar a reducir el impacto de las caídas del mercado."
BIZ_TXT = "Tu negocio representa tu trabajo, tus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a comprender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a apoyar la estabilidad a largo plazo."

# Replace .sr-body in service rows 01-06
html = re.sub(
    r'(<div class="sr-num">01</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + LIFE_TXT + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="sr-num">02</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + RETIREMENT_TXT + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="sr-num">03</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + ESTATE_TXT + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="sr-num">04</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + EDU_TXT + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="sr-num">05</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + FINANCIAL_TXT + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="sr-num">06</div>.*?<p class="sr-body">).*?(</p>)',
    r'\1' + BIZ_TXT + r'\2',
    html,
    flags=re.DOTALL
)

# 2.10 How It Works Step 2
STEP2_NEW = "Utilizamos un Análisis de Necesidades Financieras para revisar tu situación actual y ayudarte a identificar dónde podrían encajar opciones de protección, ahorro o jubilación según tus necesidades."

# 2.11 How It Works Step 3
STEP3_NEW = "Te presentamos opciones claras de compañías de seguros y servicios financieros bien establecidas, explicadas en un lenguaje sencillo y sin presión."

# 2.12 Ongoing Guidance
ONGOING_NEW = "La vida cambia, y tu plan también puede necesitar cambios. Seguimos disponibles para revisar tu plan, responder tus preguntas y ayudarte a hacer ajustes a medida que tu familia crece."

html = re.sub(
    r'(<div class="ps-num">02</div>.*?<p class="ps-desc">).*?(</p>)',
    r'\1' + STEP2_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="ps-num">03</div>.*?<p class="ps-desc">).*?(</p>)',
    r'\1' + STEP3_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<div class="ps-num">04</div>.*?<p class="ps-desc">).*?(</p>)',
    r'\1' + ONGOING_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 2.13 All 10 Home FAQs
FAQS_ES = [
    ("¿Qué hace exactamente Family First Legacy?", "Family First Legacy ayuda a personas, familias y dueños de negocios a comprender sus opciones de seguro de vida, planificación para la jubilación, planificación educativa y planificación de legado. Explicamos todo con claridad para que puedas tomar decisiones informadas a tu propio ritmo."),
    ("¿Es realmente asequible el seguro de vida?", "El seguro de vida puede ser más accesible de lo que muchas personas esperan. El costo depende de la edad, la salud, el monto de cobertura, el tipo de producto y la elegibilidad."),
    ("¿Necesito seguro de vida si no tengo hijos?", "El seguro de vida no es solo para padres. Puede ayudar a cubrir gastos finales, deudas como una hipoteca o apoyar a personas que dependen de ti. Algunas pólizas también pueden incluir beneficios en vida para ciertas enfermedades o condiciones cubiertas."),
    ("¿Qué son los beneficios en vida?", "Los beneficios en vida pueden permitir que los titulares de pólizas que califican accedan a una parte de los beneficios de su póliza mientras aún viven si enfrentan ciertas enfermedades o condiciones cubiertas. Estos fondos pueden ayudar con necesidades como facturas, gastos médicos o pérdida de ingresos. La disponibilidad depende de la póliza y de la elegibilidad."),
    ("¿Es el seguro de Vida Universal Indexada (IUL) una buena inversión?", "El IUL es, ante todo, un seguro de vida, no una inversión directa en el mercado de valores. Dependiendo del diseño de la póliza, puede ayudar a proteger a tu familia mientras acumula valor en efectivo vinculado a un índice de mercado. Muchas pólizas IUL incluyen un piso del 0% para la acreditación de intereses vinculados al índice, lo que puede ayudar a reducir el impacto de un rendimiento negativo del índice. Los cargos de la póliza y otros términos siguen aplicando y pueden afectar el valor en efectivo."),
    ("¿Por qué no debería usar solamente un 401(k) para la jubilación?", "Un 401(k) puede ser una herramienta valiosa para la jubilación, pero por sí solo quizá no cubra todas las necesidades de retiro. Los retiros de un 401(k) tradicional generalmente están sujetos a impuestos y el valor de la cuenta puede subir o bajar con el mercado. Algunas familias también exploran anualidades o estrategias de seguro de vida para añadir opciones de protección del capital, ingresos y mayor equilibrio a su plan de jubilación."),
    ("¿Cómo puede una anualidad ayudar a proteger mi dinero?", "Algunas anualidades fijas indexadas están diseñadas para ayudar a proteger el capital frente a un rendimiento negativo del índice, al mismo tiempo que ofrecen la posibilidad de recibir créditos de interés vinculados al índice cuando corresponda. Pueden aplicar términos del contrato, límites, tasas de participación, cargos por rescate, retiros y otras limitaciones. Como cada producto funciona de manera diferente, explicamos los detalles con claridad para que comprendas la protección, el potencial de crecimiento y las reglas antes de tomar una decisión."),
    ("¿Qué deben saber las familias sobre el proceso sucesorio?", "El proceso sucesorio puede retrasar el acceso a ciertos bienes cuando una familia más necesita dinero. Un seguro de vida con el beneficiario adecuado puede ayudar a proporcionar fondos directamente a los seres queridos para facturas, gastos funerarios o necesidades diarias mientras otros bienes todavía se gestionan. Para testamentos, fideicomisos y planificación patrimonial legal, recomendamos trabajar con un profesional legal calificado."),
    ("¿Puedo usar un seguro de vida para ayudar a pagar la educación de mi hijo?", "El seguro de vida permanente que acumula valor en efectivo puede ofrecer acceso flexible mediante préstamos o retiros de la póliza para la educación u otras necesidades futuras, dependiendo del diseño de la póliza. Como acceder al valor en efectivo puede afectar los beneficios de la póliza, es importante comprender cómo funciona tu póliza específica antes de utilizarlo. Podemos ayudarte a entender tus opciones y cómo podrían ajustarse a las metas de tu familia."),
    ("¿Cobran una tarifa por las consultas?", "No. No cobramos una tarifa por hablar con nosotros. Tu revisión financiera se ofrece sin costo y sin presión. Es simplemente una conversación para comprender tu situación, responder tus preguntas y ayudarte a ver qué opciones pueden ajustarse a tus metas. No existe obligación de continuar.")
]

for q, a in FAQS_ES:
    # Match in Q&A slides or FAQ accordions
    html = re.sub(
        rf'(<h3>{re.escape(q)}</h3>\s*<p>).*?(</p>)',
        rf'\1{a}\2',
        html,
        flags=re.DOTALL
    )
    html = re.sub(
        rf'(<div class="faq-question">{re.escape(q)}</div>\s*<div class="faq-answer">).*?(</div>)',
        rf'\1{a}\2',
        html,
        flags=re.DOTALL
    )

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Fully synchronized Section 2 & 2A on index_es.html")
