import os
import re

base_dir = '/Users/deepankarakasajoo/Downloads/Family1stLegacy'

# 1. Load the main homepage (master template)
with open(os.path.join(base_dir, 'family1stlegacy_v2_16.html'), 'r', encoding='utf-8') as f:
    master_content = f.read()

hero_idx = master_content.find('<!-- HERO SLIDESHOW ──────────────────────────────────── -->')
header_part = master_content[:hero_idx]
contact_idx = master_content.find('<section id="contact">')
footer_part = master_content[contact_idx:]

extra_css = """
<style>
.static-hero { position: relative; min-height: 70vh; display: flex; align-items: center; justify-content: center; padding: 120px 20px 80px; background-size: cover; background-position: center; }
.static-hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to right, rgba(10,10,15,0.95) 0%, rgba(10,10,15,0.7) 100%); z-index: 1; }
.sh-content { position: relative; z-index: 2; max-width: 900px; text-align: center; }
.sh-badge { display: inline-block; font-family: var(--font-body); font-size: 12px; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green); padding: 6px 16px; border: 1px solid rgba(29,158,117,0.3); border-radius: 30px; margin-bottom: 24px; }
.sh-title { font-family: var(--font-head); font-size: clamp(36px, 5vw, 56px); font-weight: 400; color: #fff; line-height: 1.1; margin-bottom: 24px; }
.sh-sub { font-family: var(--font-body); font-size: clamp(16px, 2vw, 20px); color: rgba(255,255,255,0.7); line-height: 1.6; margin-bottom: 32px; }
.sh-hook { font-family: var(--font-head); font-size: 22px; color: var(--amber); font-style: italic; border-left: 2px solid var(--amber); padding-left: 20px; text-align: left; max-width: 700px; margin: 0 auto; }
</style>
"""
header_part = header_part.replace('</head>', extra_css + '\n</head>')

# Define the content mapping for the 4 pages
pages_data = [
    {
        "filename": "family_protection.html",
        "badge": "Family Protection",
        "title": "You work hard every day to take care of your family. But what happens if you can't?",
        "sub": "You pay the mortgage. You keep the lights on. You put food on the table. Your family's entire world runs because you show up — every single day.",
        "hook": "If my income stopped tomorrow — for any reason — how long would my family actually be okay?",
        "hero_img": "images/hero_life_insurance_diverse_1777335713599.png",
        "stats": [
            {"num": "60%", "label": "Dangerously Underinsured"},
            {"num": "1 in 4", "label": "Face Illness Before Retirement"},
            {"num": "9-24m", "label": "Average Probate Wait"},
            {"num": "$0", "label": "Cost For A Review"}
        ],
        "rows": [
            {
                "num": "01",
                "title": "The Probate<br><em>Trap.</em>",
                "body": "When you die without a proper trust or beneficiary designations, your accounts are frozen. The court takes control, and 3–8% of your estate goes to legal fees before your family sees a dollar. Life insurance bypasses this entirely, delivering tax-free cash in days.",
                "img": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=800&q=80",
                "flip": False
            },
            {
                "num": "02",
                "title": "Chronic<br><em>Illness.</em>",
                "body": "You don't have to die to leave your family in crisis. A severe diagnosis can end your ability to work, stopping your paycheck while the mortgage continues. The right living benefits policy ensures your family's life isn't derailed by your health.",
                "img": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=800&q=80",
                "flip": True
            },
            {
                "num": "03",
                "title": "The Costly<br><em>Mistake.</em>",
                "body": "Most people rely solely on employer disability. But short-term only lasts a few months, and long-term often pays only 50-60% of your base salary—and it's taxable. You need an independent safety net that travels with you and pays what you actually need.",
                "img": "images/family_protection_black_1777333563521.png",
                "flip": False
            }
        ]
    },
    {
        "filename": "retirement_planning.html",
        "badge": "Retirement Planning",
        "title": "The rules of retirement have changed. Have you adapted?",
        "sub": "Pensions are gone. Social Security is uncertain. Market volatility can wipe out a decade of gains in months. The old way of saving simply doesn't work anymore.",
        "hook": "Are you saving for retirement, or are you actually planning for it?",
        "hero_img": "images/hero_retirement_diverse_1777335727638.png",
        "stats": [
            {"num": "3.5%", "label": "The New Safe Withdrawal Rate"},
            {"num": "20+", "label": "Years Spent in Retirement"},
            {"num": "15%", "label": "Average Market Correction"},
            {"num": "0", "label": "Taxes Paid on IUL Growth"}
        ],
        "rows": [
            {
                "num": "01",
                "title": "Market<br><em>Volatility.</em>",
                "body": "If the market drops 30% the year you retire, your entire plan changes. We utilize fixed indexed products that participate in market gains but have a 0% floor—meaning when the market crashes, you lose nothing.",
                "img": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80",
                "flip": False
            },
            {
                "num": "02",
                "title": "The Tax<br><em>Timebomb.</em>",
                "body": "Money in a 401(k) isn't fully yours—you have a silent partner called the IRS. We help you structure tax-advantaged vehicles like Indexed Universal Life to provide a stream of tax-free income when you need it most.",
                "img": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=800&q=80",
                "flip": True
            },
            {
                "num": "03",
                "title": "Longevity<br><em>Risk.</em>",
                "body": "People are living longer than ever. Running out of money at 85 is a very real threat. We design guaranteed income streams, much like a personal pension, that you literally cannot outlive.",
                "img": "images/retirement_planning_black_1777333576986.png",
                "flip": False
            }
        ]
    },
    {
        "filename": "education_planning.html",
        "badge": "Education Planning",
        "title": "Give them the world, without sacrificing your retirement.",
        "sub": "College costs are rising faster than inflation. Student loan debt is crippling the next generation before they even begin. You want to help your children, but how?",
        "hook": "You can borrow for college, but you cannot borrow for retirement.",
        "hero_img": "images/hero_education_diverse_1777335740128.png",
        "stats": [
            {"num": "$100k", "label": "Average Cost of 4-Year Degree"},
            {"num": "5%", "label": "Annual Tuition Inflation"},
            {"num": "1.7T", "label": "National Student Debt"},
            {"num": "$0", "label": "Financial Aid Impact with IUL"}
        ],
        "rows": [
            {
                "num": "01",
                "title": "The 529<br><em>Trap.</em>",
                "body": "Traditional 529 plans lock your money into education-only expenses and heavily impact financial aid eligibility. If your child gets a scholarship or decides not to go to college, accessing those funds comes with severe tax penalties.",
                "img": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=800&q=80",
                "flip": False
            },
            {
                "num": "02",
                "title": "A Smarter<br><em>Alternative.</em>",
                "body": "Using cash-value life insurance for education planning provides tax-free growth that does not count against FAFSA financial aid formulas. The funds grow safely and can be used for college, a down payment on a home, or starting a business.",
                "img": "images/education_planning_hispanic_1777333593369.png",
                "flip": True
            }
        ]
    },
    {
        "filename": "financial_strategy.html",
        "badge": "Financial Strategy",
        "title": "Wealth isn't created by accident. It's built by design.",
        "sub": "The wealthy don't put all their money in a checking account or risk it all on the stock market. They use sophisticated financial vehicles to protect, grow, and transfer wealth efficiently.",
        "hook": "Are your financial decisions aligned with the future you actually want?",
        "hero_img": "images/hero_business_diverse_1777335776243.png",
        "stats": [
            {"num": "100%", "label": "Control Over Your Assets"},
            {"num": "0%", "label": "Floor on Market Losses"},
            {"num": "3-8%", "label": "Avoided in Probate Fees"},
            {"num": "Day 1", "label": "Immediate Protection"}
        ],
        "rows": [
            {
                "num": "01",
                "title": "The Rule<br><em>of 72.</em>",
                "body": "Understanding how compound interest works is the first step to financial independence. If you don't know exactly what rate of return you need to reach your goals, you are flying blind. We help you calculate your exact wealth trajectory.",
                "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "flip": False
            },
            {
                "num": "02",
                "title": "Debt<br><em>Management.</em>",
                "body": "Not all debt is bad, but consumer debt will destroy wealth. We teach strategies to rapidly eliminate high-interest debt while simultaneously building liquid savings, so you stop moving one step forward and two steps back.",
                "img": "https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?auto=format&fit=crop&w=800&q=80",
                "flip": True
            },
            {
                "num": "03",
                "title": "Legacy<br><em>Transfer.</em>",
                "body": "Generational wealth isn't just about leaving money; it's about leaving it efficiently. We structure trusts and life insurance payouts to ensure your assets pass to your children tax-free and protected from their future creditors or divorces.",
                "img": "images/financial_strategy_hispanic_1777333606672.png",
                "flip": False
            }
        ]
    }
]

def build_page_html(data):
    hero = f'''
    <section class="static-hero" style="background-image:url('{data['hero_img']}');">
      <div class="sh-content">
        <div class="sh-badge">{data['badge']}</div>
        <h1 class="sh-title">{data['title']}</h1>
        <p class="sh-sub">{data['sub']}</p>
        <div class="sh-hook">{data['hook']}</div>
      </div>
    </section>
    '''
    
    # ADDING .on CLASS SO THEY ARE VISIBLE BY DEFAULT!
    stats = '''
    <section id="numbers" style="padding: 60px 0; background: var(--dark); border-bottom: 1px solid rgba(255,255,255,0.05);">
      <div class="container-full">
        <div class="numbers-grid">
    '''
    for i, st in enumerate(data['stats']):
        stats += f'''
          <div class="number-item on" style="opacity: 1; transform: none;">
            <div class="ni-num">{st['num']}</div>
            <div class="ni-label">{st['label']}</div>
          </div>
        '''
    stats += '''
        </div>
      </div>
    </section>
    '''
    
    rows_html = '''
    <section id="services" style="padding-top: 80px;">
      <div class="container">
    '''
    for r in data['rows']:
        flip_cls = " flip" if r['flip'] else ""
        # ADDING .on CLASS HERE TOO
        rows_html += f'''
        <div class="service-row{flip_cls} on" style="opacity: 1; transform: none;">
          <div class="sr-photo-wrap">
            <img class="sr-photo" src="{r['img']}" alt="{r['title'].replace('<br>', ' ').replace('<em>', '').replace('</em>', '')}">
          </div>
          <div class="sr-content">
            <div class="sr-num">{r['num']}</div>
            <h3 class="sr-title">{r['title']}</h3>
            <p class="sr-body">{r['body']}</p>
          </div>
        </div>
        '''
    rows_html += '''
      </div>
    </section>
    '''
    
    return hero + stats + rows_html

for page in pages_data:
    out_name = os.path.join(base_dir, page['filename'])
    body_content = build_page_html(page)
    full_html = header_part + body_content + footer_part
    
    full_html = re.sub(r'href="#about"', 'href="family1stlegacy_v2_16.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="family1stlegacy_v2_16.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="family1stlegacy_v2_16.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="family1stlegacy_v2_16.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="family1stlegacy_v2_16.html#reviews"', full_html)
    full_html = full_html.replace('class="nav-logo" href="#"', 'class="nav-logo" href="family1stlegacy_v2_16.html"')

    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Generated {out_name}")
