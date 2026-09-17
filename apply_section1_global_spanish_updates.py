#!/usr/bin/env python3
"""
apply_section1_global_spanish_updates.py
Refined script applying Section 1 (Global Shared Components) updates across all active Spanish HTML files:
- Trust Badges: Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa
- Contact Form Sentence: Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas.
- Privacy Sentence: Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal.
- Newsletter Subtitle: Información mensual sobre protección familiar, planificación financiera y preparación para el futuro. Puedes cancelar tu suscripción en cualquier momento.
- Main Footer Disclosure: Official 2026 Spanish legal agency disclosure.
- Office Hours: Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m.
- Service Labels Cleanup: Ensures natural Spanish service titles on cards and badges.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

TRUST_BADGES_NEW = "Con licencia y asegurados • Respuesta en 24 horas • Tu privacidad nos importa"
CONTACT_FORM_SENTENCE_NEW = "Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas."
PRIVACY_SENTENCE_NEW = "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal."
NEWSLETTER_NEW = "Información mensual sobre protección familiar, planificación financiera y preparación para el futuro. Puedes cancelar tu suscripción en cualquier momento."
FOOTER_DISCLOSURE_NEW = "Family First Legacy es una agencia independiente de servicios financieros que atiende a familias en todo Estados Unidos. Los productos de seguros y financieros son ofrecidos por profesionales debidamente licenciados y están sujetos a la aprobación de la compañía, la disponibilidad del producto, la evaluación de suscripción y los requisitos estatales aplicables. No brindamos asesoramiento fiscal ni legal; para esos asuntos, consulta a un profesional calificado. La elegibilidad individual, la disponibilidad de productos, las características de las pólizas y los resultados pueden variar."
OFFICE_HOURS_NEW = "Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m."

def update_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content

    # 1.1 Trust Badges
    content = re.sub(
        r'Con licencia y asegurados\s*•.*?(?=</div>|</p>|<span|\n)',
        TRUST_BADGES_NEW,
        content
    )
    content = re.sub(
        r'Licensed & Insured\s*•\s*24hr Response\s*•\s*Your Privacy Matters',
        TRUST_BADGES_NEW,
        content
    )

    # 1.2 Contact Form Subtitle
    content = re.sub(
        r'<div class="cf-sub">.*?</div>',
        f'<div class="cf-sub">{CONTACT_FORM_SENTENCE_NEW}</div>',
        content,
        flags=re.DOTALL
    )

    # 1.3 Privacy Sentence (below form)
    content = re.sub(
        r'<p class="form-privacy">.*?</p>',
        f'<p class="form-privacy"><svg viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>{PRIVACY_SENTENCE_NEW}</p>',
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'Tu información se procesa con cuidado y nunca se vende\.',
        PRIVACY_SENTENCE_NEW,
        content
    )

    # 1.4 Newsletter Subtitle
    content = re.sub(
        r'Perspectivas mensuales sobre protección familiar.*?(?=</p>|</div>)',
        NEWSLETTER_NEW,
        content
    )
    content = re.sub(
        r'Información mensual sobre protección familiar.*?(?=</p>|</div>)',
        NEWSLETTER_NEW,
        content
    )

    # 1.5 Main Footer Disclosure
    content = re.sub(
        r'<div class="fb-disclosure"[^>]*>.*?</div>',
        f'<div class="fb-disclosure" style="margin-top: 14px; font-size: 11px; color: rgba(255,255,255,0.4); line-height: 1.6; font-weight: 300; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 12px; max-width: 100%;">{FOOTER_DISCLOSURE_NEW}</div>',
        content,
        flags=re.DOTALL
    )

    # 1.7 Office Hours
    content = re.sub(
        r'<div class="ci-val">Lunes a viernes:.*?(?=</div>)',
        f'<div class="ci-val">{OFFICE_HOURS_NEW}</div>',
        content
    )
    content = re.sub(
        r'<div class="ci-val">Mon–Fri:.*?(?=</div>)',
        f'<div class="ci-val">{OFFICE_HOURS_NEW}</div>',
        content
    )

    # 1.0 Label Cleanup (Service Card Badges)
    content = content.replace("Educación / Planificación", "Planificación Educativa")
    content = content.replace("Financiero / Estrategia", "Estrategia Financiera")
    content = content.replace("Bienes & / Planificación heredada", "Planificación Patrimonial y de Legado")
    content = content.replace("Negocios / Estrategias", "Estrategias para Negocios")

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Updated Section 1 global elements in {os.path.basename(fpath)}")

def main():
    print("=== Refining Section 1 (Global Shared Components) Updates ===")
    spanish_files = [f for f in os.listdir(BASE) if f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]
    for fname in sorted(spanish_files):
        update_file(os.path.join(BASE, fname))
    print("=== Done! ===")

if __name__ == "__main__":
    main()
