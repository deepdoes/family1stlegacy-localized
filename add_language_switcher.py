#!/usr/bin/env python3
"""
add_language_switcher.py
Phase 2: Adds a language switcher dropdown to ALL pages (English + Spanish).

For English pages: shows EN as active, links to _es, _pt, _rw, _sw variants
For Spanish pages: shows ES as active, links to English, _pt, _rw, _sw variants

The switcher is injected:
1. In the desktop nav-links list (before the CTA button)
2. In the mobile-menu nav (near the top, after the first <a> link)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# --- CSS for the language switcher (injected into <style> on each page) ---
LANG_SWITCHER_CSS = """
/* ─── Language Switcher ─── */
.lang-switcher {
  position: relative;
  display: inline-flex;
  align-items: center;
}
.lang-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background: rgba(74,45,122,0.08);
  border: 1px solid rgba(74,45,122,0.2);
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1px;
  color: var(--dark);
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.2s, border-color 0.2s;
  text-transform: uppercase;
  font-family: var(--font-body, sans-serif);
}
.lang-btn:hover {
  background: rgba(74,45,122,0.15);
  border-color: rgba(74,45,122,0.4);
}
.lang-btn svg { width: 14px; height: 14px; flex-shrink: 0; }
.lang-btn .lang-chevron { width: 10px; height: 10px; transition: transform 0.2s; }
.lang-switcher.open .lang-chevron { transform: rotate(180deg); }
.lang-dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  background: #fff;
  border: 1px solid #E8E4EF;
  border-radius: 12px;
  padding: 6px;
  min-width: 160px;
  box-shadow: 0 8px 32px rgba(74,45,122,0.15);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-6px);
  transition: opacity 0.18s, transform 0.18s, visibility 0.18s;
  z-index: 10000;
}
.lang-switcher.open .lang-dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
.lang-dropdown a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 500;
  color: #333;
  text-decoration: none;
  transition: background 0.15s;
}
.lang-dropdown a:hover { background: #F0EBF8; color: var(--green, #4A2D7A); }
.lang-dropdown a.active { font-weight: 700; color: var(--green, #4A2D7A); }
.lang-dropdown a .lang-check { margin-left: auto; font-size: 12px; opacity: 0; }
.lang-dropdown a.active .lang-check { opacity: 1; }

/* Mobile language switcher */
.mobile-lang-switcher {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  padding: 12px 20px 4px;
  border-top: 1px solid rgba(255,255,255,0.08);
  margin-top: 4px;
}
.mobile-lang-switcher a {
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 1px;
  text-transform: uppercase;
  padding: 4px 10px !important;
  border-radius: 20px !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  color: rgba(255,255,255,0.65) !important;
  text-decoration: none;
  transition: all 0.2s;
}
.mobile-lang-switcher a:hover { background: rgba(255,255,255,0.1) !important; color: #fff !important; }
.mobile-lang-switcher a.active { 
  background: rgba(74,45,122,0.6) !important; 
  border-color: rgba(255,255,255,0.4) !important; 
  color: #fff !important; 
}
"""

# --- JS for the language switcher ---
LANG_SWITCHER_JS = """
// Language switcher toggle
(function(){
  var s = document.querySelector('.lang-switcher');
  if (!s) return;
  s.querySelector('.lang-btn').addEventListener('click', function(e){
    e.stopPropagation();
    s.classList.toggle('open');
  });
  document.addEventListener('click', function(){ s.classList.remove('open'); });
})();
"""

def build_desktop_switcher(links, active_lang):
    """Build the desktop language switcher HTML."""
    items_html = ""
    lang_names = {
        "en": ("EN", "English"),
        "es": ("ES", "Español"),
        "pt": ("PT", "Português"),
        "rw": ("RW", "Kinyarwanda"),
        "sw": ("SW", "Kiswahili"),
    }
    for code, href in links.items():
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
    """Build the mobile language switcher HTML."""
    lang_names = {
        "en": "EN",
        "es": "ES",
        "pt": "PT",
        "rw": "RW",
        "sw": "SW",
    }
    items = ""
    for code, href in links.items():
        is_active = (code == active_lang)
        active_cls = " active" if is_active else ""
        items += f'<a href="{href}" class="{active_cls.strip()}">{lang_names[code]}</a>\n    '
    return f'''<div class="mobile-lang-switcher">
    {items.strip()}
  </div>'''

# --- Page mapping: page_base -> {lang: filename} ---
# Format: base_name (without lang suffix and .html) -> available langs
PAGE_MAP = {
    "index": {"en": "index.html", "es": "index_es.html", "pt": "index_pt.html", "rw": "index_rw.html", "sw": "index_sw.html"},
    "family_protection": {"en": "family_protection.html", "es": "family_protection_es.html", "pt": "family_protection_pt.html", "rw": "family_protection_rw.html", "sw": "family_protection_sw.html"},
    "retirement_planning": {"en": "retirement_planning.html", "es": "retirement_planning_es.html", "pt": "retirement_planning_pt.html", "rw": "retirement_planning_rw.html", "sw": "retirement_planning_sw.html"},
    "education_planning": {"en": "education_planning.html", "es": "education_planning_es.html", "pt": "education_planning_pt.html", "rw": "education_planning_rw.html", "sw": "education_planning_sw.html"},
    "estate_planning": {"en": "estate_planning.html", "es": "estate_planning_es.html", "pt": "estate_planning_pt.html", "rw": "estate_planning_rw.html", "sw": "estate_planning_sw.html"},
    "financial_strategy": {"en": "financial_strategy.html", "es": "financial_strategy_es.html", "pt": "financial_strategy_pt.html", "rw": "financial_strategy_rw.html", "sw": "financial_strategy_sw.html"},
    "privacy": {"en": "privacy.html", "es": "privacy_es.html", "pt": "privacy_pt.html", "rw": "privacy_rw.html", "sw": "privacy_sw.html"},
    "terms": {"en": "terms.html", "es": "terms_es.html", "pt": "terms_pt.html", "rw": "terms_rw.html", "sw": "terms_sw.html"},
    "blog_education": {"en": "blog_education.html", "es": "blog_education_es.html", "pt": "blog_education_pt.html", "rw": "blog_education_rw.html", "sw": "blog_education_sw.html"},
    "blog_family_protection": {"en": "blog_family_protection.html", "es": "blog_family_protection_es.html", "pt": "blog_family_protection_pt.html", "rw": "blog_family_protection_rw.html", "sw": "blog_family_protection_sw.html"},
    "blog_financial_strategy": {"en": "blog_financial_strategy.html", "es": "blog_financial_strategy_es.html", "pt": "blog_financial_strategy_pt.html", "rw": "blog_financial_strategy_rw.html", "sw": "blog_financial_strategy_sw.html"},
    "blog_legacy": {"en": "blog_legacy.html", "es": "blog_legacy_es.html", "pt": "blog_legacy_pt.html", "rw": "blog_legacy_rw.html", "sw": "blog_legacy_sw.html"},
    "blog_retirement": {"en": "blog_retirement.html", "es": "blog_retirement_es.html", "pt": "blog_retirement_pt.html", "rw": "blog_retirement_rw.html", "sw": "blog_retirement_sw.html"},
    # Pages that only have English (no language variants yet)
    "business_strategies": {"en": "business_strategies.html"},
    "opportunity": {"en": "opportunity.html"},
}

def get_page_info(filename):
    """Return (base_name, lang_code) for a given filename."""
    name = filename.replace(".html", "")
    for suffix in ["_es", "_pt", "_rw", "_sw"]:
        if name.endswith(suffix):
            base = name[:-len(suffix)]
            lang = suffix[1:]
            return base, lang
    return name, "en"


def inject_css(content):
    """Inject language switcher CSS into the <style> block."""
    if "lang-switcher" in content:
        return content  # Already injected
    # Inject before </style> of first style block
    return content.replace("</style>", LANG_SWITCHER_CSS + "\n</style>", 1)


def inject_js(content):
    """Inject JS at the end of the page."""
    if "lang-switcher-desktop" not in content:
        return content  # No switcher to power
    if "lang-switcher toggle" in content:
        return content  # Already has JS
    return content.replace("</body>", f"<script>{LANG_SWITCHER_JS}</script>\n</body>", 1)


def inject_desktop_nav(content, filename):
    """Inject the desktop language switcher into the nav-links ul."""
    base, lang = get_page_info(filename)
    links = PAGE_MAP.get(base, {})
    if not links:
        return content
    
    # Only inject if not already there
    if 'lang-switcher-desktop' in content:
        return content

    switcher_html = build_desktop_switcher(links, lang)
    
    # Find the nav-cta li and insert language switcher before it
    # Pattern to match the last </li> before the CTA button
    # Look for the nav-cta anchor
    pattern = r'(<li><a\s+(?:class="nav-cta"|href="[^"]*"\s+class="nav-cta")[^>]*>[^<]+</a></li>)'
    # Also handle es-style where href="#contact" comes first
    pattern2 = r'(<li><a\s+class="nav-cta"\s+href="[^"]*">[^<]+</a></li>)'
    
    match = re.search(pattern, content)
    if not match:
        match = re.search(pattern2, content)
    
    if match:
        content = content.replace(match.group(0), switcher_html + "\n        " + match.group(0))
        return content
    
    # Fallback: inject before </ul> of nav-links
    content = content.replace('</ul>\n      <button class="nav-toggle"', 
                              switcher_html + '\n        </ul>\n      <button class="nav-toggle"', 1)
    return content


def inject_mobile_nav(content, filename):
    """Inject the mobile language switcher into the mobile menu."""
    base, lang = get_page_info(filename)
    links = PAGE_MAP.get(base, {})
    if not links:
        return content

    if 'mobile-lang-switcher' in content:
        return content

    switcher_html = build_mobile_switcher(links, lang)

    # Inject before the closing </div> of mobile-menu (before mobile-menu-footer)
    if 'mobile-menu-footer' in content:
        content = content.replace('<div class="mobile-menu-footer">', 
                                  switcher_html + '\n  <div class="mobile-menu-footer">', 1)
    else:
        # Fallback: inject before </div> closing the mobile-menu div
        content = content.replace('</div>\n\n<!-- HERO', 
                                  switcher_html + '\n</div>\n\n<!-- HERO', 1)
    return content


def process_file(filename):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has switcher
    if 'mobile-lang-switcher' in content and 'lang-switcher-desktop' in content:
        print(f"  SKIP (already has switcher): {filename}")
        return True

    original = content
    content = inject_css(content)
    content = inject_desktop_nav(content, filename)
    content = inject_mobile_nav(content, filename)
    content = inject_js(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  OK: {filename}")
    else:
        print(f"  UNCHANGED: {filename}")
    return True


def main():
    print("=== Phase 2: Adding language switcher to all pages ===\n")

    all_files = []
    for base, langs in PAGE_MAP.items():
        for lang, filename in langs.items():
            all_files.append(filename)

    for filename in sorted(set(all_files)):
        process_file(filename)

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
