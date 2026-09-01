#!/usr/bin/env python3
"""
update_index_es_blog_carousel.py
Syncs the homepage blog section of index_es.html with the Left/Right Arrow Carousel format.
"""

import re

FPATH = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy/index_es.html"

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# Inject CSS & JS if needed
CSS = """
/* ─── Homepage Blog Carousel Enhancement ─── */
.blog-carousel-header {
  display: flex !important;
  justify-content: space-between !important;
  align-items: flex-end !important;
  margin-bottom: 36px !important;
  gap: 24px !important;
  flex-wrap: wrap !important;
}
.blog-nav-btn {
  width: 48px !important;
  height: 48px !important;
  background: #ffffff !important;
  border: 1.5px solid rgba(74, 45, 122, 0.14) !important;
  border-radius: 50% !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer !important;
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
}
.blog-nav-btn:hover {
  background: #1D9E75 !important;
  border-color: #1D9E75 !important;
  transform: scale(1.05) !important;
  box-shadow: 0 8px 24px rgba(29, 158, 117, 0.25) !important;
}
.blog-nav-btn svg {
  width: 18px !important;
  height: 18px !important;
  stroke: #4A2D7A !important;
  fill: none !important;
  stroke-width: 2.2 !important;
  transition: stroke 0.25s !important;
}
.blog-nav-btn:hover svg {
  stroke: #ffffff !important;
}
.blog-slider-wrap {
  overflow-x: auto !important;
  scroll-behavior: smooth !important;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
  padding: 8px 4px 24px 4px !important;
}
.blog-slider-wrap::-webkit-scrollbar {
  display: none !important;
}
.blog-slider-track {
  display: flex !important;
  gap: 28px !important;
  width: max-content !important;
}
.blog-slider-track .blog-card {
  width: 350px !important;
  max-width: 85vw !important;
  flex-shrink: 0 !important;
}
"""

JS = """
<script>
function slideHomeBlog(direction) {
  const container = document.querySelector('.blog-slider-wrap');
  if(!container) return;
  const scrollAmount = direction === 'left' ? -375 : 375;
  container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}
</script>
"""

if "Homepage Blog Carousel Enhancement" not in html:
    html = html.replace("</head>", f"<style>{CSS}</style>\n</head>")
if "function slideHomeBlog" not in html:
    html = html.replace("</body>", f"{JS}\n</body>")

# Replace section#blog inner in index_es.html
es_blog_inner = """
    <div class="blog-carousel-header">
      <div class="blog-header-left">
        <p class="t-label" data-reveal style="color:var(--green)"><span class="green-dot" style="background:var(--green)"></span>PERSPECTIVAS FINANCIERAS</p>
        <h2 class="t-h1" data-reveal data-delay="1">Últimos artículos y<br>Estrategias.</h2>
      </div>
      <div class="blog-header-right" data-reveal data-delay="1" style="display:flex; gap:12px; align-items:center;">
        <button class="blog-nav-btn" onclick="slideHomeBlog('left')" aria-label="Artículos anteriores">
          <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        </button>
        <button class="blog-nav-btn" onclick="slideHomeBlog('right')" aria-label="Siguientes artículos">
          <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
    </div>

    <div class="blog-slider-wrap" data-reveal data-delay="2">
      <div class="blog-slider-track">
        <!-- Card 1 -->
        <a href="blog_family_protection_es.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/family_protection_black_1777333563521.png" alt="Protección Familiar" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Protección Familiar</div>
            <h3 class="bc-title">¿Confía su familia solo en beneficios laborales?</h3>
            <p class="bc-excerpt">El seguro de vida del empleador puede ser útil, pero conozca sus límites y opciones portátiles.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>

        <!-- Card 2 -->
        <a href="blog_retirement_es.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/retirement_planning_black_1777333576986.png" alt="Jubilación" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Jubilación</div>
            <h3 class="bc-title">¿Podrían los impuestos reducir sus ingresos de jubilación?</h3>
            <p class="bc-excerpt">Aprenda sobre los 3 cubos de impuestos y estrategias de protección contra caídas.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>

        <!-- Card 3 -->
        <a href="blog_education_es.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/education_planning_hispanic_1777333593369.png" alt="Educación" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Educación</div>
            <h3 class="bc-title">¿Qué pasa si el camino de su hijo cambia después de ahorrar?</h3>
            <p class="bc-excerpt">Explore opciones flexibles de ahorro para la educación universitaria o profesional.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>

        <!-- Card 4 -->
        <a href="blog_living_benefits.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/critical_illness_diverse_1777393231898.png" alt="Beneficios en Vida" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Beneficios en Vida</div>
            <h3 class="bc-title">¿Qué pasa si sobrevive a la enfermedad, pero sus ingresos no?</h3>
            <p class="bc-excerpt">Los beneficios en vida le permiten acceder a fondos durante enfermedades graves.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>

        <!-- Card 5 -->
        <a href="blog_financial_strategy_es.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/financial_strategy_hispanic_1777333606672.png" alt="Estrategia Financiera" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Estrategia Financiera</div>
            <h3 class="bc-title">Cómo las estrategias claras construyen seguridad duradera</h3>
            <p class="bc-excerpt">Los 4 pilares de la salud financiera familiar explicados de forma sencilla.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>

        <!-- Card 6 -->
        <a href="blog_legacy_es.html" class="blog-card">
          <div class="bc-img-wrap"><img src="images/wealth_transfer_diverse_1777393288351.png" alt="Legado y Patrimonio" class="bc-img"></div>
          <div class="bc-content">
            <div class="bc-cat">Legado y Patrimonio</div>
            <h3 class="bc-title">Preservar su legado: Planificación para generaciones futuras</h3>
            <p class="bc-excerpt">Proteja sus activos, evite demoras de sucesiones y transfiera riqueza.</p>
            <div class="bc-link">Leer Artículo <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
          </div>
        </a>
      </div>
    </div>
"""

pattern = r'<section id="blog"[^>]*>\s*<div class="container">(.*?)</div>\s*</section>'
html = re.sub(pattern, f'<section id="blog">\n  <div class="container">\n{es_blog_inner}\n  </div>\n</section>', html, flags=re.DOTALL)

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Successfully updated index_es.html with Left/Right Arrow Carousel")
