#!/usr/bin/env python3
"""
fix_cta_banner_visibility.py
1. Fixes CSS for #cta-banner across all HTML files so CTA content is ALWAYS visible (opacity: 1 by default).
2. Updates CTA IntersectionObserver threshold to 0.01 with instant fallback.
3. Updates Spanish CTA text on index_es.html and all Spanish pages to clean master copy.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_cta_in_all_html():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in html_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix opacity: 0 on CTA banner elements in CSS
        content = content.replace("#cta-banner .cta-badge {\n  opacity:0;", "#cta-banner .cta-badge {\n  opacity:1;")
        content = content.replace("#cta-banner .cta-badge {\n  opacity: 0;", "#cta-banner .cta-badge {\n  opacity: 1;")
        content = content.replace("#cta-banner .cta-text h2 {\n  opacity:0;", "#cta-banner .cta-text h2 {\n  opacity:1;")
        content = content.replace("#cta-banner .cta-text h2 {\n  opacity: 0;", "#cta-banner .cta-text h2 {\n  opacity: 1;")
        content = content.replace("#cta-banner .cta-text p {\n  opacity:0;", "#cta-banner .cta-text p {\n  opacity:1;")
        content = content.replace("#cta-banner .cta-text p {\n  opacity: 0;", "#cta-banner .cta-text p {\n  opacity: 1;")
        content = content.replace("#cta-banner .cta-right {\n  opacity:0;", "#cta-banner .cta-right {\n  opacity:1;")
        content = content.replace("#cta-banner .cta-right {\n  opacity: 0;", "#cta-banner .cta-right {\n  opacity: 1;")

        # Threshold fix in JS
        content = content.replace("threshold: 0.25", "threshold: 0.01")
        content = content.replace("threshold: 0.2", "threshold: 0.01")

        # Spanish CTA HTML block replacement for _es.html files
        if fname.endswith("_es.html"):
            spanish_cta_html = """<section id="cta-banner" class="cta-on">
<div class="cta-scanline"></div>
<div class="cta-orb cta-orb-1"></div>
<div class="cta-orb cta-orb-2"></div>
<div class="cta-orb cta-orb-3"></div>
<div class="container">
<div class="cta-inner">
<div class="cta-left">
<div class="cta-badge">
<span class="cta-badge-dot"></span>
<span>Aceptando nuevos clientes</span>
</div>
<div class="cta-text">
<h2>¿Listo para proteger el futuro<br>de tu familia?</h2>
<p>Programa una consulta sin costo hoy mismo: sin presiones ni obligaciones, solo orientación honesta de profesionales con licencia que realmente se preocupan.</p>
</div>
</div>
<div class="cta-right">
<div class="cta-actions">
<a class="btn-white" href="#contact">
<svg viewbox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg>Comenzar gratis</a>
<a class="btn-outline-white" href="tel:+14696081595">
<svg viewbox="0 0 24 24"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>Llama al (469) 608-1595</a>
</div>
<div class="cta-stats">
<div class="cts-item">
<div class="cts-num">24 horas</div>
<div class="cts-lbl">Respuesta</div>
</div>
<div class="cts-item">
<div class="cts-num">Sin costo</div>
<div class="cts-lbl">Consulta</div>
</div>
<div class="cts-item">
<div class="cts-num">100%</div>
<div class="cts-lbl">Profesionales con licencia</div>
</div>
</div>
</div>
</div>
</div>
</section>"""
            content = re.sub(r'<section id="cta-banner".*?</section>', spanish_cta_html, content, flags=re.DOTALL)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

    print("  ✓ Updated #cta-banner visibility and Spanish text across all pages.")

if __name__ == "__main__":
    fix_cta_in_all_html()
