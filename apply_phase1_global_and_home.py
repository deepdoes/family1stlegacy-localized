#!/usr/bin/env python3
"""
apply_phase1_global_and_home.py
Applies Section 1 (Global Shared Components) and Section 2 & 2A (Home Page) from Document 1.
"""

import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

spanish_files = [f for f in os.listdir(BASE_DIR) if f.endswith("_es.html") and os.path.isfile(os.path.join(BASE_DIR, f))]
print(f"Found {len(spanish_files)} Spanish HTML files.")

# Exact Strings from Document 1
TRUST_BADGES_NEW = "Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa"
CONTACT_FORM_NEW = "Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas."
PRIVACY_LINE_NEW = "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal."
NEWSLETTER_NEW = "Información mensual sobre protección familiar, planificación financiera y preparación para el futuro. Puedes cancelar tu suscripción en cualquier momento."
FOOTER_DISCLOSURE_NEW = (
    "Family First Legacy es una agencia independiente de servicios financieros que atiende a familias en todo Estados Unidos. "
    "Los productos de seguros y financieros son ofrecidos por profesionales debidamente licenciados y están sujetos a la aprobación "
    "de la compañía, la disponibilidad del producto, la evaluación de suscripción y los requisitos estatales aplicables. "
    "No brindamos asesoramiento fiscal ni legal; para esos asuntos, consulta a un profesional calificado. "
    "La elegibilidad individual, la disponibilidad de productos, las características de las pólizas y los resultados pueden variar."
)
HOURS_NEW = "Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m."

# Phase 1: Apply Global updates across all Spanish pages
for fname in spanish_files:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Trust badges
    # Replace any previous trust badges variants
    content = re.sub(
        r'Con licencia y asegurados\s*•\s*Respuesta en 24 horas\s*•\s*Su privacidad importa',
        TRUST_BADGES_NEW,
        content
    )
    content = re.sub(
        r'Con licencia y asegurados\s*•\s*Respuesta en 24 horas\s*•\s*Tu privacidad importa',
        TRUST_BADGES_NEW,
        content
    )
    content = re.sub(
        r'Con licencia y asegurados\s*•\s*Respuesta 24h\s*•\s*Su privacidad importa',
        TRUST_BADGES_NEW,
        content
    )
    content = re.sub(
        r'Licensed & Insured\s*•\s*24hr Response\s*•\s*Your Privacy Matters',
        TRUST_BADGES_NEW,
        content
    )

    # 2. Contact form sentence
    content = re.sub(
        r'Complete el formulario a continuación y nos pondremos en contacto con usted dentro de las 24 horas\.',
        CONTACT_FORM_NEW,
        content
    )
    content = re.sub(
        r'Complete el formulario a continuación; nuestra meta es responderle dentro de las próximas 24 horas\.',
        CONTACT_FORM_NEW,
        content
    )
    content = re.sub(
        r'Completa el formulario a continuación y nos pondremos en contacto contigo dentro de las 24 horas\.',
        CONTACT_FORM_NEW,
        content
    )

    # 3. Privacy line
    content = re.sub(
        r'Su información se maneja con cuidado y se mantiene privada\. No vendemos su información personal\.',
        PRIVACY_LINE_NEW,
        content
    )
    content = re.sub(
        r'Tu información se maneja con cuidado y se mantiene privada\. Nunca vendemos tu información personal\.',
        PRIVACY_LINE_NEW,
        content
    )

    # 4. Newsletter
    content = re.sub(
        r'Información mensual sobre protección familiar, planificación financiera y preparación para el futuro\. Cancele su suscripción en cualquier momento\.',
        NEWSLETTER_NEW,
        content
    )

    # 5. Office hours
    content = re.sub(
        r'Sáb:\s*10\s*a\.\s*m\.\s*–\s*4\s*p\.\s*m\.',
        'Sáb: 2 p. m. – 6 p. m.',
        content
    )
    content = re.sub(
        r'Sáb:\s*10\s*am\s*–\s*4\s*pm',
        'Sáb: 2 p. m. – 6 p. m.',
        content
    )
    content = re.sub(
        r'Sat:\s*10am\s*–\s*4pm',
        'Sáb: 2 p. m. – 6 p. m.',
        content
    )

    # 6. Split service labels
    content = content.replace("Educación / Planificación", "Planificación Educativa")
    content = content.replace("Financiero / Estrategia", "Estrategia Financiera")
    content = content.replace("Bienes & / Planificación heredada", "Planificación Patrimonial y de Legado")
    content = content.replace("Bienes y / Planificación heredada", "Planificación Patrimonial y de Legado")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

print("Global shared components updated across all Spanish pages.")

# Phase 2: Home Page (index_es.html) updates
idx_path = os.path.join(BASE_DIR, "index_es.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# 2.1 Hero Slide 6 (Career Opportunity)
hero_opp_old_pattern = r'<p class="slide-sub">Únase a miles de emprendedores que convirtieron su pasión por ayudar a las familias en un próspero negocio de servicios financieros\. Comience a tiempo parcial, pase a tiempo completo: la oportunidad es suya para definirla\.</p>'
hero_opp_new = (
    '<p class="slide-sub">Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. '
    'Puedes comenzar a tiempo parcial o crecer hasta trabajar a tiempo completo, con capacitación, mentoría y apoyo durante el proceso. '
    'Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más les importa.</p>'
)
idx_content = re.sub(hero_opp_old_pattern, hero_opp_new, idx_content)

# 2.2 Focus / Proof section in Hero Stats Bar
old_stats_bar_pattern = r'<div class="hero-stats-bar">.*?</div>\s*</div>\s*</div>\s*</div>'
# Let's inspect exact hero-stats-bar
stats_bar_match = re.search(r'<div class="hero-stats-bar">[\s\S]*?</div>\s*</div>\s*</div>', idx_content)
if stats_bar_match:
    new_stats_bar = """<div class="hero-stats-bar">
    <div class="hsb-item">
      <div class="hsb-num" style="font-size:18px; font-weight:800; letter-spacing:1px; color:#fff;">TU FAMILIA.</div>
      <div class="hsb-label" style="font-weight:700; color:var(--amber-lt);">NUESTRO ENFOQUE.</div>
    </div>
    <div class="hsb-item">
      <div class="hsb-num">100%</div>
      <div class="hsb-label">Profesionales con licencia</div>
    </div>
    <div class="hsb-item">
      <div class="hsb-num">DFW y EE. UU.</div>
      <div class="hsb-label">Sirviendo a familias en todo el país</div>
    </div>
  </div>"""
    # Replace only the hero-stats-bar
    idx_content = idx_content[:stats_bar_match.start()] + new_stats_bar + idx_content[stats_bar_match.start() + len(stats_bar_match.group(0)): ]
    print("  ✓ Replaced Hero Stats Bar in index_es.html")

# 2.3 Guidance for Every Stage paragraph
guidance_old_pattern = r'Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a comprender tus opciones y construir una estrategia que se adapte a cada etapa de tu vida\.'
# Verify it exists or replace if different

# 2.4 - 2.9 Service Cards
# Life Insurance (2.4)
idx_content = re.sub(
    r'<p class="sc-desc">Su familia depende de usted todos los días\..*?</p>',
    '<p class="sc-desc">Tu familia cuenta contigo todos los días. Te explicamos de manera sencilla el seguro de vida a término, el seguro de vida entera y el seguro de vida universal indexado (IUL), para que puedas elegir una cobertura que apoye a las personas que amas, tu presupuesto y tus metas futuras.</p>',
    idx_content,
    flags=re.DOTALL
)

# How It Works (2.10 - 2.12)
step2_old = '<div class="ps-body">Utilizamos un análisis integral de necesidades financieras para mapear su panorama actual e identificar exactamente qué estrategias de protección y crecimiento se aplican.</div>'
step2_new = '<div class="ps-body">Utilizamos un Análisis de Necesidades Financieras para revisar tu situación actual y ayudarte a identificar dónde podrían encajar opciones de protección, ahorro o jubilación según tus necesidades.</div>'
idx_content = idx_content.replace(step2_old, step2_new)

step3_old = '<div class="ps-body">Presentamos una estrategia clara y personalizada con los mejores productos de nuestra cartera de operadores con calificación A+, sin jerga ni presión.</div>'
step3_new = '<div class="ps-body">Te presentamos opciones claras de compañías de seguros y servicios financieros bien establecidas, explicadas en un lenguaje sencillo y sin presión.</div>'
idx_content = idx_content.replace(step3_old, step3_new)

ongoing_old = '<div class="ps-body">La vida cambia, y también debería hacerlo su plan. Nos quedamos con usted en cada hito, ajustando su estrategia a medida que su familia crece.</div>'
ongoing_new = '<div class="ps-body">La vida cambia, y tu plan también puede necesitar cambios. Seguimos disponibles para revisar tu plan, responder tus preguntas y ayudarte a hacer ajustes a medida que tu familia crece.</div>'
idx_content = idx_content.replace(ongoing_old, ongoing_new)

# 2.13 All 10 Home FAQs
home_faqs_html = """        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué hace exactamente Family First Legacy?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Family First Legacy ayuda a personas, familias y dueños de negocios a comprender sus opciones de seguro de vida, planificación para la jubilación, planificación educativa y planificación de legado. Explicamos todo con claridad para que puedas tomar decisiones informadas a tu propio ritmo.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Es realmente asequible el seguro de vida?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El seguro de vida puede ser más accesible de lo que muchas personas esperan. El costo depende de la edad, la salud, el monto de cobertura, el tipo de producto y la elegibilidad.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Necesito seguro de vida si no tengo hijos?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El seguro de vida no es solo para padres. Puede ayudar a cubrir gastos finales, deudas como una hipoteca o apoyar a personas que dependen de ti. Algunas pólizas también pueden incluir beneficios en vida para ciertas enfermedades o condiciones cubiertas.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué son los beneficios en vida?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Los beneficios en vida pueden permitir que los titulares de pólizas que califican accedan a una parte de los beneficios de su póliza mientras aún viven si enfrentan ciertas enfermedades o condiciones cubiertas. Estos fondos pueden ayudar con necesidades como facturas, gastos médicos o pérdida de ingresos. La disponibilidad depende de la póliza y de la elegibilidad.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Es el seguro de Vida Universal Indexada (IUL) una buena inversión?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El IUL es, ante todo, un seguro de vida, no una inversión directa en el mercado de valores. Dependiendo del diseño de la póliza, puede ayudar a proteger a tu familia mientras acumula valor en efectivo vinculado a un índice de mercado. Muchas pólizas IUL incluyen un piso del 0% para la acreditación de intereses vinculados al índice, lo que puede ayudar a reducir el impacto de un rendimiento negativo del índice. Los cargos de la póliza y otros términos siguen aplicando y pueden afectar el valor en efectivo.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Por qué no debería usar solamente un 401(k) para la jubilación?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Un 401(k) puede ser una herramienta valiosa para la jubilación, pero por sí solo quizá no cubra todas las necesidades de retiro. Los retiros de un 401(k) tradicional generalmente están sujetos a impuestos y el valor de la cuenta puede subir o bajar con el mercado. Algunas familias también exploran anualidades o estrategias de seguro de vida para añadir opciones de protección del capital, ingresos y mayor equilibrio a su plan de jubilación.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo puede una anualidad ayudar a proteger mi dinero?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Algunas anualidades fijas indexadas están diseñadas para ayudar a proteger el capital frente a un rendimiento negativo del índice, al mismo tiempo que ofrecen la posibilidad de recibir créditos de interés vinculados al índice cuando corresponda. Pueden aplicar términos del contrato, límites, tasas de participación, cargos por rescate, retiros y otras limitaciones. Como cada producto funciona de manera diferente, explicamos los detalles con claridad para que comprendas la protección, el potencial de crecimiento y las reglas antes de tomar una decisión.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué deben saber las familias sobre el proceso sucesorio?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El proceso sucesorio puede retrasar el acceso a ciertos bienes cuando una familia más necesita dinero. Un seguro de vida con el beneficiario adecuado puede ayudar a proporcionar fondos directamente a los seres queridos para facturas, gastos funerarios o necesidades diarias mientras otros bienes todavía se gestionan. Para testamentos, fideicomisos y planificación patrimonial legal, recomendamos trabajar con un profesional legal calificado.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Puedo usar un seguro de vida para ayudar a pagar la educación de mi hijo?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El seguro de vida permanente que acumula valor en efectivo puede ofrecer acceso flexible mediante préstamos o retiros de la póliza para la educación u otras necesidades futuras, dependiendo del diseño de la póliza. Como acceder al valor en efectivo puede afectar los beneficios de la póliza, es importante comprender cómo funciona tu póliza específica antes de utilizarlo. Podemos ayudarte a entender tus opciones y cómo podrían ajustarse a las metas de tu familia.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cobran una tarifa por las consultas?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>No. No cobramos una tarifa por hablar con nosotros. Tu revisión financiera se ofrece sin costo y sin presión. Es simplemente una conversación para comprender tu situación, responder tus preguntas y ayudarte a ver qué opciones pueden ajustarse a tus metas. No existe obligación de continuar.</p></div>
        </div>"""

faq_container_match = re.search(r'<div class="faq-list">[\s\S]*?</div>\s*</div>\s*</section>', idx_content)
if faq_container_match:
    idx_content = (
        idx_content[:faq_container_match.start()]
        + '<div class="faq-list">\n' + home_faqs_html + '\n      </div>\n    </div>\n  </section>'
        + idx_content[faq_container_match.end():]
    )
    print("  ✓ Replaced all 10 FAQs in index_es.html")

# Write updated index_es.html
with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Home page (index_es.html) Phase 1 updates applied successfully.")
