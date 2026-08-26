#!/usr/bin/env python3
"""
build_seamless_mobile_bottom_sheets_and_logo_sync.py
1. Pixel-syncs the header logo position with the mobile menu logo position on mobile screens.
2. Creates interactive mobile bottom sheets:
   - Tapping Services opens a liquid glass Services Popover Drawer listing all 6 services with icons.
   - Tapping Menu slides up a native mobile bottom menu sheet instead of launching the full overlay.
3. Automatically highlights the active icon in the bottom floating nav bar based on scroll position and active page URL.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

UNIFIED_MOBILE_NAV_CSS = """
/* ─────────────────────────────────────────────────────────────
   PIXEL-SYNCED MOBILE HEADER LOGO & FLOATING BOTTOM SHEETS
───────────────────────────────────────────────────────────── */

@media (max-width: 768px) {
  #nav {
    padding: 0 !important;
  }
  #nav > div {
    padding: 18px 24px !important;
    align-items: center !important;
    height: auto !important;
  }
  .nav-logo {
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  .nav-logo img {
    height: 54px !important;
    max-height: 54px !important;
    width: auto !important;
    object-fit: contain !important;
    margin: 0 !important;
  }
  
  .mobile-menu {
    padding: 18px 24px 36px 24px !important;
    justify-content: flex-start !important;
    overflow-y: auto !important;
  }
  .mobile-menu-header {
    margin-top: 0 !important;
    margin-bottom: 24px !important;
    padding-bottom: 16px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
  }
  .mobile-menu-logo {
    height: 54px !important;
    max-height: 54px !important;
    width: auto !important;
    object-fit: contain !important;
    filter: brightness(0) invert(1) !important;
    margin: 0 !important;
  }
}

/* Sheet Overlay Background */
.mobile-sheet-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 898;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.mobile-sheet-overlay.open {
  display: block;
  opacity: 1;
}

/* Floating Services & Menu Sheets */
.mobile-services-sheet,
.mobile-menu-sheet {
  position: fixed;
  bottom: 84px;
  left: 14px;
  right: 14px;
  background: rgba(15, 12, 28, 0.96);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 28px;
  z-index: 900;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.25);
  padding: 20px;
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px) scale(0.95);
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s;
  max-height: 80vh;
  overflow-y: auto;
}

.mobile-services-sheet.open,
.mobile-menu-sheet.open {
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
}

/* Drag Handle Accent */
.mms-drag-handle {
  width: 40px;
  height: 4px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 4px;
  margin: 0 auto 16px auto;
}

.mss-header, .mms-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.mss-title {
  font-family: var(--font-head, sans-serif);
  font-size: 16px;
  font-weight: 700;
  color: #F5D061;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.mms-logo {
  height: 42px;
  width: auto;
  filter: brightness(0) invert(1);
}

.mss-close, .mms-close {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #fff;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.mss-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}

.mss-grid a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  color: #FFFFFF;
  text-decoration: none;
  font-size: 15px;
  font-weight: 600;
  transition: background 0.2s, border-color 0.2s;
}

.mss-grid a:hover, .mss-grid a.active {
  background: rgba(29, 158, 117, 0.2);
  border-color: #1D9E75;
  color: #F5D061;
}

.mss-grid a svg {
  width: 20px;
  height: 20px;
  stroke: #1D9E75;
  flex-shrink: 0;
}

/* Mobile Menu Sheet Links */
.mms-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.mms-links a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.04);
  border-radius: 14px;
  color: #FFFFFF;
  font-size: 16px;
  font-weight: 700;
  text-decoration: none;
}

.mms-links a:hover {
  color: #F5D061;
  background: rgba(255, 255, 255, 0.08);
}

.mms-lang {
  display: flex;
  gap: 10px;
  margin-top: 8px;
}

.mms-lang a {
  flex: 1;
  text-align: center;
  justify-content: center;
  padding: 10px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  color: #fff;
  font-size: 14px;
}

.mms-lang a.active {
  background: #1D9E75;
  color: #fff;
}

.mms-cta-btn {
  background: linear-gradient(135deg, #1D9E75, #4A2D7A) !important;
  color: #fff !important;
  text-align: center;
  justify-content: center !important;
  padding: 14px !important;
  border-radius: 16px !important;
  font-size: 16px !important;
  font-weight: 800 !important;
  margin-top: 6px;
  box-shadow: 0 6px 20px rgba(29, 158, 117, 0.4);
}
"""

EN_MOBILE_BOTTOM_NAV_AND_SHEETS = """
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
    <a href="index.html#about" onclick="closeMobileSheets()">About</a>
    <a href="javascript:void(0)" onclick="toggleMobileServicesSheet()">Services <span>▾</span></a>
    <a href="index.html#process" onclick="closeMobileSheets()">How It Works</a>
    <a href="opportunity.html" onclick="closeMobileSheets()">Opportunity</a>
    <a href="index.html#reviews" onclick="closeMobileSheets()">Stories</a>
    <a href="index.html#blog" onclick="closeMobileSheets()">Knowledgebase</a>
    <div class="mms-lang">
      <a href="index.html" class="active">EN</a>
      <a href="index_es.html">ES</a>
    </div>
    <a href="#contact" class="mms-cta-btn" onclick="closeMobileSheets()">Free Consultation</a>
  </nav>
</div>

<!-- FLOATING BOTTOM NAVIGATION BAR -->
<nav class="mobile-bottom-nav">
  <a href="index.html#hero" class="mbn-item" id="mbn-home">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Home</span>
  </a>
  <button class="mbn-item" id="mbn-services" onclick="toggleMobileServicesSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Services</span>
  </button>
  <a href="#contact" class="mbn-cta" id="mbn-cta">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consult</span>
  </a>
  <a href="index.html#reviews" class="mbn-item" id="mbn-stories">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Stories</span>
  </a>
  <button class="mbn-item" id="mbn-menu" onclick="toggleMobileMenuSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menu</span>
  </button>
</nav>

<script>
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

ES_MOBILE_BOTTOM_NAV_AND_SHEETS = """
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
    <a href="index_es.html#about" onclick="closeMobileSheets()">Acerca de</a>
    <a href="javascript:void(0)" onclick="toggleMobileServicesSheet()">Servicios <span>▾</span></a>
    <a href="index_es.html#process" onclick="closeMobileSheets()">Cómo funciona</a>
    <a href="opportunity_es.html" onclick="closeMobileSheets()">Oportunidad</a>
    <a href="index_es.html#reviews" onclick="closeMobileSheets()">Historias</a>
    <a href="index_es.html#blog" onclick="closeMobileSheets()">Base de conocimientos</a>
    <div class="mms-lang">
      <a href="index.html">EN</a>
      <a href="index_es.html" class="active">ES</a>
    </div>
    <a href="#contact" class="mms-cta-btn" onclick="closeMobileSheets()">Consulta Gratuita</a>
  </nav>
</div>

<!-- FLOATING BOTTOM NAVIGATION BAR -->
<nav class="mobile-bottom-nav">
  <a href="index_es.html#hero" class="mbn-item" id="mbn-home">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
    <span>Inicio</span>
  </a>
  <button class="mbn-item" id="mbn-services" onclick="toggleMobileServicesSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
    <span>Servicios</span>
  </button>
  <a href="#contact" class="mbn-cta" id="mbn-cta">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
    <span>Consulta</span>
  </a>
  <a href="index_es.html#reviews" class="mbn-item" id="mbn-stories">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
    <span>Historias</span>
  </a>
  <button class="mbn-item" id="mbn-menu" onclick="toggleMobileMenuSheet(event)">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <span>Menú</span>
  </button>
</nav>

<script>
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

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS
    pattern_css = r'/\* ─+ \s* PIXEL-SYNCED MOBILE HEADER LOGO & FLOATING BOTTOM SHEETS \s* ─+ \*/.*?(?=</style>|\Z)'
    if re.search(pattern_css, content, flags=re.DOTALL):
        content = re.sub(pattern_css, UNIFIED_MOBILE_NAV_CSS, content, flags=re.DOTALL)
    elif "</style>" in content:
        content = content.replace("</style>", UNIFIED_MOBILE_NAV_CSS + "\n</style>", 1)

    # 2. Replace previous bottom nav html with new unified sheets HTML
    pattern_nav = r'<!-- APP-LIKE FIXED BOTTOM NAVIGATION FOR MOBILE -->.*?(?=</body>|</html>|\Z)'
    new_sheets_html = ES_MOBILE_BOTTOM_NAV_AND_SHEETS if "_es.html" in filename else EN_MOBILE_BOTTOM_NAV_AND_SHEETS

    if re.search(pattern_nav, content, flags=re.DOTALL):
        content = re.sub(pattern_nav, new_sheets_html + "\n", content, flags=re.DOTALL)
    elif "</body>" in content:
        content = content.replace("</body>", new_sheets_html + "\n</body>", 1)
    elif "</html>" in content:
        content = content.replace("</html>", new_sheets_html + "\n</html>", 1)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Synced mobile header logo & bottom sheets in {filename}")

def main():
    print("=== Syncing Mobile Header Logo & Injecting Interactive Bottom Sheets Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
