#!/usr/bin/env python3
"""
create_blog_living_benefits_es.py
Creates the missing Spanish Living Benefits article (blog_living_benefits_es.html) using the client's master translation:
- Title: ¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no?
- Category: BENEFICIOS EN VIDA
- Full Spanish body content
- Standardized 2-column sticky sidebar layout
- Standardized header logo (70px / 56px stuck)
- Updated trust badges: Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
SRC_PATH = os.path.join(BASE, "blog_living_benefits.html")
DST_PATH = os.path.join(BASE, "blog_living_benefits_es.html")

with open(SRC_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Replace HTML language and title
html = html.replace('lang="en"', 'lang="es"')
html = html.replace("<title>What If You Survive the Illness – But Your Income Does Not? | Family First Legacy</title>", "<title>¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no? | Family First Legacy</title>")

# Replace nav links with Spanish versions
html = html.replace('href="index.html#about"', 'href="index_es.html#about"')
html = html.replace('href="index.html#process"', 'href="index_es.html#process"')
html = html.replace('href="index.html#opportunity"', 'href="index_es.html#opportunity"')
html = html.replace('href="index.html#reviews"', 'href="index_es.html#reviews"')
html = html.replace('href="family_protection.html"', 'href="family_protection_es.html"')
html = html.replace('href="retirement_planning.html"', 'href="retirement_planning_es.html"')
html = html.replace('href="education_planning.html"', 'href="education_planning_es.html"')
html = html.replace('href="estate_planning.html"', 'href="estate_planning_es.html"')
html = html.replace('href="financial_strategy.html"', 'href="financial_strategy_es.html"')
html = html.replace('href="business_strategies.html"', 'href="business_strategies_es.html"')

# Language selector set to ES
html = html.replace('class="no-pill active"><span>EN</span> English', 'class="no-pill"><span>EN</span> English')
html = html.replace('class="no-pill"><span>ES</span> Español', 'class="no-pill active"><span>ES</span> Español')

# Article Header
html = html.replace("FAMILY PROTECTION", "BENEFICIOS EN VIDA")
html = html.replace("What If You Survive the Illness – But Your Income Does Not?", "¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no?")
html = html.replace("Reviewed by Licensed Financial Professionals • Family First Legacy Team", "Revisado por profesionales financieros con licencia • Equipo de Family First Legacy")
html = html.replace("4 min read", "3 min de lectura")

# Key Takeaways Box
KT_SPANISH = """
<div class="kt-box-elevated">
  <div class="kt-header">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:18px; height:18px;"><path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
    PUNTOS CLAVE DEL ARTÍCULO
  </div>
  <ul>
    <li><strong>Más allá de la salud:</strong> Una enfermedad grave puede interrumpir tus ingresos y presionar el presupuesto familiar.</li>
    <li><strong>Beneficios en vida:</strong> Algunas pólizas de seguro de vida permiten acceder a parte de los beneficios mientras estás con vida si enfrentas una enfermedad terminal, crónica o crítica cubierta.</li>
    <li><strong>Tranquilidad integral:</strong> Un plan sólido de protección familiar contempla tanto el fallecimiento como la incapacidad de trabajar debido a una enfermedad.</li>
  </ul>
</div>
"""

html = re.sub(r'<div class="kt-box-elevated">.*?</div>\s*</div>', KT_SPANISH, html, flags=re.DOTALL)

# Article Body
BODY_SPANISH = """
<p class="t-lead">La mayoría de las familias saben que la vida puede cambiar cuando alguien fallece. Pero muchas no están preparadas para otra realidad dolorosa: a veces una persona sobrevive a la enfermedad, pero los ingresos de la familia no sobreviven con ella.</p>

<p>Un derrame cerebral, cáncer, ataque cardíaco o enfermedad crónica puede convertir un hogar estable en uno con dificultades casi de la noche a la mañana. La familia puede estar agradecida de que su ser querido siga vivo, pero las facturas no se detienen. La hipoteca o la renta sigue llegando. Los hijos siguen necesitando cuidado. La comida, el transporte, las visitas médicas y los gastos diarios continúan.</p>

<p>Y en ese momento, la pregunta se vuelve muy real: <strong>Si me enfermara gravemente y no pudiera trabajar como antes, ¿mi familia seguiría estando bien?</strong></p>

<p>Sobrevivir a la enfermedad es una bendición. Sobrevivir a la presión financiera puede requerir un plan.</p>

<h2>Cuando la enfermedad afecta más que la salud</h2>

<p>Una enfermedad grave no afecta solo el cuerpo. Puede afectar todo el hogar.</p>

<p>Un padre puede necesitar tiempo fuera del trabajo. Un cónyuge puede necesitar reducir horas para brindar cuidado. Las citas médicas, el tiempo de recuperación, el transporte y los gastos diarios pueden crear presión muy rápidamente.</p>

<p>Para muchas familias, la pregunta no es solo: <em>¿Sobreviviré?</em> También es: <strong>¿Mi familia se mantendrá financieramente estable mientras me recupero?</strong></p>

<h2>Cómo pueden ayudar los beneficios en vida</h2>

<p>Algunas pólizas de seguro de vida pueden incluir beneficios en vida. Estos beneficios pueden permitir acceso a parte del beneficio por fallecimiento mientras la persona asegurada aún vive, si califica por una enfermedad terminal, crónica o crítica cubierta.</p>

<p>Ese dinero puede ayudar con facturas del hogar, hipoteca o renta, gastos relacionados con la atención médica, cuidado de hijos, transporte o simplemente dar a la familia tiempo para ajustarse.</p>

<p>Los beneficios dependen de la póliza, riders, requisitos de elegibilidad y reglas de la compañía de seguros. Por eso es importante entender qué incluye una póliza antes de necesitarla.</p>

<h2>La protección no es solo para después de la muerte</h2>

<p>El seguro de vida a menudo se ve como algo que solo ayuda después de que alguien fallece. Pero en algunos casos, también puede ayudar mientras una persona aún vive y enfrenta una de las temporadas más difíciles de la vida.</p>

<p>Un plan sólido de protección familiar debe hacer dos preguntas importantes:</p>

<ul>
  <li><strong>¿Qué pasa si fallezco?</strong></li>
  <li><strong>¿Qué pasa si vivo, pero no puedo trabajar como antes?</strong></li>
</ul>

<p>Ambas preguntas importan.</p>

<h2>Un plan puede traer tranquilidad</h2>

<p>La meta no es causar temor. La meta es la preparación.</p>

<p>Tu familia merece más que esperanza. Merece un plan que ayude a protegerla durante los momentos más difíciles de la vida.</p>
"""

html = re.sub(r'<div class="article-content-card">.*?</div>\s*<!-- Sidebar -->', f'<div class="article-content-card">\n{BODY_SPANISH}\n</div>\n<!-- Sidebar -->', html, flags=re.DOTALL)

# Sidebar & Trust Badges Update
html = html.replace("Licensed & Insured", "Con licencia y asegurados")
html = html.replace("24hr Response", "Respuesta en 24 horas")
html = html.replace("Your Privacy Matters", "Tu privacidad nos importa")
html = html.replace("Why Family First Legacy", "Por qué Family First Legacy")
html = html.replace("Schedule a Free Review", "Solicitar una consulta gratis")
html = html.replace("Need Guidance?", "¿Necesitas orientación?")

with open(DST_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Successfully created blog_living_benefits_es.html")
