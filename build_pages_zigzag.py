import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

# 1. Load the main homepage (master template)
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    master_content = f.read()

hero_idx = master_content.find('<!-- HERO SLIDESHOW ──────────────────────────────────── -->')
header_part = master_content[:hero_idx]
contact_idx = master_content.find('<section id="contact">')
footer_part = master_content[contact_idx:]

# Fix the JS in footer_part so it doesn't crash on subpages
js_fix = """
    if (prevBtn) prevBtn.disabled = currentIdx === 0;
    if (nextBtn) nextBtn.disabled = currentIdx === maxIndex;
"""
footer_part = footer_part.replace('prevBtn.disabled = currentIdx === 0;', js_fix).replace('nextBtn.disabled = currentIdx === maxIndex;', '')

# Wrap the slideshow engine so it doesn't throw a null error on document.getElementById('hero')
footer_part = footer_part.replace("const SLIDE_DURATION = 6500;", "if(document.getElementById('hero')){\nconst SLIDE_DURATION = 6500;")
footer_part = footer_part.replace("// ── Navbar + active pills", "}\n// ── Navbar + active pills")

extra_css = """
<style>
/* Force ALL animated elements visible on subpages */
[data-reveal], [data-reveal].on,
[data-stagger] > *,
.service-row, .service-row.on,
.sm-item, .number-item, .ps, .rv-card,
.faq-item, .glass-card,
#contact, #contact [data-reveal], #contact [data-stagger] > *,
#cta-banner, #cta-banner [data-reveal], #cta-banner [data-stagger] > *,
footer, footer [data-reveal], footer [data-stagger] > * {
    opacity: 1 !important;
    transform: none !important;
    visibility: visible !important;
}

/* Mobile hamburger menu support */
@media(max-width:768px) {
  .nav-toggle { display:block !important; }
  .nav-links { display:none !important; }
  .static-hero { padding-top: 140px !important; min-height: auto !important; }
}

/* ──────────────────────────────────────────────────────
   LIQUID GLASS HERO (FULL SCREEN + PARALLAX)
────────────────────────────────────────────────────── */
.static-hero { 
    position: relative; 
    min-height: 100vh; /* Full screen */
    display: flex; 
    flex-direction: column;
    align-items: center; 
    justify-content: flex-end; /* Push content down slightly */
    padding: 200px 20px 60px; 
    background-size: cover; 
    background-position: center; 
    background-attachment: fixed; /* Parallax effect */
    overflow: hidden;
}
.static-hero::before { 
    content: ''; 
    position: absolute; 
    inset: 0; 
    /* Beautiful deep gradient */
    background: linear-gradient(to bottom, rgba(10,10,15,0.75) 0%, rgba(10,10,15,0.4) 40%, rgba(10,10,15,0.95) 100%); 
    z-index: 1; 
}
.sh-content { 
    position: relative; 
    z-index: 2; 
    max-width: 900px; 
    text-align: center; 
    margin-bottom: 60px;
    animation: fadeInDown 1s cubic-bezier(0.2,0.8,0.2,1) forwards;
}
@keyframes fadeInDown {
    from { opacity: 0; transform: translateY(-30px); }
    to { opacity: 1; transform: translateY(0); }
}

.sh-badge { 
    display: inline-block; font-family: var(--font-body); font-size: 13px; font-weight: 700; 
    letter-spacing: 0.18em; text-transform: uppercase; color: #fff; 
    padding: 10px 24px; 
    background: rgba(29,158,117,0.35);
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.25); 
    border-radius: 30px; margin-bottom: 28px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.15);
    text-shadow: 0 1px 4px rgba(0,0,0,0.4);
}
.sh-title { font-family: var(--font-head); font-size: clamp(36px, 5vw, 56px); font-weight: 400; color: #fff; line-height: 1.1; margin-bottom: 24px; }
.sh-sub { font-family: var(--font-body); font-size: clamp(16px, 2vw, 20px); color: rgba(255,255,255,0.7); line-height: 1.6; margin-bottom: 32px; }
.sh-hook { font-family: var(--font-head); font-size: 22px; color: var(--amber); font-style: italic; border-left: 2px solid var(--amber); padding-left: 20px; text-align: left; max-width: 700px; margin: 0 auto; }

/* Liquid Glass Cards */
.sh-stats-container {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 1200px;
}
.numbers-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}
@media (max-width: 900px) {
    .numbers-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 500px) {
    .numbers-grid { grid-template-columns: 1fr; }
}

.glass-card {
    background: rgba(255, 255, 255, 0.03); /* Extremely transparent */
    backdrop-filter: blur(24px); /* Heavy glass blur */
    -webkit-backdrop-filter: blur(24px);
    border: 1px solid rgba(255, 255, 255, 0.08); /* Subtle white edge */
    border-radius: 24px;
    padding: 40px 20px;
    text-align: center;
    box-shadow: 0 10px 40px 0 rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255,255,255,0.1);
    transition: transform 0.5s cubic-bezier(0.2,0.8,0.2,1), background 0.5s, border-color 0.5s, box-shadow 0.5s;
    transform: translateY(60px);
    opacity: 0;
    animation: slideUpGlass 1s cubic-bezier(0.2,0.8,0.2,1) forwards;
}

/* Staggered entry */
.glass-card:nth-child(1) { animation-delay: 0.2s; }
.glass-card:nth-child(2) { animation-delay: 0.35s; }
.glass-card:nth-child(3) { animation-delay: 0.5s; }
.glass-card:nth-child(4) { animation-delay: 0.65s; }

@keyframes slideUpGlass {
    to { transform: translateY(0); opacity: 1; }
}

.glass-card:hover {
    transform: translateY(-12px) !important;
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.25);
    box-shadow: 0 20px 50px 0 rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255,255,255,0.3);
}

.glass-num {
    font-family: var(--font-head);
    font-size: clamp(36px, 4vw, 52px);
    font-weight: 700;
    color: #fff;
    line-height: 1;
    margin-bottom: 12px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}
.glass-label {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.7);
}

/* ──────────────────────────────────────────────────────
   MICRO-INTERACTIONS & BODY ANIMATIONS
────────────────────────────────────────────────────── */
.service-row {
    transition: transform 0.6s cubic-bezier(0.2,0.8,0.2,1);
}
.sr-photo-wrap {
    overflow: hidden; 
    border-radius: 24px;
    transform: translateY(0) scale(1);
    transition: transform 0.7s cubic-bezier(0.2,0.8,0.2,1), box-shadow 0.7s;
}
.sr-photo {
    transition: transform 1.2s cubic-bezier(0.2,0.8,0.2,1);
}

/* Hover effects */
.service-row:hover .sr-photo-wrap {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(0,0,0,0.5);
}
.service-row:hover .sr-photo {
    transform: scale(1.08);
}
.service-row:hover .sr-title {
    color: var(--amber); /* Subtle color shift on hover */
    transition: color 0.4s ease;
}

</style>
"""
header_part = header_part.replace('</head>', extra_css + '\n</head>')

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
                "img": "images/probate_trap_diverse_1777393105349.png",
                "flip": False
            },
            {
                "num": "02",
                "title": "Chronic<br><em>Illness.</em>",
                "body": "You don't have to die to leave your family in crisis. A severe diagnosis like MS or severe arthritis can end your ability to work, stopping your paycheck while the mortgage continues. The right living benefits policy ensures your family's life isn't derailed by your health.",
                "img": "images/chronic_illness_diverse_1777393119808.png",
                "flip": True
            },
            {
                "num": "03",
                "title": "Critical<br><em>Illness.</em>",
                "body": "A critical illness policy pays a tax-free lump sum — often $25,000 to $100,000+ — at diagnosis of a heart attack, stroke, or cancer. No restrictions. Pay the mortgage, cover treatment gaps, or simply keep your family's life intact while you heal.",
                "img": "images/critical_illness_diverse_1777393231898.png",
                "flip": False
            },
            {
                "num": "04",
                "title": "The Costly<br><em>Mistake.</em>",
                "body": "Most people rely solely on employer disability. But short-term only lasts a few months, and long-term often pays only 50-60% of your base salary—and it's taxable. You need an independent safety net that travels with you and pays what you actually need.",
                "img": "images/costly_mistake_diverse_1777393245000.png",
                "flip": True
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
                "img": "images/market_volatility_diverse_1777393133743.png",
                "flip": False
            },
            {
                "num": "02",
                "title": "The Tax<br><em>Timebomb.</em>",
                "body": "Money in a 401(k) isn't fully yours—you have a silent partner called the IRS. We help you structure tax-advantaged vehicles like Indexed Universal Life to provide a stream of tax-free income when you need it most.",
                "img": "images/tax_timebomb_diverse_1777393258870.png",
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
                "img": "images/college_savings_diverse_1777393273467.png",
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
                "img": "images/financial_strategy_hispanic_1777333606672.png",
                "flip": False
            },
            {
                "num": "02",
                "title": "Debt<br><em>Management.</em>",
                "body": "Not all debt is bad, but consumer debt will destroy wealth. We teach strategies to rapidly eliminate high-interest debt while simultaneously building liquid savings, so you stop moving one step forward and two steps back.",
                "img": "images/opportunity_photo_diverse_1777333636514.png",
                "flip": True
            },
            {
                "num": "03",
                "title": "Legacy<br><em>Transfer.</em>",
                "body": "Generational wealth isn't just about leaving money; it's about leaving it efficiently. We structure trusts and life insurance payouts to ensure your assets pass to your children tax-free and protected from their future creditors or divorces.",
                "img": "images/wealth_transfer_diverse_1777393288351.png",
                "flip": False
            }
        ]
    },
    {
        "filename": "estate_planning.html",
        "badge": "Estate & Legacy",
        "title": "Build a legacy that lasts for generations.",
        "sub": "Ensure your assets reach the people and causes you care about, without being diminished by taxes or tied up in probate court.",
        "hook": "Who will decide what happens to your life's work?",
        "hero_img": "images/hero_estate_diverse_1777335759302.png",
        "stats": [
            {"num": "100%", "label": "Control Maintained"},
            {"num": "0", "label": "Probate Delays"},
            {"num": "Tax", "label": "Efficient Transfers"},
            {"num": "Peace", "label": "Of Mind"}
        ],
        "rows": [
            {
                "num": "01",
                "title": "Will vs.<br><em>Trust.</em>",
                "body": "A will still goes through probate court, making your estate public and costing your family time and money. A trust bypasses probate, keeping your affairs private and delivering assets immediately.",
                "img": "images/probate_trap_diverse_1777393105349.png",
                "flip": False
            },
            {
                "num": "02",
                "title": "Wealth<br><em>Preservation.</em>",
                "body": "Estate taxes can consume a massive portion of what you leave behind. We work with legal professionals to structure life insurance and trusts that provide the liquidity needed to pay these taxes, preserving your physical assets.",
                "img": "images/wealth_transfer_diverse_1777393288351.png",
                "flip": True
            },
            {
                "num": "03",
                "title": "Generational<br><em>Impact.</em>",
                "body": "Whether it is endowing a charity, funding a grandchild's education, or ensuring a special needs dependent is cared for for life—we help you design a financial structure that guarantees your wishes are carried out exactly as intended.",
                "img": "images/andre_and_eline_about_1777333551750.png",
                "flip": False
            }
        ]
    }
]

faq_data_map = {
    "family_protection.html": [
        {"q": "What is the primary purpose of Family Protection insurance?", "a": "Its main goal is to replace your income and cover living expenses, debts, and future goals if you pass away prematurely, ensuring your family's lifestyle isn't disrupted."},
        {"q": "Does my employer's life insurance offer enough protection?", "a": "Typically, no. Most employer plans cover only 1-2 times your salary and end when you leave the job. We recommend owning an independent policy that stays with you."},
        {"q": "What are living benefits?", "a": "Living benefits are riders on a life insurance policy that allow you to access your death benefit early if you suffer a qualifying terminal, chronic, or critical illness."},
        {"q": "How much life insurance do I actually need?", "a": "A common rule of thumb is 10-15 times your annual income, but the exact amount depends on your debts, mortgage, number of children, and future goals like college funding."},
        {"q": "What is the difference between Term and Permanent insurance?", "a": "Term insurance covers you for a specific period (e.g., 10-30 years) and is highly affordable. Permanent insurance (like IUL or Whole Life) lasts your entire life and builds cash value."},
        {"q": "Can life insurance bypass the probate process?", "a": "Yes! Because life insurance is a contract with a named beneficiary, the payout avoids the lengthy and expensive probate court process and goes directly to your heirs."},
        {"q": "Are life insurance payouts taxable?", "a": "In almost all cases, the death benefit from a life insurance policy is paid out to your beneficiaries completely income-tax-free."},
        {"q": "Can stay-at-home parents get life insurance?", "a": "Absolutely. The financial value of a stay-at-home parent is massive (childcare, household management, etc.). If they were to pass away, the surviving spouse would need funds to cover these new costs."},
        {"q": "Do I need to take a medical exam to get covered?", "a": "Not necessarily. Many top-rated carriers now offer 'non-med' or simplified issue policies that use a quick health questionnaire and background check instead of a physical exam."},
        {"q": "When is the best time to buy life insurance?", "a": "Right now. Life insurance rates are based on your age and health. Every year you wait, the cost goes up, and you risk developing a condition that makes you uninsurable."}
    ],
    "retirement_planning.html": [
        {"q": "Why shouldn't I rely entirely on a 401(k) or IRA?", "a": "These accounts are subject to market volatility and future tax increases. Diversifying with tax-free and market-protected vehicles ensures a safer, more stable retirement."},
        {"q": "What is a Fixed Indexed Annuity (FIA)?", "a": "An FIA is a retirement product that protects your principal from market downturns (a 0% floor) while allowing you to capture a portion of market gains when the index goes up."},
        {"q": "Will I lose my money if the stock market crashes?", "a": "Not if your money is in a fixed indexed product like an FIA or IUL. These products are guaranteed not to lose value due to market drops."},
        {"q": "What is the 'tax timebomb' in retirement planning?", "a": "Money in 401(k)s and traditional IRAs is tax-deferred, meaning you haven't paid taxes on it yet. If tax rates rise in the future, you could lose a massive portion of your savings to the IRS."},
        {"q": "Can an annuity provide a guaranteed income for life?", "a": "Yes! Many annuities offer lifetime income riders that guarantee you will receive a specific paycheck every month for the rest of your life, even if your account balance goes to zero."},
        {"q": "What is the 'Safe Withdrawal Rate'?", "a": "Historically, financial planners recommended withdrawing 4% of your portfolio per year. Due to modern market volatility and inflation, many now suggest 3% or less to ensure you don't run out of money."},
        {"q": "How does Indexed Universal Life (IUL) help with retirement?", "a": "An IUL allows your cash value to grow tax-deferred based on a market index. You can then borrow against that cash value tax-free to supplement your retirement income."},
        {"q": "Are annuities only for wealthy individuals?", "a": "No, annuities can be funded with as little as $10,000. They are designed for anyone who wants to protect their savings and guarantee an income stream in retirement."},
        {"q": "How do taxes impact my Social Security benefits?", "a": "Depending on your combined income, up to 85% of your Social Security benefits may be subject to federal income tax. Proper planning can help minimize this impact."},
        {"q": "Is it too late to start planning for retirement?", "a": "It's never too late. Even if you are 5 or 10 years away from retirement, we can implement strategies to protect the money you've saved and maximize your future income."}
    ],
    "education_planning.html": [
        {"q": "What are the limitations of a traditional 529 Plan?", "a": "While 529 plans offer tax-free growth for education, the funds are heavily penalized if your child decides not to go to college and you withdraw the money for non-educational purposes."},
        {"q": "How does life insurance help pay for college?", "a": "Cash value from permanent life insurance (like an IUL) can be accessed tax-free to pay for tuition, housing, or any other expense, and it doesn't count against FAFSA financial aid calculations."},
        {"q": "Does a 529 plan impact my child's financial aid?", "a": "Yes, a 529 plan is considered a parental asset on the FAFSA, which can reduce the amount of need-based financial aid your child qualifies for."},
        {"q": "What if my child decides not to attend college?", "a": "If you use an IUL or other cash-value vehicle, the money is fully flexible. Your child can use it to start a business, buy a home, or keep it growing for their own retirement without penalties."},
        {"q": "Is the cash value in an IUL guaranteed to grow?", "a": "IUL policies have a 0% floor, meaning you will never lose cash value due to a market crash. The growth depends on the performance of the chosen market index, up to a cap."},
        {"q": "When should I start saving for my child's education?", "a": "As early as possible. The power of compound interest means that starting when your child is a baby requires much less money out-of-pocket than waiting until they are in high school."},
        {"q": "Can grandparents contribute to an IUL for education?", "a": "Absolutely. Grandparents can fund a policy on their grandchild, providing a tax-advantaged gift that will grow and be available for college or other life milestones."},
        {"q": "What happens if the stock market drops right before tuition is due?", "a": "If your funds are in a 529 plan invested in mutual funds, you could lose a significant portion. If your funds are in an IUL, your cash value is protected from market losses via the 0% floor."},
        {"q": "Can I use an IUL for private K-12 schooling?", "a": "Yes! Because you can access the cash value for any reason, you can easily use the funds to pay for private school tuition before college."},
        {"q": "Is it complicated to set up a life insurance policy for a child?", "a": "Not at all. Juvenile policies are typically very affordable and easy to qualify for, locking in their insurability for the rest of their lives."}
    ],
    "financial_strategy.html": [
        {"q": "What is the Rule of 72?", "a": "The Rule of 72 is a simple formula to estimate how long it takes for an investment to double. Divide 72 by your annual rate of return. For example, at a 7% return, your money doubles in about 10 years."},
        {"q": "How do you help with debt management?", "a": "We analyze your current debts and implement strategies like the 'snowball' or 'avalanche' methods to accelerate payoff, freeing up cash flow to redirect into wealth-building vehicles."},
        {"q": "What does it mean to be your own bank?", "a": "This concept involves using a high-cash-value life insurance policy to finance major purchases (cars, homes, business expenses) by borrowing against your own policy while your underlying cash value continues to grow."},
        {"q": "How can I protect my assets from market crashes?", "a": "We utilize indexed products, such as Fixed Indexed Annuities (FIAs) and Indexed Universal Life (IUL), which credit interest based on a market index but feature a 0% floor to protect against losses."},
        {"q": "What is a 'tax-free retirement'?", "a": "It refers to structuring your savings in vehicles like Roth IRAs or cash-value life insurance so that your withdrawals in retirement are not subject to federal or state income taxes."},
        {"q": "Why is compound interest so important?", "a": "Compound interest is when you earn interest on both your original money and the interest it has already earned. Over time, it creates an exponential growth curve that is the foundation of wealth building."},
        {"q": "Do I need a financial strategy if I'm not wealthy?", "a": "Yes! A financial strategy is exactly how you *become* wealthy. We help everyday families optimize their budgets, eliminate debt, and start saving efficiently, regardless of their current income."},
        {"q": "What is sequence of returns risk?", "a": "It's the danger of experiencing negative market returns early in your retirement. If the market crashes right after you stop working, withdrawing money compounds the losses and can destroy your portfolio."},
        {"q": "How does an IUL compare to a Roth IRA?", "a": "Both offer tax-free growth and tax-free withdrawals. However, an IUL has no contribution limits, no income restrictions, and includes a death benefit, whereas a Roth IRA has strict IRS limits."},
        {"q": "What is a Financial Needs Analysis (FNA)?", "a": "An FNA is our free, comprehensive review of your current financial situation, debts, goals, and existing policies, allowing us to build a customized roadmap to get you to your goals."}
    ],
    "estate_planning.html": [
        {"q": "What is the difference between a Will and a Trust?", "a": "A Will states your wishes but still must go through probate court. A Trust is a legal entity that holds your assets and transfers them to your heirs privately, bypassing the entire probate process."},
        {"q": "Why should I avoid probate?", "a": "Probate is a public, time-consuming (9-24 months), and expensive court process. Lawyer fees and court costs can drain 3-8% of your estate's total value before your family sees anything."},
        {"q": "Does life insurance go through probate?", "a": "No. As long as you have a named, living beneficiary, life insurance death benefits bypass probate and are paid directly and privately to your loved ones, usually within a few weeks."},
        {"q": "What happens if I die without an estate plan?", "a": "You die 'intestate.' The state decides who gets your assets based on local laws, which may completely conflict with your actual wishes, and the court will decide who raises your minor children."},
        {"q": "Can an estate plan protect my children's inheritance from divorce?", "a": "Yes. A properly structured trust can stipulate that the assets belong only to your bloodline, protecting the inheritance if your child goes through a divorce or faces lawsuits."},
        {"q": "What are estate taxes?", "a": "Estate taxes (often called the 'death tax') are levied on the transfer of the estate of a deceased person. While the federal exemption is currently high, state-level estate taxes can apply to much smaller estates."},
        {"q": "How can life insurance help pay estate taxes?", "a": "If your estate is subject to taxes, your heirs may be forced to sell property or businesses to pay the IRS. An Irrevocable Life Insurance Trust (ILIT) can provide immediate, tax-free cash to pay the tax bill."},
        {"q": "Do I need an estate plan if I'm not rich?", "a": "Yes. Estate planning isn't just about money; it's about designating guardians for your children, establishing healthcare directives if you're incapacitated, and ensuring a smooth transition of your home and bank accounts."},
        {"q": "Can I change my estate plan later?", "a": "Yes, a Revocable Living Trust and your Will can be altered, amended, or completely revoked at any time while you are still alive and of sound mind."},
        {"q": "What is a living will or healthcare directive?", "a": "It is a legal document that specifies your preferences for medical care (like life support) if you are unable to make decisions for yourself, taking the emotional burden off your family."}
    ]
}

def build_page_html(data):
    hero = f'''
    <section class="static-hero" style="background-image:url('{data['hero_img']}');">
      <div class="sh-content">
        <div class="sh-badge">{data['badge']}</div>
        <h1 class="sh-title">{data['title']}</h1>
        <p class="sh-sub">{data['sub']}</p>
        <div class="sh-hook">{data['hook']}</div>
      </div>
      
      <div class="sh-stats-container">
        <div class="container-full">
          <div class="numbers-grid">
    '''
    for i, st in enumerate(data['stats']):
        hero += f'''
            <div class="glass-card">
              <div class="glass-num">{st['num']}</div>
              <div class="glass-label">{st['label']}</div>
            </div>
        '''
    hero += '''
          </div>
        </div>
      </div>
    </section>
    '''
    
    rows_html = '''
    <section id="services" style="padding-top: 100px;">
      <div class="container">
    '''
    for r in data['rows']:
        flip_cls = " flip" if r['flip'] else ""
        rows_html += f'''
        <div class="service-row{flip_cls}" data-reveal>
          <div class="sr-photo-wrap">
            <img class="sr-photo loaded" src="{r['img']}" alt="{r['title'].replace('<br>', ' ').replace('<em>', '').replace('</em>', '')}">
          </div>
          <div class="sr-content" data-reveal="right" data-delay="2">
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
    
    # ─── JSON-LD SCHEMA ───
    faqs_for_page = faq_data_map.get(data['filename'], [])
    json_ld = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Service", "FAQPage"],
  "name": "''' + data['badge'] + '''",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Family First Legacy",
    "image": "https://family1stlegacy.com/images/FamilyFirstLogo.png"
  },
  "description": "''' + data['sub'].replace('"', "'") + '''",
  "mainEntity": [
'''
    faq_entities = []
    for faq in faqs_for_page:
        faq_entities.append(f'''    {{
      "@type": "Question",
      "name": "{faq['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{faq['a']}"
      }}
    }}''')
    json_ld += ',\n'.join(faq_entities)
    json_ld += '''
  ]
}
</script>
'''

    # ─── FAQ SECTION HTML ───
    faq_html = '''
    <!-- FAQ ─────────────────────────────────────────────── -->
    <section id="faq">
      <div class="container">
        <div class="faq-header">
          <p class="t-label" data-reveal><span class="green-dot"></span>Dive Deeper</p>
          <h2 class="t-h1" data-reveal data-delay="1">Frequently Asked<br><em>Questions.</em></h2>
        </div>
        <div class="faq-list">
    '''
    for faq in faqs_for_page:
        faq_html += f'''
          <div class="faq-item" data-reveal>
            <button class="faq-q" onclick="this.parentElement.classList.toggle('active')">
              {faq['q']}
              <div class="faq-icon"></div>
            </button>
            <div class="faq-a"><p>{faq['a']}</p></div>
          </div>
        '''
    faq_html += '''
        </div>
      </div>
    </section>
    '''
    
    return json_ld, hero + rows_html + faq_html

for page in pages_data:
    out_name = os.path.join(base_dir, page['filename'])
    json_ld, body_content = build_page_html(page)
    
    # Inject JSON-LD into header
    injected_header = header_part.replace('</head>', json_ld + '\n</head>')
    full_html = injected_header + body_content + footer_part
    
    # Fix logo to point to homepage
    full_html = full_html.replace('class="nav-logo" href="#"', 'class="nav-logo" href="index.html"')
    full_html = full_html.replace('href="#" class="nav-logo"', 'href="index.html" class="nav-logo"')
    
    full_html = re.sub(r'href="#about"', 'href="index.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="index.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="index.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="index.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="index.html#reviews"', full_html)

    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Generated {out_name}")
