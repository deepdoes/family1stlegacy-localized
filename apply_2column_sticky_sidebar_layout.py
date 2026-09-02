#!/usr/bin/env python3
"""
apply_2column_sticky_sidebar_layout.py
Upgrades all 6 Knowledgebase article pages across English and Spanish to a Modern 2-Column Sticky Sidebar Layout:
- Main Left Column (70%): Key Takeaways, Article Content, AI FAQ, Educational Disclosure.
- Sticky Right Sidebar (30%): Interactive Table of Contents + High-Converting Consultation CTA Card + Trust Badges.
- Fully responsive across mobile, tablet, and widescreen desktop.
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

TWO_COLUMN_CSS = """
/* ─── Modern 2-Column Sticky Sidebar Article Layout ─── */
.article-container-wrap {
  max-width: 1200px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
}
.article-layout-grid {
  display: grid !important;
  grid-template-columns: 1fr 340px !important;
  gap: 48px !important;
  align-items: flex-start !important;
  margin-top: 40px !important;
}
@media (max-width: 992px) {
  .article-layout-grid {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .article-sidebar-col {
    order: -1 !important; /* Shows TOC above article on mobile */
  }
  .article-sidebar-sticky {
    position: static !important;
    top: 0 !important;
  }
}

.article-main-col {
  min-width: 0 !important;
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  padding: 40px !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
}
@media (max-width: 640px) {
  .article-main-col {
    padding: 24px 20px !important;
  }
}

.article-sidebar-sticky {
  position: sticky !important;
  top: 100px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 24px !important;
}

.sidebar-widget {
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  padding: 24px !important;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important;
}

.sidebar-widget-toc .toc-title {
  font-size: 15px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  margin-bottom: 14px !important;
  letter-spacing: 0.5px !important;
}
.sidebar-widget-toc ul {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}
.sidebar-widget-toc a {
  color: #4A2D7A !important;
  text-decoration: none !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  line-height: 1.4 !important;
  transition: color 0.2s ease !important;
}
.sidebar-widget-toc a:hover {
  color: #1D9E75 !important;
  text-decoration: underline !important;
}

.sidebar-widget-cta {
  background: linear-gradient(135deg, #4A2D7A 0%, #321c56 100%) !important;
  color: #ffffff !important;
  border: none !important;
}
.sidebar-widget-cta .swc-badge {
  display: inline-block !important;
  background: rgba(29, 158, 117, 0.2) !important;
  color: #26D07C !important;
  padding: 4px 12px !important;
  border-radius: 20px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  margin-bottom: 12px !important;
}
.sidebar-widget-cta h3 {
  font-size: 19px !important;
  font-weight: 700 !important;
  color: #ffffff !important;
  margin-bottom: 8px !important;
  line-height: 1.3 !important;
}
.sidebar-widget-cta p {
  font-size: 13.5px !important;
  color: rgba(255, 255, 255, 0.8) !important;
  line-height: 1.5 !important;
  margin-bottom: 20px !important;
}
.sidebar-widget-cta .swc-btn {
  display: block !important;
  width: 100% !important;
  padding: 12px 16px !important;
  background: #1D9E75 !important;
  color: #ffffff !important;
  text-align: center !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 30px !important;
  text-decoration: none !important;
  transition: background 0.3s ease !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.3) !important;
}
.sidebar-widget-cta .swc-btn:hover {
  background: #157959 !important;
}
.sidebar-widget-cta .swc-phone {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin-top: 14px !important;
  font-size: 13px !important;
  color: rgba(255, 255, 255, 0.9) !important;
  text-decoration: none !important;
  font-weight: 600 !important;
}
.sidebar-widget-cta .swc-phone svg {
  width: 14px !important;
  height: 14px !important;
  stroke: #26D07C !important;
}
"""

def extract_toc_links(html):
    matches = re.findall(r'<li><a href="(#section-[^"]+)">(.*?)</a></li>', html)
    if not matches:
        return ""
    toc_items = ""
    for href, text in matches:
        toc_items += f'<li><a href="{href}">{text}</a></li>\n'
    return toc_items

def build_sidebar_html(fname, html_content):
    is_es = "_es." in fname
    toc_links = extract_toc_links(html_content)

    toc_title = "En esta guía" if is_es else "In This Guide"
    cta_badge = "Consulta Gratuita" if is_es else "No-Cost Consultation"
    cta_title = "¿Listo para orientación honesta?" if is_es else "Ready for Honest Guidance?"
    cta_text = "Reserve una revisión sin compromiso con un profesional con licencia." if is_es else "Schedule a review with a licensed professional — no pressure, no obligation."
    cta_btn = "Programar Revisión →" if is_es else "Schedule a Review →"

    sidebar_html = f"""
    <!-- RIGHT SIDEBAR (Sticky) -->
    <div class="article-sidebar-col">
      <div class="article-sidebar-sticky">
        
        <!-- Widget 1: Table of Contents -->
        {f'''<div class="sidebar-widget sidebar-widget-toc">
          <div class="toc-title">📖 {toc_title}</div>
          <ul>
            {toc_links}
          </ul>
        </div>''' if toc_links else ''}

        <!-- Widget 2: Consultation CTA Card -->
        <div class="sidebar-widget sidebar-widget-cta">
          <span class="swc-badge">{cta_badge}</span>
          <h3>{cta_title}</h3>
          <p>{cta_text}</p>
          <a href="index.html#contact" class="swc-btn">{cta_btn}</a>
          <a href="tel:+14696081595" class="swc-phone">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            Call (469) 608-1595
          </a>
        </div>

        <!-- Widget 3: Trust Badges -->
        <div class="sidebar-widget" style="background:#F8FAFC;">
          <div style="font-size:12px; font-weight:700; color:#4A2D7A; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">Why Family First Legacy</div>
          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Licensed & Insured</li>
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> 24hr Response</li>
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Your Privacy Matters</li>
          </ul>
        </div>

      </div>
    </div>
"""
    return sidebar_html

def update_file(fname):
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject 2-Column CSS
    if "Modern 2-Column Sticky Sidebar Article Layout" not in html:
        html = html.replace("</head>", f"<style>{TWO_COLUMN_CSS}</style>\n</head>")

    # Extract article-body content
    body_match = re.search(r'<div class="article-body"[^>]*>(.*?)</div>\s*</div>\s*</section>', html, flags=re.DOTALL)
    if not body_match:
        body_match = re.search(r'<div class="article-body"[^>]*>(.*?)</div>\s*<!-- MORE ARTICLES', html, flags=re.DOTALL)

    if not body_match:
        print(f"  ⚠️ Could not find article-body in {fname}")
        return

    main_article_content = body_match.group(1)

    # Remove in-body TOC box if present since TOC is now in sidebar
    main_article_content = re.sub(r'<div class="toc-box">.*?</div>\s*</div>', '', main_article_content, flags=re.DOTALL)
    main_article_content = re.sub(r'<div class="toc-box">.*?</div>', '', main_article_content, flags=re.DOTALL)

    sidebar_html = build_sidebar_html(fname, main_article_content)

    new_section_html = f"""
    <!-- 2-COLUMN ARTICLE LAYOUT -->
    <section id="blog-article" style="padding: 40px 0 80px 0; background: #F8FAFC;">
      <div class="article-container-wrap">
        
        <div class="article-header" data-reveal style="text-align:center; max-width:800px; margin:0 auto 32px auto;">
          <div class="article-badge" style="justify-content:center;"><span class="green-dot"></span>Educational Resource</div>
        </div>

        <div class="article-layout-grid">
          
          <!-- LEFT MAIN CONTENT COLUMN -->
          <div class="article-main-col" data-reveal>
            {main_article_content}
          </div>

          {sidebar_html}

        </div>
      </div>
    </section>
"""

    pattern = r'<section id="blog-article"[^>]*>.*?</section>'
    html = re.sub(pattern, new_section_html, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ Converted {fname} to 2-Column Sticky Sidebar Layout")

def main():
    print("=== Converting All Blog Pages to 2-Column Sticky Sidebar Layout ===")
    files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
