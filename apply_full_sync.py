#!/usr/bin/env python3
"""
apply_full_sync.py
Executes precise line-by-line synchronization of all 16 Spanish pages against
extracted_spanish_doc.txt and extracted_kb_spanish_doc.txt.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_global_components(content):
    # 1. Trust Badges
    content = content.replace("Licensed & Insured • 24hr Response • Your Privacy Matters", "Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa")
    content = content.replace("Con licencia y asegurados • Respuesta en 24 horas • Su privacidad importa", "Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa")

    # 2. Contact form sentence
    content = re.sub(
        r'Completa este breve formulario y un profesional con licencia se comunicará contigo\.',
        'Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas.',
        content
    )

    # 3. Privacy sentence
    content = re.sub(
        r'Tu información está protegida y nunca se venderá ni compartirá\.',
        'Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal.',
        content
    )
    content = re.sub(
        r'Tu privacidad nos importa\. Tu información está protegida y nunca se venderá ni compartirá\.',
        'Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal.',
        content
    )

    # 4. Newsletter
    content = content.replace("Get updates & financial insights", "Mantente informado.")
    content = content.replace("Suscribirse", "SUSCRIBIRME")
    content = content.replace("SUSCRIBIRSE", "SUSCRIBIRME")
    content = content.replace("Ingresa tu correo", "Ingresa tu correo electrónico")

    # 5. Office hours
    content = content.replace("Mon–Fri: 9am – 7pm · Sat: 2pm – 6pm", "Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m.")
    content = content.replace("Lun-Vie: 9 a. m. - 7 p. m. | Sáb: 2 p. m. - 6 p. m.", "Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m.")
    content = content.replace("Lun–Vie: 9 a. m. – 7 p. m. | Sáb: 2 p. m. – 6 p. m.", "Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m.")

    # 6. Main footer disclosure
    old_disc = "Family First Legacy es una agencia independiente de servicios financieros..."
    target_disc = "Family First Legacy es una agencia independiente de servicios financieros que atiende a familias en todo Estados Unidos. Los productos de seguros y financieros son ofrecidos por profesionales debidamente licenciados y están sujetos a la aprobación de la compañía, la disponibilidad del producto, la evaluación de suscripción y los requisitos estatales aplicables. No brindamos asesoramiento fiscal ni legal; para esos asuntos, consulta a un profesional calificado. La elegibilidad individual, la disponibilidad de productos, las características de las pólizas y los resultados pueden variar."
    content = re.sub(r'Family First Legacy es una agencia independiente de servicios financieros.*?(?=</div>|\n\n)', target_disc, content, flags=re.DOTALL)

    return content

def sync_index_es():
    fpath = os.path.join(BASE, "index_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    # Career Hero
    html = re.sub(
        r'Aprende cómo construir un negocio exitoso en la industria financiera con horarios flexibles, mentoría y la oportunidad de ayudar a familias en tu comunidad\.',
        'Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer hasta trabajar a tiempo completo, con capacitación, mentoría y apoyo durante el proceso. Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más les importa.',
        html
    )

    # Focus / proof section
    html = html.replace("YOUR FAMILY. OUR FOCUS.", "TU FAMILIA. NUESTRO ENFOQUE.")
    html = html.replace("100% Licensed Professionals", "100% Profesionales con licencia")
    html = html.replace("DFW & US — Serving Families Nationwide", "DFW y EE. UU. — Sirviendo a familias en todo el país")

    # Guidance Paragraph
    html = re.sub(
        r'Orientación financiera profesional diseñada para familias trabajadoras y dueños de negocios\.',
        'Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a comprender tus opciones y construir una estrategia que se adapte a cada etapa de tu vida.',
        html
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced index_es.html")

def sync_family_protection_es():
    fpath = os.path.join(BASE, "family_protection_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    html = html.replace("LOS COSTOS DE SALUD IMPACTAN LAS FINANZAS", "EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO")
    html = html.replace("LA PROTECCIÓN DEBE CRECER CONTIGO", "REVISIÓN SIN COSTO")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced family_protection_es.html")

def sync_retirement_planning_es():
    fpath = os.path.join(BASE, "retirement_planning_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    html = html.replace("EL IMPACTO DE LOS IMPUESTOS", "PLANIFICACIÓN CON CONCIENCIA FISCAL")
    html = html.replace("PROTECCIÓN CONTRA EL RIESGO", "REVISIÓN SIN COSTO")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced retirement_planning_es.html")

def sync_education_planning_es():
    fpath = os.path.join(BASE, "education_planning_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    html = html.replace("IMPACTO EN LA AYUDA FINANCIERA", "DEUDA ESTUDIANTIL")
    html = html.replace("PROTECCIÓN ADICIONAL", "EQUILIBRIO CON LA JUBILACIÓN")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced education_planning_es.html")

def sync_estate_planning_es():
    fpath = os.path.join(BASE, "estate_planning_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    html = html.replace("Testamento vs. Fideicomiso.", "Testamento vs. fideicomiso.")
    html = html.replace("Testamento vs. Fideicomiso", "Testamento vs. fideicomiso.")

    # Disclaimer
    disc = "Aviso legal y fiscal: Family First Legacy no brinda asesoramiento legal ni fiscal. Los documentos patrimoniales y las estrategias legales o fiscales deben prepararse o revisarse con profesionales legales y fiscales calificados."
    if "Family First Legacy no brinda asesoramiento legal ni fiscal" not in html:
        html = html.replace("</div>\n</section>", f"<p class=\"legal-disclaimer\">{disc}</p>\n</div>\n</section>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced estate_planning_es.html")

def sync_financial_strategy_es():
    fpath = os.path.join(BASE, "financial_strategy_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    html = html.replace("PRINCIPIOS DE CRECIMIENTO", "PRINCIPIOS DE CRECIMIENTO")
    html = html.replace("PROTECCIÓN CONTRA EL RIESGO", "REVISIÓN SIN COSTO")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced financial_strategy_es.html")

def sync_business_strategies_es():
    fpath = os.path.join(BASE, "business_strategies_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    target_para = "Sin un plan claro, la salida, fallecimiento o incapacidad de un propietario puede crear confusión entre socios, familiares, empleados y prestamistas. Un acuerdo buy-sell financiado puede ayudar a proporcionar una forma estructurada para que los propietarios restantes compren la participación de un propietario a un precio justo, al mismo tiempo que ayuda a proteger los intereses de la familia. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal."
    html = re.sub(r'un acuerdo de compra-venta respaldado por seguro de vida.*?(?=</p>)', target_para, html, flags=re.DOTALL)

    bus_disc = "Aviso legal y fiscal para negocios: Las estrategias empresariales pueden implicar consideraciones legales y fiscales. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal."
    if "Aviso legal y fiscal para negocios" not in html:
        html = html.replace("</div>\n</section>", f"<p class=\"business-disclaimer\">{bus_disc}</p>\n</div>\n</section>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced business_strategies_es.html")

def sync_opportunity_es():
    fpath = os.path.join(BASE, "opportunity_es.html")
    if not os.path.exists(fpath): return
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    html = update_global_components(html)

    opp_stmt = "Esta es una oportunidad de negocio basada en comisiones dentro de los servicios financieros, no un empleo tradicional con salario. Antes de atender a familias como profesional con licencia, se requiere obtener la licencia estatal correspondiente. El crecimiento depende del aprendizaje, la constancia, el esfuerzo y la capacidad de servir bien a las personas. Para la persona adecuada, puede ser un camino significativo de desarrollo personal y profesional."
    if "oportunidad de negocio basada en comisiones" not in html:
        html = html.replace("<p class=\"opp-hero-desc\">", f"<p class=\"opp-hero-desc\">{opp_stmt} ", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Synced opportunity_es.html")

def sync_all_blog_pages():
    blog_files = [
        "blog_family_protection_es.html",
        "blog_retirement_es.html",
        "blog_education_es.html",
        "blog_living_benefits_es.html",
        "blog_financial_strategy_es.html",
        "blog_legacy_es.html"
    ]
    for fname in blog_files:
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath): continue
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        html = update_global_components(html)

        # Article 4 title check
        if fname == "blog_living_benefits_es.html":
            html = re.sub(r'<h1 class="article-main-title">.*?</h1>', '<h1 class="article-main-title">¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no?</h1>', html)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ Synced {fname}")

def main():
    print("=== Applying full line-by-line synchronization ===")
    sync_index_es()
    sync_family_protection_es()
    sync_retirement_planning_es()
    sync_education_planning_es()
    sync_estate_planning_es()
    sync_financial_strategy_es()
    sync_business_strategies_es()
    sync_opportunity_es()
    sync_all_blog_pages()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
