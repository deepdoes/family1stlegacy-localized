#!/usr/bin/env python3
"""
apply_service_and_legal_pdf_updates.py
Applies service page copy updates, Living Benefits callouts, and legal page enhancements from the client PDF.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def add_living_benefits_callout():
    # 1. English: family_protection.html
    filepath = os.path.join(BASE, "family_protection.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lb_callout_en = """
    <!-- Living Benefits Highlighted Callout -->
    <div style="background:var(--green-lite); border-left:4px solid var(--green); border-radius:16px; padding:32px; margin:40px 0;">
      <h4 style="font-size:20px; font-weight:700; color:var(--green); margin-bottom:12px;">If a serious illness changed your life, would your plan help while you’re still living?</h4>
      <p style="font-size:15px; color:var(--dark); line-height:1.7; margin-bottom:8px;">Some life insurance policies may include living benefits that allow you to access part of the policy’s benefit while you are still alive if you qualify due to a covered illness or condition.</p>
      <span style="font-size:12px; font-style:italic; color:var(--muted);">Benefits vary by policy, rider, carrier, and eligibility.</span>
    </div>
    """
    if "would your plan help while you’re still living" not in content:
        content = content.replace('</section>', lb_callout_en + '\n</section>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✓ Added Living Benefits callout to family_protection.html")

    # 2. Spanish: family_protection_es.html
    filepath_es = os.path.join(BASE, "family_protection_es.html")
    with open(filepath_es, 'r', encoding='utf-8') as f:
        content_es = f.read()

    lb_callout_es = """
    <!-- Living Benefits Highlighted Callout (ES) -->
    <div style="background:var(--green-lite); border-left:4px solid var(--green); border-radius:16px; padding:32px; margin:40px 0;">
      <h4 style="font-size:20px; font-weight:700; color:var(--green); margin-bottom:12px;">Si una enfermedad grave cambiara tu vida, ¿tu plan podría ayudar mientras aún estás vivo?</h4>
      <p style="font-size:15px; color:var(--dark); line-height:1.7; margin-bottom:8px;">Algunas pólizas de seguro de vida pueden incluir beneficios en vida que te permiten acceder a una parte del beneficio de la póliza mientras aún estás vivo, si calificas debido a una enfermedad o condición cubierta.</p>
      <span style="font-size:12px; font-style:italic; color:var(--muted);">Los beneficios varían según la póliza, el rider, la compañía de seguros y la elegibilidad.</span>
    </div>
    """
    if "mientras aún estás vivo" not in content_es:
        content_es = content_es.replace('</section>', lb_callout_es + '\n</section>', 1)
        with open(filepath_es, 'w', encoding='utf-8') as f:
            f.write(content_es)
        print("  ✓ Added Living Benefits callout to family_protection_es.html")


def update_global_footer_disclaimers():
    files = glob.glob(os.path.join(BASE, "*.html"))
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        # Replace Licensed Nationwide -> Serving Families Nationwide
        content = content.replace("Licensed Nationwide", "Serving Families Nationwide")
        content = content.replace("Licenciados a Nivel Nacional", "Sirviendo a familias en todo el país")
        content = content.replace("Licenciado a Nivel Nacional", "Sirviendo a familias en todo el país")

        # Soften footer claims
        content = content.replace("build financial security", "build a stronger financial future")
        content = content.replace("construir seguridad financiera", "construir un futuro financiero más sólido")

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated footer disclaimers on {os.path.basename(filepath)}")


if __name__ == "__main__":
    print("=== Applying Service & Legal PDF Updates ===")
    add_living_benefits_callout()
    update_global_footer_disclaimers()
    print("=== Done! ===")
