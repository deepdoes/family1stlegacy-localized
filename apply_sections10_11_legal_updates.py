#!/usr/bin/env python3
"""
apply_sections10_11_legal_updates.py
Replaces Spanish legal pages (privacy_es.html & terms_es.html) with exact pre-approved August 2026 master legal copy:
- Section 10: Privacy Policy (privacy_es.html)
- Section 11: Terms of Service (terms_es.html)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_privacy():
    fpath = os.path.join(BASE, "privacy_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    PRIVACY_CONTENT_ES = """
    <p class="legal-date">Última actualización: agosto de 2026</p>
    <p>Family First Legacy respeta tu privacidad. Esta Política de Privacidad explica cómo recopilamos, usamos, protegemos y compartimos información cuando visitas nuestro sitio web, envías un formulario, solicitas una consulta o te comunicas con nosotros.</p>
    <p>Al utilizar este sitio web, aceptas las prácticas descritas a continuación.</p>

    <h2>Información que recopilamos</h2>
    <p>Podemos recopilar información que tú decidas proporcionar, como: tu nombre; dirección de correo electrónico; número de teléfono; estado de residencia; servicios de interés; preguntas o mensajes enviados a través de nuestros formularios.</p>

    <h2>Cómo usamos tu información</h2>
    <p>Podemos usar tu información para responder a tus preguntas o solicitudes de consulta, programar citas o seguimientos, proporcionar información sobre los servicios solicitados, comprender tus metas y necesidades de protección, mejorar nuestro sitio web y nuestras comunicaciones, y cumplir con requisitos legales, regulatorios o comerciales. No vendemos tu información personal.</p>

    <h2>Cómo compartimos tu información</h2>
    <p>Podemos compartir información únicamente cuando sea razonablemente necesario para responder a tu solicitud, prestar servicios, operar nuestro negocio o cumplir con la ley.</p>

    <h2>Formularios del sitio web y almacenamiento de datos</h2>
    <p>Family First Legacy no utiliza intencionalmente este sitio web como repositorio de información personal sensible. La información enviada mediante formularios puede ser procesada o almacenada por los proveedores de servicios que utilizamos para operar formularios, correo electrónico, CRM, programación de citas, análisis o alojamiento del sitio web.</p>

    <h2>Cookies, análisis y herramientas de comunicación</h2>
    <p>Podemos utilizar cookies, herramientas de análisis, software CRM, plataformas de programación de calendarios y servicios de comunicación por correo electrónico o SMS para ayudar a operar nuestro sitio web, responder a solicitudes de consulta, administrar citas y comunicarnos contigo de manera efectiva.</p>

    <h2>Seguridad de los datos</h2>
    <p>Tomamos medidas razonables para ayudar a proteger la información enviada a través de este sitio web. Sin embargo, ningún sitio web, transmisión por internet, correo electrónico, mensaje de texto o sistema electrónico puede garantizarse como 100% seguro.</p>

    <h2>Contáctanos</h2>
    <p>Family First Legacy<br/>
    Correo electrónico: info@family1stlegacy.com<br/>
    Sitio web: family1stlegacy.com</p>
    """

    html = re.sub(
        r'<div class="legal-body">.*?</div>\s*</div>\s*</main>',
        f'<div class="legal-body">\n{PRIVACY_CONTENT_ES}\n</div>\n</div>\n</main>',
        html,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Updated privacy_es.html to August 2026 master legal copy")

def update_terms():
    fpath = os.path.join(BASE, "terms_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    TERMS_CONTENT_ES = """
    <p class="legal-date">Última actualización: agosto de 2026</p>
    <p>Bienvenido a Family First Legacy. Estos Términos de Servicio explican cómo puedes utilizar este sitio web y la información que se proporciona en él. Al acceder o utilizar este sitio web, aceptas estos Términos.</p>

    <h2>1. Propósito de este sitio web</h2>
    <p>Family First Legacy proporciona información educativa relacionada con seguro de vida, protección familiar, planificación para la jubilación, planificación educativa, planificación patrimonial y de legado, protección empresarial y temas financieros relacionados. La información de este sitio web se proporciona únicamente con fines educativos generales. No debe considerarse asesoramiento legal, fiscal, de inversión ni asesoramiento financiero personalizado.</p>

    <h2>2. Servicios proporcionados</h2>
    <p>Family First Legacy puede ayudar a personas y familias a comprender las opciones de seguros y financieras disponibles. Cualquier producto de seguro o financiero mencionado está sujeto a disponibilidad del producto, elegibilidad, evaluación de suscripción, aprobación de la compañía, términos de la póliza y leyes aplicables.</p>

    <h2>3. No existe garantía de cobertura, aprobación, tarifas o resultados</h2>
    <p>Enviar un formulario, reservar una cita, solicitar información o hablar con un representante no garantiza que calificarás para cobertura de seguro, recibirás una tarifa específica, obtendrás un producto determinado o lograrás un resultado financiero específico.</p>

    <h2>4. Cotizaciones, ilustraciones y ejemplos</h2>
    <p>Cualquier cotización, ilustración, ejemplo o escenario educativo mostrado en este sitio web se proporciona únicamente con fines educativos generales y puede no reflejar tu situación exacta.</p>

    <h2>5. Ley aplicable</h2>
    <p>Estos Términos se rigen por las leyes del Estado de Texas.</p>

    <h2>6. Contáctanos</h2>
    <p>Family First Legacy<br/>
    Correo electrónico: info@family1stlegacy.com<br/>
    Teléfono: (469) 608-1595<br/>
    Ubicación: Dallas–Fort Worth, Texas</p>

    <div class="legal-disclaimer-box" style="margin-top:32px; padding:20px; background:#F8FAFC; border-left:4px solid #4A2D7A; border-radius:12px; font-size:13px; color:#475569;">
      <strong>AVISO IMPORTANTE DEL SITIO WEB:</strong> La información de este sitio web se proporciona únicamente con fines educativos y no garantiza aprobación de seguro, cobertura, tarifas ni resultados financieros específicos.
    </div>
    """

    html = re.sub(
        r'<div class="legal-body">.*?</div>\s*</div>\s*</main>',
        f'<div class="legal-body">\n{TERMS_CONTENT_ES}\n</div>\n</div>\n</main>',
        html,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ Updated terms_es.html to August 2026 master legal copy")

def main():
    print("=== Updating Spanish Legal Pages (Privacy & Terms) to August 2026 Master ===")
    update_privacy()
    update_terms()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
