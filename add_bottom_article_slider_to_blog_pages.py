#!/usr/bin/env python3
"""
add_bottom_article_slider_to_blog_pages.py
Adds a responsive 'More Articles & Strategies' section at the bottom of all blog article pages
(right above the CTA banner).
Features:
- Full interactive grid/slider showing the remaining blog articles.
- Includes updated Read Article action buttons (pill buttons).
- Fully responsive on mobile and desktop.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

blog_files = [
    "blog_family_protection.html",
    "blog_retirement.html",
    "blog_education.html",
    "blog_living_benefits.html",
    "blog_financial_strategy.html",
    "blog_legacy.html"
]

def build_more_articles_section(current_file):
    is_es = "_es." in current_file

    section_title = "Explorar más artículos y estrategias" if is_es else "More Articles & Strategies"
    section_sub = "Guías educativas para ayudar a su familia a planificar el futuro." if is_es else "Educational resources and insights to help your family plan for the future."
    read_text = "Leer Artículo" if is_es else "Read Article"

    # All articles metadata
    all_articles = [
        {
            "file": "blog_family_protection_es.html" if is_es else "blog_family_protection.html",
            "key": "family_protection",
            "img": "images/family_protection_black_1777333563521.png",
            "cat": "Protección Familiar" if is_es else "Family Protection",
            "title": "¿Confía su familia solo en beneficios laborales?" if is_es else "Is Your Family Counting on Work Benefits Alone?",
            "excerpt": "El seguro de vida del empleador puede ser útil, pero conozca sus límites y opciones portátiles." if is_es else "Employer life insurance is a helpful benefit, but understanding portability and coverage limits is key."
        },
        {
            "file": "blog_retirement_es.html" if is_es else "blog_retirement.html",
            "key": "retirement",
            "img": "images/retirement_planning_black_1777333576986.png",
            "cat": "Jubilación" if is_es else "Retirement",
            "title": "¿Podrían los impuestos reducir sus ingresos de jubilación?" if is_es else "Could Taxes Reduce the Retirement Income You're Counting On?",
            "excerpt": "Aprenda sobre los 3 cubos de impuestos y estrategias de protección contra caídas." if is_es else "Learn about the 3 tax buckets and principal protection strategies like FIAs."
        },
        {
            "file": "blog_education_es.html" if is_es else "blog_education.html",
            "key": "education",
            "img": "images/education_planning_hispanic_1777333593369.png",
            "cat": "Educación" if is_es else "Education",
            "title": "¿Qué pasa si el camino de su hijo cambia después de ahorrar?" if is_es else "What If Your Child's Path Changes After You Save?",
            "excerpt": "Explore opciones flexibles de ahorro para la educación universitaria o profesional." if is_es else "Explore flexible education funding options beyond restrictive 529 plans."
        },
        {
            "file": "blog_living_benefits.html" if is_es else "blog_living_benefits.html",
            "key": "living_benefits",
            "img": "images/critical_illness_diverse_1777393231898.png",
            "cat": "Beneficios en Vida" if is_es else "Living Benefits",
            "title": "¿Qué pasa si sobrevive a la enfermedad, pero sus ingresos no?" if is_es else "What If You Survive the Illness - But Your Income Does Not?",
            "excerpt": "Los beneficios en vida le permiten acceder a fondos durante enfermedades graves." if is_es else "Living benefits allow access to policy funds during qualifying health events."
        },
        {
            "file": "blog_financial_strategy_es.html" if is_es else "blog_financial_strategy.html",
            "key": "financial_strategy",
            "img": "images/family_financial_planning_1777393245465.png",
            "cat": "Estrategia Financiera" if is_es else "Financial Strategy",
            "title": "Cómo las estrategias claras construyen seguridad duradera" if is_es else "How Clear Financial Strategies Help Families Build Security",
            "excerpt": "Los 4 pilares de la salud financiera familiar explicados de forma sencilla." if is_es else "The 4 pillars of family financial health explained clearly for long-term peace of mind."
        },
        {
            "file": "blog_legacy_es.html" if is_es else "blog_legacy.html",
            "key": "legacy",
            "img": "images/estate_planning_senior_couple_1777393261191.png",
            "cat": "Legado y Patrimonio" if is_es else "Legacy Planning",
            "title": "Preservar su legado: Planificación para generaciones futuras" if is_es else "Preserving Your Legacy: Planning for Future Generations",
            "excerpt": "Proteja sus activos, evite demoras de sucesiones y transfiera riqueza." if is_es else "Protect your assets, minimize probate delays, and transfer generational wealth smoothly."
        }
    ]

    # Filter out current article
    current_key = current_file.replace("blog_", "").replace("_es.html", "").replace(".html", "")
    filtered_articles = [a for a in all_articles if a["key"] != current_key][:3]

    cards_html = ""
    for a in filtered_articles:
        cards_html += f"""
        <a href="{a['file']}" class="blog-card" style="flex:none;">
          <div class="bc-img-wrap"><img src="{a['img']}" alt="{a['title']}" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">{a['cat']}</div>
            <h3 class="bc-title">{a['title']}</h3>
            <p class="bc-excerpt">{a['excerpt']}</p>
            <div class="bc-link">{read_text} <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>"""

    section_html = f"""
    <!-- MORE ARTICLES SLIDER / GRID SECTION -->
    <section class="more-articles-section" style="padding: 80px 0; background: #F8FAFC; border-top: 1px solid #E2E8F0;">
      <div class="container">
        <div style="margin-bottom: 40px;">
          <p class="t-label" style="color:var(--green)"><span class="green-dot" style="background:var(--green)"></span>{section_title.upper()}</p>
          <h2 class="t-h1" style="font-size: 32px; color: var(--dark);">{section_title}</h2>
          <p style="color: var(--muted); font-size: 16px; margin-top: 8px;">{section_sub}</p>
        </div>
        <div class="blog-grid" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:32px;">
          {cards_html}
        </div>
      </div>
    </section>
    """
    return section_html

def apply():
    files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove previous section if present
        content = re.sub(r'<!-- MORE ARTICLES SLIDER / GRID SECTION -->.*?</section>', '', content, flags=re.DOTALL)

        # Inject right before CTA BANNER
        more_section = build_more_articles_section(fname)
        if "<!-- CTA BANNER" in content:
            content = content.replace("<!-- CTA BANNER", f"{more_section}\n    <!-- CTA BANNER")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added 'More Articles & Strategies' bottom section to {fname}")

def main():
    print("=== Adding 'More Articles & Strategies' Section to All Blog Pages ===")
    apply()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
