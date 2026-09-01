#!/usr/bin/env python3
"""
preserve_article_hero_header.py
Ensures every blog file has its complete Hero Header (H1 Article Title, Category Badge, Read Time, and Hero Image)
positioned prominently at the top of the page above the 2-Column Sticky Sidebar layout grid!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

ARTICLE_HERO_DATA = {
    "blog_family_protection.html": {
        "cat": "Family Protection",
        "title": "Is Your Family Counting on Work Benefits Alone?",
        "read": "5 min read",
        "img": "images/hero_life_insurance_diverse_1777335713599.png",
    },
    "blog_family_protection_es.html": {
        "cat": "Protección Familiar",
        "title": "¿Confía su familia solo en beneficios laborales?",
        "read": "5 min de lectura",
        "img": "images/hero_life_insurance_diverse_1777335713599.png",
    },
    "blog_retirement.html": {
        "cat": "Retirement Planning",
        "title": "Could Taxes Reduce the Retirement Income You're Counting On?",
        "read": "4 min read",
        "img": "images/hero_retirement_diverse_1777335727638.png",
    },
    "blog_retirement_es.html": {
        "cat": "Planificación de Jubilación",
        "title": "¿Podrían los impuestos reducir sus ingresos de jubilación?",
        "read": "4 min de lectura",
        "img": "images/hero_retirement_diverse_1777335727638.png",
    },
    "blog_education.html": {
        "cat": "Education Planning",
        "title": "What If Your Child's Path Changes After You Save?",
        "read": "5 min read",
        "img": "images/hero_education_diverse_1777335740128.png",
    },
    "blog_education_es.html": {
        "cat": "Planificación Educativa",
        "title": "¿Qué pasa si el camino de su hijo cambia después de ahorrar?",
        "read": "5 min de lectura",
        "img": "images/hero_education_diverse_1777335740128.png",
    },
    "blog_living_benefits.html": {
        "cat": "Living Benefits",
        "title": "What If You Survive the Illness - But Your Income Does Not?",
        "read": "4 min read",
        "img": "images/critical_illness_diverse_1777393231898.png",
    },
    "blog_financial_strategy.html": {
        "cat": "Financial Strategy",
        "title": "How Clear Financial Strategies Help Families Build Security",
        "read": "4 min read",
        "img": "images/financial_strategy_hispanic_1777333606672.png",
    },
    "blog_financial_strategy_es.html": {
        "cat": "Estrategia Financiera",
        "title": "Cómo las estrategias claras construyen seguridad duradera",
        "read": "4 min de lectura",
        "img": "images/financial_strategy_hispanic_1777333606672.png",
    },
    "blog_legacy.html": {
        "cat": "Legacy Planning",
        "title": "Preserving Your Legacy: Planning for Future Generations",
        "read": "4 min read",
        "img": "images/hero_estate_diverse_1777335759302.png",
    },
    "blog_legacy_es.html": {
        "cat": "Planificación de Legado",
        "title": "Preservar su legado: Planificación para generaciones futuras",
        "read": "4 min de lectura",
        "img": "images/hero_estate_diverse_1777335759302.png",
    },
}

def update_hero_header(fname):
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Determine Hero Data
    data = ARTICLE_HERO_DATA.get(fname)
    if not data:
        # Fallback to family protection defaults
        data = ARTICLE_HERO_DATA["blog_family_protection.html"]

    hero_html = f"""
    <!-- ARTICLE HERO HEADER -->
    <div class="article-hero-section" style="padding: 40px 0 20px 0; background: #ffffff;">
      <div class="article-container-wrap">
        <div class="article-header" data-reveal style="text-align:center; max-width:850px; margin:0 auto 32px auto;">
          <div class="article-badge" style="display:inline-flex; align-items:center; gap:6px; background:rgba(29,158,117,0.08); border:1px solid rgba(29,158,117,0.2); color:#1D9E75; padding:6px 16px; border-radius:100px; font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-bottom:16px;">
            <span class="green-dot" style="width:6px; height:6px; background:#1D9E75; border-radius:50%;"></span>
            {data['cat']}
          </div>
          <h1 class="article-title" style="font-family:var(--font-head); font-size:42px; font-weight:800; color:var(--dark); line-height:1.2; margin-bottom:16px;">{data['title']}</h1>
          <div class="article-meta" style="font-size:14px; color:var(--muted); font-weight:600;">{data['read']}</div>
        </div>

        <div class="article-hero-wrap" data-reveal data-delay="1" style="max-width:1050px; margin:0 auto 40px auto; border-radius:24px; overflow:hidden; box-shadow:0 12px 36px rgba(0,0,0,0.06);">
          <img src="{data['img']}" class="article-hero-img" alt="{data['title']}" style="width:100%; height:auto; max-height:480px; object-fit:cover; display:block;">
        </div>
      </div>
    </div>
"""

    # Inject hero_html right before section#blog-article if not already present
    if "<!-- ARTICLE HERO HEADER -->" in html:
        html = re.sub(r'<!-- ARTICLE HERO HEADER -->.*?</div>\s*</div>\s*</div>', hero_html.strip(), html, flags=re.DOTALL)
    else:
        html = html.replace('<section id="blog-article"', f'{hero_html}\n    <section id="blog-article"')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ Preserved H1 Title & Hero Image header in {fname}")

def main():
    print("=== Preserving Article H1 Titles & Hero Images Above 2-Column Grid ===")
    for fname in sorted(ARTICLE_HERO_DATA.keys()):
        update_hero_header(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
