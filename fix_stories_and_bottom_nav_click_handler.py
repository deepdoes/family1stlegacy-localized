#!/usr/bin/env python3
"""
fix_stories_and_bottom_nav_click_handler.py
Fixes bottom nav click events (specifically Stories/Historias, Home, Consult):
1. Sets pointer-events: none on SVG/span inside .mbn-item and .mbn-cta so click events are never blocked.
2. Adds smooth-scroll handleMbnClick JS function that smoothly scrolls to #reviews, #hero, #contact on index page, and navigates correctly on subpages.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CLICK_POINTER_CSS = """
.mbn-item *, .mbn-cta * {
  pointer-events: none !important;
}
"""

EN_BOTTOM_NAV_AND_SHEETS = """
<div class="mobile-sheet-overlay" id="mobileSheetOverlay" onclick="closeMobileSheets()"></div>

<!-- SERVICES POPOVER SHEET -->
<div class="mobile-services-sheet" id="mobileServicesSheet">
  <div class="mss-header">
    <span class="mss-title">Our Services</span>
    <button class="mss-close" onclick="closeMobileSheets()">✕</button>
  </div>
  <div class="mss-grid">
    <a href="family_protection.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Life Insurance</a>
    <a href="retirement_planning.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V6m0 12v-2m0 0c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Retirement Planning</a>
    <a href="education_planning.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>Education Planning</a>
    <a href="estate_planning.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>Estate & Legacy Planning</a>
    <a href="financial_strategy.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>Financial Strategy</a>
    <a href="business_strategies.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>Business Strategies</a>
  </div>
</div>

<!-- FULL MENU BOTTOM DRAWER SHEET -->
<div class="mobile-menu-sheet" id="mobileMenuSheet">
  <div class="mms-drag-handle"></div>
  <div class="mms-header">
    <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" class="mms-logo">
    <button class="mms-close" onclick="closeMobileSheets()">✕</button>
  </div>
  <nav class="mms-links">
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'about', 'index.html')">About</a>
    <a href="javascript:void(0)" onclick="toggleMobileServicesSheet()">Services <span>▾</span></a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'process', 'index.html')">How It Works</a>
    <a href="opportunity.html" onclick="closeMobileSheets()">Opportunity</a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'reviews', 'index.html')">Stories</a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'blog', 'index.html')">Knowledgebase</a>
    <div class="mms-lang">
      <a href="index.html" class="active">EN</a>
      <a href="index_es.html">ES</a>
    </div>
    <a href="javascript:void(0)" class="mms-cta-btn" onclick="handleMbnClick(event, 'contact', 'index.html')">Free Consultation</a>
  </nav>
</div>

<!-- FLOATING BOTTOM NAVIGATION BAR -->
<nav class="mobile-bottom-nav">
  <a href="javascript:void(0)" class="mbn-item" id="mbn-home" onclick="handleMbnClick(event, 'hero', 'index.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Home</span>
  </a>
  <button class="mbn-item" id="mbn-services" onclick="toggleMobileServicesSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Services</span>
  </button>
  <a href="javascript:void(0)" class="mbn-cta" id="mbn-cta" onclick="handleMbnClick(event, 'contact', 'index.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consult</span>
  </a>
  <a href="javascript:void(0)" class="mbn-item" id="mbn-stories" onclick="handleMbnClick(event, 'reviews', 'index.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Stories</span>
  </a>
  <button class="mbn-item" id="mbn-menu" onclick="toggleMobileMenuSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menu</span>
  </button>
</nav>

<script>
function handleMbnClick(e, targetId, homePage) {
  if (e) e.preventDefault();
  closeMobileSheets();
  
  const currentPath = window.location.pathname;
  const isHomePage = currentPath.endsWith(homePage) || (homePage === 'index.html' && (currentPath.endsWith('/') || currentPath.endsWith('/index.html')));

  if (isHomePage) {
    const el = document.getElementById(targetId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    window.location.href = homePage + '#' + targetId;
  }
}

function toggleMobileServicesSheet(e) {
  if(e) e.preventDefault();
  const sheet = document.getElementById('mobileServicesSheet');
  const menuSheet = document.getElementById('mobileMenuSheet');
  const overlay = document.getElementById('mobileSheetOverlay');
  
  menuSheet.classList.remove('open');
  sheet.classList.toggle('open');
  if(sheet.classList.contains('open')) {
    overlay.classList.add('open');
    setActiveMbn('mbn-services');
  } else {
    overlay.classList.remove('open');
  }
}

function toggleMobileMenuSheet(e) {
  if(e) e.preventDefault();
  const menuSheet = document.getElementById('mobileMenuSheet');
  const sheet = document.getElementById('mobileServicesSheet');
  const overlay = document.getElementById('mobileSheetOverlay');
  
  sheet.classList.remove('open');
  menuSheet.classList.toggle('open');
  if(menuSheet.classList.contains('open')) {
    overlay.classList.add('open');
    setActiveMbn('mbn-menu');
  } else {
    overlay.classList.remove('open');
  }
}

function closeMobileSheets() {
  document.getElementById('mobileServicesSheet')?.classList.remove('open');
  document.getElementById('mobileMenuSheet')?.classList.remove('open');
  document.getElementById('mobileSheetOverlay')?.classList.remove('open');
}

function setActiveMbn(id) {
  document.querySelectorAll('.mbn-item').forEach(el => el.classList.remove('active'));
  document.getElementById(id)?.classList.add('active');
}

document.addEventListener('DOMContentLoaded', function() {
  const p = window.location.pathname;
  if (p.includes('family_protection') || p.includes('retirement_planning') || 
      p.includes('education_planning') || p.includes('estate_planning') || 
      p.includes('financial_strategy') || p.includes('business_strategies')) {
    setActiveMbn('mbn-services');
  } else if (p.includes('opportunity')) {
    setActiveMbn('mbn-menu');
  } else {
    setActiveMbn('mbn-home');
  }
});
</script>
"""

ES_BOTTOM_NAV_AND_SHEETS = """
<div class="mobile-sheet-overlay" id="mobileSheetOverlay" onclick="closeMobileSheets()"></div>

<!-- SERVICES POPOVER SHEET -->
<div class="mobile-services-sheet" id="mobileServicesSheet">
  <div class="mss-header">
    <span class="mss-title">Nuestros Servicios</span>
    <button class="mss-close" onclick="closeMobileSheets()">✕</button>
  </div>
  <div class="mss-grid">
    <a href="family_protection_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Seguro de Vida</a>
    <a href="retirement_planning_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V6m0 12v-2m0 0c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>Planificación de Jubilación</a>
    <a href="education_planning_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 14l9-5-9-5-9 5 9 5z"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z"/></svg>Planificación Educativa</a>
    <a href="estate_planning_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>Patrimonio y Legado</a>
    <a href="financial_strategy_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>Estrategia Financiera</a>
    <a href="business_strategies_es.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>Estrategias para Negocios</a>
  </div>
</div>

<!-- FULL MENU BOTTOM DRAWER SHEET -->
<div class="mobile-menu-sheet" id="mobileMenuSheet">
  <div class="mms-drag-handle"></div>
  <div class="mms-header">
    <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" class="mms-logo">
    <button class="mms-close" onclick="closeMobileSheets()">✕</button>
  </div>
  <nav class="mms-links">
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'about', 'index_es.html')">Acerca de</a>
    <a href="javascript:void(0)" onclick="toggleMobileServicesSheet()">Servicios <span>▾</span></a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'process', 'index_es.html')">Cómo funciona</a>
    <a href="opportunity_es.html" onclick="closeMobileSheets()">Oportunidad</a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'reviews', 'index_es.html')">Historias</a>
    <a href="javascript:void(0)" onclick="handleMbnClick(event, 'blog', 'index_es.html')">Base de conocimientos</a>
    <div class="mms-lang">
      <a href="index.html">EN</a>
      <a href="index_es.html" class="active">ES</a>
    </div>
    <a href="javascript:void(0)" class="mms-cta-btn" onclick="handleMbnClick(event, 'contact', 'index_es.html')">Consulta Gratuita</a>
  </nav>
</div>

<!-- FLOATING BOTTOM NAVIGATION BAR -->
<nav class="mobile-bottom-nav">
  <a href="javascript:void(0)" class="mbn-item" id="mbn-home" onclick="handleMbnClick(event, 'hero', 'index_es.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Inicio</span>
  </a>
  <button class="mbn-item" id="mbn-services" onclick="toggleMobileServicesSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Servicios</span>
  </button>
  <a href="javascript:void(0)" class="mbn-cta" id="mbn-cta" onclick="handleMbnClick(event, 'contact', 'index_es.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consulta</span>
  </a>
  <a href="javascript:void(0)" class="mbn-item" id="mbn-stories" onclick="handleMbnClick(event, 'reviews', 'index_es.html')">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Historias</span>
  </a>
  <button class="mbn-item" id="mbn-menu" onclick="toggleMobileMenuSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menú</span>
  </button>
</nav>

<script>
function handleMbnClick(e, targetId, homePage) {
  if (e) e.preventDefault();
  closeMobileSheets();
  
  const currentPath = window.location.pathname;
  const isHomePage = currentPath.endsWith(homePage) || (homePage === 'index_es.html' && currentPath.includes('index_es.html')) || (homePage === 'index.html' && (currentPath.endsWith('/') || currentPath.endsWith('/index.html')));

  if (isHomePage) {
    const el = document.getElementById(targetId);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  } else {
    window.location.href = homePage + '#' + targetId;
  }
}

function toggleMobileServicesSheet(e) {
  if(e) e.preventDefault();
  const sheet = document.getElementById('mobileServicesSheet');
  const menuSheet = document.getElementById('mobileMenuSheet');
  const overlay = document.getElementById('mobileSheetOverlay');
  
  menuSheet.classList.remove('open');
  sheet.classList.toggle('open');
  if(sheet.classList.contains('open')) {
    overlay.classList.add('open');
    setActiveMbn('mbn-services');
  } else {
    overlay.classList.remove('open');
  }
}

function toggleMobileMenuSheet(e) {
  if(e) e.preventDefault();
  const menuSheet = document.getElementById('mobileMenuSheet');
  const sheet = document.getElementById('mobileServicesSheet');
  const overlay = document.getElementById('mobileSheetOverlay');
  
  sheet.classList.remove('open');
  menuSheet.classList.toggle('open');
  if(menuSheet.classList.contains('open')) {
    overlay.classList.add('open');
    setActiveMbn('mbn-menu');
  } else {
    overlay.classList.remove('open');
  }
}

function closeMobileSheets() {
  document.getElementById('mobileServicesSheet')?.classList.remove('open');
  document.getElementById('mobileMenuSheet')?.classList.remove('open');
  document.getElementById('mobileSheetOverlay')?.classList.remove('open');
}

function setActiveMbn(id) {
  document.querySelectorAll('.mbn-item').forEach(el => el.classList.remove('active'));
  document.getElementById(id)?.classList.add('active');
}

document.addEventListener('DOMContentLoaded', function() {
  const p = window.location.pathname;
  if (p.includes('family_protection') || p.includes('retirement_planning') || 
      p.includes('education_planning') || p.includes('estate_planning') || 
      p.includes('financial_strategy') || p.includes('business_strategies')) {
    setActiveMbn('mbn-services');
  } else if (p.includes('opportunity')) {
    setActiveMbn('mbn-menu');
  } else {
    setActiveMbn('mbn-home');
  }
});
</script>
"""

def fix_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add pointer-events CSS
    if "pointer-events: none !important;" not in content:
        if "</style>" in content:
            content = content.replace("</style>", CLICK_POINTER_CSS + "\n</style>", 1)

    # 2. Replace bottom nav HTML & JS
    pattern_nav = r'<div class="mobile-sheet-overlay".*?(?=</body>|</html>|\Z)'
    new_nav_html = ES_BOTTOM_NAV_AND_SHEETS if "_es.html" in filename else EN_BOTTOM_NAV_AND_SHEETS

    if re.search(pattern_nav, content, flags=re.DOTALL):
        content = re.sub(pattern_nav, new_nav_html.strip() + "\n", content, flags=re.DOTALL)
    elif "</body>" in content:
        content = content.replace("</body>", new_nav_html.strip() + "\n</body>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed bottom nav click & smooth scroll in {filename}")

def main():
    print("=== Fixing Stories & Bottom Nav Click Events Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        fix_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
