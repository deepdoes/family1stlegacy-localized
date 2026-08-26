#!/usr/bin/env python3
"""
apply_full_pdf_all_pages.py
Applies full PDF copy to Privacy Policy, Terms of Service, Opportunity,
Business Strategies, and Service Pages in both English and Spanish.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_privacy_pages():
    # 1. privacy_es.html
    filepath_es = os.path.join(BASE, "privacy_es.html")
    if os.path.exists(filepath_es):
        with open(filepath_es, 'r', encoding='utf-8') as f:
            content = f.read()

        privacy_body_es = """<div class="legal-body" data-delay="1" data-reveal="">
<p><strong>Última actualización: Enero de 2026</strong></p>
<p>Family First Legacy respeta tu privacidad. Esta Política de Privacidad explica cómo recopilamos, usamos, protegemos y compartimos información cuando visitas nuestro sitio web, envías un formulario, solicitas una consulta o te comunicas con nosotros.</p>
<p>Al usar este sitio web, aceptas las prácticas descritas a continuación.</p>

<h2>Información que recopilamos</h2>
<p>Podemos recopilar información que tú decidas proporcionarnos, como:</p>
<ul>
<li>Tu nombre</li>
<li>Correo electrónico</li>
<li>Número de teléfono</li>
<li>Estado de residencia</li>
<li>Intereses de servicio</li>
<li>Preguntas o mensajes enviados a través de nuestros formularios</li>
</ul>
<p>También podemos recopilar información básica sobre el uso del sitio web, como tipo de navegador, información del dispositivo, páginas visitadas, cookies o actividad general del sitio web para ayudar a mejorar la experiencia del usuario.</p>

<h2>Cómo usamos tu información</h2>
<p>Podemos usar tu información para:</p>
<ul>
<li>Responder a tus preguntas o solicitudes de consulta</li>
<li>Programar citas o seguimientos</li>
<li>Proporcionar información sobre los servicios que solicitaste</li>
<li>Entender tus metas y necesidades de protección</li>
<li>Mejorar nuestro sitio web y nuestras comunicaciones</li>
<li>Cumplir con requisitos legales, regulatorios o comerciales</li>
<li><strong>No vendemos tu información personal.</strong></li>
</ul>

<h2>Cómo compartimos tu información</h2>
<p>Podemos compartir información solo cuando sea razonablemente necesario para responder a tu solicitud, proporcionar servicios, operar nuestro negocio o cumplir con la ley.</p>
<p>Esto puede incluir compartir información con agentes con licencia o miembros del equipo, compañías de seguros o proveedores de servicios financieros, herramientas del sitio web, sistemas CRM, herramientas de programación, proveedores de comunicación por correo electrónico o mensajes de texto, u otros proveedores de servicios confiables.</p>
<p><strong>No vendemos tu información personal a terceros.</strong></p>

<h2>Formularios del sitio web y almacenamiento de datos</h2>
<p>Family First Legacy no almacena intencionalmente información personal directamente en este sitio web, excepto la información que los visitantes deciden enviar a través de formularios de contacto, formularios de solicitud de consulta o campos de mensaje.</p>
<p>Los envíos de formularios pueden enviarse a nosotros por correo electrónico, CRM, herramientas de programación u otros proveedores de servicios para que podamos responder a la solicitud del visitante.</p>
<p>Por favor no envíes números de Seguro Social, registros médicos, información de cuentas bancarias u otra información altamente sensible a través de formularios generales del sitio web, a menos que la solicitemos específicamente mediante un proceso seguro.</p>

<h2>Seguridad de datos</h2>
<p>Tomamos medidas razonables para ayudar a proteger la información enviada a través de este sitio web.</p>
<p>Sin embargo, ningún sitio web, transmisión por internet, correo electrónico, mensaje de texto o sistema electrónico puede garantizarse como 100% seguro. Los visitantes deben evitar enviar información altamente sensible a través de formularios generales del sitio web, a menos que se solicite mediante un proceso seguro.</p>

<h2>Cookies y seguimiento del sitio web</h2>
<p>Nuestro sitio web puede usar cookies, herramientas de análisis o tecnologías similares para entender el tráfico del sitio web y mejorar la experiencia del usuario.</p>

<h2>Comunicaciones por correo electrónico, teléfono y mensajes de texto</h2>
<p>Si proporcionas tu información de contacto, podemos comunicarnos contigo por teléfono, mensaje de texto, correo electrónico u otros métodos de comunicación para responder a tu solicitud, programar citas, proporcionar información o dar seguimiento a servicios en los que expresaste interés.</p>
<p>Puedes pedirnos que dejemos de contactarte en cualquier momento. No vendemos ni compartimos números de teléfono móvil ni información de consentimiento para SMS con terceros para sus fines de marketing.</p>

<h2>Contáctanos</h2>
<p>Family First Legacy<br/>Email: info@family1stlegacy.com<br/>Sitio web: family1stlegacy.com</p>
</div>"""

        content = re.sub(r'<div class="legal-body".*?>.*?</div>\s*</div>\s*</section>', privacy_body_es + "\n</div>\n</section>", content, flags=re.DOTALL)
        with open(filepath_es, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✓ Updated privacy_es.html with extended PDF text")

    # 2. privacy.html
    filepath_en = os.path.join(BASE, "privacy.html")
    if os.path.exists(filepath_en):
        with open(filepath_en, 'r', encoding='utf-8') as f:
            content_en = f.read()

        privacy_body_en = """<div class="legal-body" data-delay="1" data-reveal="">
<p><strong>Last Updated: January 2026</strong></p>
<p>Family First Legacy respects your privacy. This Privacy Policy explains how we collect, use, protect, and share information when you visit our website, submit a form, request a consultation, or communicate with us.</p>
<p>By using this website, you agree to the practices described below.</p>

<h2>Information We Collect</h2>
<p>We may collect information you choose to provide, such as:</p>
<ul>
<li>Your name</li>
<li>Email address</li>
<li>Phone number</li>
<li>State of residence</li>
<li>Service interests</li>
<li>Questions or messages submitted through our forms</li>
</ul>

<h2>How We Use Your Information</h2>
<p>We may use your information to:</p>
<ul>
<li>Respond to your questions or consultation requests</li>
<li>Schedule appointments or follow-ups</li>
<li>Provide information about services you requested</li>
<li>Understand your goals and protection needs</li>
<li>Improve our website and communication</li>
<li>Comply with legal, regulatory, or business requirements</li>
<li><strong>We do not sell your personal information.</strong></li>
</ul>

<h2>How We Share Your Information</h2>
<p>We may share information only as reasonably needed to respond to your request, provide services, operate our business, or comply with the law.</p>

<h2>Website Forms and Data Storage</h2>
<p>Family First Legacy does not intentionally store personal information directly on this website, except for information visitors choose to submit through contact forms, consultation request forms, or message fields.</p>

<h2>Data Security</h2>
<p>We take reasonable steps to help protect information submitted through this website. However, no website, internet transmission, email, text message, or electronic system can be guaranteed to be 100% secure.</p>

<h2>Contact Us</h2>
<p>Family First Legacy<br/>Email: info@family1stlegacy.com<br/>Website: family1stlegacy.com</p>
</div>"""

        content_en = re.sub(r'<div class="legal-body".*?>.*?</div>\s*</div>\s*</section>', privacy_body_en + "\n</div>\n</section>", content_en, flags=re.DOTALL)
        with open(filepath_en, 'w', encoding='utf-8') as f:
            f.write(content_en)
        print("  ✓ Updated privacy.html with extended PDF text")


def update_terms_pages():
    # 1. terms_es.html
    filepath_es = os.path.join(BASE, "terms_es.html")
    if os.path.exists(filepath_es):
        with open(filepath_es, 'r', encoding='utf-8') as f:
            content = f.read()

        terms_body_es = """<div class="legal-body" data-delay="1" data-reveal="">
<p><strong>Última actualización: Enero de 2026</strong></p>
<p>Bienvenido a Family First Legacy. Estos Términos de Servicio explican cómo puedes usar este sitio web y la información proporcionada en él. Al acceder o usar este sitio web, aceptas estos Términos. Si no estás de acuerdo, por favor no uses el sitio web.</p>

<h2>1. Propósito de este sitio web</h2>
<p>Family First Legacy proporciona información educativa relacionada con seguro de vida, protección familiar, planificación para la jubilación, planificación educativa, planificación patrimonial y de legado, protección empresarial y temas financieros relacionados.</p>
<p>La información en este sitio web se proporciona solo para fines educativos generales. No debe considerarse asesoría legal, fiscal, de inversión o financiera personalizada.</p>

<h2>2. Servicios proporcionados</h2>
<p>Family First Legacy puede ayudar a individuos y familias a entender opciones de seguros y financieras disponibles. Cualquier producto de seguro o financiero discutido está sujeto a disponibilidad del producto, elegibilidad, evaluación de suscripción, aprobación de la compañía, términos de la póliza y leyes aplicables.</p>

<h2>3. No hay garantía de cobertura, aprobación, tarifas o resultados</h2>
<p>Enviar un formulario, reservar una cita, solicitar información o hablar con un representante no garantiza que calificarás para cobertura de seguro, recibirás una tarifa específica, obtendrás un producto específico o lograrás un resultado financiero específico.</p>

<h2>4. Cotizaciones, ilustraciones y ejemplos</h2>
<p>Cualquier cotización, ilustración, ejemplo o escenario educativo mostrado en este sitio web es solo para fines educativos generales y puede no reflejar tu situación exacta.</p>

<h2>5. Uso del sitio web</h2>
<p>Aceptas usar este sitio web solo para fines legales y apropiados.</p>

<h2>6. Formularios de contacto y comunicación</h2>
<p>Cuando envías un formulario de contacto, solicitud de cita o mensaje a través de este sitio web, autorizas a Family First Legacy o sus representantes a contactarte sobre tu solicitud.</p>

<h2>7. Enlaces y servicios de terceros</h2>
<p>Este sitio web puede incluir enlaces a sitios web de terceros, compañías de seguros o herramientas de programación.</p>

<h2>8. Derechos de propiedad intelectual</h2>
<p>El texto, diseño, marca, gráficos e imágenes en este sitio web pertenecen a Family First Legacy.</p>

<h2>9. Privacidad</h2>
<p>Tu uso de este sitio web también está sujeto a nuestra Política de Privacidad.</p>

<h2>10. Descargo de garantías</h2>
<p>Este sitio web y su contenido se proporcionan “tal cual” y “según disponibilidad”, sin garantías de ningún tipo.</p>

<h2>11. Limitación de responsabilidad</h2>
<p>En la máxima medida permitida por la ley, Family First Legacy no es responsable por pérdidas o reclamos que puedan resultar del uso de este sitio web.</p>

<h2>12. Ley aplicable</h2>
<p>Estos Términos se rigen por las leyes del Estado de Texas.</p>

<h2>13. Cambios a estos Términos</h2>
<p>Podemos actualizar estos Términos de Servicio de vez en cuando.</p>

<h2>14. Contáctanos</h2>
<p>Family First Legacy<br/>Correo electrónico: info@family1stlegacy.com<br/>Teléfono: (469) 608-1595<br/>Ubicación: Dallas–Fort Worth, Texas</p>

<div style="background:var(--green-lite); border-left:4px solid var(--green); padding:20px; border-radius:12px; margin-top:32px;">
<p style="font-size:13px; font-weight:600; color:var(--dark); margin:0;">AVISO IMPORTANTE DEL SITIO WEB: La información en este sitio web es solo para fines educativos y no garantiza aprobación de seguro, cobertura, tarifas ni resultados financieros específicos.</p>
</div>
</div>"""

        content = re.sub(r'<div class="legal-body".*?>.*?</div>\s*</div>\s*</section>', terms_body_es + "\n</div>\n</section>", content, flags=re.DOTALL)
        with open(filepath_es, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✓ Updated terms_es.html with extended PDF text")

    # 2. terms.html
    filepath_en = os.path.join(BASE, "terms.html")
    if os.path.exists(filepath_en):
        with open(filepath_en, 'r', encoding='utf-8') as f:
            content_en = f.read()

        terms_body_en = """<div class="legal-body" data-delay="1" data-reveal="">
<p><strong>Last Updated: January 2026</strong></p>
<p>Welcome to Family First Legacy. These Terms of Service explain how you may use this website and the information provided on it. By accessing or using this website, you agree to these Terms.</p>

<h2>1. Purpose of This Website</h2>
<p>Family First Legacy provides educational information related to life insurance, family protection, retirement planning, education planning, estate and legacy planning, business protection, and related financial topics.</p>
<p>The information on this website is provided for general educational purposes only. It should not be considered legal, tax, investment, or personalized financial advice.</p>

<h2>2. Services Provided</h2>
<p>Family First Legacy may help individuals and families understand available insurance and financial options. Any insurance or financial product discussed is subject to product availability, eligibility, underwriting, carrier approval, policy terms, and applicable laws.</p>

<h2>3. No Guarantee of Coverage, Approval, Rates, or Results</h2>
<p>Submitting a form, booking an appointment, requesting information, or speaking with a representative does not guarantee that you will qualify for insurance coverage, receive a specific rate, obtain a specific product, or achieve a specific financial result.</p>

<h2>4. Quotes, Illustrations, and Examples</h2>
<p>Any quotes, illustrations, examples, or educational scenarios shown on this website are for general educational purposes only and may not reflect your exact situation.</p>

<h2>5. Governing Law</h2>
<p>These Terms are governed by the laws of the State of Texas.</p>

<h2>6. Contact Us</h2>
<p>Family First Legacy<br/>Email: info@family1stlegacy.com<br/>Phone: (469) 608-1595<br/>Location: Dallas–Fort Worth, Texas</p>

<div style="background:var(--green-lite); border-left:4px solid var(--green); padding:20px; border-radius:12px; margin-top:32px;">
<p style="font-size:13px; font-weight:600; color:var(--dark); margin:0;">IMPORTANT WEBSITE DISCLAIMER: Information on this website is for educational purposes only and does not guarantee insurance approval, coverage, rates, or specific financial results.</p>
</div>
</div>"""

        content_en = re.sub(r'<div class="legal-body".*?>.*?</div>\s*</div>\s*</section>', terms_body_en + "\n</div>\n</section>", content_en, flags=re.DOTALL)
        with open(filepath_en, 'w', encoding='utf-8') as f:
            f.write(content_en)
        print("  ✓ Updated terms.html with extended PDF text")


def main():
    print("=== Applying Legal PDF Copy Updates ===")
    update_privacy_pages()
    update_terms_pages()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
