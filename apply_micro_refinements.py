#!/usr/bin/env python3
"""
apply_micro_refinements.py
Applies all micro-level text refinements identified during our deep audit across:
1. index_es.html (Slides 3 & 4 titles, FAQ header, Card 06 body)
2. business_strategies_es.html (Hero H1, Subtitle, Tile cards, Section 8.1 narrative, Card 02-04 titles)
3. family_protection_es.html (Proof Card 2 subtitle)
4. retirement_planning_es.html (Hero hook)
5. blog_*.html (Sidebar widget 3 translation to Spanish in all 6 articles)
6. blog_living_benefits_es.html (Sidebar CTA and more-articles section with Spanish cards)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def refine_index_es():
    filepath = os.path.join(BASE, "index_es.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Slide 4: pueda durar generaciones -> pueda perdurar por generaciones
    content = content.replace(
        '<h1 class="slide-title">Deja un legado<br>que <em>pueda durar generaciones</em></h1>',
        '<h1 class="slide-title">Deja un legado<br>que <em>pueda perdurar por generaciones</em></h1>'
    )

    # 2. Slide 3: futuro brillante -> brillante futuro
    content = content.replace(
        '<h1 class="slide-title">Invierte en su<br><em>futuro brillante</em></h1>',
        '<h1 class="slide-title">Invierte en su<br><em>brillante futuro</em></h1>'
    )

    # 3. FAQ header: Preguntas frecuentes Preguntas -> Preguntas frecuentes
    content = re.sub(
        r'<h2 class="t-h1" [^>]*>Preguntas frecuentes<br/><em>Preguntas\.</em></h2>',
        '<h2 class="t-h1" data-delay="1" data-reveal="">Preguntas<br/><em>frecuentes.</em></h2>',
        content
    )

    # 4. Service Card 06 (Business Strategies) body
    old_card_06_body = 'Tu negocio representa tu trabajo, tus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a comprender las opciones de protección, estrategias de sucesión y herramientas de planificación que puedan apoyar la estabilidad a largo plazo.'
    new_card_06_body = 'Tu negocio representa tu trabajo, tus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a comprender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a apoyar la estabilidad a largo plazo.'
    content = content.replace(old_card_06_body, new_card_06_body)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Refined index_es.html")


def refine_business_strategies():
    filepath = os.path.join(BASE, "business_strategies_es.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Hero H1
    content = content.replace(
        '<h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">Si no pudieras presentarte mañana, ¿tu negocio seguiría funcionando?</h1>',
        '<h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">Si mañana no pudieras estar presente, ¿tu negocio seguiría adelante?</h1>'
    )

    # 2. Subtitle
    content = content.replace(
        'Tú construiste el negocio. Pero ¿quién lo protege si tú no puedes estar ahí?',
        'Tú construiste el negocio. Pero ¿quién lo protege si tú no puedes estar?'
    )

    # 3. Tile card 2 subtitle
    content = content.replace(
        '¿Qué pasa si un dueño, socio o persona clave ya no puede continuar?',
        '¿Qué sucede si un propietario, socio o persona clave ya no puede continuar?'
    )

    # 4. Tile card 3 subtitle
    content = content.replace(
        '¿Sabrían cómo manejar lo que trabajaste tanto para construir?',
        '¿Sabrían cómo manejar lo que tanto te costó construir?'
    )

    # 5. Tile card 4 label
    content = content.replace(
        'PROTEGE EL VALOR QUE ESTÁS CONSTRUYENDO',
        'PROTEGE EL VALOR'
    )

    # 6. Card 02: Heading & Section 8.1 narrative
    old_card_02 = """      <!-- 02 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">02</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Qué pasa si la propiedad cambia de repente?</h3>
          <p class="t-body">Si tu negocio tiene más de un dueño, todos deberían entender qué pasa si un dueño fallece, se va o ya no puede continuar.<br><br>Una estrategia buy-sell puede ayudar a crear un camino más claro para cambios de propiedad, valor del negocio y protección familiar. El seguro de vida se usa con frecuencia para ayudar a financiar estos acuerdos.</p>
        </div>
      </div>"""

    new_card_02 = """      <!-- 02 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">02</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Qué sucede con el negocio si cambia la propiedad?</h3>
          <p class="t-body">Sin un plan claro, la salida, fallecimiento o incapacidad de un propietario puede crear confusión entre socios, familiares, empleados y prestamistas. Un acuerdo buy-sell financiado puede ayudar a proporcionar una forma estructurada para que los propietarios restantes compren la participación de un propietario a un precio justo, al mismo tiempo que ayuda a proteger los intereses de la familia. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal.</p>
        </div>
      </div>"""

    if old_card_02 in content:
        content = content.replace(old_card_02, new_card_02)
    else:
        # Fallback regex replace for card 2
        content = re.sub(
            r'<h3 class="t-h3"[^>]*>¿Qué pasa si la propiedad cambia de repente\?</h3>\s*<p class="t-body">.*?</p>',
            '<h3 class="t-h3" style="margin-bottom:12px;">¿Qué sucede con el negocio si cambia la propiedad?</h3>\n          <p class="t-body">Sin un plan claro, la salida, fallecimiento o incapacidad de un propietario puede crear confusión entre socios, familiares, empleados y prestamistas. Un acuerdo buy-sell financiado puede ayudar a proporcionar una forma estructurada para que los propietarios restantes compren la participación de un propietario a un precio justo, al mismo tiempo que ayuda a proteger los intereses de la familia. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal.</p>',
            content,
            flags=re.DOTALL
        )

    # 7. Card 03 Heading
    content = content.replace(
        '<h3 class="t-h3" style="margin-bottom:12px;">¿Tu familia tendría claridad o confusión?</h3>',
        '<h3 class="t-h3" style="margin-bottom:12px;">Tu familia merece claridad. ¿Claridad o confusión?</h3>'
    )

    # 8. Card 04 Heading
    content = content.replace(
        '<h3 class="t-h3" style="margin-bottom:12px;">¿Estás protegiendo el valor que estás construyendo?</h3>',
        '<h3 class="t-h3" style="margin-bottom:12px;">Protegiendo el valor. Estabilidad a largo plazo.</h3>'
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Refined business_strategies_es.html")


def refine_family_protection():
    filepath = os.path.join(BASE, "family_protection_es.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Proof Card 2 Subtitle
    content = content.replace(
        '<div class="glass-label">¿Podría tu familia seguir pagando las facturas el próximo mes?</div>',
        '<div class="glass-label">¿Podría tu familia mantenerse al día con las facturas el próximo mes?</div>'
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Refined family_protection_es.html")


def refine_retirement_planning():
    filepath = os.path.join(BASE, "retirement_planning_es.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Hero Hook
    content = content.replace(
        '<div class="sh-hook">¿Está ahorrando para su jubilación o realmente lo está planificando?</div>',
        '<div class="sh-hook">Las reglas de la jubilación han cambiado. ¿Te has adaptado?</div>'
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Refined retirement_planning_es.html")


def refine_all_article_sidebars():
    articles = [
        "blog_family_protection_es.html",
        "blog_retirement_es.html",
        "blog_education_es.html",
        "blog_living_benefits_es.html",
        "blog_financial_strategy_es.html",
        "blog_legacy_es.html"
    ]

    old_widget_3 = """          <div class="sidebar-card-widget" style="background:#F8FAFC;">
            <div style="font-size:12px; font-weight:800; color:#4A2D7A; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">Why Family First Legacy</div>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Licensed & Insured</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> 24hr Response</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Your Privacy Matters</li>
            </ul>
          </div>"""

    new_widget_3 = """          <div class="sidebar-card-widget" style="background:#F8FAFC;">
            <div style="font-size:12px; font-weight:800; color:#4A2D7A; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">Por qué Family First Legacy</div>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Con licencia y asegurados</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Respuesta en 24 horas</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Tu privacidad nos importa</li>
            </ul>
          </div>"""

    for art in articles:
        filepath = os.path.join(BASE, art)
        with open(filepath, "r", encoding="utf-8") as f:
            c = f.read()

        if old_widget_3 in c:
            c = c.replace(old_widget_3, new_widget_3)
        else:
            # Flexible replacement
            c = re.sub(
                r'Why Family First Legacy.*?Your Privacy Matters\s*</li>\s*</ul>\s*</div>',
                'Por qué Family First Legacy</div>\n            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">\n              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Con licencia y asegurados</li>\n              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Respuesta en 24 horas</li>\n              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Tu privacidad nos importa</li>\n            </ul>\n          </div>',
                c,
                flags=re.DOTALL
            )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"  ✓ Refined sidebar Widget 3 in {art}")


def refine_living_benefits_article():
    filepath = os.path.join(BASE, "blog_living_benefits_es.html")
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Sidebar CTA widget
    old_cta = """          <div class="sidebar-card-widget sidebar-cta-widget">
            <span class="scw-badge">NO-COST CONSULTATION</span>
            <h3>Ready for Honest Guidance?</h3>
            <p>Schedule a review with a licensed professional — no pressure, no obligation.</p>
            <a href="index.html#contact" class="scw-btn">Book Consultation</a>
          </div>"""

    new_cta = """          <div class="sidebar-card-widget sidebar-cta-widget">
            <span class="scw-badge">CONSULTA GRATUITA</span>
            <h3>¿Listo para orientación honesta?</h3>
            <p>Reserve una revisión sin compromiso con un profesional con licencia.</p>
            <a href="index_es.html#contact" class="scw-btn">Programar consulta</a>
          </div>"""

    if old_cta in c:
        c = c.replace(old_cta, new_cta)
    else:
        c = re.sub(
            r'<div class="sidebar-card-widget sidebar-cta-widget">.*?Book Consultation</a>\s*</div>',
            new_cta.strip(),
            c,
            flags=re.DOTALL
        )

    # 2. More Articles Section Header & Spanish Track Cards
    spanish_more_articles_section = """    <!-- MORE ARTICLES SLIDER / CAROUSEL SECTION -->
    <section class="more-articles-section">
      <div class="container">
        
        <div class="ma-header">
          <div>
            <p class="t-label" style="color:var(--green)"><span class="green-dot" style="background:var(--green)"></span>MÁS ARTÍCULOS Y ESTRATEGIAS</p>
            <h2 class="t-h1" style="font-size: 32px; color: var(--dark); margin: 4px 0 0 0;">Más artículos y estrategias</h2>
            <p style="color: var(--muted); font-size: 15px; margin-top: 6px;">Guías educativas para ayudar a su familia a planificar el futuro.</p>
          </div>

          <!-- Carousel Navigation Left / Right Arrows -->
          <div style="display: flex; gap: 10px; align-items: center;">
            <button class="ma-nav-btn" onclick="slideMoreArticles('left')" aria-label="Previous article">
              <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            </button>
            <button class="ma-nav-btn" onclick="slideMoreArticles('right')" aria-label="Next article">
              <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
          </div>
        </div>

        <!-- Scrollable Carousel Track -->
        <div class="ma-slider-wrap">
          <div class="ma-slider-track">
            
          <a href="blog_family_protection_es.html" class="blog-card">
            <div class="bc-img-wrap"><img src="images/family_protection_black_1777333563521.png" alt="¿Confía su familia solo en beneficios laborales?" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">Protección Familiar</div>
              <h3 class="bc-title">¿Confía su familia solo en beneficios laborales?</h3>
              <p class="bc-excerpt">El seguro de vida del empleador puede ser útil, pero conozca sus límites y opciones portátiles.</p>
              <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>
          <a href="blog_retirement_es.html" class="blog-card">
            <div class="bc-img-wrap"><img src="images/retirement_planning_black_1777333576986.png" alt="¿Podrían los impuestos reducir sus ingresos de jubilación?" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">Jubilación</div>
              <h3 class="bc-title">¿Podrían los impuestos reducir sus ingresos de jubilación?</h3>
              <p class="bc-excerpt">Aprenda sobre los 3 cubos de impuestos y estrategias de protección contra caídas.</p>
              <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>
          <a href="blog_education_es.html" class="blog-card">
            <div class="bc-img-wrap"><img src="images/education_planning_hispanic_1777333593369.png" alt="¿Qué pasa si el camino de su hijo cambia después de ahorrar?" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">Educación</div>
              <h3 class="bc-title">¿Qué pasa si el camino de su hijo cambia después de ahorrar?</h3>
              <p class="bc-excerpt">Explore opciones flexibles de ahorro para la educación y herramientas con valor en efectivo.</p>
              <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>
          <a href="blog_financial_strategy_es.html" class="blog-card">
            <div class="bc-img-wrap"><img src="images/financial_strategy_hispanic_1777333606672.png" alt="Cómo las estrategias claras construyen seguridad duradera" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">Estrategia Financiera</div>
              <h3 class="bc-title">Cómo las estrategias claras construyen seguridad duradera</h3>
              <p class="bc-excerpt">Los 4 pilares de la salud financiera familiar explicados de forma sencilla.</p>
              <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>
          <a href="blog_legacy_es.html" class="blog-card">
            <div class="bc-img-wrap"><img src="images/wealth_transfer_diverse_1777393288351.png" alt="Preservar su legado: Planificación para generaciones futuras" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">Legado y Patrimonio</div>
              <h3 class="bc-title">Preservar su legado: Planificación para generaciones futuras</h3>
              <p class="bc-excerpt">Proteja sus activos, evite demoras de sucesiones y transfiera riqueza.</p>
              <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>
          </div>
        </div>

      </div>
    </section>"""

    # Replace the old more articles section in blog_living_benefits_es.html
    pos_sec_start = c.find('<section class="more-articles-section">')
    pos_sec_end = c.find('</section>', pos_sec_start) + len('</section>')
    if pos_sec_start != -1 and pos_sec_end != -1:
        c = c[:pos_sec_start] + spanish_more_articles_section.strip() + c[pos_sec_end:]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(c)
    print("  ✓ Refined blog_living_benefits_es.html (CTA & Carousel)")


if __name__ == "__main__":
    print("=== Applying Deep Audit Micro Refinements ===")
    refine_index_es()
    refine_business_strategies()
    refine_family_protection()
    refine_retirement_planning()
    refine_all_article_sidebars()
    refine_living_benefits_article()
    print("=== All Micro Refinements Applied! ===")
