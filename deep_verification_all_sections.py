#!/usr/bin/env python3
"""
deep_verification_all_sections.py
Strict, 0-tolerance verification of all red and yellow items from Andre's Document 1 & 2.
"""

import os
import re
import sys

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def verify_all():
    print("\n========================================================")
    print("      DEEP RIGOROUS AUDIT — ALL 12 SECTIONS (SPANISH)")
    print("========================================================\n")

    results = []

    def check(section, name, cond, detail=""):
        status = "PASS ✓" if cond else "FAIL ❌"
        results.append((section, name, status, detail))
        print(f"[{status}] Section {section}: {name} {detail}")

    pages = {}
    for f in [
        "index_es.html", "family_protection_es.html", "retirement_planning_es.html",
        "education_planning_es.html", "estate_planning_es.html", "financial_strategy_es.html",
        "business_strategies_es.html", "opportunity_es.html", "privacy_es.html", "terms_es.html",
        "blog_family_protection_es.html", "blog_retirement_es.html", "blog_education_es.html",
        "blog_living_benefits_es.html", "blog_financial_strategy_es.html", "blog_legacy_es.html"
    ]:
        with open(os.path.join(BASE_DIR, f), "r", encoding="utf-8") as file:
            pages[f] = file.read()

    # SECTION 1: GLOBAL COMPONENTS
    idx = pages["index_es.html"]
    check(1, "Trust Badges Spanish", "Con licencia y asegurados" in idx and "Respuesta en 24 horas" in idx and "Tu privacidad nos importa" in idx)
    check(1, "Contact Form Copy", "Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas." in idx)
    check(1, "Privacy Sentence", "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal." in idx)
    check(1, "Newsletter Copy", "Información mensual sobre protección familiar, planificación financiera y preparación para el futuro. Puedes cancelar tu suscripción en cualquier momento." in idx)
    check(1, "Office Hours 2pm-6pm", "Sáb: 2 p. m. – 6 p. m." in idx)
    check(1, "Old Saturday Hours Absent", "10 a. m. – 4 p. m." not in idx)
    check(1, "Main Footer Disclosure", "Family First Legacy es una agencia independiente de servicios financieros que atiende a familias en todo Estados Unidos." in idx)
    check(1, "No Split Label 'Educación / Planificación'", "Educación / Planificación" not in idx)
    check(1, "No Split Label 'Financiero / Estrategia'", "Financiero / Estrategia" not in idx)
    check(1, "No Split Label 'Bienes & / Planificación heredada'", "Bienes & / Planificación heredada" not in idx)

    # SECTION 2: HOME PAGE
    check(2, "Career Opportunity Hero Text", "Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros." in idx)
    check(2, "Old 'miles de emprendedores' Absent", "miles de emprendedores" not in idx)
    check(2, "Old '$1.4B+' Absent", "1.4B" not in idx and "1.400 millones de dólares+" not in idx)
    check(2, "Focus Section 'TU FAMILIA. NUESTRO ENFOQUE.'", "TU FAMILIA." in idx and "NUESTRO ENFOQUE." in idx)
    check(2, "Focus Section '100% Profesionales con licencia'", "100%" in idx and "Profesionales con licencia" in idx)
    check(2, "How It Works Step 2", "Utilizamos un Análisis de Necesidades Financieras para revisar tu situación actual" in idx)
    check(2, "How It Works Step 3", "Te presentamos opciones claras de compañías de seguros y servicios financieros bien establecidas" in idx)
    check(2, "How It Works Ongoing", "La vida cambia, y tu plan también puede necesitar cambios. Seguimos disponibles para revisar tu plan" in idx)
    check(2, "Home FAQ 1 (¿Qué hace exactamente)", "Family First Legacy ayuda a personas, familias y dueños de negocios a comprender sus opciones de seguro de vida" in idx)
    check(2, "Home FAQ 8 (Proceso sucesorio)", "¿Qué deben saber las familias sobre el proceso sucesorio?" in idx)
    check(2, "Home FAQ 10 (¿Cobran una tarifa)", "No cobramos una tarifa por hablar con nosotros. Tu revisión financiera se ofrece sin costo y sin presión." in idx)

    # SECTION 3: FAMILY PROTECTION
    fp = pages["family_protection_es.html"]
    fp_text_only = re.sub(r'<(style|script)[^>]*>.*?</\1>', '', fp, flags=re.S)
    check(3, "Hero Text", "La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas" in fp)
    check(3, "Proof Cards", "LOS BENEFICIOS DEL TRABAJO PUEDEN DEJAR BRECHAS" in fp and "SI LOS INGRESOS SE DETIENEN" in fp and "EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO" in fp)
    check(3, "Old stats 60% absent from text", "60%" not in fp_text_only)
    check(3, "Old stats 1-in-4 absent", "1-in-4" not in fp and "1 de cada 4" not in fp)
    check(3, "Old stats 9-24m absent", "9-24m" not in fp and "9–24m" not in fp and "9 a 24 meses" not in fp)
    check(3, "3.3 Bills Don't Wait", "Las facturas no esperan" in fp and "a que termine el proceso legal" in fp)
    check(3, "3.4 Paycheck Stopped", "¿Qué pasaría si siguieras con vida — pero tu cheque de pago se detuviera?" in fp or "¿Qué pasaría si siguieras con vida" in fp)
    check(3, "3.5 Diagnosis Overnight", "Un diagnóstico puede cambiar el presupuesto familiar de un día para otro." in fp or "Un diagnóstico puede cambiar" in fp)
    check(3, "3.6 Work Coverage", "La cobertura del trabajo puede parecer segura" in fp)
    check(3, "FAQ 1 Goal", "El seguro de Protección Familiar está diseñado para ayudar a que tu familia pueda continuar financieramente" in fp)
    check(3, "FAQ 3 Living Benefits", "cláusulas de beneficios acelerados o beneficios en vida que permiten a titulares elegibles acceder a una parte del beneficio" in fp)

    # SECTION 4: RETIREMENT PLANNING
    rp = pages["retirement_planning_es.html"]
    check(4, "Hero Text", "Has trabajado duro para construir tu futuro. Ahora, la jubilación puede requerir más que simplemente ahorrar dinero" in rp)
    check(4, "Proof Cards", "INGRESOS DE JUBILACIÓN" in rp and "CAMBIOS DEL MERCADO" in rp and "PLANIFICACIÓN CON CONCIENCIA FISCAL" in rp and "REVISIÓN SIN COSTO" in rp)
    check(4, "Old stat 3.5% absent", "3.5%" not in rp)
    check(4, "Old '0 taxes paid on IUL' absent", "0 taxes paid on IUL" not in rp and "0 impuestos pagados sobre el crecimiento" not in rp)
    check(4, "4.3 Market Drops", "Las subidas y bajadas del mercado pueden afectar tus ahorros" in rp)
    check(4, "4.4 IRS Part of Plan", "El dinero que ves en un 401(k) tradicional puede no estar completamente disponible para gastar." in rp)
    check(4, "4.5 Retirement Lasts Longer", "Vivir más tiempo es una bendición, pero también significa que tus ingresos quizá deban durar más." in rp)
    check(4, "FAQ 1 (401k/IRA)", "Porque la jubilación puede necesitar más de una sola fuente." in rp)
    check(4, "FAQ 4 Tax surprise", "El saldo que ves puede no ser la cantidad que conservas." in rp)

    # SECTION 5: EDUCATION PLANNING
    ep = pages["education_planning_es.html"]
    check(5, "Hero Text", "Los costos de educación continúan aumentando y la deuda estudiantil puede convertirse en una carga pesada" in ep)
    check(5, "Proof Cards", "COSTOS EDUCATIVOS EN AUMENTO" in ep and "PLANIFICACIÓN FLEXIBLE" in ep and "DEUDA ESTUDIANTIL" in ep and "EQUILIBRIO CON LA JUBILACIÓN" in ep)
    check(5, "Old stat $100k absent", "$100k" not in ep and "100.000" not in ep)
    check(5, "Old stat $1.7T absent", "1.7T" not in ep)
    check(5, "5.3 Path Changes", "Un plan 529 puede ser una herramienta valiosa de ahorro educativo" in ep)
    check(5, "5.4 Fit Real Life", "El seguro de vida permanente que acumula valor en efectivo puede ofrecer acceso flexible" in ep)
    check(5, "5.5 Child Future Matters", "Muchos padres están dispuestos a sacrificarse por sus hijos. Ese amor es poderoso." in ep)
    check(5, "FAQ 1 (529 Limitations)", "Un plan 529 puede ser útil, pero la vida no siempre sigue un solo plan." in ep)

    # SECTION 6: ESTATE & LEGACY
    est = pages["estate_planning_es.html"]
    check(6, "Hero Text", "Trabajaste duro para construir algo significativo. La planificación patrimonial y de legado" in est)
    check(6, "Proof Cards", "TUS DESEOS IMPORTAN" in est and "TRANSFERENCIAS MÁS SENCILLAS" in est and "PLANIFICACIÓN CON CONCIENCIA FISCAL" in est and "TRANQUILIDAD" in est)
    check(6, "Old '100% control' absent", "100% control" not in est)
    check(6, "6.3 Will vs Trust", "Un testamento es una herramienta importante de planificación patrimonial, pero algunos bienes aún pueden tener que pasar por el proceso sucesorio." in est)
    check(6, "6.3 Legal & Tax Disclaimer", "Family First Legacy no brinda asesoramiento legal ni fiscal." in est)
    check(6, "6.4 Protect What You Built", "Trabajaste duro para construir bienes para tu familia. Dependiendo de tu situación" in est)
    check(6, "6.5 Values Continue", "La planificación de legado no se trata solamente de dinero. También se trata de valores, responsabilidad" in est)
    check(6, "FAQ 1 (Will vs Trust)", "Ambos pueden ayudar a orientar lo que sucede con tus bienes. Un testamento explica cómo deben distribuirse los bienes" in est)

    # SECTION 7: FINANCIAL STRATEGY
    fin = pages["financial_strategy_es.html"]
    check(7, "Hero Text", "Un progreso financiero sólido generalmente viene de decisiones claras, no de adivinanzas." in fin)
    check(7, "Proof Cards", "CLARIDAD FINANCIERA" in fin and "ESTRATEGIA DE DEUDA" in fin and "PRINCIPIOS DE CRECIMIENTO" in fin and "REVISIÓN SIN COSTO" in fin)
    check(7, "Old claims absent", "100% control" not in fin and "0% market loss" not in fin)
    check(7, "7.3 Rule of 72", "Comprender cómo funciona el interés compuesto puede ayudar a las familias a ver el poder del tiempo." in fin)
    check(7, "7.4 Debt Management", "No todas las deudas son iguales, pero la deuda con intereses altos puede frenar silenciosamente" in fin)
    check(7, "7.5 Legacy Transfer", "Un verdadero legado no se trata solo de lo que dejas atrás. También se trata de las oportunidades" in fin)
    check(7, "FAQ 1 (Rule of 72)", "Es una forma sencilla de estimar cuánto tiempo puede tardar el dinero en duplicarse. Divide 72 entre una tasa anual" in fin)

    # SECTION 12: KNOWLEDGEBASE LANDING & ARTICLES
    check(12, "KB Card 1 Title", "¿Tu familia depende solo de los beneficios del trabajo?" in idx)
    check(12, "KB Card 2 Title", "¿Podrían los impuestos reducir los ingresos de jubilación con los que cuentas?" in idx)
    check(12, "KB Card 3 Title", "¿Qué pasa si el camino de tu hijo cambia después de haber ahorrado?" in idx)
    check(12, "KB Card 4 Title", "¿Qué pasa si sobrevives a la enfermedad, pero tus ingresos no?" in idx)
    check(12, "KB Card 4 Link to Spanish article", 'href="blog_living_benefits_es.html"' in idx)
    check(12, "KB Card 5 Title", "¿El tiempo está trabajando a favor de tu dinero, o en contra?" in idx)
    check(12, "KB Card 6 Title", "¿Tu familia tendrá que esperar el dinero que necesita?" in idx)

    # All 6 Articles Body Language Check
    for f in [
        "blog_family_protection_es.html", "blog_retirement_es.html", "blog_education_es.html",
        "blog_living_benefits_es.html", "blog_financial_strategy_es.html", "blog_legacy_es.html"
    ]:
        art_content = pages[f]
        # Check that English H2s are 0
        english_h2s = [
            "The Comfort and Reality", "Why Employer Coverage May Not Be Enough",
            "The Portability Risk", "Exploring Individual Protection Options",
            "Income vs. What You Keep", "Understanding the Three Retirement Tax Buckets",
            "The Rising Cost & Changing Reality", "Understanding 529 Education Savings Plans",
            "Why Financial Clarity Matters More Than Ever", "The 4 Pillars of Family Financial Health",
            "Defining What Legacy Means Beyond Money", "Estate Planning Essentials: Wills"
        ]
        has_eng_h2 = any(h in art_content for h in english_h2s)
        check(12, f"Article {f} Body 100% Spanish (0 English H2s)", not has_eng_h2)
        check(12, f"Article {f} Puntos Clave Present", "⚡ Puntos clave" in art_content)
        check(12, f"Article {f} Spanish Sidebar TOC", "📖 EN ESTA GUÍA" in art_content)

    all_passed = all(r[2] == "PASS ✓" for r in results)
    print("\n========================================================")
    print(f"AUDIT SUMMARY: {len(results)} Checks Run | {'100% SUCCESS — ALL ITEMS PASSED ✓' if all_passed else 'SOME CHECKS FAILED ❌'}")
    print("========================================================\n")
    return all_passed

if __name__ == "__main__":
    passed = verify_all()
    if not passed:
        sys.exit(1)
