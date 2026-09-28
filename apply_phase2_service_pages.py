#!/usr/bin/env python3
"""
apply_phase2_service_pages.py
Updates all 5 Service Pages in Spanish according to Document 1:
- family_protection_es.html (Restores missing #services and #faq sections with exact copy)
- retirement_planning_es.html (Hero, Proof cards, 3 service rows, 10 FAQs)
- education_planning_es.html (Hero, Proof cards, 2 service rows, 10 FAQs)
- estate_planning_es.html (Hero, Proof cards, 3 service rows, 8 FAQs)
- financial_strategy_es.html (Hero, Proof cards, 3 service rows, 10 FAQs)
"""

import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_family_protection():
    fpath = os.path.join(BASE_DIR, "family_protection_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Hero title and subtitle (3.1)
    hero_title_old = r'<h1 class="sh-title">.*?</h1>'
    hero_title_new = '<h1 class="sh-title">Protege a las personas<br><em>que más importan.</em></h1>'
    content = re.sub(hero_title_old, hero_title_new, content, count=1, flags=re.DOTALL)

    hero_sub_old = r'<p class="sh-sub">.*?</p>'
    hero_sub_new = '<p class="sh-sub">La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesiten. Te ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para ajustarse a tus necesidades, tu presupuesto y tu vida.</p>'
    content = re.sub(hero_sub_old, hero_sub_new, content, count=1, flags=re.DOTALL)

    # 2. Update Proof cards (3.2) - Remove old 60%, 1-in-4, 9-24m stats!
    proof_cards_html = """          <div class="numbers-grid">
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">LOS BENEFICIOS DEL TRABAJO PUEDEN DEJAR BRECHAS</div>
              <div class="glass-label">Conoce qué protege a tu familia antes de que la vida cambie</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">SI LOS INGRESOS SE DETIENEN</div>
              <div class="glass-label">¿Podría tu familia seguir pagando las facturas el próximo mes?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO</div>
              <div class="glass-label">Planifica antes de que tus seres queridos lo necesiten</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">REVISIÓN SIN COSTO</div>
              <div class="glass-label">Pregunta ahora. Decide con claridad y sin presión.</div>
            </div>
          </div>"""

    content = re.sub(r'<div class="numbers-grid">[\s\S]*?</div>\s*</div>\s*</div>', proof_cards_html + '\n        </div>\n      </div>', content)

    # 3. Restore #services and #faq sections before #contact!
    services_section_html = """    <section id="services" style="padding-top: 100px;">
      <div class="container">
    
        <!-- 3.3 Bills Don't Wait -->
        <div class="service-row" data-reveal>
          <div class="sr-photo-wrap">
            <img class="sr-photo loaded" src="images/probate_trap_diverse_1777393105349.png" alt="El proceso sucesorio puede demorar el dinero.">
          </div>
          <div class="sr-content" data-reveal="right" data-delay="2">
            <div class="sr-num">01</div>
            <h3 class="sr-title">Las facturas no esperan<br><em>a que termine el proceso legal.</em></h3>
            <p class="sr-body">Después de una pérdida, tu familia puede necesitar dinero de inmediato para gastos funerarios, renta o hipoteca, alimentos y las necesidades de los hijos. Sin embargo, algunos bienes pueden demorarse durante el proceso sucesorio. Un seguro de vida con el beneficiario adecuado puede ayudar a proporcionar fondos directamente a tus seres queridos mientras otros bienes todavía están siendo gestionados.</p>
          </div>
        </div>
        
        <!-- 3.4 What If You Were Alive -->
        <div class="service-row flip" data-reveal>
          <div class="sr-photo-wrap">
            <img class="sr-photo loaded" src="images/chronic_illness_diverse_1777393119808.png" alt="Enfermedad grave.">
          </div>
          <div class="sr-content" data-reveal="right" data-delay="2">
            <div class="sr-num">02</div>
            <h3 class="sr-title">¿Qué pasaría si siguieras con vida —<br><em>pero tu cheque de pago se detuviera?</em></h3>
            <p class="sr-body">Una enfermedad de larga duración puede afectar más que tu salud. Puede afectar tu capacidad para trabajar, reducir o interrumpir tus ingresos y ejercer presión sobre la vida diaria de tu familia. Algunas pólizas de seguro de vida pueden incluir cláusulas de beneficios acelerados o beneficios en vida que permiten a los titulares elegibles acceder a una parte del beneficio por fallecimiento después de un evento cubierto que califique. La disponibilidad, las condiciones de elegibilidad, los montos de los beneficios, los cargos y el efecto sobre el beneficio por fallecimiento restante dependen de los términos de la póliza y de la cláusula adicional.</p>
          </div>
        </div>
        
        <!-- 3.5 A Diagnosis Can Change -->
        <div class="service-row" data-reveal>
          <div class="sr-photo-wrap">
            <img class="sr-photo loaded" src="images/critical_illness_diverse_1777393231898.png" alt="Diagnóstico crítico.">
          </div>
          <div class="sr-content" data-reveal="right" data-delay="2">
            <div class="sr-num">03</div>
            <h3 class="sr-title">Un diagnóstico puede cambiar el<br><em>presupuesto familiar de un día para otro.</em></h3>
            <p class="sr-body">Un ataque cardíaco, un derrame cerebral, cáncer u otra enfermedad grave puede traer gastos médicos, tiempo sin trabajar y presión financiera al mismo tiempo. Algunas pólizas de seguro de vida con beneficios en vida pueden ayudar a proporcionar fondos durante una enfermedad crítica cubierta, dando a tu familia más espacio para concentrarse en el cuidado, la recuperación y las necesidades diarias.</p>
          </div>
        </div>
        
        <!-- 3.6 Work Coverage -->
        <div class="service-row flip" data-reveal>
          <div class="sr-photo-wrap">
            <img class="sr-photo loaded" src="images/costly_mistake_diverse_1777393245000.png" alt="Cobertura del trabajo.">
          </div>
          <div class="sr-content" data-reveal="right" data-delay="2">
            <div class="sr-num">04</div>
            <h3 class="sr-title">La cobertura del trabajo puede parecer segura —<br><em>hasta que la vida la pone a prueba.</em></h3>
            <p class="sr-body">Muchas familias dependen de los beneficios del empleador sin saber exactamente qué tienen, cuánto cubren o qué sucede si cambia el empleo. La cobertura del trabajo puede ser un buen comienzo, pero tu familia también puede necesitar una protección más estable que no dependa únicamente de tu empleador. Una revisión sencilla puede ayudarte a comprender tu protección antes de que la vida te obligue a hacerte esa pregunta.</p>
          </div>
        </div>
        
      </div>
    </section>

    <!-- Intermediate CTA Banner -->
    <section id="cta-banner" class="cta-on">
      <div class="container">
        <div class="cta-banner-box">
          <div class="cta-content">
            <h2 class="cta-title">¿Listo para proteger el futuro<br>de tu familia?</h2>
            <p class="cta-sub">Hablemos hoy mismo. Una llamada de 15 minutos puede darte la claridad que necesitas.</p>
          </div>
          <div class="cta-action">
            <a href="#contact" class="btn btn-green">Agenda tu llamada de 15 minutos</a>
          </div>
        </div>
      </div>
    </section>

    <!-- 3.7 FAQ Section -->
    <section id="faq" style="background:#fcfbf9; padding:120px 0;">
      <div class="container">
        <div class="faq-header" data-reveal>
          <p class="t-label" style="justify-content:center; display:flex; align-items:center; gap:8px;">PREGUNTAS FRECUENTES</p>
          <h2 class="t-h1">Preguntas frecuentes sobre<br><em>Protección Familiar.</em></h2>
        </div>

        <div class="faq-list">
          <div class="faq-item" data-reveal>
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuál es el objetivo principal del seguro de Protección Familiar?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>El seguro de Protección Familiar está diseñado para ayudar a que tu familia pueda continuar financieramente si el principal proveedor de ingresos fallece inesperadamente. Puede ayudar con gastos de vida, deudas y metas futuras para que tus seres queridos no tengan que cargar con todo solos.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="1">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿El seguro de vida de mi empleador ofrece suficiente protección?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>La cobertura del empleador puede ser un buen comienzo, pero quizá no sea suficiente para todas las necesidades de tu familia. También puede cambiar o terminar cuando cambia tu empleo, por lo que una revisión puede ayudarte a entender qué protección tienes realmente.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="2">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué son los beneficios en vida?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>Algunas pólizas de seguro de vida pueden incluir cláusulas de beneficios acelerados o beneficios en vida que permiten a titulares elegibles acceder a una parte del beneficio por fallecimiento después de un evento cubierto que califique. La disponibilidad, las condiciones de elegibilidad, los montos, los cargos y el efecto sobre el beneficio por fallecimiento restante dependen de los términos de la póliza y la cláusula adicional.</p></div>
          </div>

          <div class="faq-item" data-reveal>
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuánto seguro de vida necesito?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>No tienes que adivinar. La cantidad adecuada depende de tus ingresos, deudas, responsabilidades familiares y metas futuras, y una revisión sencilla puede ayudarte a entender qué podría ajustarse a tu familia.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="1">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuál es la diferencia entre seguro a término y seguro permanente?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>El seguro a término ofrece protección durante un período específico, como 10, 20 o 30 años. El seguro de vida permanente puede ofrecer cobertura a largo plazo y puede acumular valor en efectivo, dependiendo de la póliza.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="2">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Puede el seguro de vida ayudar a evitar el proceso sucesorio?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>Cuando se designan correctamente los beneficiarios adecuados, los beneficios del seguro de vida generalmente se pagan directamente a ellos. Esto puede ayudar a que los seres queridos reciban fondos de manera más directa cuando más los necesitan.</p></div>
          </div>

          <div class="faq-item" data-reveal>
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Los beneficios del seguro de vida están sujetos a impuestos?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>En muchas situaciones, los beneficios por fallecimiento del seguro de vida generalmente se pagan a los beneficiarios libres del impuesto sobre la renta. El tratamiento fiscal puede depender de la situación, por lo que las familias deben consultar a un profesional fiscal calificado.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="1">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Pueden los padres que se quedan en casa obtener seguro de vida?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>Sí. Un padre o una madre que se queda en casa aporta un valor real mediante el cuidado de los hijos, las comidas, el transporte y el apoyo diario. El seguro de vida puede ayudar a la familia a cubrir esas necesidades si esa persona ya no está, y algunas pólizas permanentes pueden acumular valor en efectivo para necesidades futuras.</p></div>
          </div>

          <div class="faq-item" data-reveal data-delay="2">
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Necesito un examen médico?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>No siempre. Algunas opciones de seguro de vida pueden estar disponibles sin examen médico, dependiendo de la compañía, el producto, el historial de salud y la elegibilidad. No dejes que el temor a un examen te impida preguntar.</p></div>
          </div>

          <div class="faq-item" data-reveal>
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuándo es el mejor momento para contratar un seguro de vida?<div class="faq-icon"></div></button>
            <div class="faq-a"><p>Generalmente, antes de que la vida te obligue a hacerte la pregunta. Con el tiempo aumenta la edad y la salud puede cambiar, lo que puede afectar el costo, la elegibilidad y las opciones disponibles. Empezar antes puede darle a tu familia más opciones.</p></div>
          </div>
        </div>
      </div>
    </section>
"""

    if '<section id="services"' not in content:
        # Insert before <section id="contact">
        contact_idx = content.find('<section id="contact">')
        if contact_idx != -1:
            content = content[:contact_idx] + services_section_html + '\n' + content[contact_idx:]
            print("  ✓ Restored #services and #faq sections into family_protection_es.html")
        else:
            print("  ❌ Could not find <section id=\"contact\"> in family_protection_es.html")
    else:
        print("  Info: #services already exists in family_protection_es.html")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print("family_protection_es.html updated successfully.")

update_family_protection()
