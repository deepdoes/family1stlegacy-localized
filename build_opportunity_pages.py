#!/usr/bin/env python3
"""
build_opportunity_pages.py
Creates opportunity.html and opportunity_es.html with full client PDF specifications.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def build_opportunity_en():
    filepath = os.path.join(BASE, "opportunity.html")
    content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>The Career Opportunity | Family First Legacy</title>
<meta content="Build a purpose-driven business in financial services. Learn with mentorship, training, and support while helping families protect what matters most." name="description"/>
<link rel="alternate" hreflang="en" href="https://family1stlegacy.com/opportunity.html"/>
<link rel="alternate" hreflang="es" href="https://family1stlegacy.com/opportunity_es.html"/>
<link rel="alternate" hreflang="x-default" href="https://family1stlegacy.com/opportunity.html"/>
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
.page-hero { position: relative; padding: 160px 0 100px; background: linear-gradient(135deg, #251442 0%, #0A0A0F 100%); color: #fff; overflow: hidden; }
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
        <li><a href="opportunity.html" style="color:var(--green); font-weight:700;">Opportunity</a></li>
        <li><a href="index.html#blog">Knowledgebase</a></li>
        <li><a href="index.html#contact" class="btn-cta">Free Consultation</a></li>
      </ul>
    </div>
  </div>
</header>

<!-- Hero Section -->
<section class="page-hero">
  <div class="hero-content">
    <div class="t-label" style="color:var(--amber-lt); margin-bottom:16px;">THE OPPORTUNITY</div>
    <h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">Build a Purpose-Driven Business in Financial Services</h1>
    <p class="t-body" style="color:rgba(255,255,255,0.85); font-size:18px; max-width:850px; margin-bottom:24px;">At Family First Legacy, we believe financial education can help families make better decisions and feel more prepared for the future. If you have a heart for helping people, we provide training, mentorship, and support to help you learn the financial services business with confidence.</p>
    <p style="color:var(--amber-lt); font-size:17px; font-style:italic; margin-bottom:36px; max-width:800px;">Right now, someone in your life may need to make an important financial decision — they just don’t know where to start yet. Could you become the person who shows up with guidance, education, and care?</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
      <a href="index.html#contact" class="btn-cta" style="padding:14px 32px; font-size:16px; border-radius:30px;">Schedule an Information Session</a>
      <a href="index.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:14px 32px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Start With a Conversation</a>
    </div>
  </div>
</section>

<!-- Bottom Tiles Section -->
<section style="padding-bottom:80px;">
  <div class="tiles-grid">
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">PURPOSE-DRIVEN WORK</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Help families understand decisions that may affect generations.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">TRAINING &amp; MENTORSHIP</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Learn with guidance, support, and practical tools.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">FLEXIBLE START</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Begin part-time or grow as your goals and schedule allow.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">BUILD YOUR OWN BUSINESS</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Grow through learning, consistency, service, and personal effort.</div>
    </div>
  </div>
</section>

<!-- Why This Opportunity Matters & Sections -->
<section style="padding:80px 0; background:#fff;">
  <div style="max-width:1100px; margin:0 auto; padding:0 32px;">
    
    <div style="margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">WHY THIS OPPORTUNITY MATTERS</div>
      <h2 class="t-h2" style="margin-bottom:20px;">More Than Business. A Mission to Educate Families.</h2>
      <p class="t-body" style="font-size:17px; margin-bottom:16px;">Many families want to make better financial decisions, but they do not always know where to start. They may have questions about life insurance, retirement planning, education planning, income protection, or leaving a legacy.</p>
      <p class="t-body" style="font-size:17px; margin-bottom:16px;">That is where the right person can make a difference.</p>
      <p class="t-body" style="font-size:17px;">At Family First Legacy, we are looking for people who care about families, are willing to learn, and want to be part of a mission built on education, trust, and service.</p>
    </div>

    <!-- Who This May Be For -->
    <div style="background:var(--bg); border:1px solid var(--line); border-radius:28px; padding:48px; margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">WHO THIS MAY BE FOR</div>
      <h3 class="t-h3" style="margin-bottom:24px;">This Opportunity May Be a Good Fit If You:</h3>
      
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Care about helping families</h4>
          <p class="t-body" style="font-size:14px;">You enjoy listening, encouraging others, and helping people understand important decisions.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Want to build something of your own</h4>
          <p class="t-body" style="font-size:14px;">You understand that growth takes effort, patience, consistency, and a willingness to learn.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Do not want to pressure people</h4>
          <p class="t-body" style="font-size:14px;">You believe families deserve to be educated, respected, and guided — not pushed. When you focus on serving people the right way, the business can grow naturally through trust, consistency, and care.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Need flexibility</h4>
          <p class="t-body" style="font-size:14px;">You may want to start part-time while balancing work, family, school, or other responsibilities.</p>
        </div>
      </div>
    </div>

    <!-- A Real Opportunity to Grow and Serve -->
    <div style="margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">TRANSPARENT DISCLOSURE</div>
      <h2 class="t-h2" style="margin-bottom:20px;">A Real Opportunity to Grow and Serve</h2>
      <p class="t-body" style="font-size:16px; margin-bottom:16px;">This opportunity is for people who want to build in financial services while helping families make informed decisions. It is not a traditional salaried job — it is a commission-based business opportunity. Before serving families as a licensed professional, proper licensing is required. Growth depends on learning, consistency, effort, and the ability to serve people well.</p>
      <p class="t-body" style="font-size:16px; margin-bottom:16px;">For the right person, this can be a meaningful path to personal growth, professional development, and income opportunity. Results are not guaranteed and may vary based on individual effort, training, consistency, time commitment, client needs, product availability, carrier approval, and other business factors.</p>
      <p class="t-body" style="font-size:16px;">Most importantly, this work is about people. There is real satisfaction in helping families understand their options, protect what matters most, and feel more prepared for the future.</p>
    </div>

    <!-- Our Simple Starting Process -->
    <div style="background:var(--green-lite); border:1px solid var(--green); border-radius:28px; padding:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">OUR SIMPLE STARTING PROCESS</div>
      <h2 class="t-h2" style="color:var(--green); margin-bottom:32px;">4 Steps to Get Started</h2>
      
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:24px;">
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">01 — Information Session</div>
          <p class="t-body" style="font-size:14px;">We start with a simple conversation so you can learn what the opportunity is, how the business works, how compensation works, and whether it may fit your goals.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">02 — Licensing Guidance</div>
          <p class="t-body" style="font-size:14px;">Before you can recommend life insurance options or help families apply for coverage, you must be properly licensed. We help explain the licensing steps clearly and guide you as you prepare.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">03 — Training &amp; Mentorship</div>
          <p class="t-body" style="font-size:14px;">You begin learning how to speak with families, understand basic financial concepts, and serve people with care and professionalism.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">04 — Build With Support</div>
          <p class="t-body" style="font-size:14px;">As you grow, you receive continued guidance, tools, and support to help you develop your skills and confidence.</p>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- Opportunity FAQs -->
<section style="padding:80px 0; background:var(--bg);">
  <div style="max-width:900px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:8px;">FREQUENTLY ASKED QUESTIONS</div>
      <h2 class="t-h2">Opportunity FAQs</h2>
    </div>

    <div class="faq-list">
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Is this a job or a business opportunity? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">This is a commission-based business opportunity in the financial services industry, not a traditional salaried job. We start with an information session so you can understand how the opportunity works, what licensing is required, how compensation works, and whether it may fit your goals.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">What if I’m not good at selling or convincing people? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">That is okay. We are not looking for pushy salespeople. We are looking for people who care, listen, learn, and want to help families understand their options. This opportunity is built around education, not pressure. You will learn how to ask good questions, explain financial concepts clearly, and help families make informed decisions at their own pace.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Do I need a license? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Yes. To recommend life insurance options or help families apply for coverage, you must be properly licensed. We guide you through the licensing steps so you can understand what is required before serving families as a licensed professional.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Do I need experience in financial services? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. Many people begin without prior financial services experience. What matters most is your willingness to learn, follow the process, and serve families with honesty and care.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Can I start part-time? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Yes. Many people begin part-time while balancing work, family, school, or other responsibilities.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Will I receive training? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Yes. Training, mentorship, and ongoing support are part of the process.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Is income guaranteed? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. This is a commission-based business opportunity, so income, advancement, and business results are not guaranteed. Results may vary based on individual effort, training, consistency, time commitment, ability to serve families well, client needs, product availability, carrier approval, and other business factors.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">Who is a good fit for this opportunity? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Someone who cares about helping families, is coachable, communicates well, understands that results require effort, and is willing to learn how to serve people with professionalism and integrity.</div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<section style="padding:100px 0; background:linear-gradient(135deg, #3A2060 0%, #1A0D30 100%); color:#fff; text-align:center;">
  <div style="max-width:800px; margin:0 auto; padding:0 32px;">
    <h2 class="t-h2" style="color:#fff; margin-bottom:20px;">Ready to Learn More?</h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.85); margin-bottom:36px; line-height:1.7;">If you are looking for a meaningful opportunity, personal growth, and a way to build in financial services while helping families make informed decisions, we would love to talk with you.</p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
      <a href="index.html#contact" class="btn-cta" style="padding:16px 36px; font-size:17px; border-radius:30px; display:inline-block;">Schedule an Information Session</a>
      <a href="index.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:16px 36px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Start With a Conversation</a>
    </div>
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
    print("  ✓ Created opportunity.html")


def build_opportunity_es():
    filepath = os.path.join(BASE, "opportunity_es.html")
    content = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>La Oportunidad de Carrera | Family First Legacy</title>
<meta content="Construye un negocio con propósito en servicios financieros. Aprende con mentoría, capacitación y apoyo mientras ayudas a las familias a proteger lo que más importa." name="description"/>
<link rel="alternate" hreflang="en" href="https://family1stlegacy.com/opportunity.html"/>
<link rel="alternate" hreflang="es" href="https://family1stlegacy.com/opportunity_es.html"/>
<link rel="alternate" hreflang="x-default" href="https://family1stlegacy.com/opportunity.html"/>
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
.page-hero { position: relative; padding: 160px 0 100px; background: linear-gradient(135deg, #251442 0%, #0A0A0F 100%); color: #fff; overflow: hidden; }
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
        <li><a href="opportunity_es.html" style="color:var(--green); font-weight:700;">Oportunidad</a></li>
        <li><a href="index_es.html#blog">Base de conocimientos</a></li>
        <li><a href="index_es.html#contact" class="btn-cta">Consulta Gratuita</a></li>
      </ul>
    </div>
  </div>
</header>

<!-- Hero Section -->
<section class="page-hero">
  <div class="hero-content">
    <div class="t-label" style="color:var(--amber-lt); margin-bottom:16px;">LA OPORTUNIDAD</div>
    <h1 class="t-h1" style="max-width:900px; margin-bottom:24px;">Construye un negocio con propósito en servicios financieros</h1>
    <p class="t-body" style="color:rgba(255,255,255,0.85); font-size:18px; max-width:850px; margin-bottom:24px;">En Family First Legacy, creemos que la educación financiera puede ayudar a las familias a tomar mejores decisiones y sentirse más preparadas para el futuro. Si tienes un corazón para ayudar a las personas, ofrecemos capacitación, mentoría y apoyo para ayudarte a aprender el negocio de servicios financieros con confianza.</p>
    <p style="color:var(--amber-lt); font-size:17px; font-style:italic; margin-bottom:36px; max-width:800px;">Ahora mismo, alguien en tu vida puede necesitar tomar una decisión financiera importante; simplemente aún no sabe por dónde empezar. ¿Podrías convertirte en la persona que se presenta con orientación, educación y cuidado?</p>
    <div style="display:flex; gap:16px; flex-wrap:wrap;">
      <a href="index_es.html#contact" class="btn-cta" style="padding:14px 32px; font-size:16px; border-radius:30px;">Programa una sesión informativa</a>
      <a href="index_es.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:14px 32px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Comienza con una conversación</a>
    </div>
  </div>
</section>

<!-- Bottom Tiles Section -->
<section style="padding-bottom:80px;">
  <div class="tiles-grid">
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">TRABAJO CON PROPÓSITO</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Ayuda a las familias a entender decisiones que pueden afectar generaciones.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">CAPACITACIÓN Y MENTORÍA</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Aprende con orientación, apoyo y herramientas prácticas.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">INICIO FLEXIBLE</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Comienza a tiempo parcial o crece según tus metas y tu horario lo permitan.</div>
    </div>
    <div class="tile-card">
      <div style="color:var(--green); font-size:12px; font-weight:700; letter-spacing:2px; margin-bottom:8px;">CONSTRUYE TU PROPIO NEGOCIO</div>
      <div style="font-weight:600; font-size:15px; color:var(--dark);">Crece mediante aprendizaje, constancia, servicio y esfuerzo personal.</div>
    </div>
  </div>
</section>

<!-- Por qué importa esta oportunidad -->
<section style="padding:80px 0; background:#fff;">
  <div style="max-width:1100px; margin:0 auto; padding:0 32px;">
    
    <div style="margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">POR QUÉ IMPORTA ESTA OPORTUNIDAD</div>
      <h2 class="t-h2" style="margin-bottom:20px;">Más que un negocio. Una misión para educar a las familias.</h2>
      <p class="t-body" style="font-size:17px; margin-bottom:16px;">Muchas familias desean tomar mejores decisiones financieras, pero no siempre saben por dónde empezar. Pueden tener preguntas sobre seguro de vida, planificación para la jubilación, planificación educativa, protección de ingresos o cómo dejar un legado.</p>
      <p class="t-body" style="font-size:17px; margin-bottom:16px;">Ahí es donde la persona correcta puede marcar la diferencia.</p>
      <p class="t-body" style="font-size:17px;">En Family First Legacy, buscamos personas que se preocupen por las familias, estén dispuestas a aprender y quieran ser parte de una misión construida sobre educación, confianza y servicio.</p>
    </div>

    <!-- Para quién puede ser -->
    <div style="background:var(--bg); border:1px solid var(--line); border-radius:28px; padding:48px; margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">PARA QUIÉN PUEDE SER</div>
      <h3 class="t-h3" style="margin-bottom:24px;">Esta oportunidad puede ser una buena opción si tú:</h3>
      
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:24px;">
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Te importa ayudar a las familias</h4>
          <p class="t-body" style="font-size:14px;">Disfrutas escuchar, animar a los demás y ayudar a las personas a entender decisiones importantes.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Quieres construir algo propio</h4>
          <p class="t-body" style="font-size:14px;">Entiendes que el crecimiento requiere esfuerzo, paciencia, constancia y disposición para aprender.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">No quieres presionar a las personas</h4>
          <p class="t-body" style="font-size:14px;">Crees que las familias merecen ser educadas, respetadas y guiadas, no presionadas. Cuando te enfocas en servir correctamente, el negocio crece de forma natural mediante confianza y cuidado.</p>
        </div>
        <div>
          <h4 style="font-size:16px; font-weight:700; color:var(--dark); margin-bottom:8px;">Necesitas flexibilidad</h4>
          <p class="t-body" style="font-size:14px;">Puedes comenzar a tiempo parcial mientras equilibras trabajo, familia, estudios u otras responsabilidades.</p>
        </div>
      </div>
    </div>

    <!-- Una oportunidad real para crecer y servir -->
    <div style="margin-bottom:60px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">DIVULGACIÓN TRANSPARENTE</div>
      <h2 class="t-h2" style="margin-bottom:20px;">Una oportunidad real para crecer y servir</h2>
      <p class="t-body" style="font-size:16px; margin-bottom:16px;">Esta oportunidad es para personas que desean construir en servicios financieros mientras ayudan a las familias a tomar decisiones informadas. No es un empleo tradicional con salario; es una oportunidad de negocio basada en comisiones. Antes de servir a las familias como profesional con licencia, se requiere la licencia adecuada. El crecimiento depende del aprendizaje, la constancia, el esfuerzo y la capacidad de servir bien a las personas.</p>
      <p class="t-body" style="font-size:16px; margin-bottom:16px;">Para la persona adecuada, esto puede ser un camino significativo hacia el crecimiento personal, el desarrollo profesional y una oportunidad de ingresos. Los resultados no están garantizados y pueden variar según el esfuerzo individual, la capacitación, la constancia, el tiempo dedicado, las necesidades de los clientes, la disponibilidad de productos, la aprobación de la compañía y otros factores comerciales.</p>
      <p class="t-body" style="font-size:16px;">Lo más importante es que este trabajo se trata de personas. Hay una verdadera satisfacción en ayudar a las familias a entender sus opciones, proteger lo que más importa y sentirse más preparadas para el futuro.</p>
    </div>

    <!-- Nuestro proceso simple de inicio -->
    <div style="background:var(--green-lite); border:1px solid var(--green); border-radius:28px; padding:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:12px;">NUESTRO PROCESO SIMPLE DE INICIO</div>
      <h2 class="t-h2" style="color:var(--green); margin-bottom:32px;">4 pasos para comenzar</h2>
      
      <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:24px;">
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">01 — Sesión informativa</div>
          <p class="t-body" style="font-size:14px;">Comenzamos con una conversación sencilla para que puedas aprender qué es la oportunidad, cómo funciona el negocio, cómo funciona la compensación y si puede ajustarse a tus metas.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">02 — Orientación para la licencia</div>
          <p class="t-body" style="font-size:14px;">Antes de poder recomendar opciones de seguro de vida o ayudar a las familias a solicitar cobertura, debes tener la licencia adecuada. Te ayudamos a entender claramente los pasos para obtener la licencia.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">03 — Capacitación y mentoría</div>
          <p class="t-body" style="font-size:14px;">Comienzas a aprender cómo hablar con las familias, entender conceptos financieros básicos y servir a las personas con cuidado y profesionalismo.</p>
        </div>
        <div>
          <div style="font-size:24px; font-weight:800; color:var(--green); margin-bottom:8px;">04 — Construye con apoyo</div>
          <p class="t-body" style="font-size:14px;">A medida que creces, recibes orientación continua, herramientas y apoyo para ayudarte a desarrollar tus habilidades y confianza.</p>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- Opportunity FAQs -->
<section style="padding:80px 0; background:var(--bg);">
  <div style="max-width:900px; margin:0 auto; padding:0 32px;">
    <div style="text-align:center; margin-bottom:48px;">
      <div class="t-label" style="color:var(--green); margin-bottom:8px;">PREGUNTAS FRECUENTES</div>
      <h2 class="t-h2">Preguntas frecuentes sobre la oportunidad</h2>
    </div>

    <div class="faq-list">
      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Esto es un empleo o una oportunidad de negocio? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Esta es una oportunidad de negocio basada en comisiones dentro de la industria de servicios financieros, no un empleo tradicional con salario. Comenzamos con una sesión informativa para que puedas entender cómo funciona la oportunidad, qué licencia se requiere, cómo funciona la compensación y si puede ajustarse a tus metas.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Qué pasa si no soy bueno vendiendo o convenciendo a las personas? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Está bien. No buscamos vendedores insistentes. Buscamos personas que se preocupen, escuchen, aprendan y quieran ayudar a las familias a entender sus opciones. Esta oportunidad está construida alrededor de la educación, no de la presión. Aprenderás a hacer buenas preguntas, explicar conceptos financieros con claridad y ayudar a las familias a tomar decisiones informadas a su propio ritmo.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Necesito una licencia? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Sí. Para recomendar opciones de seguro de vida o ayudar a las familias a solicitar cobertura, debes tener la licencia adecuada. Te guiamos en los pasos para obtener la licencia para que entiendas lo que se requiere antes de servir a las familias como profesional con licencia.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Necesito experiencia en servicios financieros? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. Muchas personas comienzan sin experiencia previa en servicios financieros. Lo más importante es tu disposición para aprender, seguir el proceso y servir a las familias con honestidad y cuidado.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Puedo comenzar a tiempo parcial? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Sí. Muchas personas comienzan a tiempo parcial mientras equilibran trabajo, familia, estudios u otras responsabilidades.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Recibiré capacitación? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Sí. La capacitación, mentoría y apoyo continuo son parte del proceso.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Los ingresos están garantizados? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">No. Esta es una oportunidad de negocio basada en comisiones, por lo que los ingresos, ascensos y resultados comerciales no están garantizados. Los resultados pueden variar según el esfuerzo individual, la capacitación, la constancia, el tiempo dedicado, la capacidad de servir bien a las familias, las necesidades de los clientes, la disponibilidad de productos, la aprobación de la compañía y otros factores comerciales.</div>
      </div>

      <div class="faq-item" onclick="this.classList.toggle('open')">
        <div class="faq-question">¿Quién puede ser una buena opción para esta oportunidad? <span class="faq-icon">▼</span></div>
        <div class="faq-answer">Alguien que se preocupa por ayudar a las familias, acepta orientación, se comunica bien, entiende que los resultados requieren esfuerzo y está dispuesto a aprender a servir a las personas con profesionalismo e integridad.</div>
      </div>
    </div>
  </div>
</section>

<!-- Final CTA Section -->
<section style="padding:100px 0; background:linear-gradient(135deg, #3A2060 0%, #1A0D30 100%); color:#fff; text-align:center;">
  <div style="max-width:800px; margin:0 auto; padding:0 32px;">
    <h2 class="t-h2" style="color:#fff; margin-bottom:20px;">¿Listo para aprender más?</h2>
    <p style="font-size:17px; color:rgba(255,255,255,0.85); margin-bottom:36px; line-height:1.7;">Si buscas una oportunidad significativa, crecimiento personal y una forma de construir en servicios financieros mientras ayudas a las familias a tomar decisiones informadas, nos encantaría hablar contigo.</p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap;">
      <a href="index_es.html#contact" class="btn-cta" style="padding:16px 36px; font-size:17px; border-radius:30px; display:inline-block;">Programa una sesión informativa</a>
      <a href="index_es.html#contact" style="background:rgba(255,255,255,0.12); color:#fff; padding:16px 36px; border-radius:30px; text-decoration:none; font-weight:600; border:1px solid rgba(255,255,255,0.2);">Comienza con una conversación</a>
    </div>
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
    print("  ✓ Created opportunity.html & opportunity_es.html")

if __name__ == "__main__":
    print("=== Creating Opportunity Standalone Pages ===")
    build_opportunity_en()
    build_opportunity_es()
    print("=== Done! ===")
