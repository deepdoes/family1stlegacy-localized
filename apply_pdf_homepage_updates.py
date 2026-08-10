#!/usr/bin/env python3
"""
apply_pdf_homepage_updates.py
Applies all client PDF copy, compliance, structure, and interactive section updates to index.html and index_es.html.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_index_html():
    filepath = os.path.join(BASE, "index.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Navigation updates: Careers -> Opportunity ---
    content = content.replace('<li><a href="opportunity.html">Opportunity</a></li>', '<li><a href="opportunity.html">Opportunity</a></li>')
    content = content.replace('<a href="opportunity.html">Opportunity</a>', '<a href="opportunity.html">Opportunity</a>')

    # --- 2. Hero slider updates ---
    # Slide 1
    content = re.sub(
        r'<div class="slide-eyebrow">Life Insurance Protection</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">Life Insurance Protection</div>\n          <h1 class="slide-title">Protect the People<br>Who <em>Matter Most</em></h1>\n          <p class="slide-sub">Life can change in a moment. The people you love deserve a plan that helps protect them when they need it most.<br><br>We help you explore coverage options from well-established carriers — designed to fit your needs, budget, and life.</p>',
        content, flags=re.DOTALL
    )
    
    # Slide 2
    content = re.sub(
        r'<div class="slide-eyebrow">Retirement Planning</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">Retirement Planning</div>\n          <h1 class="slide-title">Your Golden Years,<br><em>Planned With Care</em></h1>\n          <p class="slide-sub">Retirement should feel peaceful, not uncertain. Whether you’re just starting to save or fine-tuning an existing plan, we help you build a retirement strategy tailored to your timeline.<br><br>So you can move toward the future you’ve imagined with more clarity and confidence.</p>',
        content, flags=re.DOTALL
    )

    # Slide 3
    content = re.sub(
        r'<div class="slide-eyebrow">Education Planning</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">Education Planning</div>\n          <h1 class="slide-title">Invest in Their<br><em>Brilliant Future</em></h1>\n          <p class="slide-sub">Every child deserves the chance to dream bigger. Start planning today so your children can pursue any dream — any school, any path — with fewer financial limits standing in the way.<br><br>Give them opportunity, while keeping your family’s future in mind.</p>',
        content, flags=re.DOTALL
    )

    # Slide 4
    content = re.sub(
        r'<div class="slide-eyebrow">Estate &amp; Legacy Planning</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">Estate &amp; Legacy Planning</div>\n          <h1 class="slide-title">Leave a Legacy That<br>Can <em>Last Generations</em></h1>\n          <p class="slide-sub">Everything you worked for tells a story. We help you explore estate and legacy strategies that honor your values and help your family be better prepared.<br><br>Your legacy is not just what you leave behind — it is how you care for the people and causes that matter most.</p>',
        content, flags=re.DOTALL
    )

    # Slide 5
    content = re.sub(
        r'<div class="slide-eyebrow">Business Strategies</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">Business Strategies</div>\n          <h1 class="slide-title">Protect the Business<br>You <em>Built</em></h1>\n          <p class="slide-sub">You worked hard to build your business. From key-person coverage and buy-sell planning to executive benefits and succession strategies, we help business owners explore ways to protect what they have worked so hard to create.<br><br>Because your business is more than income — it is responsibility, sacrifice, and legacy.</p>',
        content, flags=re.DOTALL
    )

    # Slide 6
    content = re.sub(
        r'<div class="slide-eyebrow">The Career Opportunity</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">The Career Opportunity</div>\n          <h1 class="slide-title">Build Your Own<br><em>Financial Legacy</em></h1>\n          <p class="slide-sub">Turn your passion for helping families into a meaningful financial services career. Start part-time or grow full-time — with training, mentorship, and support along the way.<br><br>Build something with purpose while helping families understand how to protect what matters most.</p>',
        content, flags=re.DOTALL
    )

    # --- 3. Who We Are section updates ---
    who_we_are_en = """<div class="who-we-are-body">
            <h2 class="t-h2" style="margin-bottom:24px; color:var(--dark);">We Put Family First. Always.</h2>
            <p class="t-lead" style="margin-bottom:20px;">Every family deserves the opportunity to protect what they’ve built, prepare for tomorrow, and pursue the future they dream of.</p>
            <p class="t-body" style="margin-bottom:16px;">We believe every family — regardless of background or income — deserves access to honest, knowledgeable guidance to help them make informed financial decisions.</p>
            <p class="t-body" style="margin-bottom:16px;">Family First Legacy is an independent financial services agency rooted in the Dallas–Fort Worth community and serving families across the United States. We help individuals, families, and business owners explore insurance and financial options from a network of well-established insurance and financial services companies.</p>
            <p class="t-body" style="margin-bottom:16px;">Our licensed professionals take the time to listen, understand your goals and concerns, and learn about the people who matter most to you before helping you explore options that may align with your needs.</p>
            <p class="t-body" style="margin-bottom:24px;">Whether you’re protecting your family, preparing for retirement, planning for your children’s future, or building a legacy, our goal is to provide honest guidance, clear explanations, and the information you need to make confident decisions — without pressure and at your own pace.</p>
            <blockquote style="border-left: 3px solid var(--green); padding-left: 20px; font-style: italic; color: var(--green-mid); margin-bottom: 32px; font-size: 18px; line-height: 1.6;">
              “We do more than offer insurance — we build relationships, educate families, and help them create plans focused on protecting what matters most.”
              <footer style="font-style: normal; font-size: 14px; color: var(--muted); margin-top: 8px;">— Family First Legacy Team</footer>
            </blockquote>
            <a href="#contact" class="btn btn-green">Schedule a Free Review</a>
          </div>"""
    
    content = re.sub(r'<div class="who-we-are-body">.*?<a href="#contact" class="btn btn-green">.*?</a>\s*</div>', who_we_are_en, content, flags=re.DOTALL)

    # --- 4. How We Can Help (Client Solutions) Section ---
    # Update label and titles
    content = content.replace('<div class="t-label" style="color:var(--green); margin-bottom:16px;">Client Solutions</div>', '<div class="t-label" style="color:var(--green); margin-bottom:16px;">HOW WE CAN HELP</div>')
    content = content.replace('<h2 class="t-h1" style="color:var(--dark); max-width:800px; margin:0 auto 24px;">Protection for Every Stage of Life</h2>', '<h2 class="t-h1" style="color:var(--dark); max-width:800px; margin:0 auto 24px;">Guidance for Every Stage of Life</h2>')
    content = content.replace('From protecting your family today to preparing for retirement and building wealth for the future, we offer custom strategies from top-rated carriers.', 'From protecting your family today to preparing for retirement and planning the legacy you want to leave behind, we’re here to help you understand your options and build a strategy that fits each chapter of your life.')
    content = content.replace('Talk to an Agent', 'Start With a Conversation')

    # Add 5th Business Strategies tile card if not present
    if 'business_strategies.html' not in content:
        business_tile = """
          <!-- Card 5: Business Strategies -->
          <div class="service-card" style="background:var(--white); border:1px solid var(--line); border-radius:24px; padding:40px; display:flex; flex-direction:column; justify-content:space-between; transition:transform .3s, box-shadow .3s;">
            <div>
              <div style="width:48px; height:48px; background:var(--green-lite); border-radius:12px; display:flex; align-items:center; justify-content:center; margin-bottom:24px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="var(--green)" stroke-width="2" style="width:24px; height:24px;"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg>
              </div>
              <h3 class="t-h3" style="color:var(--dark); margin-bottom:12px;">Business Strategies</h3>
              <p class="t-body" style="font-size:15px; margin-bottom:24px;">Your business carries your work, your income, and the people who depend on it. We help business owners understand protection options, succession strategies, and planning tools that may help support long-term stability.</p>
            </div>
            <a href="business_strategies.html" class="btn btn-ghost" style="width:100%; justify-content:center;">Learn How It Works →</a>
          </div>"""
        
        # Insert after card 4 (Education Planning card)
        content = re.sub(r'(<!-- Card 4: Education Planning -->.*?</div>\s*</div>)', r'\1\n' + business_tile, content, flags=re.DOTALL)

    # --- 5. Interactive Section: "Real Questions. Clear Guidance." ---
    real_questions_en = """<!-- ── REAL QUESTIONS. CLEAR GUIDANCE. SECTION ── -->
<section id="reviews" style="padding:120px 0; background:var(--bg); position:relative;">
  <div style="max-width:1280px; margin:0 auto; padding:0 32px; box-sizing:border-box;">
    
    <!-- Top Purple Featured Rotating Section -->
    <div id="rq-featured-box" style="background:linear-gradient(135deg, #3A2060 0%, #201238 100%); border-radius:32px; padding:56px; color:#fff; position:relative; overflow:hidden; box-shadow:0 24px 64px rgba(32,18,56,0.35); margin-bottom:40px;">
      <div style="position:absolute; top:-100px; right:-100px; width:400px; height:400px; background:radial-gradient(circle, rgba(139,125,168,0.2) 0%, transparent 70%); pointer-events:none;"></div>
      
      <div style="display:grid; grid-template-columns: 1fr 1.3fr; gap:48px; align-items:start;">
        <!-- Left Side Intro -->
        <div>
          <div class="t-label" style="color:var(--amber-lt); margin-bottom:12px; letter-spacing:3px;">REAL QUESTIONS</div>
          <h2 class="t-h2" style="color:#fff; margin-bottom:20px; font-size:clamp(32px, 3.8vw, 48px); line-height:1.1;">Real Questions.<br>Clear Guidance.</h2>
          <p style="color:rgba(255,255,255,0.8); font-size:16px; line-height:1.7; font-weight:300;">Families do not always come to us with perfect plans. Many come with questions, concerns, and uncertainty. Our role is to help them understand their options clearly, so they can make decisions with confidence.</p>
        </div>

        <!-- Right Side Dynamic Display Card -->
        <div style="background:rgba(255,255,255,0.06); backdrop-filter:blur(16px); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:40px; position:relative; min-height:340px; display:flex; flex-direction:column; justify-content:space-between; transition:opacity 0.3s ease, transform 0.3s ease;" id="rq-card-display">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <span id="rq-counter" style="font-size:13px; font-weight:700; color:var(--amber-lt); letter-spacing:1px;">01 of 06 - Family Protection</span>
              <span id="rq-badge" style="background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:600; color:#fff;">Guidance with care</span>
            </div>
            <h3 id="rq-question" style="font-family:var(--font-head); font-size:clamp(20px, 2.2vw, 26px); font-weight:700; color:#fff; line-height:1.3; margin-bottom:16px;">“If my income stopped tomorrow, how long would my family be okay?”</h3>
            <p id="rq-desc" style="color:rgba(255,255,255,0.82); font-size:15px; line-height:1.7; margin-bottom:28px; font-weight:300;">Many families have some coverage through work, but they are not sure if it is enough — or if it would stay with them if life changed. A simple review can help identify possible gaps, explain available protection options, and help families understand what may fit their needs, budget, and responsibilities.</p>
          </div>
          <div>
            <a href="#contact" class="btn" style="background:#fff; color:var(--dark); font-weight:700; padding:14px 28px; border-radius:30px; text-decoration:none; display:inline-flex; align-items:center; gap:8px; transition:all 0.2s ease;" id="rq-btn">Start with a Simple Review →</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom White Preview Section -->
    <div style="background:#fff; border:1px solid var(--line); border-radius:28px; padding:48px; box-shadow:0 12px 40px rgba(0,0,0,0.04);">
      <div style="text-align:center; margin-bottom:36px;">
        <div class="t-label" style="color:var(--green); margin-bottom:8px;">COMMON CONCERNS</div>
        <h3 class="t-h3" style="color:var(--dark);">Concerns Families Bring to Us</h3>
      </div>

      <!-- 6 Clickable Preview Cards -->
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;" id="rq-preview-grid">
        
        <div class="rq-preview-card active" onclick="switchRqCard(0)" style="background:var(--green-lite); border:2px solid var(--green); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--green); margin-bottom:6px; text-transform:uppercase;">Family Protection</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“If my income stopped tomorrow...”</div>
          <span style="font-size:11px; background:rgba(74,45,122,0.1); color:var(--green); padding:3px 10px; border-radius:12px; font-weight:600;">Guidance with care</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(1)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Living Benefits</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“If illness stopped my income...”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Living benefits guidance</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(2)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Retirement Planning</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“Preparing or just hoping?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Retirement guidance with care</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(3)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Business Strategies</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“What happens to my business?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Business protection guidance</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(4)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Education Planning</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“Help my children with fewer limits?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Education planning guidance</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(5)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Legacy Planning</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“Will my family have clarity?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Legacy planning guidance</span>
        </div>

      </div>

      <p style="font-size:12px; color:var(--muted); margin-top:28px; text-align:center; font-style:italic;">These examples are for educational purposes and show common concerns families may face. Individual needs, eligibility, and results may vary.</p>
    </div>

  </div>
</section>

<script>
const rqData = [
  {
    counter: "01 of 06 - Family Protection",
    badge: "Guidance with care",
    question: "“If my income stopped tomorrow, how long would my family be okay?”",
    desc: "Many families have some coverage through work, but they are not sure if it is enough — or if it would stay with them if life changed. A simple review can help identify possible gaps, explain available protection options, and help families understand what may fit their needs, budget, and responsibilities."
  },
  {
    counter: "02 of 06 - Living Benefits",
    badge: "Living benefits guidance",
    question: "“What if I survive the illness — but my income does not?”",
    desc: "A serious illness can affect more than health. It can affect income, bills, and the whole household. Some life insurance policies may include living benefits that can help provide support if someone qualifies due to a covered critical, chronic, or terminal illness."
  },
  {
    counter: "03 of 06 - Retirement Planning",
    badge: "Retirement guidance with care",
    question: "“Am I preparing for retirement — or just hoping it works out?”",
    desc: "Many hardworking families save what they can, but still wonder if they are doing enough. Clear guidance can help them understand retirement options, possible risks, and steps that may support their long-term goals."
  },
  {
    counter: "04 of 06 - Business Strategies",
    badge: "Business protection guidance",
    question: "“If something happened to me, what would happen to the business I built?”",
    desc: "Business owners carry responsibility for their family, employees, clients, and years of hard work. We help them understand protection options, including key-person coverage and business planning strategies that may strengthen their overall plan."
  },
  {
    counter: "05 of 06 - Education Planning",
    badge: "Education planning guidance",
    question: "“How can I help my children pursue education with fewer financial limits?”",
    desc: "Many parents want to support their children’s future, but they are not sure which education planning option gives the right balance of growth, flexibility, and control. Clear guidance can help families understand choices that may fit their goals."
  },
  {
    counter: "06 of 06 - Legacy Planning",
    badge: "Legacy planning guidance",
    question: "“Will my family receive clarity and support — or be left searching for help?”",
    desc: "Some families want to leave more than money. They want to leave direction, support, and a meaningful legacy for the people they love. A thoughtful plan can help reduce confusion and help loved ones know what to do next."
  }
];

function switchRqCard(idx) {
  const display = document.getElementById('rq-card-display');
  display.style.opacity = '0';
  display.style.transform = 'translateY(8px)';
  
  setTimeout(() => {
    document.getElementById('rq-counter').textContent = rqData[idx].counter;
    document.getElementById('rq-badge').textContent = rqData[idx].badge;
    document.getElementById('rq-question').textContent = rqData[idx].question;
    document.getElementById('rq-desc').textContent = rqData[idx].desc;

    display.style.opacity = '1';
    display.style.transform = 'translateY(0)';
  }, 200);

  const cards = document.querySelectorAll('#rq-preview-grid .rq-preview-card');
  cards.forEach((card, i) => {
    if (i === idx) {
      card.style.background = 'var(--green-lite)';
      card.style.borderColor = 'var(--green)';
      card.style.borderWidth = '2px';
      card.querySelector('span').style.background = 'rgba(74,45,122,0.1)';
      card.querySelector('span').style.color = 'var(--green)';
    } else {
      card.style.background = '#F9F8FA';
      card.style.borderColor = 'var(--line)';
      card.style.borderWidth = '1px';
      card.querySelector('span').style.background = 'rgba(0,0,0,0.05)';
      card.querySelector('span').style.color = 'var(--muted)';
    }
  });
}
</script>
"""

    content = re.sub(r'<section id="reviews".*?</section>', real_questions_en, content, flags=re.DOTALL)

    # Write updated index.html
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✓ Updated index.html")


def update_index_es_html():
    filepath = os.path.join(BASE, "index_es.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 1. Hero slider updates (ES) ---
    content = re.sub(
        r'<div class="slide-eyebrow">Protección de seguro de vida</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">PROTECCIÓN CON SEGURO DE VIDA</div>\n          <h1 class="slide-title">Protege a las personas<br>que <em>más importan</em></h1>\n          <p class="slide-sub">La vida puede cambiar en un momento. Las personas que amas merecen un plan que ayude a protegerlas cuando más lo necesiten.<br><br>Te ayudamos a explorar opciones de cobertura de compañías bien establecidas, diseñadas para ajustarse a tus necesidades, tu presupuesto y tu vida.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Protéjase hoy', 'Obtén protección hoy')
    content = content.replace('Explorar la cobertura', 'Conoce la cobertura')

    content = re.sub(
        r'<div class="slide-eyebrow">Planificación de jubilación</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">PLANIFICACIÓN PARA LA JUBILACIÓN</div>\n          <h1 class="slide-title">Tus años dorados,<br><em>planificados con cuidado</em></h1>\n          <p class="slide-sub">La jubilación debería sentirse tranquila, no incierta. Ya sea que estés comenzando a ahorrar o ajustando un plan existente, te ayudamos a crear una estrategia de jubilación adaptada a tu tiempo.<br><br>Para que puedas avanzar hacia el futuro que has imaginado con más claridad y confianza.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Planificar mi jubilación', 'Comienza mi plan de jubilación')

    content = re.sub(
        r'<div class="slide-eyebrow">Planificación de la educación</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">PLANIFICACIÓN EDUCATIVA</div>\n          <h1 class="slide-title">Invierte en su<br><em>futuro brillante</em></h1>\n          <p class="slide-sub">Cada niño merece la oportunidad de soñar en grande. Comienza a planificar hoy para que tus hijos puedan seguir cualquier sueño — cualquier escuela, cualquier camino — con menos límites financieros en el camino.<br><br>Dales oportunidades, sin perder de vista el futuro de tu familia.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Iniciar un fondo educativo', 'Comienza un fondo educativo')

    content = re.sub(
        r'<div class="slide-eyebrow">Planificación patrimonial y heredada</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">PLANIFICACIÓN PATRIMONIAL Y DE LEGADO</div>\n          <h1 class="slide-title">Deja un legado<br>que <em>pueda durar generaciones</em></h1>\n          <p class="slide-sub">Todo por lo que has trabajado cuenta una historia. Te ayudamos a explorar estrategias patrimoniales y de legado que honren tus valores y ayuden a tu familia a estar mejor preparada.<br><br>Tu legado no es solo lo que dejas atrás; también es la manera en que cuidas a las personas y causas que más importan.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Preservar mi patrimonio', 'Protege mi legado')

    content = re.sub(
        r'<div class="slide-eyebrow">Estrategias de Negocios</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">ESTRATEGIAS PARA NEGOCIOS</div>\n          <h1 class="slide-title">Protege el negocio<br>que <em>construiste</em></h1>\n          <p class="slide-sub">Trabajaste con esfuerzo para construir tu negocio. Desde cobertura para personas clave y planificación buy-sell hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a dueños de negocios a explorar formas de proteger lo que han construido con tanto esfuerzo.<br><br>Porque tu negocio es más que ingresos: es responsabilidad, sacrificio y legado.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Proteger mi negocio', 'Protege mi negocio')

    content = re.sub(
        r'<div class="slide-eyebrow">.*?Oportunidad.*?</div>\s*<h1 class="slide-title">.*?</h1>\s*<p class="slide-sub">.*?</p>',
        '<div class="slide-eyebrow">LA OPORTUNIDAD DE CARRERA</div>\n          <h1 class="slide-title">Construye tu propio<br><em>legado financiero</em></h1>\n          <p class="slide-sub">Convierte tu pasión por ayudar a las familias en una carrera significativa en servicios financieros. Puedes comenzar a tiempo parcial o crecer a tiempo completo, con capacitación, mentoría y apoyo en el camino.<br><br>Construye algo con propósito mientras ayudas a las familias a entender cómo proteger lo que más importa.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace('Explorar la oportunidad', 'Explora la oportunidad')
    content = content.replace('Habla con nosotros', 'Habla con nosotros')

    # --- 2. Who We Are Section (ES) ---
    who_we_are_es = """<div class="who-we-are-body">
            <h2 class="t-h2" style="margin-bottom:24px; color:var(--dark);">Ponemos a la familia primero. Siempre.</h2>
            <p class="t-lead" style="margin-bottom:20px;">Toda familia merece la oportunidad de proteger lo que ha construido, prepararse para el mañana y perseguir el futuro que sueña.</p>
            <p class="t-body" style="margin-bottom:16px;">Creemos que toda familia, sin importar su origen o nivel de ingresos, merece acceso a orientación honesta y bien informada que le ayude a tomar decisiones financieras con conocimiento.</p>
            <p class="t-body" style="margin-bottom:16px;">Family First Legacy es una agencia independiente de servicios financieros con raíces en la comunidad de Dallas-Fort Worth y que sirve a familias en todo Estados Unidos. Ayudamos a individuos, familias y dueños de negocios a explorar opciones de seguros y servicios financieros a través de una red de compañías bien establecidas.</p>
            <p class="t-body" style="margin-bottom:16px;">Nuestros profesionales con licencia se toman el tiempo para escucharte, entender tus metas y preocupaciones, y conocer a las personas que más importan en tu vida antes de ayudarte a explorar opciones que puedan alinearse con tus necesidades.</p>
            <p class="t-body" style="margin-bottom:24px;">Ya sea que estés protegiendo a tu familia, preparándote para la jubilación, planificando el futuro de tus hijos o construyendo un legado, nuestra meta es brindarte orientación honesta, explicaciones claras y la información que necesitas para tomar decisiones con confianza, sin presión y a tu propio ritmo.</p>
            <blockquote style="border-left: 3px solid var(--green); padding-left: 20px; font-style: italic; color: var(--green-mid); margin-bottom: 32px; font-size: 18px; line-height: 1.6;">
              “Hacemos más que ofrecer seguros: construimos relaciones, educamos a las familias y les ayudamos a crear planes enfocados en proteger lo que más importa.”
              <footer style="font-style: normal; font-size: 14px; color: var(--muted); margin-top: 8px;">— Equipo de Family First Legacy</footer>
            </blockquote>
            <a href="#contact" class="btn btn-green">Programa una revisión gratuita</a>
          </div>"""
    content = re.sub(r'<div class="who-we-are-body">.*?<a href="#contact" class="btn btn-green">.*?</a>\s*</div>', who_we_are_es, content, flags=re.DOTALL)

    # --- 3. How We Can Help Section (ES) ---
    content = content.replace('Client Solutions', 'CÓMO PODEMOS AYUDAR')
    content = content.replace('Protección para cada etapa de la vida', 'Orientación para cada etapa de la vida')
    content = content.replace('Desde la protección de su familia hoy hasta la preparación para la jubilación y la creación de riqueza para el futuro, ofrecemos estrategias personalizadas de las principales compañías de seguros.', 'Desde proteger a tu familia hoy hasta prepararte para la jubilación y planificar el legado que deseas dejar, estamos aquí para ayudarte a entender tus opciones y crear una estrategia que se ajuste a cada capítulo de tu vida.')
    content = content.replace('Hable con un Agente', 'Comienza con una conversación')

    if 'business_strategies_es.html' not in content:
        business_tile_es = """
          <!-- Card 5: Business Strategies -->
          <div class="service-card" style="background:var(--white); border:1px solid var(--line); border-radius:24px; padding:40px; display:flex; flex-direction:column; justify-content:space-between; transition:transform .3s, box-shadow .3s;">
            <div>
              <div style="width:48px; height:48px; background:var(--green-lite); border-radius:12px; display:flex; align-items:center; justify-content:center; margin-bottom:24px;">
                <svg viewBox="0 0 24 24" fill="none" stroke="var(--green)" stroke-width="2" style="width:24px; height:24px;"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z"/></svg>
              </div>
              <h3 class="t-h3" style="color:var(--dark); margin-bottom:12px;">Estrategias para Negocios</h3>
              <p class="t-body" style="font-size:15px; margin-bottom:24px;">Su negocio representa su trabajo, sus ingresos y a las personas que dependen de él. Ayudamos a los dueños de negocios a entender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a apoyar la estabilidad a largo plazo.</p>
            </div>
            <a href="business_strategies_es.html" class="btn btn-ghost" style="width:100%; justify-content:center;">Conoce cómo funciona →</a>
          </div>"""
        content = re.sub(r'(<!-- Card 4: Education Planning -->.*?</div>\s*</div>)', r'\1\n' + business_tile_es, content, flags=re.DOTALL)

    # --- 4. Interactive Q&A Section (ES) ---
    real_questions_es = """<!-- ── REAL QUESTIONS. CLEAR GUIDANCE. SECTION (ES) ── -->
<section id="reviews" style="padding:120px 0; background:var(--bg); position:relative;">
  <div style="max-width:1280px; margin:0 auto; padding:0 32px; box-sizing:border-box;">
    
    <!-- Top Purple Featured Rotating Section -->
    <div id="rq-featured-box" style="background:linear-gradient(135deg, #3A2060 0%, #201238 100%); border-radius:32px; padding:56px; color:#fff; position:relative; overflow:hidden; box-shadow:0 24px 64px rgba(32,18,56,0.35); margin-bottom:40px;">
      <div style="position:absolute; top:-100px; right:-100px; width:400px; height:400px; background:radial-gradient(circle, rgba(139,125,168,0.2) 0%, transparent 70%); pointer-events:none;"></div>
      
      <div style="display:grid; grid-template-columns: 1fr 1.3fr; gap:48px; align-items:start;">
        <!-- Left Side Intro -->
        <div>
          <div class="t-label" style="color:var(--amber-lt); margin-bottom:12px; letter-spacing:3px;">PREGUNTAS REALES</div>
          <h2 class="t-h2" style="color:#fff; margin-bottom:20px; font-size:clamp(32px, 3.8vw, 48px); line-height:1.1;">Preguntas reales.<br>Orientación clara.</h2>
          <p style="color:rgba(255,255,255,0.8); font-size:16px; line-height:1.7; font-weight:300;">Las familias no siempre llegan a nosotros con planes perfectos. Muchas vienen con preguntas, preocupaciones e incertidumbre. Nuestro papel es ayudarlas a entender sus opciones con claridad para que puedan tomar decisiones con confianza.</p>
        </div>

        <!-- Right Side Dynamic Display Card -->
        <div style="background:rgba(255,255,255,0.06); backdrop-filter:blur(16px); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:40px; position:relative; min-height:340px; display:flex; flex-direction:column; justify-content:space-between; transition:opacity 0.3s ease, transform 0.3s ease;" id="rq-card-display">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <span id="rq-counter" style="font-size:13px; font-weight:700; color:var(--amber-lt); letter-spacing:1px;">01 de 06 - Protección familiar</span>
              <span id="rq-badge" style="background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.2); padding:4px 14px; border-radius:20px; font-size:12px; font-weight:600; color:#fff;">Orientación con cuidado</span>
            </div>
            <h3 id="rq-question" style="font-family:var(--font-head); font-size:clamp(20px, 2.2vw, 26px); font-weight:700; color:#fff; line-height:1.3; margin-bottom:16px;">“Si mis ingresos se detuvieran mañana, ¿por cuánto tiempo estaría bien mi familia?”</h3>
            <p id="rq-desc" style="color:rgba(255,255,255,0.82); font-size:15px; line-height:1.7; margin-bottom:28px; font-weight:300;">Muchas familias tienen cierta cobertura a través del trabajo, pero no están seguras de si es suficiente o si permanecería con ellas si la vida cambiara. Una revisión sencilla puede ayudar a identificar posibles brechas, explicar opciones de protección disponibles y ayudar a las familias a entender qué puede ajustarse a sus necesidades, presupuesto y responsabilidades.</p>
          </div>
          <div>
            <a href="#contact" class="btn" style="background:#fff; color:var(--dark); font-weight:700; padding:14px 28px; border-radius:30px; text-decoration:none; display:inline-flex; align-items:center; gap:8px; transition:all 0.2s ease;" id="rq-btn">Comienza con una revisión sencilla →</a>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom White Preview Section -->
    <div style="background:#fff; border:1px solid var(--line); border-radius:28px; padding:48px; box-shadow:0 12px 40px rgba(0,0,0,0.04);">
      <div style="text-align:center; margin-bottom:36px;">
        <div class="t-label" style="color:var(--green); margin-bottom:8px;">PREOCUPACIONES COMUNES</div>
        <h3 class="t-h3" style="color:var(--dark);">Preocupaciones que las familias nos traen</h3>
      </div>

      <!-- 6 Clickable Preview Cards -->
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap:20px;" id="rq-preview-grid">
        
        <div class="rq-preview-card active" onclick="switchRqCard(0)" style="background:var(--green-lite); border:2px solid var(--green); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--green); margin-bottom:6px; text-transform:uppercase;">Protección familiar</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“Si mis ingresos se detuvieran mañana...”</div>
          <span style="font-size:11px; background:rgba(74,45,122,0.1); color:var(--green); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación con cuidado</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(1)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Beneficios en vida</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“Si una enfermedad detuviera mis ingresos...”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación sobre beneficios en vida</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(2)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Planificación para la jubilación</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“¿Preparándome o solo esperando?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación de jubilación con cuidado</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(3)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Estrategias para negocios</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“¿Qué pasa con mi negocio?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación para proteger el negocio</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(4)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Planificación educativa</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“¿Ayudar a mis hijos con menos límites?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación de planificación educativa</span>
        </div>

        <div class="rq-preview-card" onclick="switchRqCard(5)" style="background:#F9F8FA; border:1px solid var(--line); border-radius:18px; padding:24px; cursor:pointer; transition:all 0.25s ease;">
          <div style="font-size:12px; font-weight:700; color:var(--muted); margin-bottom:6px; text-transform:uppercase;">Planificación de legado</div>
          <div style="font-size:15px; font-weight:600; color:var(--dark); margin-bottom:12px;">“¿Mi familia tendrá claridad?”</div>
          <span style="font-size:11px; background:rgba(0,0,0,0.05); color:var(--muted); padding:3px 10px; border-radius:12px; font-weight:600;">Orientación de planificación de legado</span>
        </div>

      </div>

      <p style="font-size:12px; color:var(--muted); margin-top:28px; text-align:center; font-style:italic;">Estos ejemplos son solo para fines educativos y muestran preocupaciones comunes que las familias pueden enfrentar. Las necesidades, elegibilidad y resultados individuales pueden variar.</p>
    </div>

  </div>
</section>

<script>
const rqDataEs = [
  {
    counter: "01 de 06 - Protección familiar",
    badge: "Orientación con cuidado",
    question: "“Si mis ingresos se detuvieran mañana, ¿por cuánto tiempo estaría bien mi familia?”",
    desc: "Muchas familias tienen cierta cobertura a través del trabajo, pero no están seguras de si es suficiente o si permanecería con ellas si la vida cambiara. Una revisión sencilla puede ayudar a identificar posibles brechas, explicar opciones de protección disponibles y ayudar a las familias a entender qué puede ajustarse a sus necesidades, presupuesto y responsabilidades."
  },
  {
    counter: "02 de 06 - Beneficios en vida",
    badge: "Orientación sobre beneficios en vida",
    question: "“¿Qué pasa si sobrevivo a la enfermedad, pero mis ingresos no?”",
    desc: "Una enfermedad grave puede afectar más que la salud. Puede afectar los ingresos, las facturas y todo el hogar. Algunas pólizas de seguro de vida pueden incluir beneficios en vida que pueden ayudar a brindar apoyo si alguien califica debido a una enfermedad crítica, crónica o terminal cubierta."
  },
  {
    counter: "03 de 06 - Planificación para la jubilación",
    badge: "Orientación de jubilación con cuidado",
    question: "“¿Me estoy preparando para la jubilación, o solo espero que todo salga bien?”",
    desc: "Muchas familias trabajadoras ahorran lo que pueden, pero aún se preguntan si están haciendo lo suficiente. Una orientación clara puede ayudarles a entender opciones de jubilación, posibles riesgos y pasos que pueden apoyar sus metas a largo plazo."
  },
  {
    counter: "04 de 06 - Estrategias para negocios",
    badge: "Orientación para proteger el negocio",
    question: "“Si algo me pasara, ¿qué ocurriría con el negocio que construí?”",
    desc: "Los dueños de negocios cargan responsabilidad por su familia, empleados, clientes y años de trabajo duro. Les ayudamos a entender opciones de protección, incluyendo cobertura para personas clave y estrategias de planificación empresarial que pueden fortalecer su plan general."
  },
  {
    counter: "05 de 06 - Planificación educativa",
    badge: "Orientación de planificación educativa",
    question: "“¿Cómo puedo ayudar a mis hijos a seguir su educación con menos límites financieros?”",
    desc: "Muchos padres quieren apoyar el futuro de sus hijos, pero no están seguros de qué opción de planificación educativa ofrece el equilibrio adecuado de crecimiento, flexibilidad y control. Una orientación clara puede ayudar a las familias a entender opciones que puedan ajustarse a sus metas."
  },
  {
    counter: "06 de 06 - Planificación de legado",
    badge: "Orientación de planificación de legado",
    question: "“¿Mi familia recibirá claridad y apoyo, o quedará buscando ayuda?”",
    desc: "Algunas familias desean dejar más que dinero. Quieren dejar dirección, apoyo y un legado significativo para las personas que aman. Un plan bien pensado puede ayudar a reducir la confusión y ayudar a los seres queridos a saber qué hacer después."
  }
];

function switchRqCard(idx) {
  const display = document.getElementById('rq-card-display');
  display.style.opacity = '0';
  display.style.transform = 'translateY(8px)';
  
  setTimeout(() => {
    document.getElementById('rq-counter').textContent = rqDataEs[idx].counter;
    document.getElementById('rq-badge').textContent = rqDataEs[idx].badge;
    document.getElementById('rq-question').textContent = rqDataEs[idx].question;
    document.getElementById('rq-desc').textContent = rqDataEs[idx].desc;

    display.style.opacity = '1';
    display.style.transform = 'translateY(0)';
  }, 200);

  const cards = document.querySelectorAll('#rq-preview-grid .rq-preview-card');
  cards.forEach((card, i) => {
    if (i === idx) {
      card.style.background = 'var(--green-lite)';
      card.style.borderColor = 'var(--green)';
      card.style.borderWidth = '2px';
      card.querySelector('span').style.background = 'rgba(74,45,122,0.1)';
      card.querySelector('span').style.color = 'var(--green)';
    } else {
      card.style.background = '#F9F8FA';
      card.style.borderColor = 'var(--line)';
      card.style.borderWidth = '1px';
      card.querySelector('span').style.background = 'rgba(0,0,0,0.05)';
      card.querySelector('span').style.color = 'var(--muted)';
    }
  });
}
</script>
"""

    content = re.sub(r'<section id="reviews".*?</section>', real_questions_es, content, flags=re.DOTALL)

    # Write updated index_es.html
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✓ Updated index_es.html")


if __name__ == "__main__":
    print("=== Updating index.html & index_es.html from Client PDF ===")
    update_index_html()
    update_index_es_html()
    print("=== Done! ===")
