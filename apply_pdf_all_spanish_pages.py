#!/usr/bin/env python3
"""
apply_pdf_all_spanish_pages.py
Comprehensive script applying exact Spanish copy from client PDF across all Spanish HTML pages.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_file(filename, replacements):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print(f"  [SKIPPED] {filename} not found.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for old_str, new_str in replacements:
        if old_str in content:
            content = content.replace(old_str, new_str)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filename}")
    else:
        print(f"  - No changes needed for {filename}")

def main():
    print("=== Applying PDF Spanish Wording Across All Inner Pages ===")

    # 1. family_protection_es.html
    update_file("family_protection_es.html", [
        (
            "Trabajas duro todos los días para cuidar de tu familia. ¿Pero qué pasa si no puedes?",
            "Trabajas duro todos los días para cuidar de tu familia. Pero ¿qué pasa si no puedes?"
        ),
        (
            "Pagas la hipoteca. Mantén las luces encendidas. Pones comida en la mesa. El mundo entero de tu familia funciona porque tú apareces, todos los días.",
            "Tú pagas la hipoteca o la renta. Mantienes las luces encendidas. Pones comida en la mesa. Todo el mundo de tu familia funciona porque tú estás presente, todos los días."
        ),
        (
            "Si mis ingresos se detuvieran mañana, por cualquier motivo, ¿por cuánto tiempo mi familia estaría bien?",
            "Si mis ingresos se detuvieran mañana — por cualquier razón — ¿por cuánto tiempo estaría realmente bien mi familia?"
        ),
        (
            "Peligrosamente insuficientemente asegurado",
            "La cobertura del trabajo puede dejar brechas"
        ),
        (
            "Enfrentar la enfermedad antes de la jubilación",
            "Si los ingresos se detienen"
        ),
        (
            "Espera promedio de sucesión",
            "Probate puede retrasar el dinero"
        ),
        (
            "Costo de una revisión",
            "Revisión sin costo"
        ),
        (
            "Las facturas no esperan el papeleo judicial.",
            "Las facturas no esperan los trámites del tribunal."
        ),
        (
            "01 — LA TRAMPA DEL PROBATE",
            "01 — EL RIESGO DEL PROBATE"
        ),
        (
            "01 — LA TRAMPA DE LA SUCESIÓN",
            "01 — EL RIESGO DEL PROBATE"
        ),
        (
            "04 — EL ERROR COSTOSO",
            "04 — EL ERROR QUE PUEDE COSTARLE CARO A TU FAMILIA"
        ),
        (
            "¿Estás listo para asegurar el futuro de tu familia?",
            "Conoce qué protege a tu familia antes de que la vida cambie."
        ),
        (
            "Programa una consulta gratuita hoy: sin presión, sin obligación, solo orientación honesta de profesionales con licencia que realmente se preocupan.",
            "Haz preguntas, revisa tus opciones y decide con claridad, sin presión."
        ),
        (
            "Licenciados a Nivel Nacional",
            "Sirviendo a familias en todo el país"
        ),
        (
            "Tu información se mantiene estrictamente confidencial. Nunca compartimos tus datos.",
            "Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal."
        )
    ])

    # 2. retirement_planning_es.html
    update_file("retirement_planning_es.html", [
        (
            "PLANIFICACIÓN DE JUBILACIÓN",
            "PLANIFICACIÓN PARA LA JUBILACIÓN"
        ),
        (
            "Las reglas de la jubilación han cambiado. ¿Ha adaptado?",
            "Las reglas de la jubilación han cambiado. ¿Te has adaptado?"
        ),
        (
            "Trabajó duro para construir su futuro. Ahora la jubilación puede necesitar más que ahorrar dinero; puede necesitar un plan para ingresos, impuestos, cambios del mercado y la posibilidad de vivir más de lo esperado.",
            "Trabajaste duro para construir tu futuro. Ahora la jubilación puede necesitar más que ahorrar dinero; puede necesitar un plan para ingresos, impuestos, cambios del mercado y la posibilidad de vivir más de lo esperado."
        ),
        (
            "¿Simplemente está ahorrando para la jubilación o se está preparando para la vida que desea vivir?",
            "¿Simplemente estás ahorrando para la jubilación o te estás preparando para la vida que deseas vivir?"
        ),
        (
            "01 — VOLATILIDAD DEL MERCADO",
            "01 — MARKET VOLATILITY"
        ),
        (
            "¿Qué pasa si el mercado cae justo cuando necesita ingresos?",
            "¿Qué pasa si el mercado cae justo cuando necesitas ingresos?"
        ),
        (
            "Las subidas y bajadas del mercado pueden afectar sus ahorros, especialmente cuando está cerca de la jubilación o ya está retirando dinero. Un plan bien pensado puede ayudarle a equilibrar crecimiento, protección, necesidades de ingresos y el nivel de riesgo con el que se sienta cómodo.",
            "Las subidas y bajadas del mercado pueden afectar tus ahorros, especialmente cuando estás cerca de la jubilación o ya estás retirando dinero. Un plan bien pensado puede ayudarte a equilibrar crecimiento, protección, necesidades de ingresos y el nivel de riesgo con el que te sientas cómodo."
        ),
        (
            "02 — LA SORPRESA FISCAL",
            "02 — THE TAX SURPRISE"
        ),
        (
            "¿El IRS forma parte de su plan de jubilación?",
            "¿El IRS forma parte de tu plan de jubilación?"
        ),
        (
            "El dinero que ve en un 401(k) tradicional puede no ser todo suyo para gastar. Los retiros generalmente son gravables más adelante, lo que significa que los impuestos pueden afectar cuánto ingreso de jubilación realmente conserva. Una planificación consciente de los impuestos puede ayudarle a entender sus opciones antes de que comience la jubilación.",
            "El dinero que ves en un 401(k) tradicional puede no ser todo tuyo para gastar. Los retiros generalmente son gravables más adelante, lo que significa que los impuestos pueden afectar cuánto ingreso de jubilación realmente conservas. Una planificación consciente de los impuestos puede ayudarte a entender tus opciones antes de que comience la jubilación."
        ),
        (
            "03 — RIESGO DE LONGEVIDAD",
            "03 — LONGEVITY RISK"
        ),
        (
            "¿Qué pasa si la jubilación dura más de lo que esperaba?",
            "¿Qué pasa si la jubilación dura más de lo que esperabas?"
        ),
        (
            "Vivir más tiempo es una bendición, pero también significa que sus ingresos pueden necesitar durar más. Planificar con anticipación puede ayudarle a pensar en ingresos futuros, costos de salud y estrategias diseñadas para ayudar a mantener su estilo de vida el mayor tiempo posible.",
            "Vivir más tiempo es una bendición, pero también significa que tus ingresos pueden necesitar durar más. Planificar con anticipación puede ayudarte a pensar en ingresos futuros, costos de salud y estrategias diseñadas para ayudar a mantener tu estilo de vida el mayor tiempo posible."
        )
    ])

    # 3. estate_planning_es.html
    update_file("estate_planning_es.html", [
        (
            "Planifica un legado que dura generaciones",
            "Planifica un legado que pueda durar generaciones"
        ),
        (
            "Trabajó duro para construir algo significativo. La planificación patrimonial y de legado puede ayudar a que sus deseos se conozcan claramente, que sus seres queridos estén mejor preparados y que las personas y causas que le importan se beneficien de lo que deja.",
            "Trabajaste duro para construir algo significativo. La planificación patrimonial y de legado puede ayudar a que tus deseos se conozcan claramente, que tus seres queridos estén mejor preparados y que las personas y causas que te importan se beneficien de lo que dejas."
        ),
        (
            "¿Quién decidirá qué pasa con el trabajo de su vida?",
            "¿Quién decidirá qué pasa con el trabajo de tu vida?"
        ),
        (
            "Testamento vs. fideicomiso",
            "Testamento vs. fideicomiso"
        ),
        (
            "Un testamento es una herramienta importante de planificación patrimonial, pero algunos activos aún pueden tener que pasar por probate. Un fideicomiso, cuando está estructurado adecuadamente, puede ayudar a brindar más privacidad, claridad y eficiencia al transferir ciertos activos.",
            "Un testamento es una herramienta importante de planificación patrimonial, pero algunos activos aún pueden tener que pasar por probate. Un fideicomiso, cuando está estructurado adecuadamente, puede ayudar a brindar más privacidad, claridad y eficiencia al transferir ciertos activos."
        ),
        (
            "Protege lo que trabajaste duro para construir",
            "Protege lo que trabajaste duro para construir"
        ),
        (
            "Permite que tus valores continúen a través de las personas que amas",
            "Permite que tus valores continúen a través de las personas que amas"
        )
    ])

    # 4. education_planning_es.html
    update_file("education_planning_es.html", [
        (
            "Dales el mundo sin sacrificar su jubilación",
            "Dales el mundo sin sacrificar tu jubilación"
        ),
        (
            "Los costos de educación siguen aumentando, y la deuda estudiantil puede convertirse en una carga pesada antes de que la próxima generación siquiera comience. Quieres ayudar a tus hijos a perseguir su futuro — universidad, carrera, negocio u otro camino — pero también necesitas proteger el tuyo.",
            "Los costos de educación siguen aumentando, y la deuda estudiantil puede convertirse en una carga pesada antes de que la próxima generación siquiera comience. Quieres ayudar a tus hijos a perseguir su futuro — universidad, carrera, negocio u otro camino — pero también necesitas proteger el tuyo."
        ),
        (
            "Puedes pedir prestado para la universidad, pero no puedes pedir prestado para la jubilación.",
            "Puedes pedir prestado para la universidad, pero no puedes pedir prestado para la jubilación."
        ),
        (
            "01 — THE 529 BLIND SPOT",
            "01 — EL PUNTO CIEGO DEL 529"
        ),
        (
            "¿Qué pasa si el camino de su hijo cambia?",
            "¿Qué pasa si el camino de tu hijo cambia?"
        ),
        (
            "02 — A MORE FLEXIBLE APPROACH",
            "02 — UN ENFOQUE MÁS FLEXIBLE"
        ),
        (
            "La planificación educativa debe ajustarse a la vida real",
            "La planificación educativa debe ajustarse a la vida real"
        ),
        (
            "03 — THEIR FUTURE AND YOURS",
            "03 — SU FUTURO Y EL TUYO"
        ),
        (
            "El futuro de su hijo importa, y su jubilación también",
            "El futuro de tu hijo importa, y tu jubilación también"
        )
    ])

    # 5. financial_strategy_es.html
    update_file("financial_strategy_es.html", [
        (
            "La riqueza no se crea por accidente. Se construye por diseño.",
            "La riqueza no se crea por accidente. Se construye con diseño."
        ),
        (
            "El progreso financiero sólido normalmente viene de decisiones claras, no de adivinar. Las familias pueden beneficiarse al aprender a manejar deudas, construir ahorros, proteger lo que han trabajado y planificar pensando en el futuro.",
            "El progreso financiero sólido normalmente viene de decisiones claras, no de adivinar. Las familias pueden beneficiarse al aprender a manejar deudas, construir ahorros, proteger lo que han trabajado y planificar pensando en el futuro."
        ),
        (
            "¿Tus decisiones financieras te están ayudando a avanzar hacia el futuro que deseas?",
            "¿Tus decisiones financieras te están ayudando a avanzar hacia el futuro que deseas?"
        )
    ])

    print("=== All Inner Pages Successfully Processed ===")

if __name__ == "__main__":
    main()
