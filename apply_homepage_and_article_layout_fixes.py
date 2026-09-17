#!/usr/bin/env python3
"""
apply_homepage_and_article_layout_fixes.py
1. Updates Knowledgebase cards on all homepages (index*.html) to fit 4 cards per row on desktop (width: 280px).
2. Constrains article pages (blog_*.html) to a fixed max-width (1200px) centered layout on large screens.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_homepages():
    home_files = [f for f in os.listdir(BASE) if f.startswith("index") and f.endswith(".html") and not f.startswith("v1")]

    card_css_fix = """
.blog-slider-track .blog-card {
  width: 280px !important;
  max-width: 85vw !important;
  flex-shrink: 0 !important;
}
.blog-slider-track {
  gap: 24px !important;
}
"""

    for fname in home_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Update blog-card width rule
        content = re.sub(
            r'\.blog-slider-track \.blog-card \{\s*width:\s*\d+px !important;',
            '.blog-slider-track .blog-card {\n  width: 280px !important;',
            content
        )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Updated homepage KB cards width to 280px on {fname}")

def update_article_pages():
    blog_files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1") and not f.startswith("old")]

    article_max_width_css = """
/* ─── Fixed Max-Width Large Screen Bounds for Articles ─── */
body.article-page, body:has(.article-hero-banner) {
  background: #f8fafc !important;
}

.article-hero-banner, .article-page-wrapper {
  max-width: 1200px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}

.article-hero-banner {
  border-radius: 0 0 24px 24px !important;
}

.article-hero-container {
  max-width: 1040px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
}

.article-grid-container {
  max-width: 1040px !important;
  margin: 40px auto 0 auto !important;
  padding: 0 24px !important;
}

.article-hero-img-wrap img {
  max-height: 420px !important;
  object-fit: cover !important;
}
</style>
"""

    for fname in blog_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "/* ─── Fixed Max-Width Large Screen Bounds for Articles ─── */" not in content:
            content = content.replace("</style>", article_max_width_css, 1)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Applied fixed max-width layout to {fname}")

def main():
    print("=== Applying Layout Improvements ===")
    update_homepages()
    update_article_pages()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
