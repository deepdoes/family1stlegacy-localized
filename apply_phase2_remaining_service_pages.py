#!/usr/bin/env python3
"""
apply_phase2_remaining_service_pages.py
Updates:
- retirement_planning_es.html
- education_planning_es.html
- estate_planning_es.html
- financial_strategy_es.html
"""

import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_retirement():
    fpath = os.path.join(BASE_DIR, "retirement_planning_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 4.1 Hero
    c = re.sub(
        r'<h1 class="sh-title">.*?</h1>',
        '<h1 class="sh-title">Tus años dorados,<br><em>planificados con cuidado.</em></h1>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<p class="sh-sub">.*?</p>',
        '<p class="sh-sub">Has trabajado duro para construir tu futuro. Ahora, la jubilación puede requerir más que simplemente ahorrar dinero: puede necesitar un plan para los ingresos, los impuestos, los cambios del mercado y la posibilidad de vivir más tiempo de lo esperado.<br><br>¿Simplemente estás ahorrando para la jubilación, o te estás preparando para la vida que deseas vivir?</p>',
        c, count=1, flags=re.DOTALL
    )

    # 4.2 Proof cards
    proof_html = """          <div class="numbers-grid">
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">INGRESOS DE JUBILACIÓN</div>
              <div class="glass-label">¿Podrían tus ahorros durar tanto como tú?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">CAMBIOS DEL MERCADO</div>
              <div class="glass-label">¿Qué sucede si el mercado baja cerca de tu jubilación?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">PLANIFICACIÓN CON CONCIENCIA FISCAL</div>
              <div class="glass-label">¿Sabes cuánto podrías conservar realmente?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">REVISIÓN SIN COSTO</div>
              <div class="glass-label">Haz preguntas antes de tomar decisiones de jubilación</div>
            </div>
          </div>"""
    c = re.sub(r'<div class="numbers-grid">[\s\S]*?</div>\s*</div>\s*</div>', proof_html + '\n        </div>\n      </div>', c)

    # 4.3, 4.4, 4.5 Service Rows
    # Row 1
    c = re.sub(
        r'<h3 class="sr-title">Mercado.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">¿Qué pasa si el mercado baja<br><em>justo cuando necesitas ingresos?</em></h3>\n            <p class="sr-body">Las subidas y bajadas del mercado pueden afectar tus ahorros, especialmente cuando estás cerca de la jubilación o ya estás realizando retiros. Una anualidad fija indexada es un contrato de seguro que puede ofrecer protección del capital frente a un rendimiento negativo del índice, junto con la posibilidad de recibir créditos de interés vinculados al índice. La acreditación está sujeta a términos del contrato, como límites, tasas de participación o márgenes, y los retiros pueden estar sujetos a cargos por rescate o consecuencias fiscales.</p>',
        c, count=1, flags=re.DOTALL
    )
    # Row 2
    c = re.sub(
        r'<h3 class="sr-title">El impuesto.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">¿Forma parte el IRS<br><em>de tu plan de jubilación?</em></h3>\n            <p class="sr-body">El dinero que ves en un 401(k) tradicional puede no estar completamente disponible para gastar. Los retiros generalmente están sujetos a impuestos más adelante, lo que significa que los impuestos pueden afectar cuánto ingreso de jubilación conservas realmente. Una planificación que tome en cuenta los impuestos puede ayudarte a comprender tus opciones antes de que comience la jubilación.</p>',
        c, count=1, flags=re.DOTALL
    )
    # Row 3
    c = re.sub(
        r'<h3 class="sr-title">Longevidad.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">¿Qué pasa si la jubilación<br><em>dura más de lo que esperabas?</em></h3>\n            <p class="sr-body">Vivir más tiempo es una bendición, pero también significa que tus ingresos quizá deban durar más. Planificar con anticipación puede ayudarte a considerar los ingresos futuros, los costos de atención médica y estrategias diseñadas para apoyar tu estilo de vida durante el mayor tiempo posible.</p>',
        c, count=1, flags=re.DOTALL
    )

    # 4.6 All 10 Retirement FAQs
    ret_faqs = """        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Por qué no debería depender completamente de un 401(k) o una IRA?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Porque la jubilación puede necesitar más de una sola fuente. Un 401(k) o una IRA pueden ser útiles, pero los cambios del mercado y los impuestos pueden afectar lo que realmente conservas.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es una anualidad fija indexada (FIA)?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Una anualidad fija indexada es un contrato de seguro diseñado para ayudar a proteger tu capital frente a un rendimiento negativo del índice, al mismo tiempo que ofrece el potencial de crecimiento de intereses vinculados a un índice. Las características y los términos varían según el contrato, y podemos ayudarte a comprender cómo podría encajar en tus metas de jubilación.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Perderé mi dinero si el mercado de valores cae?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Depende de dónde esté colocado tu dinero. Las inversiones directas en el mercado pueden perder valor, mientras que algunas anualidades y estrategias de seguro de vida están diseñadas para ayudar a reducir la exposición directa al mercado.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es la “sorpresa fiscal” en la planificación de jubilación?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El saldo que ves puede no ser la cantidad que conservas. El dinero de un 401(k) tradicional o una IRA generalmente tiene impuestos diferidos, no está libre de impuestos, por lo que los retiros suelen estar sujetos a impuestos más adelante.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Puede una anualidad proporcionar ingresos de por vida?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Sí. Para algunas familias, contar con ingresos de jubilación confiables es la meta. Algunas anualidades ofrecen características de ingresos diseñadas para proporcionar pagos de por vida, dependiendo del contrato.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es la “tasa de retiro seguro”?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Es una guía, no una garantía. Ayuda a estimar cuánto puede retirar una persona de sus ahorros de jubilación cada año.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo puede el IUL ayudar con la planificación de jubilación?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Puede añadir flexibilidad. El IUL es ante todo un seguro de vida, pero puede acumular valor en efectivo al que se puede acceder para necesidades futuras, dependiendo del diseño de la póliza.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Las anualidades son solo para personas adineradas?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>No. Algunas anualidades pueden comenzar con cantidades más modestas, dependiendo de la compañía y del producto.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo afectan los impuestos a mis beneficios del Seguro Social?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El Seguro Social puede no estar completamente libre de impuestos. Dependiendo de tus ingresos combinados, una parte de tus beneficios puede estar sujeta a impuestos.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Es demasiado tarde para comenzar a planificar la jubilación?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>No. Incluso si faltan 5 o 10 años para jubilarte, revisar tus opciones puede ayudarte a proteger lo que has ahorrado, comprender las opciones de ingresos y tomar decisiones más informadas.</p></div>
        </div>"""

    c = re.sub(r'<div class="faq-list">[\s\S]*?</div>\s*</div>\s*</section>', '<div class="faq-list">\n' + ret_faqs + '\n      </div>\n    </div>\n  </section>', c)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print("retirement_planning_es.html updated successfully.")

def update_education():
    fpath = os.path.join(BASE_DIR, "education_planning_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 5.1 Hero
    c = re.sub(
        r'<h1 class="sh-title">.*?</h1>',
        '<h1 class="sh-title">Dales un mundo de oportunidades<br><em>sin sacrificar tu jubilación.</em></h1>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<p class="sh-sub">.*?</p>',
        '<p class="sh-sub">Los costos de educación continúan aumentando y la deuda estudiantil puede convertirse en una carga pesada antes de que la próxima generación siquiera comience. Quieres ayudar a tus hijos a seguir su futuro — universidad, carrera, negocio u otro camino — pero también necesitas proteger el tuyo.<br><br>Puedes pedir prestado para la universidad, pero no para la jubilación.</p>',
        c, count=1, flags=re.DOTALL
    )

    # 5.2 Proof cards - Remove $100k, 5%, $1.7T, $0 FAFSA!
    proof_html = """          <div class="numbers-grid">
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">COSTOS EDUCATIVOS EN AUMENTO</div>
              <div class="glass-label">¿Estás preparado antes de que llegue la factura?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">PLANIFICACIÓN FLEXIBLE</div>
              <div class="glass-label">¿Qué pasa si cambia el camino de tu hijo?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">DEUDA ESTUDIANTIL</div>
              <div class="glass-label">¿Podría la planificación reducir futuros préstamos?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">EQUILIBRIO CON LA JUBILACIÓN</div>
              <div class="glass-label">¿Puedes ayudarles sin perjudicar tu propio futuro?</div>
            </div>
          </div>"""
    c = re.sub(r'<div class="numbers-grid">[\s\S]*?</div>\s*</div>\s*</div>', proof_html + '\n        </div>\n      </div>', c)

    # 5.3, 5.4 & 5.5 Service Rows
    c = re.sub(
        r'<h3 class="sr-title">El 529.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">¿Qué pasa si cambia<br><em>el camino de tu hijo?</em></h3>\n            <p class="sr-body">Un plan 529 puede ser una herramienta valiosa de ahorro educativo, pero está diseñado principalmente para gastos educativos calificados. Si tu hijo recibe una beca, elige un camino profesional diferente, inicia un negocio o decide no asistir a la universidad, tu familia puede necesitar más flexibilidad. Antes de elegir un solo camino, ayuda comprender cómo funciona cada estrategia educativa y qué sucede si la vida no sale exactamente como se planeó.</p>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<h3 class="sr-title">Un más inteligente.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">La planificación educativa<br><em>debe adaptarse a la vida real.</em></h3>\n            <p class="sr-body">El seguro de vida permanente que acumula valor en efectivo puede ofrecer acceso flexible mediante préstamos o retiros de la póliza. Dependiendo del diseño de la póliza, el valor en efectivo puede utilizarse para gastos educativos, vivienda, oportunidades de negocio, necesidades de jubilación u otras metas futuras si cambia el camino de tu hijo. Ayudamos a las familias a comprender cómo funciona esta estrategia antes de decidir si se ajusta a sus metas.<br><br>Muchos padres están dispuestos a sacrificarse por sus hijos. Ese amor es poderoso. Pero ayudar a tu hijo no debería significar poner en riesgo tu propia jubilación. Una estrategia educativa bien pensada puede ayudarte a apoyar los sueños de tu hijo sin perder de vista el plan familiar a largo plazo.</p>',
        c, count=1, flags=re.DOTALL
    )

    # 5.6 All 10 Education FAQs
    edu_faqs = """        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuáles son las limitaciones de un plan 529 tradicional?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Un plan 529 puede ser útil, pero la vida no siempre sigue un solo plan. Está diseñado principalmente para gastos educativos calificados, y los retiros no calificados pueden estar sujetos a impuestos o penalidades sobre las ganancias si cambian los planes de tu hijo.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo puede ayudar el seguro de vida con la planificación educativa?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Algunas pólizas de seguro de vida permanente, como el IUL, pueden acumular valor en efectivo al que se puede acceder mediante préstamos o retiros de la póliza para la educación u otras necesidades futuras, dependiendo de la póliza. Acceder al valor en efectivo puede afectar los beneficios de la póliza, por lo que es importante comprender cómo funciona. Podemos ayudarte a explorar si esta opción se ajusta a las metas de tu familia.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Un plan 529 afecta la ayuda financiera?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El tratamiento para la ayuda financiera puede variar según quién sea el propietario de la cuenta, el tipo de activo y las reglas actuales de FAFSA. Las familias deben revisar la orientación federal vigente sobre ayuda estudiantil antes de elegir una estrategia.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué pasa si mi hijo decide no asistir a la universidad?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Ahí es donde la flexibilidad importa. Dependiendo del diseño de la póliza, el seguro de vida con valor en efectivo puede ayudar a apoyar otras metas, como un negocio, vivienda o futuras necesidades familiares.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Está garantizado el crecimiento del valor en efectivo?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Algunas pólizas IUL incluyen un piso del 0% en la acreditación de intereses vinculados al índice, lo que puede ayudar a brindar protección frente a un rendimiento negativo del índice. Los cargos y términos de la póliza siguen aplicando, y podemos ayudarte a comprender cómo funciona la póliza para tus metas.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuándo debo comenzar a ahorrar para la educación de mi hijo?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Empezar antes generalmente le da a tu familia más tiempo y más opciones. Comenzar temprano puede darle a tu dinero más tiempo para crecer y ayudarte a planificar con menos presión.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Pueden contribuir los abuelos?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Sí. Los abuelos también pueden formar parte del futuro del niño. Pueden ayudar a financiar una estrategia que apoye la educación, oportunidades futuras o etapas importantes de la vida.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué sucede si el mercado baja antes de que venza la matrícula?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El momento puede importar cuando se necesita dinero para la educación. Las cuentas basadas en el mercado pueden bajar cuando cae el mercado, mientras que algunas pólizas IUL están diseñadas para ayudar a proteger intereses vinculados al índice que ya fueron acreditados, dependiendo de los términos de la póliza.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Puedo usar un IUL para educación privada K–12?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>En algunos casos, sí. Dependiendo del diseño de la póliza, se puede acceder al valor en efectivo para ayudar con la matrícula privada K–12 u otros gastos relacionados con la educación.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Es complicado establecer una póliza de seguro de vida para un hijo?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>No siempre. En muchos casos, el proceso puede ser sencillo, y comenzar temprano puede dar a las familias más opciones y flexibilidad para el futuro.</p></div>
        </div>"""

    c = re.sub(r'<div class="faq-list">[\s\S]*?</div>\s*</div>\s*</section>', '<div class="faq-list">\n' + edu_faqs + '\n      </div>\n    </div>\n  </section>', c)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print("education_planning_es.html updated successfully.")

def update_estate():
    fpath = os.path.join(BASE_DIR, "estate_planning_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 6.1 Hero
    c = re.sub(
        r'<h1 class="sh-title">.*?</h1>',
        '<h1 class="sh-title">Planifica un legado que pueda<br><em>perdurar por generaciones.</em></h1>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<p class="sh-sub">.*?</p>',
        '<p class="sh-sub">Trabajaste duro para construir algo significativo. La planificación patrimonial y de legado puede ayudar a que tus deseos queden claramente expresados, a que tus seres queridos estén mejor preparados y a que las personas y causas que te importan se beneficien de lo que dejas.<br><br>¿Quién decidirá qué sucederá con el trabajo de tu vida?</p>',
        c, count=1, flags=re.DOTALL
    )

    # 6.2 Proof cards - Remove 100% control, zero probate delays!
    proof_html = """          <div class="numbers-grid">
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">TUS DESEOS IMPORTAN</div>
              <div class="glass-label">Deja claras tus intenciones</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">TRANSFERENCIAS MÁS SENCILLAS</div>
              <div class="glass-label">Ayuda a tus seres queridos a evitar confusión</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">PLANIFICACIÓN CON CONCIENCIA FISCAL</div>
              <div class="glass-label">Planifica teniendo en cuenta los impuestos</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">TRANQUILIDAD</div>
              <div class="glass-label">Prepárate antes de que la vida cambie</div>
            </div>
          </div>"""
    c = re.sub(r'<div class="numbers-grid">[\s\S]*?</div>\s*</div>\s*</div>', proof_html + '\n        </div>\n      </div>', c)

    # 6.3, 6.4, 6.5 Service Rows
    c = re.sub(
        r'<h3 class="sr-title">Testamento vs\..*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">Testamento vs.<br><em>fideicomiso.</em></h3>\n            <p class="sr-body">Un testamento es una herramienta importante de planificación patrimonial, pero algunos bienes aún pueden tener que pasar por el proceso sucesorio. Un fideicomiso, cuando está correctamente estructurado, puede ayudar a brindar mayor privacidad, claridad y eficiencia al transferir ciertos bienes. Un plan patrimonial bien pensado puede ayudar a dejar claros tus deseos y dar a tus seres queridos una orientación más clara durante un momento difícil.<br><br><strong>Aviso legal y fiscal:</strong> Family First Legacy no brinda asesoramiento legal ni fiscal. Los documentos patrimoniales y las estrategias legales o fiscales deben prepararse o revisarse con profesionales legales y fiscales calificados.</p>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<h3 class="sr-title">Protege lo que trabajaste.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">Protege lo que trabajaste<br><em>duro para construir.</em></h3>\n            <p class="sr-body">Trabajaste duro para construir bienes para tu familia. Dependiendo de tu situación, los impuestos, los costos legales, las demoras del proceso sucesorio o la falta de planificación pueden afectar la facilidad con la que tus bienes pasan a las personas que amas. Trabajamos junto con profesionales legales y fiscales calificados para ayudar a las familias a explorar estrategias que pueden preservar una mayor parte de lo que han construido y transferirlo con mayor claridad. El seguro de vida y las herramientas de planificación patrimonial también pueden ayudar a proporcionar liquidez y flexibilidad cuando las familias más lo necesitan.</p>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<h3 class="sr-title">generacional.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">Deja que tus valores continúen<br><em>a través de las personas que amas.</em></h3>\n            <p class="sr-body">La planificación de legado no se trata solamente de dinero. También se trata de valores, responsabilidad y de las personas que más importan. Ya sea que tu meta sea apoyar la educación, ayudar a seres queridos, contribuir a causas que valoras o planificar el cuidado de alguien con necesidades especiales, planificar con anticipación puede ayudar a que tu legado refleje lo que más importa para ti.</p>',
        c, count=1, flags=re.DOTALL
    )

    # 6.6 All 8 Estate FAQs
    estate_faqs = """        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cuál es la diferencia entre un testamento y un fideicomiso?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Ambos pueden ayudar a orientar lo que sucede con tus bienes. Un testamento explica cómo deben distribuirse los bienes después del fallecimiento, mientras que un fideicomiso puede mantener y transferir ciertos bienes según instrucciones específicas y puede ayudar a simplificar el proceso cuando está correctamente estructurado.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Por qué debería preocuparme por las demoras del proceso sucesorio?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Porque cuando una familia está de duelo, las facturas y las necesidades diarias continúan. El proceso sucesorio puede tardar varios meses o más y puede retrasar el acceso a ciertos bienes. Planificar con anticipación puede ayudar a tus seres queridos a tener una dirección más clara cuando más la necesitan.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿El seguro de vida pasa por el proceso sucesorio?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Depende de cómo esté designado el beneficiario. Generalmente, el seguro de vida con un beneficiario vivo nombrado se paga directamente a ese beneficiario y puede evitar el proceso sucesorio. El proceso sucesorio aún puede intervenir si no se nombró beneficiario, si se nombró al patrimonio o si no existe un beneficiario suplente.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué pasa si fallezco sin un plan patrimonial?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Tu familia puede quedar con confusión durante un momento que ya es difícil. Decisiones importantes sobre tus bienes y tus seres queridos pueden quedar sujetas a la ley estatal y al sistema judicial. Un plan puede ayudar a dejar claros tus deseos antes de que llegue un momento difícil.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Puede un plan patrimonial ayudar a proteger la herencia de mis hijos frente a divorcio o acreedores?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Muchos padres desean que lo que dejan beneficie a sus hijos. Los fideicomisos correctamente estructurados pueden ayudar a brindar protección adicional en ciertas situaciones, incluidos divorcios, demandas o reclamaciones de acreedores. Estas decisiones deben revisarse con un profesional legal calificado.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué son los impuestos patrimoniales?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Los impuestos patrimoniales pueden afectar lo que se transmite a los seres queridos. Pueden aplicarse cuando se transfiere patrimonio después del fallecimiento de una persona, dependiendo del tamaño del patrimonio, las leyes vigentes y el estado correspondiente.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo puede ayudar el seguro de vida con impuestos o gastos patrimoniales?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Algunas familias pueden necesitar efectivo rápidamente para gastos relacionados con el patrimonio. En ciertas situaciones, el seguro de vida puede ayudar a proporcionar liquidez, especialmente cuando se coordina con planificación legal y fiscal.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Necesito un plan patrimonial si no soy una persona adinerada?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>La planificación patrimonial no es solo para familias adineradas. Puede ayudar a las personas a dejar claros sus deseos, organizar decisiones importantes y brindar una dirección más clara a sus seres queridos.</p></div>
        </div>"""

    c = re.sub(r'<div class="faq-list">[\s\S]*?</div>\s*</div>\s*</section>', '<div class="faq-list">\n' + estate_faqs + '\n      </div>\n    </div>\n  </section>', c)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print("estate_planning_es.html updated successfully.")

def update_financial_strategy():
    fpath = os.path.join(BASE_DIR, "financial_strategy_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 7.1 Hero
    c = re.sub(
        r'<h1 class="sh-title">.*?</h1>',
        '<h1 class="sh-title">El patrimonio no se crea por accidente.<br><em>Se construye con intención.</em></h1>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<p class="sh-sub">.*?</p>',
        '<p class="sh-sub">Un progreso financiero sólido generalmente viene de decisiones claras, no de adivinanzas. Las familias pueden beneficiarse de aprender a manejar deudas, construir ahorros, proteger lo que han trabajado por conseguir y planificar pensando en el futuro.<br><br>¿Tus decisiones financieras te están ayudando a avanzar hacia el futuro que deseas?</p>',
        c, count=1, flags=re.DOTALL
    )

    # 7.2 Proof cards - Remove 100% control, 0% market loss, 3-8% probate fee, Day 1!
    proof_html = """          <div class="numbers-grid">
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">CLARIDAD FINANCIERA</div>
              <div class="glass-label">¿Sabes adónde va tu dinero?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">ESTRATEGIA DE DEUDA</div>
              <div class="glass-label">¿Podrían los intereses estar frenando tu progreso?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">PRINCIPIOS DE CRECIMIENTO</div>
              <div class="glass-label">¿Está el tiempo trabajando a favor de tu dinero?</div>
            </div>
            <div class="glass-card">
              <div class="glass-num" style="font-size:15px; font-weight:700;">REVISIÓN SIN COSTO</div>
              <div class="glass-label">Construye un plan con claridad y sin presión.</div>
            </div>
          </div>"""
    c = re.sub(r'<div class="numbers-grid">[\s\S]*?</div>\s*</div>\s*</div>', proof_html + '\n        </div>\n      </div>', c)

    # 7.3, 7.4, 7.5 Service Rows
    c = re.sub(
        r'<h3 class="sr-title">La Regla del 72\..*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">La Regla del 72.<br><em>El poder del tiempo.</em></h3>\n            <p class="sr-body">Comprender cómo funciona el interés compuesto puede ayudar a las familias a ver el poder del tiempo. La Regla del 72 es una manera sencilla de estimar cuánto tiempo podría tardar el dinero en duplicarse a una determinada tasa anual de rendimiento. Cuando entiendes cómo funciona el crecimiento, puedes tomar mejores decisiones sobre ahorro, inversión, deuda y planificación a largo plazo.</p>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<h3 class="sr-title">Manejo de deudas\..*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">Manejo de deudas.<br><em>Apoya tu futuro.</em></h3>\n            <p class="sr-body">No todas las deudas son iguales, pero la deuda con intereses altos puede frenar silenciosamente el progreso de una familia. Una buena estrategia financiera te ayuda a comprender lo que debes, reducir deudas innecesarias con el tiempo y crear espacio para el ahorro y las metas futuras. La meta es sencilla: ayudar a que tu dinero apoye tu futuro en lugar de ir únicamente al pago de deudas.</p>',
        c, count=1, flags=re.DOTALL
    )
    c = re.sub(
        r'<h3 class="sr-title">Legado.*?</h3>\s*<p class="sr-body">.*?</p>',
        '<h3 class="sr-title">Transferencia de legado.<br><em>Valores y dirección.</em></h3>\n            <p class="sr-body">Un verdadero legado no se trata solo de lo que dejas atrás. También se trata de las oportunidades, los valores y la dirección que creas para las personas que amas. Ayudamos a las familias a explorar estrategias que pueden apoyar a futuras generaciones, proteger lo que han trabajado duro para construir y transmitir sus valores con mayor claridad.</p>',
        c, count=1, flags=re.DOTALL
    )

    # 7.6 All 10 Financial Strategy FAQs
    fin_faqs = """        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es la Regla del 72?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Es una forma sencilla de estimar cuánto tiempo puede tardar el dinero en duplicarse. Divide 72 entre una tasa anual de rendimiento; por ejemplo, al 7%, el dinero podría duplicarse en aproximadamente 10 años.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo pueden ayudar con el manejo de deuda?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>La deuda puede frenar silenciosamente el progreso. Ayudamos a las familias a comprender sus deudas, mejorar el flujo de efectivo y explorar pasos prácticos para reducir la deuda con el tiempo.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué significa “convertirte en tu propio banco”?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Es un concepto, no un banco literal. Generalmente se refiere a usar el valor en efectivo de una póliza de seguro de vida correctamente estructurada como una posible fuente de fondos para necesidades futuras, dependiendo del diseño de la póliza.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo puedo ayudar a proteger mis activos de las caídas del mercado?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Cuando el mercado baja, el dinero invertido directamente en el mercado puede perder valor. Algunas FIA y pólizas IUL están diseñadas para ayudar a reducir la exposición a pérdidas directas del mercado mediante estrategias vinculadas a índices. La meta es ayudar a proteger lo que has trabajado duro para construir, manteniendo al mismo tiempo cierta oportunidad de crecimiento futuro, dependiendo de los términos del producto o la póliza.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es una estrategia de jubilación con eficiencia fiscal?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Dependiendo del diseño de la póliza y de la ley fiscal vigente, en algunas situaciones se puede acceder al valor en efectivo de manera fiscalmente favorable. Acceder al valor en efectivo puede afectar los beneficios de la póliza y puede tener implicaciones fiscales. Consulta a un profesional fiscal calificado.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Por qué es importante el interés compuesto?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El interés compuesto ayuda a que tu dinero crezca tanto sobre la cantidad original como sobre el crecimiento ya obtenido. Con el tiempo, esto puede convertirse en una de las bases para construir patrimonio, porque pequeños pasos constantes pueden crecer hasta convertirse en algo significativo.</p></div>
        </div>

        <div class="faq-item" data-reveal>
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Necesito una estrategia financiera si no soy una persona adinerada?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Sí. Una estrategia financiera no es solo para personas adineradas. Puede ayudar a las familias a reducir deudas, construir ahorros, proteger lo que han trabajado por conseguir y tomar decisiones con mayor confianza.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="1">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Qué es el riesgo de secuencia de rendimientos?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>El momento importa durante la jubilación. El riesgo de secuencia de rendimientos ocurre cuando se producen pérdidas de mercado al principio de la jubilación mientras ya han comenzado los retiros, lo que puede afectar cuánto tiempo duran los ahorros.</p></div>
        </div>

        <div class="faq-item" data-reveal data-delay="2">
          <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">¿Cómo se compara un IUL con una Roth IRA?<div class="faq-icon"></div></button>
          <div class="faq-a"><p>Ambos pueden ofrecer ventajas fiscales, pero funcionan de manera diferente. Una Roth IRA tiene límites de ingresos y contribuciones establecidos por el IRS. Un IUL es un seguro de vida con valor en efectivo y beneficio por fallecimiento, y no sigue las mismas reglas de contribución de una Roth IRA; en cambio, sigue las reglas de la póliza y las normas fiscales aplicables.</p></div>
        </div>"""

    c = re.sub(r'<div class="faq-list">[\s\S]*?</div>\s*</div>\s*</section>', '<div class="faq-list">\n' + fin_faqs + '\n      </div>\n    </div>\n  </section>', c)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print("financial_strategy_es.html updated successfully.")

if __name__ == "__main__":
    update_retirement()
    update_education()
    update_estate()
    update_financial_strategy()
