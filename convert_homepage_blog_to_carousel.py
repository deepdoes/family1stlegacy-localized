#!/usr/bin/env python3
"""
convert_homepage_blog_to_carousel.py
Converts the 'Latest Articles & Strategies' section on the homepage (index.html, index_es.html, etc.)
from a 6-card multi-row grid into a clean, compact interactive horizontal carousel with Left (←) and Right (→) Navigation Arrows!
- Drastically reduces vertical homepage height.
- Keeps all 6 articles easily accessible.
- Matches the header & slider button styling of the Testimonials carousel.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

HOMEPAGE_CAROUSEL_CSS = """
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

HOMEPAGE_CAROUSEL_JS = """
<script>
function slideHomeBlog(direction) {
  const container = document.querySelector('.blog-slider-wrap');
  if(!container) return;
  const scrollAmount = direction === 'left' ? -375 : 375;
  container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}
</script>
"""

def update_homepage_blog(fname):
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject CSS & JS
    if "Homepage Blog Carousel Enhancement" not in html:
        html = html.replace("</head>", f"<style>{HOMEPAGE_CAROUSEL_CSS}</style>\n</head>")
    if "function slideHomeBlog" not in html:
        html = html.replace("</body>", f"{HOMEPAGE_CAROUSEL_JS}\n</body>")

    is_es = "_es." in fname
    section_title = "Últimos artículos y estrategias." if is_es else "Latest Articles &<br>Strategies."
    section_label = "PERSPECTIVAS FINANCIERAS" if is_es else "FINANCIAL INSIGHTS"

    # Extract all 6 cards inside #blog
    card_pattern = r'<a href="blog_[^"]+" class="blog-card"[^>]*>.*?</a>'
    cards = re.findall(card_pattern, html, flags=re.DOTALL)

    if not cards:
        print(f"  ⚠️ Could not find blog cards in {fname}")
        return

    cards_joined = "\n".join(cards)

    new_blog_section_inner = f"""
    <div class="blog-carousel-header">
      <div class="blog-header-left">
        <p class="t-label" data-reveal style="color:var(--green)"><span class="green-dot" style="background:var(--green)"></span>{section_label}</p>
        <h2 class="t-h1" data-reveal data-delay="1">{section_title}</h2>
      </div>
      <div class="blog-header-right" data-reveal data-delay="1" style="display:flex; gap:12px; align-items:center;">
        <button class="blog-nav-btn" onclick="slideHomeBlog('left')" aria-label="Previous articles">
          <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
        </button>
        <button class="blog-nav-btn" onclick="slideHomeBlog('right')" aria-label="Next articles">
          <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
    </div>

    <div class="blog-slider-wrap" data-reveal data-delay="2">
      <div class="blog-slider-track">
        {cards_joined}
      </div>
    </div>
"""

    # Replace container inner inside section#blog
    section_pattern = r'<section id="blog"[^>]*>\s*<div class="container">(.*?)</div>\s*</section>'
    match = re.search(section_pattern, html, flags=re.DOTALL)
    if match:
        html = re.sub(section_pattern, f'<section id="blog">\n  <div class="container">\n{new_blog_section_inner}\n  </div>\n</section>', html, flags=re.DOTALL)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✓ Converted homepage blog section to Left/Right Arrow Carousel in {fname}")

def main():
    print("=== Converting Homepage Blog Section to Left/Right Arrow Carousel ===")
    index_files = ["index.html", "index_es.html", "index_pt.html", "index_rw.html", "index_sw.html"]
    for idx_file in index_files:
        update_homepage_blog(idx_file)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
