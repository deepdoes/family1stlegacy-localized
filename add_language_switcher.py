#!/usr/bin/env python3
"""
add_language_switcher.py
Phase 2: Adds a 2-language switcher dropdown (English & Spanish ONLY) to ALL pages.

For English pages: EN active, links to _es variant
For Spanish pages: ES active, links to English variant
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def build_desktop_switcher(links, active_lang):
    """Build the desktop 2-language switcher HTML."""
    lang_names = {
        "en": ("EN", "English"),
        "es": ("ES", "Español"),
    }
    items_html = ""
    for code in ["en", "es"]:
        if code not in links:
            continue
        href = links[code]
        is_active = (code == active_lang)
        name_short, name_full = lang_names[code]
        active_cls = " active" if is_active else ""
        items_html += f'<a href="{href}" class="no-pill{active_cls}"><span>{name_short}</span> {name_full}<span class="lang-check">✓</span></a>\n              '
    
    active_short = lang_names[active_lang][0]
    return f'''<li class="lang-switcher" id="lang-switcher-desktop">
          <button class="lang-btn" aria-label="Select language">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
            {active_short}
            <svg class="lang-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
          </button>
          <div class="lang-dropdown">
              {items_html.strip()}
          </div>
        </li>'''

def build_mobile_switcher(links, active_lang):
    """Build the mobile 2-language switcher HTML."""
    lang_names = {
        "en": "EN",
        "es": "ES",
    }
    items = ""
    for code in ["en", "es"]:
        if code not in links:
            continue
        href = links[code]
        is_active = (code == active_lang)
        active_cls = " active" if is_active else ""
        items += f'<a href="{href}" class="{active_cls.strip()}">{lang_names[code]}</a>\n    '
    return f'''<div class="mobile-lang-switcher">
    {items.strip()}
  </div>'''

# --- Page mapping: page_base -> {lang: filename} ---
PAGE_MAP = {
    "index": {"en": "index.html", "es": "index_es.html"},
    "family_protection": {"en": "family_protection.html", "es": "family_protection_es.html"},
    "retirement_planning": {"en": "retirement_planning.html", "es": "retirement_planning_es.html"},
    "education_planning": {"en": "education_planning.html", "es": "education_planning_es.html"},
    "estate_planning": {"en": "estate_planning.html", "es": "estate_planning_es.html"},
    "financial_strategy": {"en": "financial_strategy.html", "es": "financial_strategy_es.html"},
    "business_strategies": {"en": "business_strategies.html", "es": "business_strategies_es.html"},
    "opportunity": {"en": "opportunity.html", "es": "opportunity_es.html"},
    "privacy": {"en": "privacy.html", "es": "privacy_es.html"},
    "terms": {"en": "terms.html", "es": "terms_es.html"},
    "blog_education": {"en": "blog_education.html", "es": "blog_education_es.html"},
    "blog_family_protection": {"en": "blog_family_protection.html", "es": "blog_family_protection_es.html"},
    "blog_financial_strategy": {"en": "blog_financial_strategy.html", "es": "blog_financial_strategy_es.html"},
    "blog_legacy": {"en": "blog_legacy.html", "es": "blog_legacy_es.html"},
    "blog_retirement": {"en": "blog_retirement.html", "es": "blog_retirement_es.html"},
}

def get_page_info(filename):
    """Return (base_name, lang_code) for a given filename."""
    name = filename.replace(".html", "")
    if name.endswith("_es"):
        return name[:-3], "es"
    return name, "en"

def process_file(filename):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    base, lang = get_page_info(filename)
    links = PAGE_MAP.get(base, {})
    if not links:
        return False

    # Remove existing switcher blocks to rebuild with 2 languages only
    content = re.sub(r'<li class="lang-switcher".*?</li>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="mobile-lang-switcher">.*?</div>', '', content, flags=re.DOTALL)

    desktop_html = build_desktop_switcher(links, lang)
    mobile_html = build_mobile_switcher(links, lang)

    # Inject desktop switcher before CTA button in nav-links
    pattern = r'(<li><a\s+[^>]*class="nav-cta"[^>]*>.*?</a></li>)'
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        content = content.replace(match.group(0), desktop_html + "\n        " + match.group(0), 1)

    # Inject mobile switcher before mobile-menu-footer
    if '<div class="mobile-menu-footer">' in content:
        content = content.replace('<div class="mobile-menu-footer">', mobile_html + '\n  <div class="mobile-menu-footer">', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Updated 2-lang switcher on {filename}")
    return True

def main():
    print("=== Updating Language Switcher to 2 Languages Only (EN & ES) ===\n")
    all_files = []
    for base, langs in PAGE_MAP.items():
        for lang, filename in langs.items():
            all_files.append(filename)

    for filename in sorted(set(all_files)):
        process_file(filename)

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
