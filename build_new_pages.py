#!/usr/bin/env python3
"""
build_new_pages.py
Creates the new standalone Business Strategies and Opportunity pages in English and Spanish according to the client PDF specifications.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def build_business_strategies_en():
    filepath = os.path.join(BASE, "business_strategies.html")
    content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Business Strategies | Family First Legacy</title>
<meta content="Protect the business you built. From key-person coverage and buy-sell strategies to succession planning and executive benefits, we help business owners safeguard what they have created." name="description"/>
<link rel="alternate" hreflang="en" href="https://family1stlegacy.com/business_strategies.html"/>
<link rel="alternate" hreflang="es" href="https://family1stlegacy.com/business_strategies_es.html"/>
<link rel="alternate" hreflang="x-default" href="https://family1stlegacy.com/business_strategies.html"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<style>
:root {
  --bg: #F4F2F6; --white: #FFFFFF; --dark: #0A0A0F;
  --green: #4A2D7A; --green-mid: #6B4A9C; --green-lite: #EDE6F5;
  --amber: #8B7DA8; --amber-lt: #B5A8C9; --sand: #E6E2EC; --muted: #5C5566; --line: #D6D0DC;
  --font-head: 'Poppins', sans-serif; --font-body: 'Plus Jakarta Sans', sans-serif;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font-body); background: var(--bg); color: var(--dark); overflow-x: hidden; font-weight: 300; }

.t-h1 { font-family: var(--font-head); font-size: clamp(38px, 5vw, 64px); font-weight: 800; line-height: 1.05; letter-spacing: -2px; }
.t-h2 { font-family: var(--font-head); font-size: clamp(28px, 3.5vw, 44px); font-weight: 700; line-height: 1.15; letter-spacing: -1px; }
.t-h3 { font-family: var(--font-head); font-size: clamp(20px, 2.2vw, 28px); font-weight: 700; line-height: 1.25; }
.t-label { font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; }
.t-body { font-size: 16px; line-height: 1.75; font-weight: 300; color: var(--muted); }

/* Header / Nav */
#nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(244,242,246,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }
.nav-bar { display: flex; align-items: center; justify-content: space-between; height: 80px; max-width: 1280px; margin: 0 auto; }
.nav-links { display: flex; align-items: center; gap: 28px; list-style: none; }
.nav-links a { text-decoration: none; color: var(--dark); font-weight: 500; font-size: 14px; transition: color 0.2s; }
.nav-links a:hover { color: var(--green); }
.btn-cta { background: var(--green); color: #fff !important; padding: 10px 20px; border-radius: 20px; font-weight: 600 !important; }

/* Hero */
.page-hero { position: relative; padding: 160px 0 100px; background: linear-gradient(135deg, #1C0F30 0%, #0A0A0F 100%); color: #fff; overflow: hidden; }
.page-hero-bg { position: absolute; inset: 0; background-image: url('images/small_business_hero_1777398700055.png'); background-size: cover; background-position: center; opacity: 0.25; }
.hero-content { position: relative; max-width: 1280px; margin: 0 auto; padding: 0 32px; }

/* Grid / Tiles */
.tiles-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; margin-top: -40px; position: relative; z-index: 10; max-width: 1280px; margin-left: auto; margin-right: auto; padding: 0 32px; }
.tile-card { background: #fff; border: 1px solid var(--line); border-radius: 20px; padding: 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.05); }

/* FAQ Accordion */
.faq-item { background: #fff; border: 1px solid var(--line); border-radius: 16px; margin-bottom: 16px; overflow: hidden; }
.faq-question { padding: 24px; font-weight: 700; font-size: 18px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.faq-answer { padding: 0 24px 24px; font-size: 15px; line-height: 1.7; color: var(--muted); display: none; }
.faq-item.open .faq-answer { display: block; }
.faq-item.open .faq-icon { transform: rotate(180deg); }
</style>
</head>
<body>

<!-- Header -->
<header id="nav">
  <div style="width:100%; padding:0 32px; box-sizing:border-box;">
    <div class="nav-bar">
      <a href="index.html" class="nav-logo">
        <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" style="height: 70px; width: auto; object-fit: contain;">
      </a>
      <ul class="nav-links">
        <li><a href="index.html#about">About</a></li>
        <li><a href="index.html#services">Services</a></li>
        <li><a href="index.html#process">How It Works</a></li>
        <li><a href="opportunity.html">Opportunity</a></li>
        <li><a href="index.html#blog">Knowledgebase</a></li>
        <li><a href="index.html#contact" class="btn-cta">Free Consultation</a></li>
      </ul>
    </div>
  </div>
</header>

<!-- Hero Section -->
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="hero-content">
    <div class="t-label" style="color:var(--amber-lt); margin-bottom:16px;">BUSINESS STRATEGIES</div>
    <h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">If You Couldn’t Show Up Tomorrow, Would Your Business Keep Moving?</h1>
    <p class="t-body" style="color:rgba(255,255,255,0.85); font-size:18px; max-width:800px; margin-bottom:24px;">The business you built supports more than income. It may support your family, your employees, your customers, and years of sacrifice. We help business owners understand protection options, succession strategies, and planning tools that may help prepare for the unexpected.</p>
    <p style="color:var(--amber-lt); font-size:17px; font-style:italic; margin-bottom:36px;">You built the business. But who protects it if you cannot be there?</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
      <a href="index.html#contact" class="btn-cta" style="padding:14px 32px; font-size:16px; border-radius:30px;">Protect My Business</a>
      <a href="index.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:14px 32px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Start With a Conversation</a>
    </div>
  </div>
</section>

<!-- Bottom Tiles Section -->
<section style="padding-bottom:80px;">
  <div class="tiles-grid">
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">KEY PEOPLE MATTER</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Could your business continue without the people it depends on most?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">OWNERSHIP NEEDS A PLAN</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">What happens if an owner, partner, or key person can no longer continue?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">YOUR FAMILY DESERVES CLARITY</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Would they know how to handle what you worked so hard to build?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">PROTECT THE VALUE YOU’RE BUILDING</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Plan for stability before life forces difficult decisions.</div>
    </div>
  </div>
</section>

<!-- Questions Every Business Owner Should Answer -->
<section style="padding:80px 0; background:#fff;">
  <div style="max-width:1100px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">BUSINESS PLANNING</div>
      <h2 class="t-h2">Questions Every Business Owner Should Answer</h2>
      <p class="t-body" style="margin-top:12px;">Before life changes, know what could happen to your business, your family, and the people who depend on you.</p>
    </div>

    <div style="display:flex; flex-direction:column; gap:40px;">
      
      <!-- 01 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">01</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">Could the Business Survive Losing a Key Person?</h3>
          <p class="t-body">Some businesses depend heavily on one owner, partner, manager, or top producer. If that person could no longer serve the business, the financial impact could be serious.<br><br>Key-person coverage may help provide financial support while the business adjusts, replaces talent, protects operations, or manages unexpected pressure.</p>
        </div>
      </div>

      <!-- 02 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">02</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">What Happens if Ownership Changes Suddenly?</h3>
          <p class="t-body">If your business has more than one owner, everyone should understand what happens if one owner passes away, leaves, or becomes unable to continue.<br><br>A buy-sell strategy can help create a clearer path for ownership changes, business value, and family protection. Life insurance is often used to help fund these agreements.</p>
        </div>
      </div>

      <!-- 03 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">03</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">Would Your Family Have Clarity — or Confusion?</h3>
          <p class="t-body">Your business may be one of the most valuable things you have built. But without a plan, your family may be left with questions instead of direction.<br><br>Succession planning helps you think through who may continue the business, how ownership may transfer, and how your family or partners may be supported.</p>
        </div>
      </div>

      <!-- 04 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">04</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">Are You Protecting the Value You’re Building?</h3>
          <p class="t-body">As your business grows, so do the responsibilities connected to it. You may need to think about key people, ownership changes, family needs, and how the business would continue if life changed unexpectedly.<br><br>We help business owners understand options that may support long-term stability and protect the value they are working hard to build.</p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Business Strategy FAQs -->
<section style="padding:80px 0; background:var(--bg);">
  <div style="max-width:900px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:8px;">FREQUENTLY ASKED QUESTIONS</div>
      <h2 class="t-h2">Business Protection FAQs</h2>
    </div>

    <div class="faq-list">
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Do small business owners really need business protection planning? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Yes. Even a small business may support a family, employees, customers, and partners. A clear plan can help reduce confusion if something unexpected happens.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">What is key-person insurance? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Key-person insurance is coverage a business may use to help reduce the financial impact of losing an important owner, partner, or employee. Availability depends on the company, policy, and eligibility.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">What is a buy-sell agreement? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">A buy-sell agreement is a plan between business owners that explains what may happen if one owner passes away, leaves, or becomes unable to continue. Life insurance may be used to help fund the agreement.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Can business planning help my family? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">It may help create clarity. If your family depends on the business, planning can help them understand ownership, business value, and possible financial support if something unexpected happens.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Do you provide legal or tax advice? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. Family First Legacy does not provide legal or tax advice. We help explain insurance and financial strategies, and we encourage business owners to consult qualified legal and tax professionals when needed.</div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<section style="padding:100px 0; background:linear-gradient(135deg, #3A2060 0%, #1A0D30 100%); color:#fff; text-align:center;">
  <div style="max-width:800px; margin:0 auto; padding:0 32px;">
    <h2 class="t-h2" style="color:#fff; margin-bottom:20px;">Your Business Has a Story. Let’s Help Protect the Next Chapter.</h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.85); margin-bottom:36px; line-height:1.7;">You built something that matters. Before life forces difficult questions, let’s start with a simple conversation about how to help protect your business, your family, and the people who depend on what you created.</p>
    <a href="index.html#contact" class="btn-cta" style="padding:16px 36px; font-size:17px; border-radius:30px; display:inline-block;">Start With a Conversation</a>
  </div>
</section>

<!-- Footer -->
<footer style="background:#0A0A0F; color:rgba(255,255,255,0.7); padding:60px 0 30px; font-size:14px;">
  <div style="max-width:1280px; margin:0 auto; padding:0 32px; text-align:center;">
    <p style="margin-bottom:16px;">Empowering families to build a stronger financial future, help protect their loved ones, and create a meaningful legacy for generations to come.</p>
    <div style="display:inline-block; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.15); padding:6px 16px; border-radius:20px; font-size:12px; margin-bottom:24px; color:#fff;">Serving Families Nationwide</div>
    <p style="font-size:12px; color:rgba(255,255,255,0.4); max-width:900px; margin:0 auto; line-height:1.6;">Family First Legacy is an independent financial services agency serving families across the United States. Insurance and financial products are offered through properly licensed professionals and are subject to carrier approval, product availability, underwriting, and applicable state requirements. We do not provide tax or legal advice; please consult a qualified professional for those matters. Individual eligibility, product availability, policy features, and results may vary.</p>
  </div>
</footer>

</body>
</html>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✓ Created business_strategies.html")


def build_business_strategies_es():
    filepath = os.path.join(BASE, "business_strategies_es.html")
    content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Estrategias para Negocios | Family First Legacy</title>
<meta content="Protege el negocio que construiste. Desde cobertura para personas clave y planificación buy-sell hasta beneficios ejecutivos y estrategias de sucesión, ayudamos a dueños de negocios a salvaguardar su esfuerzo." name="description"/>
<link rel="alternate" hreflang="en" href="https://family1stlegacy.com/business_strategies.html"/>
<link rel="alternate" hreflang="es" href="https://family1stlegacy.com/business_strategies_es.html"/>
<link rel="alternate" hreflang="x-default" href="https://family1stlegacy.com/business_strategies.html"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<style>
:root {
  --bg: #F4F2F6; --white: #FFFFFF; --dark: #0A0A0F;
  --green: #4A2D7A; --green-mid: #6B4A9C; --green-lite: #EDE6F5;
  --amber: #8B7DA8; --amber-lt: #B5A8C9; --sand: #E6E2EC; --muted: #5C5566; --line: #D6D0DC;
  --font-head: 'Poppins', sans-serif; --font-body: 'Plus Jakarta Sans', sans-serif;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: var(--font-body); background: var(--bg); color: var(--dark); overflow-x: hidden; font-weight: 300; }

.t-h1 { font-family: var(--font-head); font-size: clamp(38px, 5vw, 64px); font-weight: 800; line-height: 1.05; letter-spacing: -2px; }
.t-h2 { font-family: var(--font-head); font-size: clamp(28px, 3.5vw, 44px); font-weight: 700; line-height: 1.15; letter-spacing: -1px; }
.t-h3 { font-family: var(--font-head); font-size: clamp(20px, 2.2vw, 28px); font-weight: 700; line-height: 1.25; }
.t-label { font-size: 12px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; }
.t-body { font-size: 16px; line-height: 1.75; font-weight: 300; color: var(--muted); }

/* Header / Nav */
#nav { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(244,242,246,0.92); backdrop-filter: blur(12px); border-bottom: 1px solid var(--line); }
.nav-bar { display: flex; align-items: center; justify-content: space-between; height: 80px; max-width: 1280px; margin: 0 auto; }
.nav-links { display: flex; align-items: center; gap: 28px; list-style: none; }
.nav-links a { text-decoration: none; color: var(--dark); font-weight: 500; font-size: 14px; transition: color 0.2s; }
.nav-links a:hover { color: var(--green); }
.btn-cta { background: var(--green); color: #fff !important; padding: 10px 20px; border-radius: 20px; font-weight: 600 !important; }

/* Hero */
.page-hero { position: relative; padding: 160px 0 100px; background: linear-gradient(135deg, #1C0F30 0%, #0A0A0F 100%); color: #fff; overflow: hidden; }
.page-hero-bg { position: absolute; inset: 0; background-image: url('images/small_business_hero_1777398700055.png'); background-size: cover; background-position: center; opacity: 0.25; }
.hero-content { position: relative; max-width: 1280px; margin: 0 auto; padding: 0 32px; }

/* Grid / Tiles */
.tiles-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; margin-top: -40px; position: relative; z-index: 10; max-width: 1280px; margin-left: auto; margin-right: auto; padding: 0 32px; }
.tile-card { background: #fff; border: 1px solid var(--line); border-radius: 20px; padding: 32px; box-shadow: 0 12px 32px rgba(0,0,0,0.05); }

/* FAQ Accordion */
.faq-item { background: #fff; border: 1px solid var(--line); border-radius: 16px; margin-bottom: 16px; overflow: hidden; }
.faq-question { padding: 24px; font-weight: 700; font-size: 18px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
.faq-answer { padding: 0 24px 24px; font-size: 15px; line-height: 1.7; color: var(--muted); display: none; }
.faq-item.open .faq-answer { display: block; }
.faq-item.open .faq-icon { transform: rotate(180deg); }
</style>
</head>
<body>

<!-- Header -->
<header id="nav">
  <div style="width:100%; padding:0 32px; box-sizing:border-box;">
    <div class="nav-bar">
      <a href="index_es.html" class="nav-logo">
        <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" style="height: 70px; width: auto; object-fit: contain;">
      </a>
      <ul class="nav-links">
        <li><a href="index_es.html#about">Acerca de</a></li>
        <li><a href="index_es.html#services">Servicios</a></li>
        <li><a href="index_es.html#process">Cómo funciona</a></li>
        <li><a href="opportunity_es.html">Oportunidad</a></li>
        <li><a href="index_es.html#blog">Base de conocimientos</a></li>
        <li><a href="index_es.html#contact" class="btn-cta">Consulta Gratuita</a></li>
      </ul>
    </div>
  </div>
</header>

<!-- Hero Section -->
<section class="page-hero">
  <div class="page-hero-bg"></div>
  <div class="hero-content">
    <div class="t-label" style="color:var(--amber-lt); margin-bottom:16px;">ESTRATEGIAS PARA NEGOCIOS</div>
    <h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">Si no pudieras presentarte mañana, ¿tu negocio seguiría funcionando?</h1>
    <p class="t-body" style="color:rgba(255,255,255,0.85); font-size:18px; max-width:800px; margin-bottom:24px;">El negocio que construiste sostiene más que ingresos. Puede sostener a tu familia, tus empleados, tus clientes y años de sacrificio. Ayudamos a dueños de negocios a entender opciones de protección, estrategias de sucesión y herramientas de planificación que pueden ayudar a prepararse para lo inesperado.</p>
    <p style="color:var(--amber-lt); font-size:17px; font-style:italic; margin-bottom:36px;">Tú construiste el negocio. Pero ¿quién lo protege si tú no puedes estar ahí?</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
      <a href="index_es.html#contact" class="btn-cta" style="padding:14px 32px; font-size:16px; border-radius:30px;">Protege mi negocio</a>
      <a href="index_es.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:14px 32px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Comienza con una conversación</a>
    </div>
  </div>
</section>

<!-- Bottom Tiles Section -->
<section style="padding-bottom:80px;">
  <div class="tiles-grid">
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">LAS PERSONAS CLAVE IMPORTAN</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">¿Podría tu negocio continuar sin las personas de las que más depende?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">LA PROPIEDAD NECESITA UN PLAN</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">¿Qué pasa si un dueño, socio o persona clave ya no puede continuar?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">TU FAMILIA MERECE CLARIDAD</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">¿Sabrían cómo manejar lo que trabajaste tanto para construir?</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">PROTEGE EL VALOR QUE ESTÁS CONSTRUYENDO</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Planifica para la estabilidad antes de que la vida obligue a tomar decisiones difíciles.</div>
    </div>
  </div>
</section>

<!-- Preguntas que todo dueño de negocio debe responder -->
<section style="padding:80px 0; background:#fff;">
  <div style="max-width:1100px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">PLANIFICACIÓN EMPRESARIAL</div>
      <h2 class="t-h2">Preguntas que todo dueño de negocio debe responder</h2>
      <p class="t-body" style="margin-top:12px;">Antes de que la vida cambie, conoce qué podría pasar con tu negocio, tu familia y las personas que dependen de ti.</p>
    </div>

    <div style="display:flex; flex-direction:column; gap:40px;">
      
      <!-- 01 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">01</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Podría el negocio sobrevivir a la pérdida de una persona clave?</h3>
          <p class="t-body">Algunos negocios dependen mucho de un dueño, socio, gerente o productor principal. Si esa persona ya no pudiera servir al negocio, el impacto financiero podría ser serio.<br><br>La cobertura para personas clave puede ayudar a proporcionar apoyo financiero mientras el negocio se ajusta, reemplaza talento, protege operaciones o maneja presión inesperada.</p>
        </div>
      </div>

      <!-- 02 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">02</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Qué pasa si la propiedad cambia de repente?</h3>
          <p class="t-body">Si tu negocio tiene más de un dueño, todos deberían entender qué pasa si un dueño fallece, se va o ya no puede continuar.<br><br>Una estrategia buy-sell puede ayudar a crear un camino más claro para cambios de propiedad, valor del negocio y protección familiar. El seguro de vida se usa con frecuencia para ayudar a financiar estos acuerdos.</p>
        </div>
      </div>

      <!-- 03 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">03</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Tu familia tendría claridad o confusión?</h3>
          <p class="t-body">Tu negocio puede ser una de las cosas más valiosas que has construido. Pero sin un plan, tu familia puede quedarse con preguntas en lugar de dirección.<br><br>La planificación de sucesión te ayuda a pensar quién puede continuar el negocio, cómo puede transferirse la propiedad y cómo tu familia o socios pueden recibir apoyo.</p>
        </div>
      </div>

      <!-- 04 -->
      <div style="background:var(--bg); border:1px solid var(--line); border-radius:24px; padding:40px; display:grid; grid-template-columns:80px 1fr; gap:24px;">
        <div style="font-size:36px; font-weight:800; color:var(--green);">04</div>
        <div>
          <h3 class="t-h3" style="margin-bottom:12px;">¿Estás protegiendo el valor que estás construyendo?</h3>
          <p class="t-body">A medida que tu negocio crece, también crecen las responsabilidades relacionadas con él. Puede que necesites pensar en personas clave, cambios de propiedad, necesidades familiares y cómo continuaría el negocio si la vida cambiara inesperadamente.<br><br>Ayudamos a dueños de negocios a entender opciones que pueden apoyar la estabilidad a largo plazo y proteger el valor que están trabajando duro para construir.</p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Business Strategy FAQs -->
<section style="padding:80px 0; background:var(--bg);">
  <div style="max-width:900px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:8px;">PREGUNTAS FRECUENTES</div>
      <h2 class="t-h2">Preguntas frecuentes sobre protección empresarial</h2>
    </div>

    <div class="faq-list">
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Los dueños de pequeños negocios realmente necesitan planificación de protección empresarial? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Sí. Incluso un pequeño negocio puede apoyar a una familia, empleados, clientes y socios. Un plan claro puede ayudar a reducir la confusión si algo inesperado ocurre.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Qué es el seguro para persona clave? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">El seguro para persona clave es una cobertura que un negocio puede usar para ayudar a reducir el impacto financiero de perder a un dueño, socio o empleado importante. La disponibilidad depende de la compañía, la póliza y la elegibilidad.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Qué es un acuerdo buy-sell? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Un acuerdo buy-sell es un plan entre dueños de negocios que explica lo que puede suceder si un dueño fallece, se va o ya no puede continuar. El seguro de vida puede usarse para ayudar a financiar el acuerdo.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿La planificación empresarial puede ayudar a mi familia? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Puede ayudar a crear claridad. Si tu familia depende del negocio, la planificación puede ayudarles a entender la propiedad, el valor del negocio y posible apoyo financiero si algo inesperado sucede.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Ofrecen asesoría legal o fiscal? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. Family First Legacy no ofrece asesoría legal ni fiscal. Ayudamos a explicar estrategias de seguros y financieras, y animamos a los dueños de negocios a consultar con profesionales legales y fiscales calificados cuando sea necesario.</div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<section style="padding:100px 0; background:linear-gradient(135deg, #3A2060 0%, #1A0D30 100%); color:#fff; text-align:center;">
  <div style="max-width:800px; margin:0 auto; padding:0 32px;">
    <h2 class="t-h2" style="color:#fff; margin-bottom:20px;">Tu negocio tiene una historia. Ayudemos a proteger el siguiente capítulo.</h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.85); margin-bottom:36px; line-height:1.7;">Construiste algo que importa. Antes de que la vida traiga preguntas difíciles, comencemos con una conversación sencilla sobre cómo ayudar a proteger tu negocio, tu familia y las personas que dependen de lo que creaste.</p>
    <a href="index_es.html#contact" class="btn-cta" style="padding:16px 36px; font-size:17px; border-radius:30px; display:inline-block;">Comienza con una conversación</a>
  </div>
</section>

<!-- Footer -->
<footer style="background:#0A0A0F; color:rgba(255,255,255,0.7); padding:60px 0 30px; font-size:14px;">
  <div style="max-width:1280px; margin:0 auto; padding:0 32px; text-align:center;">
    <p style="margin-bottom:16px;">Ayudamos a las familias a construir un futuro financiero más sólido, ayudar a proteger a sus seres queridos y crear un legado significativo para las generaciones futuras.</p>
    <div style="display:inline-block; background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.15); padding:6px 16px; border-radius:20px; font-size:12px; margin-bottom:24px; color:#fff;">Sirviendo a familias en todo el país</div>
    <p style="font-size:12px; color:rgba(255,255,255,0.4); max-width:900px; margin:0 auto; line-height:1.6;">Family First Legacy es una agencia independiente de servicios financieros que sirve a familias en todo Estados Unidos. Los productos de seguros y financieros se ofrecen a través de profesionales debidamente licenciados y están sujetos a aprobación de la compañía, disponibilidad de productos, evaluación de suscripción y requisitos estatales aplicables. No ofrecemos asesoría legal ni fiscal; consulta con un profesional calificado para esos asuntos. La elegibilidad individual, disponibilidad de productos, características de la póliza y resultados pueden variar.</p>
  </div>
</footer>

</body>
</html>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("  ✓ Created business_strategies_es.html")


if __name__ == "__main__":
    print("=== Creating New Standalone Pages ===")
    build_business_strategies_en()
    build_business_strategies_es()
    print("=== Done! ===")
