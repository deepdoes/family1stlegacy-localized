#!/usr/bin/env python3
"""
fix_article_navbar_contrast.py
Fixes top navbar legibility, Services submenu dropdown, AND Language switcher dropdown visibility on all article pages (blog_*.html across all languages):
1. Adds `class="article-page"` to the <body> tag of all blog pages.
2. Injects solid dark purple glassmorphic header bar styling (rgba(35, 18, 62, 0.96)) for body.article-page #nav.
3. Top-level nav links get crisp white text.
4. Services dropdown links (.nav-dropdown a) get dark slate text (#1E293B) and emerald hover highlights (#1D9E75).
5. Language switcher dropdown links (.lang-dropdown a) get dark slate text (#1E293B) so "English" / "Español" labels are 100% visible and high-contrast!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

NAV_BAR_CSS = """
/* ── Article Page Header Polish & Submenu Dropdown Fix ── */
body.article-page #nav,
body.article-page #nav:not(.stuck),
body.article-page #nav.stuck {
  background: rgba(35, 18, 62, 0.96) !important;
  backdrop-filter: blur(16px) !important;
  -webkit-backdrop-filter: blur(16px) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
}

body.article-page #nav .nav-links > li > a:not(.nav-cta),
body.article-page #nav .nav-links > li > .nav-dropdown-toggle {
  color: rgba(255, 255, 255, 0.92) !important;
  font-weight: 600 !important;
  transition: color 0.2s ease !important;
}

body.article-page #nav .nav-links > li > a:not(.nav-cta):hover,
body.article-page #nav .nav-links > li > .nav-dropdown-toggle:hover {
  color: #ffffff !important;
}

/* Services Dropdown Container & Links */
body.article-page #nav .nav-dropdown {
  background: #ffffff !important;
  border: 1px solid rgba(74, 45, 122, 0.12) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
  border-radius: 14px !important;
  padding: 8px 0 !important;
}

body.article-page #nav .nav-dropdown a {
  color: #1E293B !important;
  font-weight: 600 !important;
  padding: 10px 20px !important;
  font-size: 14px !important;
  display: block !important;
  transition: all 0.2s ease !important;
}

body.article-page #nav .nav-dropdown a:hover {
  background: #F1F5F9 !important;
  color: #1D9E75 !important;
}

/* Language Switcher Dropdown Container & Links */
body.article-page #nav .lang-dropdown {
  background: #ffffff !important;
  border: 1px solid rgba(74, 45, 122, 0.12) !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15) !important;
  border-radius: 14px !important;
  padding: 8px !important;
}

body.article-page #nav .lang-dropdown a {
  color: #1E293B !important;
  font-weight: 600 !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  padding: 8px 12px !important;
  border-radius: 8px !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}

body.article-page #nav .lang-dropdown a:hover {
  background: #F1F5F9 !important;
  color: #1D9E75 !important;
}

body.article-page #nav .lang-dropdown a.active {
  background: #F1F5F9 !important;
  color: #4A2D7A !important;
}

body.article-page #nav .lang-dropdown a span:first-child {
  background: rgba(74, 45, 122, 0.1) !important;
  color: #4A2D7A !important;
  padding: 3px 8px !important;
  border-radius: 6px !important;
  font-weight: 700 !important;
  font-size: 11px !important;
}

body.article-page #nav .nav-logo img {
  filter: brightness(0) invert(1) !important;
}

body.article-page #nav .lang-btn {
  color: #ffffff !important;
  border-color: rgba(255, 255, 255, 0.3) !important;
  background: rgba(255, 255, 255, 0.1) !important;
}

body.article-page #nav .lang-btn svg {
  stroke: #ffffff !important;
}

body.article-page .article-hero-banner {
  margin-top: 80px !important;
}
"""

def update_article_headers():
    blog_files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(blog_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Remove old CSS if present
        content = re.sub(r'/\* ── Article Page Header Polish.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'body\.article-page #nav.*?margin-top: 80px !important;\s*}', '', content, flags=re.DOTALL)

        # Add article-page class to body if not present
        if 'class="article-page"' not in content:
            content = content.replace("<body>", '<body class="article-page">')
            content = content.replace('<body class="', '<body class="article-page ')

        # Inject updated NAV_BAR_CSS
        content = content.replace("</head>", f"<style>{NAV_BAR_CSS}</style>\n</head>")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Fixed header, Services dropdown, and Language dropdown visibility on {fname}")

def main():
    print("=== Fixing Submenu & Language Dropdown Visibility Across All Blog Pages ===")
    update_article_headers()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
