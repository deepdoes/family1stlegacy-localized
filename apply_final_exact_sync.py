#!/usr/bin/env python3
"""
apply_final_exact_sync.py
Applies the remaining exact master strings to ensure 100% test pass.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def sync_index():
    fpath = os.path.join(BASE, "index_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Career Hero text
    old_career = "Aprende cómo construir un negocio exitoso en la industria financiera con horarios flexibles, mentoría y la oportunidad de ayudar a familias en tu comunidad."
    target_career = "Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer hasta trabajar a tiempo completo, con capacitación, mentoría y apoyo durante el proceso. Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más les importa."
    content = content.replace(old_career, target_career)

    # Proof section headline
    content = content.replace("YOUR FAMILY. OUR FOCUS.", "TU FAMILIA. NUESTRO ENFOQUE.")
    content = content.replace("Tu Familia. Nuestro Enfoque.", "TU FAMILIA. NUESTRO ENFOQUE.")
    content = content.replace("Tu familia. Nuestro enfoque.", "TU FAMILIA. NUESTRO ENFOQUE.")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Synced index_es.html final strings")

def sync_estate():
    fpath = os.path.join(BASE, "estate_planning_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace("LOS BENEFICIOS DEL TRABAJO PUEDEN DEJAR BRECHAS", "TUS DESEOS IMPORTAN")
    content = content.replace("SI LOS INGRESOS SE DETIENEN", "TRANSFERENCIAS MÁS SENCILLAS")
    content = content.replace("EL PROCESO SUCESORIO PUEDE RETRASAR EL DINERO", "PLANIFICACIÓN CON CONCIENCIA FISCAL")
    content = content.replace("REVISIÓN SIN COSTO", "TRANQUILIDAD")

    content = content.replace("Testamento vs. Fideicomiso", "Testamento vs. fideicomiso")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Synced estate_planning_es.html final strings")

def sync_business():
    fpath = os.path.join(BASE, "business_strategies_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    target_para = "Sin un plan claro, la salida, fallecimiento o incapacidad de un propietario puede crear confusión entre socios, familiares, empleados y prestamistas. Un acuerdo buy-sell financiado puede ayudar a proporcionar una forma estructurada para que los propietarios restantes compren la participación de un propietario a un precio justo, al mismo tiempo que ayuda a proteger los intereses de la familia. Trabaja con profesionales legales y fiscales calificados al establecer acuerdos o determinar el tratamiento fiscal."
    content = re.sub(r'un acuerdo de compra-venta respaldado por seguro de vida.*?(?=</p>)', target_para, content, flags=re.DOTALL)
    if "Sin un plan claro" not in content:
        content = content.replace("Un acuerdo de compra-venta financiado", target_para)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Synced business_strategies_es.html final strings")

def sync_blog4():
    fpath = os.path.join(BASE, "blog_living_benefits_es.html")
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    content = content.replace('placeholder="Ingresa tu correo electrónico electrónico"', 'placeholder="Ingresa tu correo electrónico"')
    content = content.replace('>Suscribir<', '>SUSCRIBIRME<')
    content = content.replace('>Suscribirse<', '>SUSCRIBIRME<')

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Synced blog_living_benefits_es.html final strings")

def main():
    sync_index()
    sync_estate()
    sync_business()
    sync_blog4()

if __name__ == "__main__":
    main()
