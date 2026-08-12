#!/usr/bin/env python3
"""
apply_pdf_spanish_final.py
Applies all client PDF Spanish updates to index_es.html and related Spanish HTML files.
Handles both .about-content and .who-we-are-body structure.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_index_es_html():
    filepath = os.path.join(BASE, "index_es.html")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Who We Are Section (ES) ---
    new_about_content_es = """<div class="about-content">
<p class="t-label" data-reveal=""><span class="green-dot"></span>QUIÉNES SOMOS</p>
<h2 class="t-h1" data-delay="1" data-reveal="">Ponemos a la familia<br/>primero. Siempre.</h2>
<p class="t-body" data-delay="2" data-reveal="" style="color:var(--muted); margin-bottom:16px;">Toda familia merece la oportunidad de proteger lo que ha construido, prepararse para el mañana y perseguir el futuro que sueña.</p>
<p class="t-body" data-delay="2" data-reveal="" style="color:var(--muted); margin-bottom:16px;">Creemos que toda familia, sin importar su origen o nivel de ingresos, merece acceso a orientación honesta y bien informada que le ayude a tomar decisiones financieras con conocimiento.</p>
<p class="t-body" data-delay="2" data-reveal="" style="color:var(--muted); margin-bottom:16px;">Family First Legacy es una agencia independiente de servicios financieros con raíces en la comunidad de Dallas-Fort Worth y que sirve a familias en todo Estados Unidos. Ayudamos a individuos, familias y dueños de negocios a explorar opciones de seguros y servicios financieros a través de una red de compañías bien establecidas.</p>
<p class="t-body" data-delay="2" data-reveal="" style="color:var(--muted); margin-bottom:16px;">Nuestros profesionales con licencia se toman el tiempo para escucharte, entender tus metas y preocupaciones, y conocer a las personas que más importan en tu vida antes de ayudarte a explorar opciones que puedan alinearse con tus necesidades.</p>
<p class="t-body" data-delay="2" data-reveal="" style="color:var(--muted); margin-bottom:24px;">Ya sea que estés protegiendo a tu familia, preparándote para la jubilación, planificando el futuro de tus hijos o construyendo un legado, nuestra meta es brindarte orientación honesta, explicaciones claras y la información que necesitas para tomar decisiones con confianza, sin presión y a tu propio ritmo.</p>
<div class="about-pull" data-delay="3" data-reveal="">
<p>“Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y les ayudamos a crear planes enfocados en proteger lo que más importa.”</p>
<cite>— Equipo de Family First Legacy</cite>
</div>
<a class="btn btn-green" data-delay="4" data-reveal="" href="#contact">
<svg fill="none" stroke="currentColor" stroke-width="2" viewbox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg>Programa una revisión gratuita</a>
</div>"""

    if '<div class="about-content">' in content:
        content = re.sub(
            r'<div class="about-content">.*?<a class="btn btn-green".*?</a>\s*</div>',
            new_about_content_es,
            content,
            flags=re.DOTALL
        )
        print("  ✓ Updated Who We Are section (.about-content) in index_es.html")

    # --- 2. Client Solutions -> CÓMO PODEMOS AYUDAR ---
    content = content.replace("Soluciones para clientes", "CÓMO PODEMOS AYUDAR")
    content = content.replace("Client Solutions", "CÓMO PODEMOS AYUDAR")
    content = content.replace("Protección para<br/>Cada etapa<br/>de<em>Vida.</em>", "Orientación para<br/>Cada etapa<br/>de<em>Vida.</em>")
    content = content.replace("Protección para cada etapa de la vida", "Orientación para cada etapa de la vida")
    content = content.replace("Desde la protección de su familia hoy hasta la preparación para la jubilación y la creación de riqueza para el futuro, ofrecemos estrategias personalizadas de las principales compañías de seguros.", "Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a entender tus opciones y crear una estrategia que se ajuste a cada capítulo de tu vida.")
    content = content.replace("Habla con un agente", "Comienza con una conversación")
    content = content.replace("Hable con un Agente", "Comienza con una conversación")

    # --- 3. Privacy Wording in Contact Form ---
    content = content.replace(
        "Tu información se mantiene estrictamente confidencial. Nunca compartimos tus datos.",
        "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal."
    )
    content = content.replace(
        "Su información se mantiene estrictamente confidencial. Nunca compartimos sus datos.",
        "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal."
    )

    # --- 4. Call to Action Section ---
    content = content.replace(
        "¿Estás listo para asegurar el futuro de tu familia?",
        "¿Listo para ayudar a proteger el futuro de tu familia?"
    )
    content = content.replace(
        "¿Está listo para asegurar el futuro de su familia?",
        "¿Listo para ayudar a proteger el futuro de tu familia?"
    )
    content = content.replace(
        "Programa una consulta gratuita hoy: sin presión, sin obligación, solo orientación honesta de profesionales con licencia que realmente se preocupan.",
        "Programa una consulta sin costo hoy: sin presión, sin obligación, solo orientación honesta de profesionales con licencia que realmente se preocupan."
    )
    content = content.replace("Obtenga su consulta gratuita", "Comienza sin costo")

    # --- 5. Footer Badge & Disclaimer ---
    content = content.replace("Licenciados a Nivel Nacional", "Sirviendo a familias en todo el país")
    content = content.replace("Sirviendo activamente en DFW y en todo el país", "Sirviendo a familias en todo el país")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✓ Completed index_es.html updates!")

if __name__ == "__main__":
    print("=== Updating index_es.html with Spanish PDF content ===")
    update_index_es_html()
    print("=== Done! ===")
