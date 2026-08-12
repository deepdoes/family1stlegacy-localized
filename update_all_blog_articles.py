#!/usr/bin/env python3
"""
update_all_blog_articles.py
Updates all 5 existing blog articles (English & Spanish) with the compliance-conscious,
family-focused copy from PDF Pages 76–101, and creates the 6th article (Living Benefits).
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

ARTICLES_ES = {
    "blog_family_protection_es.html": {
        "title": "¿Tu familia depende solo de los beneficios del trabajo?",
        "meta_desc": "El seguro de vida del empleador puede ser un beneficio útil, pero puede dejar brechas cuando la vida cambia o el empleo termina.",
        "badge": "Protección familiar",
        "read_time": "Lectura de 5 minutos",
        "hero_img": "images/hero_life_insurance_diverse_1777335713599.png",
        "body": """<p>El seguro de vida del empleador puede ser un beneficio útil. Para muchas familias trabajadoras y profesionales, puede ser el primer tipo de protección que reciben. Como viene a través del trabajo, puede sentirse simple, conveniente y fácil de confiar.</p>
<p>Pero la conveniencia a veces puede crear una falsa sensación de seguridad.</p>
<p>Muchas familias nunca se detienen a preguntar qué cubren realmente sus beneficios del trabajo, cuánto tiempo dura la cobertura o qué pasa si el empleo cambia. La respuesta importa porque la protección familiar no se trata solo de tener una póliza; se trata de saber si las personas que dependen de ti estarían realmente bien si la vida cambiara de repente.</p>

<h2>La comodidad de la cobertura del empleador</h2>
<p>El seguro de vida a través del trabajo a menudo se siente automático. Puede ofrecerse durante la inscripción, deducirse de la nómina o incluirse como parte del paquete de beneficios del empleado. Por eso, muchas personas asumen que su familia está completamente protegida.</p>
<p>En algunos casos, la cobertura del empleador puede proporcionar un punto de partida útil. Pero para muchas familias, puede no estar diseñada para reemplazar años de ingresos, pagar deudas importantes, cubrir necesidades futuras de los hijos o ayudar a un cónyuge sobreviviente a mantener el hogar.</p>
<p>Eso no significa que la cobertura del trabajo sea mala. Simplemente significa que debe revisarse como parte de una visión más amplia.</p>

<h2>¿Qué pasa si el trabajo cambia?</h2>
<p>Una pregunta importante que muchas familias pasan por alto es si su cobertura permanece con ellas.</p>
<p>El seguro de vida proporcionado por el empleador puede cambiar o terminar cuando cambia el empleo. Si alguien deja un trabajo, pierde un trabajo, se jubila o cambia de empleador, la cobertura con la que contaba puede no continuar de la misma manera.</p>
<p>Eso puede convertirse en un problema serio si la familia nunca creó protección fuera del trabajo.</p>
<p>Un plan de protección familiar más fuerte mira más allá del trabajo y pregunta: <em>¿Qué protección permanece con la familia, incluso cuando la vida o el empleo cambian?</em></p>

<blockquote>“Las personas que dependen de tus ingresos no trabajan para tu empleador. Por eso la protección de tu familia no debería depender solo de tu trabajo.”
<cite>— Family First Legacy</cite></blockquote>

<h2>¿Cuánta protección necesita realmente una familia?</h2>
<p>No hay una respuesta única para todos. Cada familia tiene diferentes responsabilidades, ingresos, deudas y metas. Una familia puede necesitar pensar en:</p>
<ul>
<li><strong>Reemplazo de ingresos:</strong> ¿Por cuánto tiempo necesitaría apoyo la familia si un cheque de pago se detuviera?</li>
<li><strong>Hipoteca o renta:</strong> ¿Podrían los seres queridos permanecer en el hogar?</li>
<li><strong>Deudas:</strong> ¿Hay tarjetas de crédito, préstamos de auto, préstamos personales u otras obligaciones?</li>
<li><strong>Necesidades de los hijos:</strong> ¿Quién ayudaría a cubrir cuidado infantil, escuela, comida, ropa y gastos diarios?</li>
<li><strong>Metas futuras:</strong> ¿La familia aún tendría apoyo para educación, ahorros o planes a largo plazo?</li>
</ul>
<p>La meta no es crear miedo. La meta es traer claridad. Cuando las familias entienden lo que tienen y lo que puede faltar, pueden tomar decisiones con más confianza.</p>

<h2>La protección no se trata solo de fallecer</h2>
<p>El seguro de vida moderno también puede incluir beneficios en vida, dependiendo de la póliza. Estos beneficios pueden permitir que los titulares que califiquen accedan a parte de los beneficios de su póliza durante ciertos eventos de salud cubiertos, como una enfermedad crónica, crítica o terminal.</p>
<p>Esto importa porque la vida puede cambiar incluso mientras una persona aún vive. Una enfermedad grave puede reducir ingresos, detener un cheque de pago, aumentar gastos o poner presión sobre toda la familia. Tener el tipo correcto de protección puede ayudar a una familia a prepararse para más de un tipo de riesgo.</p>

<h2>El riesgo de asumir</h2>
<p>El mayor problema no siempre es la falta de cobertura. A veces es la falta de entendimiento.</p>
<p>Una persona puede tener beneficios del trabajo pero no saber la cantidad. Puede tener una póliza pero no saber si es portable. Puede creer que su familia está protegida pero nunca ha comparado la cobertura con sus gastos mensuales reales.</p>
<p>Por eso una revisión sencilla puede ser valiosa. Puede ayudar a las familias a entender lo que tienen actualmente, qué puede cambiar si el empleo cambia y si se puede necesitar protección adicional.</p>

<h2>Antes de que la vida cambie, revisa lo que tienes</h2>
<p>La protección familiar es un acto de amor y responsabilidad. No se trata de esperar lo peor, sino de prepararse sabiamente para las personas que dependen de ti.</p>
<p>Los beneficios del trabajo pueden ser un buen comienzo, pero no deberían ser lo único que una familia entiende. Antes de que la vida cambie, toma tiempo para hacer las preguntas correctas, revisar tu cobertura y asegurarte de que tu familia sepa qué protección realmente existe.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Programa una revisión sin costo</a>
</div>"""
    },

    "blog_retirement_es.html": {
        "title": "¿Podrían los impuestos reducir los ingresos de jubilación con los que cuentas?",
        "meta_desc": "Aprende por qué una planificación consciente de los impuestos antes de la jubilación puede ayudarte a entender lo que realmente podrías conservar.",
        "badge": "Planificación para la jubilación",
        "read_time": "Lectura de 6 minutos",
        "hero_img": "images/hero_retirement_diverse_1777335727638.png",
        "body": """<p>Un 401(k) puede ser una herramienta valiosa para la jubilación. Para muchas familias trabajadoras, es uno de los primeros lugares donde comienzan a ahorrar para el futuro, especialmente cuando un empleador ofrece contribuciones equivalentes.</p>
<p>Pero hay una pregunta que muchas personas no hacen lo suficientemente temprano: <em>¿Cuánto de ese dinero de jubilación conservaré realmente después de impuestos?</em></p>
<p>Ahorrar para la jubilación es importante. Pero la planificación de jubilación no se trata solo del saldo que ves en un estado de cuenta. También se trata de entender cómo los impuestos, los cambios del mercado y las necesidades de ingresos pueden afectar el dinero con el que cuentas más adelante.</p>

<h2>El saldo que ves puede no ser la cantidad que conservas</h2>
<p>Las cuentas tradicionales 401(k) e IRA pueden ofrecer ventajas fiscales hoy porque las contribuciones pueden hacerse antes de pagar impuestos. Eso puede ayudar a muchas familias a ahorrar más durante sus años de trabajo.</p>
<p>Pero esos impuestos no desaparecen. En muchos casos, se posponen.</p>
<p>Cuando se retira dinero de un 401(k) o IRA tradicional durante la jubilación, esos retiros generalmente son gravables. Eso significa que la cantidad mostrada en tu estado de cuenta puede no ser la misma cantidad que puedes gastar.</p>

<h2>La pregunta fiscal que muchas familias pasan por alto</h2>
<p>Muchas personas planifican alrededor del saldo de jubilación que esperan construir. Pero menos personas se detienen a preguntar cómo podrían verse los impuestos cuando más necesiten ese dinero.</p>
<p>Una familia puede ver una cuenta de jubilación grande y sentirse confiada. Pero si los retiros crean ingresos gravables, los impuestos pueden afectar cuánto rinde ese dinero.</p>

<blockquote>“No planifiques la jubilación solo alrededor del saldo que ves. Planifica alrededor del ingreso que realmente podrías conservar.”
<cite>— Family First Legacy</cite></blockquote>

<h2>Por qué importa la planificación consciente de impuestos</h2>
<p>La planificación consciente de impuestos no significa tratar de evitar impuestos de manera inapropiada. Significa entender cómo se pueden tratar diferentes tipos de ingresos de jubilación y cómo pueden funcionar juntos.</p>
<p>Algunas familias pueden beneficiarse al aprender sobre opciones como cuentas Roth, conversiones Roth, anualidades o seguros de vida con valor en efectivo correctamente estructurados. Cada opción funciona de manera diferente y tiene reglas, costos, beneficios y limitaciones.</p>

<h2>Los impuestos no son el único riesgo de jubilación</h2>
<p>Los impuestos son importantes, pero no son el único tema que las familias deben considerar.</p>
<p>El momento del mercado también puede importar. Si el mercado cae cerca de la jubilación o durante los primeros años de retiros, puede afectar cuánto duran los ahorros. Esto a menudo se llama riesgo de secuencia de retornos.</p>
<p>Una estrategia de jubilación bien pensada debe considerar: Ingresos, Impuestos, Riesgo de mercado, Longevidad y Flexibilidad.</p>

<h2>Antes de que comience la jubilación, conoce lo que podrías conservar</h2>
<p>Un plan de jubilación sólido debe hacer más que ayudarte a ahorrar. Debe ayudarte a entender cómo puede funcionar tu dinero cuando llegue el momento de usarlo.</p>
<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Programa una revisión sin costo</a>
</div>"""
    },

    "blog_education_es.html": {
        "title": "¿Qué pasa si el camino de tu hijo cambia después de haber ahorrado?",
        "meta_desc": "Aprende a comparar formas flexibles de apoyar el futuro de tu hijo mientras proteges tu propia jubilación.",
        "badge": "Planificación educativa",
        "read_time": "Lectura de 5 minutos",
        "hero_img": "images/hero_education_diverse_1777335740128.png",
        "body": """<p>Todo padre desea darle a su hijo un comienzo sólido. Para muchas familias, eso significa ahorrar temprano, reducir la necesidad de préstamos estudiantiles y darle al hijo más opciones para el futuro.</p>
<p>Pero los hijos crecen. Los sueños cambian. La vida no siempre sigue un solo plan.</p>
<p>Tu hijo puede ir a la universidad y terminar, y esa es una meta maravillosa. Pero incluso entonces, los detalles pueden cambiar. Puede recibir una beca, elegir otra escuela, necesitar vivienda, continuar estudios de posgrado, iniciar un negocio o necesitar ayuda después de graduarse.</p>

<h2>Un plan 529 puede ayudar, pero conoce las reglas</h2>
<p>Un plan 529 puede ser una forma útil de ahorrar para gastos educativos calificados. Para familias que están seguras de que el dinero se usará para la escuela, puede tener sentido.</p>
<p>Pero un 529 está diseñado principalmente para educación. Si el dinero se usa para gastos no calificados, las ganancias pueden estar sujetas a impuestos y penalidades. Un plan 529 propiedad de los padres también generalmente se trata como un activo parental en la FAFSA y puede considerarse al determinar elegibilidad para ayuda financiera basada en necesidad.</p>

<blockquote>“El futuro de un hijo debe tener espacio para crecer. El plan que elijas debe poder ajustarse cuando la vida no siga exactamente el camino que esperabas.”
<cite>— Family First Legacy</cite></blockquote>

<h2>Los préstamos estudiantiles pueden seguir a un hijo por años</h2>
<p>Muchos padres no solo quieren que su hijo asista a la escuela. Quieren que su hijo comience la vida adulta con más libertad y menos presión financiera.</p>
<p>Planificar con anticipación puede ayudar a reducir préstamos futuros y darle a tu hijo más opciones después de la escuela.</p>

<h2>El futuro de tu hijo importa, y el tuyo también</h2>
<p>Muchos padres están dispuestos a sacrificarse por sus hijos. Ese amor es poderoso. Pero ayudar a un hijo no debería significar poner en riesgo tu propia jubilación.</p>
<p><em>Puedes pedir prestado para la universidad, pero no puedes pedir prestado para la jubilación.</em></p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Programa una revisión sin costo</a>
</div>"""
    },

    "blog_financial_strategy_es.html": {
        "title": "¿El tiempo está trabajando a favor de tu dinero, o en contra?",
        "meta_desc": "Descubre cómo la Regla del 72 y hábitos pequeños pueden marcar una gran diferencia en la construcción de tu patrimonio.",
        "badge": "Estrategia financiera",
        "read_time": "Lectura de 3 minutos",
        "hero_img": "images/hero_estate_diverse_1777335759302.png",
        "body": """<p>La mayoría de las familias trabajan duro. Pagan facturas, cuidan a sus hijos, apoyan a sus seres queridos y tratan de ahorrar lo que pueden. Pero incluso con buenas intenciones, a menudo se ignora una pregunta importante:</p>
<p><em>¿El tiempo está ayudando a que tu dinero crezca, o está trabajando silenciosamente en contra de tu familia?</em></p>

<h2>La Regla del 72: una lección sencilla sobre el crecimiento</h2>
<p>Una forma sencilla de entender el poder del tiempo es la Regla del 72.</p>
<p>La Regla del 72 ayuda a estimar cuánto tiempo puede tardar el dinero en duplicarse a una cierta tasa de crecimiento. No es una promesa ni una garantía. Es solo una herramienta educativa.</p>
<p><strong>Fórmula:</strong> 72 dividido entre la tasa de crecimiento = años estimados para que el dinero se duplique.</p>

<h2>El tiempo también puede trabajar en tu contra</h2>
<p>La Regla del 72 no se aplica solo a los ahorros. También puede ayudar a explicar la deuda. La deuda con intereses altos puede crecer rápidamente cuando no se maneja con cuidado.</p>

<h2>El crecimiento necesita protección</h2>
<p>Hacer crecer el dinero es importante, pero la protección también importa. El crecimiento ayuda a una familia a avanzar. La protección ayuda a evitar que la familia retroceda.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Programa una revisión financiera sin costo</a>
</div>"""
    },

    "blog_legacy_es.html": {
        "title": "¿Tu familia tendrá que esperar el dinero que necesita?",
        "meta_desc": "El proceso de probate puede retrasar el acceso a ciertos activos. Aprende cómo el seguro de vida puede proporcionar ayuda inmediata.",
        "badge": "Planificación patrimonial",
        "read_time": "Lectura de 3 minutos",
        "hero_img": "images/small_business_hero_1777398700055.png",
        "body": """<p>Cuando un ser querido fallece, la familia enfrenta más que dolor. También puede enfrentar necesidades financieras inmediatas.</p>
<p>Las facturas siguen llegando. La hipoteca o la renta puede seguir venciendo. Los gastos funerarios pueden necesitar atención. Los hijos pueden seguir necesitando apoyo.</p>
<p>En esos momentos, el tiempo importa. El dinero que llega cuando la familia más lo necesita puede traer estabilidad, dignidad y espacio para respirar.</p>

<blockquote>“Un testamento puede dejar instrucciones. El seguro de vida puede ayudar a dejar apoyo inmediato.”
<cite>— Family First Legacy</cite></blockquote>

<h2>El problema con probate</h2>
<p>Muchas personas creen que tener un testamento significa que todo pasará automáticamente a sus seres queridos de inmediato. Pero no siempre funciona así.</p>
<p>Un testamento es importante, pero algunos activos aún pueden tener que pasar por probate antes de distribuirse.</p>

<h2>Protege a las personas que amas</h2>
<p>La planificación patrimonial no es solo para familias adineradas. Es para cualquier familia que desea hacer las cosas más fáciles, más claras y menos estresantes para las personas que ama.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Programa una revisión de legado sin costo</a>
</div>"""
    }
}

ARTICLES_EN = {
    "blog_family_protection.html": {
        "title": "Is Your Family Counting on Work Benefits Alone?",
        "meta_desc": "Employer life insurance can be a helpful benefit, but it may leave gaps when life changes or employment ends.",
        "badge": "Family Protection",
        "read_time": "5 min read",
        "hero_img": "images/hero_life_insurance_diverse_1777335713599.png",
        "body": """<p>Employer life insurance can be a helpful benefit. For many working families and professionals, it may be the first type of protection they receive. Because it comes through work, it can feel simple, convenient, and easy to trust.</p>
<p>But convenience can sometimes create a false sense of security.</p>
<p>Many families never stop to ask what their work benefits actually cover, how long the coverage lasts, or what happens if employment changes. The answer matters because family protection is not just about having a policy — it is about knowing whether the people who depend on you would truly be okay if life changed suddenly.</p>

<h2>The Comfort of Employer Coverage</h2>
<p>Life insurance through work often feels automatic. It may be offered during enrollment, deducted from payroll, or included as part of an employee benefits package. Because of that, many people assume their family is fully protected.</p>
<p>In some cases, employer coverage may provide a helpful starting point. But for many families, it may not be designed to replace years of income, pay off major debts, cover children’s future needs, or help a surviving spouse maintain the household.</p>
<p>That does not mean work coverage is bad. It simply means it should be reviewed as part of a bigger picture.</p>

<h2>What Happens If the Job Changes?</h2>
<p>One important question many families overlook is whether their coverage stays with them.</p>
<p>Employer-provided life insurance may change or end when employment changes. If someone leaves a job, loses a job, retires, or changes employers, the coverage they were counting on may not continue in the same way.</p>
<p>That can become a serious issue if the family never created protection outside of work.</p>
<p>A stronger family protection plan looks beyond the job and asks: <em>What protection stays with the family, even when life or employment changes?</em></p>

<blockquote>“The people who depend on your income do not work for your employer. That is why your family’s protection should not depend only on your job.”
<cite>— Family First Legacy</cite></blockquote>

<h2>How Much Protection Does a Family Really Need?</h2>
<p>There is no one-size-fits-all answer. Every family has different responsibilities, income, debts, and goals. A family may need to think about:</p>
<ul>
<li><strong>Income replacement:</strong> How long would the family need support if a paycheck stopped?</li>
<li><strong>Mortgage or rent:</strong> Could loved ones stay in the home?</li>
<li><strong>Debt:</strong> Are there credit cards, car loans, personal loans, or other obligations?</li>
<li><strong>Children’s needs:</strong> Who would help cover childcare, school, food, clothing, and daily expenses?</li>
<li><strong>Future goals:</strong> Would the family still have support for education, savings, or long-term plans?</li>
</ul>
<p>The goal is not to create fear. The goal is to bring clarity. When families understand what they have and what may be missing, they can make decisions with more confidence.</p>

<h2>Protection Is Not Only About Passing Away</h2>
<p>Modern life insurance may also include living benefits, depending on the policy. These benefits may allow qualified policyholders to access part of their policy benefits during certain covered health events, such as a chronic, critical, or terminal illness.</p>
<p>This matters because life can change even while a person is still living. A serious illness may reduce income, stop a paycheck, increase expenses, or place pressure on the entire family. Having the right type of protection may help a family prepare for more than one kind of risk.</p>

<h2>The Risk of Assuming</h2>
<p>The biggest issue is not always lack of coverage. Sometimes it is lack of understanding.</p>
<p>A person may have work benefits but not know the amount. They may have a policy but not know whether it is portable. They may believe their family is protected but have never compared the coverage to their real monthly expenses.</p>

<h2>Before Life Changes, Review What You Have</h2>
<p>Family protection is an act of love and responsibility. It is not about expecting the worst — it is about preparing wisely for the people who depend on you.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Schedule a No-Cost Review</a>
</div>"""
    },

    "blog_retirement.html": {
        "title": "Could Taxes Reduce the Retirement Income You’re Counting On?",
        "meta_desc": "Learn why tax-aware planning before retirement can help you understand what you may actually keep.",
        "badge": "Retirement Planning",
        "read_time": "6 min read",
        "hero_img": "images/hero_retirement_diverse_1777335727638.png",
        "body": """<p>A 401(k) can be a valuable retirement tool. For many working families, it is one of the first places they begin saving for the future, especially when an employer offers matching contributions.</p>
<p>But there is one question many people do not ask early enough: <em>How much of that retirement money will I actually keep after taxes?</em></p>

<h2>The Balance You See May Not Be the Amount You Keep</h2>
<p>Traditional 401(k) and IRA accounts can offer tax advantages today because contributions may be made before taxes are paid. That can help many families save more during their working years.</p>
<p>But those taxes are not gone. In many cases, they are delayed.</p>

<blockquote>“Do not plan retirement only around the balance you see. Plan around the income you may actually keep.”
<cite>— Family First Legacy</cite></blockquote>

<h2>Why Tax-Aware Planning Matters</h2>
<p>Tax-aware planning does not mean trying to avoid taxes in an improper way. It means understanding how different types of retirement income may be treated and how they may work together.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Schedule a No-Cost Review</a>
</div>"""
    },

    "blog_education.html": {
        "title": "What If Your Child’s Path Changes After You Save?",
        "meta_desc": "Learn how to compare flexible ways to support your child’s future while protecting your own retirement.",
        "badge": "Education Planning",
        "read_time": "5 min read",
        "hero_img": "images/hero_education_diverse_1777335740128.png",
        "body": """<p>Every parent wants to give their child a strong start. For many families, that means saving early, reducing the need for student loans, and giving their child more choices for the future.</p>
<p>But children grow. Dreams change. Life does not always follow one plan.</p>

<h2>A 529 Plan Can Help — But Know the Rules</h2>
<p>A 529 plan can be a helpful way to save for qualified education expenses. For families who are confident the money will be used for school, it can make sense.</p>
<p>But a 529 is mainly designed for education. If the money is used for non-qualified expenses, earnings may be subject to taxes and penalties.</p>

<blockquote>“A child’s future should have room to grow. The plan you choose should be able to adjust when life does not follow the exact path you expected.”
<cite>— Family First Legacy</cite></blockquote>

<h2>Your Child’s Future Matters — So Does Yours</h2>
<p><em>You can borrow for college, but you cannot borrow for retirement.</em></p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Schedule a No-Cost Review</a>
</div>"""
    },

    "blog_financial_strategy.html": {
        "title": "Is Time Working for Your Money — or Against It?",
        "meta_desc": "Discover how the Rule of 72 and small consistent habits can make a big difference in wealth building.",
        "badge": "Financial Strategy",
        "read_time": "3 min read",
        "hero_img": "images/hero_estate_diverse_1777335759302.png",
        "body": """<p>Most families work hard. They pay bills, care for their children, support loved ones, and try to save whatever they can. But even with good intentions, one question is often ignored:</p>
<p><em>Is time helping your money grow - or is it quietly working against your family?</em></p>

<h2>The Rule of 72: A Simple Lesson About Growth</h2>
<p>One simple way to understand the power of time is the Rule of 72.</p>
<p>The Rule of 72 helps estimate how long it may take money to double at a certain growth rate. Formula: 72 / growth rate = estimated years to double.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Schedule a No-Cost Financial Review</a>
</div>"""
    },

    "blog_legacy.html": {
        "title": "Will Your Family Wait for the Money They Need?",
        "meta_desc": "Probate can delay access to assets. Learn how life insurance can provide immediate financial support.",
        "badge": "Estate Planning",
        "read_time": "3 min read",
        "hero_img": "images/small_business_hero_1777398700055.png",
        "body": """<p>When a loved one passes away, the family faces more than grief. They may also face immediate financial needs.</p>

<blockquote>“A will can leave instructions. Life insurance can help leave immediate support.”
<cite>— Family First Legacy</cite></blockquote>

<h2>The Problem With Probate</h2>
<p>Many people believe that having a will means everything will automatically pass to their loved ones right away. But that is not always how it works.</p>

<div style="margin-top:32px;">
<a href="#contact" class="btn btn-green">Schedule a No-Cost Legacy Review</a>
</div>"""
    }
}

def update_article_file(filename, data):
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        print(f"  [NOT FOUND] {filename}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | Family First Legacy</title>', content, count=1, flags=re.DOTALL)
    
    # 2. Update Meta Description
    content = re.sub(r'<meta\s+name="description"\s+content="[^"]*"', f'<meta name="description" content="{data["meta_desc"]}"', content, count=1)

    # 3. Update Article Badge
    content = re.sub(r'<div class="article-badge">.*?</div>', f'<div class="article-badge"><span class="green-dot"></span>{data["badge"]}</div>', content, count=1, flags=re.DOTALL)

    # 4. Update Article Title (H1)
    content = re.sub(r'<h1 class="article-title">.*?</h1>', f'<h1 class="article-title">{data["title"]}</h1>', content, count=1, flags=re.DOTALL)

    # 5. Update Article Meta Line
    content = re.sub(r'<div class="article-meta">.*?</div>', f'<div class="article-meta">{data["read_time"]}</div>', content, count=1, flags=re.DOTALL)

    # 6. Update Article Body
    content = re.sub(r'<div class="article-body".*?>.*?</div>\s*</div>\s*</section>', f'<div class="article-body" data-delay="2" data-reveal="">\n{data["body"]}\n</div>\n</div>\n</section>', content, count=1, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Updated article {filename}")

def main():
    print("=== Updating All Spanish Article Pages ===")
    for filename, data in ARTICLES_ES.items():
        update_article_file(filename, data)

    print("\n=== Updating All English Article Pages ===")
    for filename, data in ARTICLES_EN.items():
        update_article_file(filename, data)

    print("\n=== Done! ===")

if __name__ == "__main__":
    main()
