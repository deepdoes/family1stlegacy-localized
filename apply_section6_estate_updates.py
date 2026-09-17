#!/usr/bin/env python3
"""
apply_section6_estate_updates.py
Applies Section 6 (Estate & Legacy Planning Page) updates to estate_planning_es.html:
- 6.1 Hero text
- 6.2 Four labels (removes 100% control, zero probate delays)
- 6.3 Will vs Trust text & Legal/Tax Disclaimer
- 6.4 Protect What You Worked Hard paragraph
- 6.5 Let Your Values Continue paragraph
- 6.6 All 8 Estate FAQs
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "estate_planning_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# 6.1 Hero
HERO_P1 = "Trabajaste duro para construir algo significativo. La planificación patrimonial y de legado puede ayudar a que tus deseos queden claramente expresados, a que tus seres queridos estén mejor preparados y a que las personas y causas que te importan se beneficien de lo que dejas."
HERO_P2 = "¿Quién decidirá qué sucederá con el trabajo de tu vida?"

html = re.sub(
    r'(<div class="service-hero-content">.*?<p class="service-hero-sub">).*?(</p>)',
    r'\1' + HERO_P1 + '<br/><br/>' + HERO_P2 + r'\2',
    html,
    flags=re.DOTALL
)

# 6.2 Four labels
L1 = "TUS DESEOS IMPORTAN — Deja claras tus intenciones"
L2 = "TRANSFERENCIAS MÁS SENCILLAS — Ayuda a tus seres queridos a evitar confusión"
L3 = "PLANIFICACIÓN CON CONCIENCIA FISCAL — Planifica teniendo en cuenta los impuestos"
L4 = "TRANQUILIDAD — Prepárate antes de que la vida cambie"

html = re.sub(r'YOUR WISHES MATTER.*?(?=</div>|</span>|</p>)', L1, html)
html = re.sub(r'SIMPLIFIED TRANSFERS.*?(?=</div>|</span>|</p>)', L2, html)
html = re.sub(r'TAX-AWARE PLANNING.*?(?=</div>|</span>|</p>)', L3, html)
html = re.sub(r'PEACE OF MIND.*?(?=</div>|</span>|</p>)', L4, html)

# Remove old statistics numeric claims (100%, 0 delays)
html = re.sub(r'<div class="stat-number">100%</div>', '<div class="stat-number">✓</div>', html)
html = re.sub(r'<div class="stat-number">0</div>', '<div class="stat-number">✓</div>', html)

# 6.3 Will vs Trust + Disclaimer
WILL_NEW = "Un testamento es una herramienta importante de planificación patrimonial, pero algunos bienes aún pueden tener que pasar por el proceso sucesorio. Un fideicomiso, cuando está correctamente estructurado, puede ayudar a brindar mayor privacidad, claridad y eficiencia al transferir ciertos bienes. Un plan patrimonial bien pensado puede ayudar a dejar claros tus deseos y dar a tus seres queridos una orientación más clara durante un momento difícil."
DISCLAIMER_NEW = "Aviso legal y fiscal: Family First Legacy no brinda asesoramiento legal ni fiscal. Los documentos patrimoniales y las estrategias legales o fiscales deben prepararse o revisarse con profesionales legales y fiscales calificados."

# 6.4 Protect What You Worked Hard
PROTECT_NEW = "Trabajaste duro para construir bienes para tu familia. Dependiendo de tu situación, los impuestos, los costos legales, las demoras del proceso sucesorio o la falta de planificación pueden afectar la facilidad con la que tus bienes pasan a las personas que amas. Trabajamos junto con profesionales legales y fiscales calificados para ayudar a las familias a explorar estrategias que pueden preservar una mayor parte de lo que han construido y transferirlo con mayor claridad. El seguro de vida y las herramientas de planificación patrimonial también pueden ayudar a proporcionar liquidez y flexibilidad cuando las familias más lo necesitan."

# 6.5 Let Your Values Continue
VALUES_NEW = "La planificación de legado no se trata solamente de dinero. También se trata de valores, responsabilidad y de las personas que más importan. Ya sea que tu meta sea apoyar la educación, ayudar a seres queridos, contribuir a causas que valoras o planificar el cuidado de alguien con necesidades especiales, planificar con anticipación puede ayudar a que tu legado refleje lo que más importa para ti."

html = re.sub(
    r'(<h2[^>]*>Testamento vs\. fideicomiso.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + WILL_NEW + '<br/><br/><em>' + DISCLAIMER_NEW + '</em>' + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>Protege lo que trabajaste duro.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + PROTECT_NEW + r'\2',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'(<h2[^>]*>Deja que tus valores continúen.*?</h2>\s*<p[^>]*>).*?(</p>)',
    r'\1' + VALUES_NEW + r'\2',
    html,
    flags=re.DOTALL
)

# 6.6 All 8 Estate FAQs
FAQS = [
    ("¿Cuál es la diferencia entre un testamento y un fideicomiso?", "Ambos pueden ayudar a orientar lo que sucede con tus bienes. Un testamento explica cómo deben distribuirse los bienes después del fallecimiento, mientras que un fideicomiso puede mantener y transferir ciertos bienes según instrucciones específicas y puede ayudar a simplificar el proceso cuando está correctamente estructurado."),
    ("¿Por qué debería preocuparme por las demoras del proceso sucesorio?", "Porque cuando una familia está de duelo, las facturas y las necesidades diarias continúan. El proceso sucesorio puede tardar varios meses o más y puede retrasar el acceso a ciertos bienes. Planificar con anticipación puede ayudar a tus seres queridos a tener una dirección más clara cuando más la necesitan."),
    ("¿El seguro de vida pasa por el proceso sucesorio?", "Depende de cómo esté designado el beneficiario. Generalmente, el seguro de vida con un beneficiario vivo nombrado se paga directamente a ese beneficiario y puede evitar el proceso sucesorio. El proceso sucesorio aún puede intervenir si no se nombró beneficiario, si se nombró al patrimonio o si no existe un beneficiario suplente."),
    ("¿Qué pasa si fallezco sin un plan patrimonial?", "Tu familia puede quedar con confusión durante un momento que ya es difícil. Decisiones importantes sobre tus bienes y tus seres queridos pueden quedar sujetas a la ley estatal y al sistema judicial. Un plan puede ayudar a dejar claros tus deseos antes de que llegue un momento difícil."),
    ("¿Puede un plan patrimonial ayudar a proteger la herencia de mis hijos frente a divorcio o acreedores?", "Muchos padres desean que lo que dejan beneficie a sus hijos. Los fideicomisos correctamente estructurados pueden ayudar a brindar protección adicional en ciertas situaciones, incluidos divorcios, demandas o reclamaciones de acreedores. Estas decisiones deben revisarse con un profesional legal calificado."),
    ("¿Qué son los impuestos patrimoniales?", "Los impuestos patrimoniales pueden afectar lo que se transmite a los seres queridos. Pueden aplicarse cuando se transfiere patrimonio después del fallecimiento de una persona, dependiendo del tamaño del patrimonio, las leyes vigentes y el estado correspondiente."),
    ("¿Cómo puede ayudar el seguro de vida con impuestos o gastos patrimoniales?", "Algunas familias pueden necesitar efectivo rápidamente para gastos relacionados con el patrimonio. En ciertas situaciones, el seguro de vida puede ayudar a proporcionar liquidez, especialmente cuando se coordina con planificación legal y fiscal."),
    ("¿Necesito un plan patrimonial si no soy una persona adinerada?", "La planificación patrimonial no es solo para familias adineradas. Puede ayudar a las personas a dejar claros sus deseos, organizar decisiones importantes y brindar una dirección más clara a sus seres queridos.")
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

print("  ✓ Synchronized Section 6 on estate_planning_es.html")
