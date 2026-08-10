#!/usr/bin/env python3
"""
sync_reviews_light_layout.py
Syncs the exact light dashboard layout of the #reviews section from index.html to index_es.html.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def main():
    index_path = os.path.join(BASE, "index.html")
    index_es_path = os.path.join(BASE, "index_es.html")

    with open(index_path, 'r', encoding='utf-8') as f:
        en_content = f.read()

    # Extract #reviews section from index.html
    reviews_match = re.search(r'(<!-- REAL QUESTIONS & CLEAR GUIDANCE ────────────────── -->.*?<\/section>)', en_content, flags=re.DOTALL)
    if not reviews_match:
        print("Error: Could not find #reviews section in index.html")
        return

    en_reviews_html = reviews_match.group(1)

    # Translate English strings to Spanish for index_es.html
    es_reviews_html = en_reviews_html
    es_reviews_html = es_reviews_html.replace('REAL QUESTIONS', 'PREGUNTAS REALES')
    es_reviews_html = es_reviews_html.replace('Real Questions.<br><em>Clear Guidance.</em>', 'Preguntas reales.<br><em>Orientación clara.</em>')
    es_reviews_html = es_reviews_html.replace('Families do not always come to us with perfect plans. Many come with questions, concerns, and uncertainty. Our role is to help them understand their options clearly, so they can make decisions with confidence.', 'Las familias no siempre llegan a nosotros con planes perfectos. Muchas vienen con preguntas, preocupaciones e incertidumbre. Nuestro papel es ayudarlas a entender sus opciones con claridad para que puedan tomar decisiones con confianza.')

    # Selectors List Translation
    es_reviews_html = es_reviews_html.replace('01 • Family Protection', '01 • Protección familiar')
    es_reviews_html = es_reviews_html.replace('“If my income stopped tomorrow...”', '“Si mis ingresos se detuvieran mañana...”')
    es_reviews_html = es_reviews_html.replace('Guidance with care', 'Orientación con cuidado')

    es_reviews_html = es_reviews_html.replace('02 • Living Benefits', '02 • Beneficios en vida')
    es_reviews_html = es_reviews_html.replace('“If illness stopped my income...”', '“Si una enfermedad detuviera mis ingresos...”')
    es_reviews_html = es_reviews_html.replace('Living benefits guidance', 'Orientación sobre beneficios en vida')

    es_reviews_html = es_reviews_html.replace('03 • Retirement Planning', '03 • Planificación de jubilación')
    es_reviews_html = es_reviews_html.replace('“Preparing or just hoping?”', '“¿Preparándome o solo esperando?”')
    es_reviews_html = es_reviews_html.replace('Retirement guidance', 'Orientación de jubilación')

    es_reviews_html = es_reviews_html.replace('04 • Business Strategies', '04 • Estrategias para negocios')
    es_reviews_html = es_reviews_html.replace('“What happens to my business?”', '“¿Qué pasa con mi negocio?”')
    es_reviews_html = es_reviews_html.replace('Business protection', 'Protección del negocio')

    es_reviews_html = es_reviews_html.replace('05 • Education Planning', '05 • Planificación educativa')
    es_reviews_html = es_reviews_html.replace('“Help my children with fewer limits?”', '“¿Ayudar a mis hijos con menos límites?”')
    es_reviews_html = es_reviews_html.replace('Education guidance', 'Orientación educativa')

    es_reviews_html = es_reviews_html.replace('06 • Legacy Planning', '06 • Planificación de legado')
    es_reviews_html = es_reviews_html.replace('“Will my family have clarity?”', '“¿Mi familia tendrá claridad?”')
    es_reviews_html = es_reviews_html.replace('Legacy planning', 'Planificación de legado')

    # Slides Full Content Translation
    es_reviews_html = es_reviews_html.replace('01 of 06 • FAMILY PROTECTION', '01 de 06 • PROTECCIÓN FAMILIAR')
    es_reviews_html = es_reviews_html.replace('“If my income stopped tomorrow, how long would my family be okay?”', '“Si mis ingresos se detuvieran mañana, ¿por cuánto tiempo estaría bien mi familia?”')
    es_reviews_html = es_reviews_html.replace('Many families have some coverage through work, but they are not sure if it is enough — or if it would stay with them if life changed. A simple review can help identify possible gaps, explain available protection options, and help families understand what may fit their needs, budget, and responsibilities.', 'Muchas familias tienen cierta cobertura a través del trabajo, pero no están seguras de si es suficiente o si permanecería con ellas si la vida cambiara. Una revisión sencilla puede ayudar a identificar posibles brechas, explicar opciones de protección disponibles y ayudar a las familias a entender qué puede ajustarse a sus necesidades, presupuesto y responsabilidades.')

    es_reviews_html = es_reviews_html.replace('02 of 06 • LIVING BENEFITS', '02 de 06 • BENEFICIOS EN VIDA')
    es_reviews_html = es_reviews_html.replace('“What if I survive the illness — but my income does not?”', '“¿Qué pasa si sobrevivo a la enfermedad, pero mis ingresos no?”')
    es_reviews_html = es_reviews_html.replace('A serious illness can affect more than health. It can affect income, bills, and the whole household. Some life insurance policies may include living benefits that can help provide support if someone qualifies due to a covered critical, chronic, or terminal illness.', 'Una enfermedad grave puede afectar más que la salud. Puede afectar los ingresos, las facturas y todo el hogar. Algunas pólizas de seguro de vida pueden incluir beneficios en vida que pueden ayudar a brindar apoyo si alguien califica debido a una enfermedad crítica, crónica o terminal cubierta.')

    es_reviews_html = es_reviews_html.replace('03 of 06 • RETIREMENT PLANNING', '03 de 06 • PLANIFICACIÓN DE JUBILACIÓN')
    es_reviews_html = es_reviews_html.replace('“Am I preparing for retirement — or just hoping it works out?”', '“¿Me estoy preparando para la jubilación, o solo espero que todo salga bien?”')
    es_reviews_html = es_reviews_html.replace('Many hardworking families save what they can, but still wonder if they are doing enough. Clear guidance can help them understand retirement options, possible risks, and steps that may support their long-term goals.', 'Muchas familias trabajadoras ahorran lo que pueden, pero aún se preguntan si están haciendo lo suficiente. Una orientación clara puede ayudarles a entender opciones de jubilación, posibles riesgos y pasos que pueden apoyar sus metas a largo plazo.')

    es_reviews_html = es_reviews_html.replace('04 of 06 • BUSINESS STRATEGIES', '04 de 06 • ESTRATEGIAS PARA NEGOCIOS')
    es_reviews_html = es_reviews_html.replace('“If something happened to me, what would happen to the business I built?”', '“Si algo me pasara, ¿qué ocurriría con el negocio que construí?”')
    es_reviews_html = es_reviews_html.replace('Business owners carry responsibility for their family, employees, clients, and years of hard work. We help them understand protection options, including key-person coverage and business planning strategies that may strengthen their overall plan.', 'Los dueños de negocios cargan responsabilidad por su familia, empleados, clientes y años de trabajo duro. Les ayudamos a entender opciones de protección, incluyendo cobertura para personas clave y estrategias de planificación empresarial que pueden fortalecer su plan general.')

    es_reviews_html = es_reviews_html.replace('05 of 06 • EDUCATION PLANNING', '05 de 06 • PLANIFICACIÓN EDUCATIVA')
    es_reviews_html = es_reviews_html.replace('“How can I help my children pursue education with fewer financial limits?”', '“¿Cómo puedo ayudar a mis hijos a seguir su educación con menos límites financieros?”')
    es_reviews_html = es_reviews_html.replace('Many parents want to support their children’s future, but they are not sure which education planning option gives the right balance of growth, flexibility, and control. Clear guidance can help families understand choices that may fit their goals.', 'Muchos padres quieren apoyar el futuro de sus hijos, pero no están seguros de qué opción de planificación educativa ofrece el equilibrio adecuado de crecimiento, flexibilidad y control. Una orientación clara puede ayudar a las familias a entender opciones que puedan ajustarse a sus metas.')

    es_reviews_html = es_reviews_html.replace('06 of 06 • LEGACY PLANNING', '06 de 06 • PLANIFICACIÓN DE LEGADO')
    es_reviews_html = es_reviews_html.replace('“Will my family receive clarity and support — or be left searching for help?”', '“¿Mi familia recibirá claridad y apoyo, o quedará buscando ayuda?”')
    es_reviews_html = es_reviews_html.replace('Some families want to leave more than money. They want to leave direction, support, and a meaningful legacy for the people they love. A thoughtful plan can help reduce confusion and help loved ones know what to do next.', 'Algunas familias desean dejar más que dinero. Quieren dejar dirección, apoyo y un legado significativo para las personas que aman. Un plan bien pensado puede ayudar a reducir la confusión y ayudar a los seres queridos a saber qué hacer después.')

    es_reviews_html = es_reviews_html.replace('Start with a Simple Review', 'Comienza con una revisión sencilla')
    es_reviews_html = es_reviews_html.replace('These examples are for educational purposes and show common concerns families may face. Individual needs, eligibility, and results may vary.', 'Estos ejemplos son solo para fines educativos y muestran preocupaciones comunes que las familias pueden enfrentar. Las necesidades, elegibilidad y resultados individuales pueden variar.')

    with open(index_es_path, 'r', encoding='utf-8') as f:
        es_content = f.read()

    # Replace #reviews section in index_es.html
    es_pattern = r'(<!-- ── REAL QUESTIONS. CLEAR GUIDANCE. SECTION \(ES\) ── -->.*?<\/section>)'
    if re.search(es_pattern, es_content, flags=re.DOTALL):
        new_es_content = re.sub(es_pattern, es_reviews_html, es_content, flags=re.DOTALL)
    else:
        es_pattern2 = r'(<section id="reviews".*?<\/section>)'
        new_es_content = re.sub(es_pattern2, es_reviews_html, es_content, flags=re.DOTALL)

    with open(index_es_path, 'w', encoding='utf-8') as f:
        f.write(new_es_content)

    print("  ✓ Successfully synced light Real Questions dashboard layout to index_es.html!")

if __name__ == "__main__":
    main()
