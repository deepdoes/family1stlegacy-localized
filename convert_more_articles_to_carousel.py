#!/usr/bin/env python3
"""
convert_more_articles_to_carousel.py
Converts the 'More Articles & Strategies' section at the bottom of all blog pages into a full
interactive horizontal carousel/slider with Left (←) and Right (→) Arrow Buttons!
- Displays ALL 5 other blog articles in a smooth track.
- Left and Right arrow navigation buttons on top right.
- Touch swipe / scroll support on mobile.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CAROUSEL_CSS_AND_JS = """
/* ─── More Articles Interactive Carousel Styling ─── */
.more-articles-section {
  padding: 80px 0 !important;
  background: #F8FAFC !important;
  border-top: 1px solid #E2E8F0 !important;
  position: relative !important;
}
.ma-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: flex-end !important;
  margin-bottom: 32px !important;
  gap: 24px !important;
  flex-wrap: wrap !important;
}
.ma-nav-btn {
  width: 44px !important;
  height: 44px !important;
  background: #ffffff !important;
  border: 1.5px solid rgba(74, 45, 122, 0.15) !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
}
.ma-nav-btn:hover {
  background: #1D9E75 !important;
  border-color: #1D9E75 !important;
  transform: scale(1.05) !important;
  box-shadow: 0 6px 18px rgba(29, 158, 117, 0.25) !important;
}
.ma-nav-btn svg {
  width: 16px !important;
  height: 16px !important;
  stroke: #4A2D7A !important;
  fill: none !important;
  stroke-width: 2.5 !important;
  transition: stroke 0.25s !important;
}
.ma-nav-btn:hover svg {
  stroke: #ffffff !important;
}
.ma-slider-wrap {
  overflow-x: auto !important;
  scroll-behavior: smooth !important;
  scrollbar-width: none !important; /* Firefox */
  -ms-overflow-style: none !important; /* IE 10+ */
  padding: 8px 4px 20px 4px !important;
}
.ma-slider-wrap::-webkit-scrollbar {
  display: none !important; /* Chrome/Safari */
}
.ma-slider-track {
  display: flex !important;
  gap: 28px !important;
  width: max-content !important;
}
.ma-slider-track .blog-card {
  width: 340px !important;
  max-width: 85vw !important;
  flex-shrink: 0 !important;
}
"""

CAROUSEL_JS = """
<script>
function slideMoreArticles(direction) {
  const container = document.querySelector('.ma-slider-wrap');
  if(!container) return;
  const scrollAmount = direction === 'left' ? -360 : 360;
  container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}
</script>
"""

def build_carousel_html(current_file):
    is_es = "_es." in current_file

    section_title = "Explorar más artículos y estrategias" if is_es else "More Articles & Strategies"
    section_sub = "Guías educativas para ayudar a su familia a planificar el futuro." if is_es else "Educational resources and insights to help your family plan for the future."
    read_text = "Leer Artículo" if is_es else "Read Article"

    # All 6 articles metadata
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
            "img": "images/financial_strategy_hispanic_1777333606672.png",
            "cat": "Estrategia Financiera" if is_es else "Financial Strategy",
            "title": "Cómo las estrategias claras construyen seguridad duradera" if is_es else "How Clear Financial Strategies Help Families Build Security",
            "excerpt": "Los 4 pilares de la salud financiera familiar explicados de forma sencilla." if is_es else "The 4 pillars of family financial health explained clearly for long-term peace of mind."
        },
        {
            "file": "blog_legacy_es.html" if is_es else "blog_legacy.html",
            "key": "legacy",
            "img": "images/wealth_transfer_diverse_1777393288351.png",
            "cat": "Legado y Patrimonio" if is_es else "Legacy Planning",
            "title": "Preservar su legado: Planificación para generaciones futuras" if is_es else "Preserving Your Legacy: Planning for Future Generations",
            "excerpt": "Proteja sus activos, evite demoras de sucesiones y transfiera riqueza." if is_es else "Protect your assets, minimize probate delays, and transfer generational wealth smoothly."
        }
    ]

    current_key = current_file.replace("blog_", "").replace("_es.html", "").replace(".html", "")
    filtered_articles = [a for a in all_articles if a["key"] != current_key]

    cards_html = ""
    for a in filtered_articles:
        cards_html += f"""
          <a href="{a['file']}" class="blog-card">
            <div class="bc-img-wrap"><img src="{a['img']}" alt="{a['title']}" class="bc-img"></div>
            <div class="bc-content">
              <div class="bc-cat">{a['cat']}</div>
              <h3 class="bc-title">{a['title']}</h3>
              <p class="bc-excerpt">{a['excerpt']}</p>
              <div class="bc-link">{read_text} <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
            </div>
          </a>"""

    section_html = f"""
    <!-- MORE ARTICLES SLIDER / CAROUSEL SECTION -->
    <section class="more-articles-section">
      <div class="container">
        
        <div class="ma-header">
          <div>
            <p class="t-label" style="color:var(--green)"><span class="green-dot" style="background:var(--green)"></span>{section_title.upper()}</p>
            <h2 class="t-h1" style="font-size: 32px; color: var(--dark); margin: 4px 0 0 0;">{section_title}</h2>
            <p style="color: var(--muted); font-size: 15px; margin-top: 6px;">{section_sub}</p>
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
            {cards_html}
          </div>
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

        # Inject Carousel CSS if missing
        if "More Articles Interactive Carousel Styling" not in content:
            content = content.replace("</head>", f"<style>{CAROUSEL_CSS_AND_JS}</style>\n</head>")

        # Inject Carousel JS if missing
        if "function slideMoreArticles" not in content:
            content = content.replace("</body>", f"{CAROUSEL_JS}\n</body>")

        # Replace previous static section with full interactive Carousel
        content = re.sub(r'<!-- MORE ARTICLES SLIDER / (GRID|CAROUSEL) SECTION -->.*?</section>', '', content, flags=re.DOTALL)

        carousel_html = build_carousel_html(fname)
        if "<!-- CTA BANNER" in content:
            content = content.replace("<!-- CTA BANNER", f"{carousel_html}\n    <!-- CTA BANNER")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added interactive Left/Right Arrow Carousel to {fname}")

def main():
    print("=== Converting 'More Articles & Strategies' to Left/Right Arrow Carousel ===")
    apply()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
