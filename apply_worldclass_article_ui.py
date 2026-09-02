#!/usr/bin/env python3
"""
apply_worldclass_article_ui.py
Completely revamps the UI/UX of all 6 Knowledgebase article pages across English and Spanish:
1. Seamless, elegant Hero Section with unified category badge, H1 title, E-E-A-T badge, and widescreen hero image.
2. Premium typography: Spacious H2 section titles with emerald accent badges, slate-colored body text (#334155), 1.75 line-height, and spacious section padding.
3. Elevated Key Takeaways Box with gradient accent background and crisp bullet layout.
4. Clean 2-Column Sticky Sidebar Grid without harsh disconnects or awkward margins.
5. 100% responsive across mobile, tablet, and widescreen desktop.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

WORLDCLASS_ARTICLE_CSS = """
/* ─── WORLD-CLASS ARTICLE PUBLICATION UI ─── */
.article-page-wrapper {
  background: #F8FAFC !important;
  padding-bottom: 80px !important;
}

.article-hero-banner {
  background: #ffffff !important;
  border-bottom: 1px solid #E2E8F0 !important;
  padding: 48px 0 40px 0 !important;
}

.article-hero-container {
  max-width: 1080px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
  text-align: center !important;
}

.article-cat-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: rgba(29, 158, 117, 0.08) !important;
  border: 1px solid rgba(29, 158, 117, 0.2) !important;
  color: #1D9E75 !important;
  padding: 6px 16px !important;
  border-radius: 100px !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 1.2px !important;
  text-transform: uppercase !important;
  margin-bottom: 16px !important;
}

.article-main-title {
  font-family: var(--font-head), 'Plus Jakarta Sans', sans-serif !important;
  font-size: 40px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  line-height: 1.25 !important;
  margin-bottom: 20px !important;
  letter-spacing: -0.5px !important;
}

@media (max-width: 768px) {
  .article-main-title {
    font-size: 28px !important;
  }
}

.article-meta-row {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 16px !important;
  flex-wrap: wrap !important;
  margin-bottom: 32px !important;
}

.eeat-badge-hero {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: #F1F5F9 !important;
  border: 1px solid #E2E8F0 !important;
  padding: 6px 16px !important;
  border-radius: 30px !important;
  font-size: 13px !important;
  color: #334155 !important;
  font-weight: 600 !important;
}
.eeat-badge-hero svg {
  width: 15px !important;
  height: 15px !important;
  fill: #1D9E75 !important;
}

.article-hero-img-wrap {
  max-width: 1080px !important;
  margin: 0 auto !important;
  border-radius: 20px !important;
  overflow: hidden !important;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.08) !important;
}
.article-hero-img-wrap img {
  width: 100% !important;
  height: auto !important;
  max-height: 480px !important;
  object-fit: cover !important;
  display: block !important;
}

/* ─── 2-Column Grid Layout ─── */
.article-grid-container {
  max-width: 1140px !important;
  margin: 48px auto 0 auto !important;
  padding: 0 24px !important;
  display: grid !important;
  grid-template-columns: 1fr 320px !important;
  gap: 48px !important;
  align-items: flex-start !important;
}

@media (max-width: 992px) {
  .article-grid-container {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .article-sidebar-sticky {
    position: static !important;
  }
}

/* ─── Main Article Column ─── */
.article-content-card {
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  padding: 48px !important;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.03) !important;
  min-width: 0 !important;
}

@media (max-width: 640px) {
  .article-content-card {
    padding: 28px 20px !important;
    border-radius: 16px !important;
  }
}

/* ─── Key Takeaways Box ─── */
.kt-box-elevated {
  background: linear-gradient(135deg, rgba(74, 45, 122, 0.04) 0%, rgba(29, 158, 117, 0.06) 100%) !important;
  border-left: 4px solid #4A2D7A !important;
  border-radius: 16px !important;
  padding: 24px 28px !important;
  margin-bottom: 40px !important;
}
.kt-box-elevated .kt-header {
  font-size: 15px !important;
  font-weight: 800 !important;
  color: #4A2D7A !important;
  text-transform: uppercase !important;
  letter-spacing: 0.8px !important;
  margin-bottom: 14px !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
}
.kt-box-elevated ul {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 12px !important;
}
.kt-box-elevated li {
  font-size: 14.5px !important;
  color: #334155 !important;
  line-height: 1.6 !important;
  position: relative !important;
  padding-left: 20px !important;
}
.kt-box-elevated li::before {
  content: "•" !important;
  position: absolute !important;
  left: 0 !important;
  color: #1D9E75 !important;
  font-weight: bold !important;
  font-size: 18px !important;
}

/* ─── Article Typography ─── */
.article-content-card h2 {
  font-family: var(--font-head), 'Plus Jakarta Sans', sans-serif !important;
  font-size: 24px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  margin-top: 48px !important;
  margin-bottom: 18px !important;
  line-height: 1.35 !important;
  letter-spacing: -0.3px !important;
  padding-bottom: 10px !important;
  border-bottom: 2px solid #F1F5F9 !important;
}
.article-content-card h2:first-of-type {
  margin-top: 0 !important;
}

.article-content-card p {
  font-size: 16px !important;
  color: #334155 !important;
  line-height: 1.75 !important;
  margin-bottom: 20px !important;
  font-weight: 400 !important;
}

.article-content-card ul {
  margin: 0 0 24px 0 !important;
  padding-left: 20px !important;
}
.article-content-card li {
  font-size: 15.5px !important;
  color: #334155 !important;
  line-height: 1.7 !important;
  margin-bottom: 10px !important;
}

/* ─── FAQ Accordion ─── */
.article-faq-container {
  margin-top: 48px !important;
  padding-top: 36px !important;
  border-top: 2px dashed #E2E8F0 !important;
}
.article-faq-container h2 {
  border-bottom: none !important;
  margin-top: 0 !important;
  margin-bottom: 24px !important;
}
.faq-accordion-card {
  background: #F8FAFC !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 14px !important;
  padding: 20px 24px !important;
  margin-bottom: 16px !important;
}
.faq-accordion-card .faq-question {
  font-size: 16px !important;
  font-weight: 700 !important;
  color: #0F172A !important;
  margin-bottom: 8px !important;
}
.faq-accordion-card .faq-answer {
  font-size: 14.5px !important;
  color: #475569 !important;
  line-height: 1.65 !important;
}

/* ─── Educational Disclosure Card ─── */
.edu-disclosure-box {
  background: #FFFBEB !important;
  border: 1px solid #FCD34D !important;
  border-radius: 16px !important;
  padding: 20px 24px !important;
  margin-top: 40px !important;
  font-size: 13.5px !important;
  color: #92400E !important;
  line-height: 1.6 !important;
}

/* ─── Right Sticky Sidebar Widgets ─── */
.article-sidebar-sticky {
  position: sticky !important;
  top: 100px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 24px !important;
}

.sidebar-card-widget {
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  padding: 24px !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03) !important;
}

.sidebar-toc-title {
  font-size: 14px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  margin-bottom: 14px !important;
  text-transform: uppercase !important;
  letter-spacing: 0.8px !important;
}

.sidebar-toc-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}
.sidebar-toc-list a {
  color: #4A2D7A !important;
  text-decoration: none !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  line-height: 1.4 !important;
  transition: color 0.2s ease !important;
}
.sidebar-toc-list a:hover {
  color: #1D9E75 !important;
}

.sidebar-cta-widget {
  background: linear-gradient(135deg, #4A2D7A 0%, #2A1747 100%) !important;
  color: #ffffff !important;
  border: none !important;
}
.sidebar-cta-widget .scw-badge {
  display: inline-block !important;
  background: rgba(29, 158, 117, 0.25) !important;
  color: #26D07C !important;
  padding: 4px 12px !important;
  border-radius: 20px !important;
  font-size: 11px !important;
  font-weight: 800 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  margin-bottom: 12px !important;
}
.sidebar-cta-widget h3 {
  font-size: 19px !important;
  font-weight: 800 !important;
  color: #ffffff !important;
  margin-bottom: 8px !important;
  line-height: 1.3 !important;
}
.sidebar-cta-widget p {
  font-size: 13.5px !important;
  color: rgba(255, 255, 255, 0.85) !important;
  line-height: 1.5 !important;
  margin-bottom: 20px !important;
}
.sidebar-cta-widget .scw-btn {
  display: block !important;
  width: 100% !important;
  padding: 12px 16px !important;
  background: #1D9E75 !important;
  color: #ffffff !important;
  text-align: center !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  border-radius: 30px !important;
  text-decoration: none !important;
  transition: background 0.3s ease !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.3) !important;
}
.sidebar-cta-widget .scw-btn:hover {
  background: #157959 !important;
}
.sidebar-cta-widget .scw-phone {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin-top: 14px !important;
  font-size: 13px !important;
  color: rgba(255, 255, 255, 0.9) !important;
  text-decoration: none !important;
  font-weight: 600 !important;
}
.sidebar-cta-widget .scw-phone svg {
  width: 14px !important;
  height: 14px !important;
  stroke: #26D07C !important;
}
"""

def update_article_page(fname):
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Inject World-Class Article CSS
    if "WORLD-CLASS ARTICLE PUBLICATION UI" not in html:
        html = html.replace("</head>", f"<style>{WORLDCLASS_ARTICLE_CSS}</style>\n</head>")

    is_es = "_es." in fname

    # Determine Page Content
    if "family_protection" in fname:
        cat = "Protección Familiar" if is_es else "Family Protection"
        title = "¿Confía su familia solo en beneficios laborales?" if is_es else "Is Your Family Counting on Work Benefits Alone?"
        read = "5 min de lectura" if is_es else "5 min read"
        img = "images/hero_life_insurance_diverse_1777335713599.png"
        
        toc_items = [
            ("1. The Comfort and Reality of Employer Coverage", "sec-1"),
            ("2. Why Employer Coverage May Not Be Enough", "sec-2"),
            ("3. The Portability Risk: Employment Changes", "sec-3"),
            ("4. Exploring Individual Protection Options", "sec-4"),
            ("5. The Role of Living Benefits", "sec-5"),
            ("6. Calculating Your Family's Protection Need", "sec-6"),
            ("7. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Employer coverage is tied to employment:</strong> Life insurance offered through work often ends or changes when you change jobs, retire, or experience company downsizing.</li>
            <li><strong>Coverage limits may leave gaps:</strong> Work policies typically provide 1x to 2x salary, which may not fully cover long-term mortgage, debt, or income replacement needs.</li>
            <li><strong>Individual coverage offers portability:</strong> Having a personal policy outside of work ensures your family remains protected regardless of your employer status.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. The Comfort and Reality of Employer Coverage</h2>
        <p>For millions of working professionals and families, group life insurance offered through an employer is the first exposure to financial protection. It feels simple, convenient, and cost-effective. Because premiums are frequently deducted directly from payroll, many individuals assume their family's financial future is fully secured.</p>
        <p>However, while group term life insurance is a valuable employee benefit, relying on it as a family's sole financial safety net can create unforeseen vulnerabilities. Understanding the distinction between group benefits and individual coverage is an essential step in building long-term financial security.</p>

        <h2 id="sec-2">2. Why Employer Coverage May Not Be Enough</h2>
        <p>Employer-provided policies typically offer coverage equal to one or two times an employee's annual salary. While this can help cover immediate final expenses or short-term transition costs, it may fall short of addressing comprehensive, long-term family needs.</p>
        <p>Consider the real financial responsibilities a family faces:</p>
        <ul>
          <li><strong>Mortgage and Housing:</strong> Paying off a 30-year mortgage or securing ongoing rental stability.</li>
          <li><strong>Income Replacement:</strong> Replacing 5 to 10 years of ongoing income to maintain household living standards.</li>
          <li><strong>Debt Obligations:</strong> Clearing credit cards, car loans, personal loans, or private student loans.</li>
          <li><strong>Future Goals:</strong> Funding college education or vocational training for children.</li>
        </ul>

        <h2 id="sec-3">3. The Portability Risk: What Happens When Employment Changes?</h2>
        <p>The most critical limitation of employer group life insurance is lack of portability. In most cases, group coverage is directly tied to active employment. If an individual changes careers, gets laid off, leaves to start a business, or retires, the coverage typically terminates.</p>
        <p>Attempting to secure a new individual policy later in life—or after a major health diagnosis—can lead to significantly higher premiums or potential uninsurability. Establishing an individual policy early locks in rates based on current health and age, guaranteeing protection regardless of career changes.</p>

        <h2 id="sec-4">4. Exploring Individual Protection Options</h2>
        <p>Individual life insurance policies are owned by you, not your employer. They remain active as long as premiums are paid, providing portable, uninterrupted protection. Common types include:</p>
        <ul>
          <li><strong>Term Life Insurance:</strong> Provides affordable, robust protection for a specified period (e.g., 10, 20, or 30 years), ideal for mortgage protection and child-rearing years.</li>
          <li><strong>Permanent Life Insurance (Whole Life & IUL):</strong> Offers lifelong protection paired with a cash-value growth component that can accumulate over time.</li>
        </ul>

        <h2 id="sec-5">5. The Role of Living Benefits in Family Protection</h2>
        <p>Modern life insurance policies often include living benefits. Unlike traditional policies that only pay out upon death, policies with living benefit riders may allow qualifying policyholders to access a portion of their death benefit while living if diagnosed with a qualifying chronic, critical, or terminal illness.</p>

        <h2 id="sec-6">6. Calculating Your Family's Protection Need</h2>
        <p>Determining your ideal coverage amount involves evaluating your family's unique financial obligations. A common framework is the <strong>DIME Method</strong> (Debt, Income, Mortgage, Education).</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>7. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">Can I keep my employer life insurance if I quit or get laid off?</div>
            <div class="faq-answer">In most cases, group life insurance ends when your employment ends. Some policies offer conversion options to an individual policy, but conversion rates are often significantly higher than purchasing an independent individual policy in advance.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">How much life insurance do most financial professionals recommend?</div>
            <div class="faq-answer">While requirements vary by household, many financial guidelines suggest maintaining coverage equal to 7 to 10 times your annual income, accounting for mortgage balances, child education, and debt.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">Does having individual life insurance affect my work benefits?</div>
            <div class="faq-answer">No. Individual life insurance policies are completely independent of your workplace benefits and operate separately alongside any coverage provided by your employer.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "retirement" in fname:
        cat = "Jubilación" if is_es else "Retirement Planning"
        title = "¿Podrían los impuestos reducir sus ingresos de jubilación?" if is_es else "Could Taxes Reduce the Retirement Income You're Counting On?"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/hero_retirement_diverse_1777335727638.png"

        toc_items = [
            ("1. Income vs. What You Keep in Retirement", "sec-1"),
            ("2. Understanding the Three Retirement Tax Buckets", "sec-2"),
            ("3. Why Traditional 401(k)s Are Only Part of the Story", "sec-3"),
            ("4. Principal Protection with FIAs", "sec-4"),
            ("5. Managing Market Volatility", "sec-5"),
            ("6. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Tax treatment impacts retirement income:</strong> It's not just how much you save in 401(k)s or IRAs, but how much you keep after taxes in retirement.</li>
            <li><strong>The Three Tax Buckets:</strong> Diversifying between Taxable, Tax-Deferred, and Tax-Advantaged accounts provides greater flexibility in retirement.</li>
            <li><strong>Downside market protection matters:</strong> Strategies like Fixed Indexed Annuities (FIAs) offer index-linked growth potential while helping protect principal from market drops.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. Income vs. What You Keep in Retirement</h2>
        <p>When planning for retirement, many individuals focus entirely on the accumulation phase—building a target account balance in a 401(k), 403(b), or traditional IRA. However, the true measure of retirement readiness is not just your total savings balance, but your net income after taxes and market adjustments.</p>
        <p>Without a clear distribution strategy, unexpected tax rate increases or prolonged market downturns during retirement can erode purchasing power when you need it most.</p>

        <h2 id="sec-2">2. Understanding the Three Retirement Tax Buckets</h2>
        <p>Financial professionals often categorize retirement assets into three distinct tax buckets:</p>
        <ul>
          <li><strong>1. Taxable Bucket:</strong> Bank savings accounts, CDs, brokerage accounts, and individual stocks. You pay taxes annually on interest, dividends, and capital gains.</li>
          <li><strong>2. Tax-Deferred Bucket:</strong> Traditional 401(k)s, 403(b)s, and traditional IRAs. Contributions may reduce current taxable income, but distributions in retirement are taxed as ordinary income.</li>
          <li><strong>3. Tax-Advantaged Bucket:</strong> Roth IRAs, certain tax-free municipal bonds, and qualifying permanent life insurance cash values. Contributions are made with after-tax dollars, allowing qualifying distributions to be accessed tax-free under current tax laws.</li>
        </ul>

        <h2 id="sec-3">3. Why Traditional 401(k)s & IRAs Are Only Part of the Story</h2>
        <p>Employer-sponsored 401(k) plans provide excellent savings momentum, especially when matching contributions are offered. However, depending solely on tax-deferred accounts leaves your future income tied to future federal income tax rates.</p>

        <h2 id="sec-4">4. Protecting Principal with Fixed Indexed Annuities (FIAs)</h2>
        <p>A Fixed Indexed Annuity (FIA) is a contract issued by an insurance company designed to help protect principal from negative index performance while offering potential for interest growth linked to a market index (such as the S&P 500).</p>

        <h2 id="sec-5">5. Managing Market Volatility & Sequence of Returns Risk</h2>
        <p>Retiring right before or during a major market decline is known as <em>sequence of returns risk</em>. Withdrawing income from a declining stock portfolio can permanently reduce the lifespan of your savings. Incorporating principal-protected strategies helps buffer against market volatility during early retirement years.</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>6. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">What is the difference between a Fixed Annuity and a Fixed Indexed Annuity?</div>
            <div class="faq-answer">A traditional Fixed Annuity pays a fixed, guaranteed interest rate. A Fixed Indexed Annuity links interest growth to a market index performance, offering higher growth potential while maintaining principal protection against market index losses.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">Are withdrawals from a Fixed Indexed Annuity taxable?</div>
            <div class="faq-answer">Interest growth in an annuity accumulates tax-deferred. When withdrawals are taken, earnings are generally taxed as ordinary income. Withdrawals before age 59½ may be subject to a 10% IRS penalty.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "education" in fname:
        cat = "Planificación Educativa" if is_es else "Education Planning"
        title = "¿Qué pasa si el camino de su hijo cambia después de ahorrar?" if is_es else "What If Your Child's Path Changes After You Save?"
        read = "5 min de lectura" if is_es else "5 min read"
        img = "images/hero_education_diverse_1777335740128.png"

        toc_items = [
            ("1. Rising Cost of Higher Education", "sec-1"),
            ("2. Understanding 529 Plans", "sec-2"),
            ("3. If Your Child Chooses Another Path", "sec-3"),
            ("4. Cash Value (IUL) Complement", "sec-4"),
            ("5. FAFSA & Aid Treatment", "sec-5"),
            ("6. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Flexibility is critical:</strong> Children's career paths change—whether attending a 4-year university, trade school, starting a business, or pursuing alternative paths.</li>
            <li><strong>529 Plans have specific rules:</strong> 529 accounts offer tax benefits for qualified education expenses, but non-qualified withdrawals may face taxes and penalties on earnings.</li>
            <li><strong>Complementary strategies exist:</strong> Certain permanent life insurance policies (like IUL) build cash value that can be accessed for education or any other goal without restricted usage rules.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. The Rising Cost & Changing Reality of Higher Education</h2>
        <p>Every parent wants to provide their children with the foundation to pursue their dreams. However, with college tuition and education costs rising consistently year after year, planning early is essential to reduce reliance on heavy student loan debt.</p>
        <p>At the same time, the modern workforce is evolving. Young adults today pursue a wide variety of paths—including four-year universities, community colleges, trade certifications, apprenticeships, or entrepreneurship.</p>

        <h2 id="sec-2">2. Understanding 529 Education Savings Plans</h2>
        <p>A 529 Plan is a state-sponsored education savings account that allows funds to grow tax-deferred, with tax-free withdrawals when used for qualified education expenses (such as tuition, books, fees, and room and board).</p>

        <h2 id="sec-3">3. The Need for Plan B: What If Your Child Chooses Another Path?</h2>
        <p>If a child receives scholarships, decides not to attend college, or chooses a non-eligible vocational path, withdrawing earnings from a 529 plan for non-qualified expenses may incur ordinary income tax plus a 10% federal penalty on earnings.</p>

        <h2 id="sec-4">4. How Permanent Cash Value Life Insurance (IUL) Complements Savings</h2>
        <p>Permanent life insurance policies, such as Indexed Universal Life (IUL), build cash value over time that can be accessed through policy loans or withdrawals for education, starting a business, or buying a home.</p>

        <h2 id="sec-5">5. FAFSA & Financial Aid Treatment of Savings Assets</h2>
        <p>Financial-aid treatment can vary based on account ownership, the type of asset, and current FAFSA rules. Families should review current federal student-aid guidance before choosing a strategy.</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>6. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">Can cash value from life insurance be used for trade school or starting a business?</div>
            <div class="faq-answer">Yes. Policy loans or withdrawals from a permanent life insurance policy's cash value can be used for any purpose, including trade school, business startup costs, or personal expenses, without penalty.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">What happens to a 529 plan if my child gets a full scholarship?</div>
            <div class="faq-answer">If a beneficiary receives a scholarship, you can withdraw up to the scholarship amount from the 529 plan without incurring the 10% penalty, though taxes on earnings may still apply.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "living_benefits" in fname:
        cat = "Beneficios en Vida" if is_es else "Living Benefits"
        title = "¿Qué pasa si sobrevive a la enfermedad, pero sus ingresos no?" if is_es else "What If You Survive the Illness - But Your Income Does Not?"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/critical_illness_diverse_1777393231898.png"

        toc_items = [
            ("1. Surviving Serious Illness Today", "sec-1"),
            ("2. What Are Living Benefits?", "sec-2"),
            ("3. Covered Qualifying Conditions", "sec-3"),
            ("4. Financial Pressure of Medical Events", "sec-4"),
            ("5. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Insurance is not only for passing away:</strong> Modern life insurance policies can protect you while you are alive if you experience a major illness.</li>
            <li><strong>Living Benefits explained:</strong> Accelerated death benefit riders allow qualifying policyholders to access funds upon diagnosis of a covered chronic, critical, or terminal illness.</li>
            <li><strong>Income & Expense Protection:</strong> Accessing living benefits can help cover medical bills, replace lost paychecks, or pay household expenses during recovery.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. The Modern Reality: Surviving Serious Illness</h2>
        <p>Thanks to advances in medical technology, more people today survive serious health events such as heart attacks, strokes, or cancer diagnoses than ever before. However, while medical outcomes have improved, the financial impact of a prolonged recovery can be devastating to a household.</p>

        <h2 id="sec-2">2. What Are Living Benefits & Accelerated Death Benefit Riders?</h2>
        <p>Living Benefits are features included in many modern life insurance policies through Accelerated Death Benefit Riders. These riders allow an eligible policyholder to access a portion of their policy's death benefit while still living if they suffer a qualifying medical condition.</p>

        <h2 id="sec-3">3. Understanding Covered Qualifying Conditions</h2>
        <p>Depending on carrier policy terms, qualifying covered conditions generally fall into three main categories:</p>
        <ul>
          <li><strong>Terminal Illness:</strong> A diagnosed illness resulting in a limited life expectancy (typically 12 to 24 months).</li>
          <li><strong>Chronic Illness:</strong> Inability to perform at least 2 of 6 Activities of Daily Living (ADLs)—such as bathing, dressing, eating, or transferring—without assistance.</li>
          <li><strong>Critical Illness:</strong> Covered major medical events such as heart attack, stroke, invasive cancer, or organ transplant.</li>
        </ul>

        <h2 id="sec-4">4. The Financial Pressure of Serious Medical Events</h2>
        <p>Health insurance covers doctors and hospitals, but it does not cover your mortgage, groceries, car payments, or lost paychecks. Living benefit payouts provide cash flexibility that can be used for any household need during recovery.</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">Do living benefits cost extra on a life insurance policy?</div>
            <div class="faq-answer">Many carriers include accelerated death benefit riders at policy issuance with no upfront fee, though an administrative fee or actuarial discount may apply at the time benefits are accelerated.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">How does accessing living benefits affect the death benefit?</div>
            <div class="faq-answer">Accelerating benefits reduces the remaining death benefit payable to your beneficiaries upon your passing.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "financial_strategy" in fname:
        cat = "Estrategia Financiera" if is_es else "Financial Strategy"
        title = "Cómo las estrategias claras construyen seguridad duradera" if is_es else "How Clear Financial Strategies Help Families Build Security"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/financial_strategy_hispanic_1777333606672.png"

        toc_items = [
            ("1. Why Financial Clarity Matters", "sec-1"),
            ("2. The 4 Pillars of Financial Health", "sec-2"),
            ("3. Managing Cash Flow & Reserves", "sec-3"),
            ("4. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Strategy over quick fixes:</strong> Long-term financial security is built through structured, repeatable habits rather than market speculation.</li>
            <li><strong>The 4 Pillars of Financial Health:</strong> Cash Flow, Emergency Reserves, Asset Protection, and Wealth Building.</li>
            <li><strong>Professional Guidance:</strong> Working with licensed professionals helps eliminate guesswork and aligns insurance and savings tools with your real goals.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. Why Financial Clarity Matters More Than Ever</h2>
        <p>In today's fast-paced economic environment, families are flooded with conflicting financial opinions. From social media tips to complex investment jargon, it is easy to feel overwhelmed or uncertain about the best steps to take.</p>
        <p>True financial security does not require complex formulas. It requires a clear, personalized strategy that prioritizes protection, manages risk, and supports your family's core values.</p>

        <h2 id="sec-2">2. The 4 Pillars of Family Financial Health</h2>
        <p>A resilient financial plan rests on four interconnected pillars:</p>
        <ul>
          <li><strong>1. Cash Flow Management:</strong> Understanding monthly income vs. expenses to create consistent savings momentum.</li>
          <li><strong>2. Emergency Reserves:</strong> Maintaining 3 to 6 months of liquid reserves for unexpected repairs or job transitions.</li>
          <li><strong>3. Risk Protection:</strong> Securing life, disability, and health coverage to shield your earning power.</li>
          <li><strong>4. Wealth Accumulation:</strong> Utilizing tax-efficient accounts for retirement, education, and legacy goals.</li>
        </ul>

        <h2 id="sec-3">3. Managing Cash Flow & Building Emergency Reserves</h2>
        <p>Before focusing on aggressive growth strategies, securing your foundational reserves is critical. Having liquid savings prevents you from having to borrow at high interest rates or liquidate long-term investments during short-term emergencies.</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>4. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">How often should a family review their financial strategy?</div>
            <div class="faq-answer">Financial professionals recommend reviewing your strategy at least once a year, or whenever major life events occur—such as marriage, the birth of a child, a career change, or buying a home.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    else: # legacy
        cat = "Planificación de Legado" if is_es else "Legacy Planning"
        title = "Preservar su legado: Planificación para generaciones futuras" if is_es else "Preserving Your Legacy: Planning for Future Generations"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/hero_estate_diverse_1777335759302.png"

        toc_items = [
            ("1. Legacy Beyond Money", "sec-1"),
            ("2. Estate Planning Essentials", "sec-2"),
            ("3. Understanding Probate Delays", "sec-3"),
            ("4. Life Insurance for Wealth Transfer", "sec-4"),
            ("5. Frequently Asked Questions", "sec-faq")
        ]

        article_body = """
        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Legacy is more than wealth:</strong> True legacy planning encompasses financial assets, personal values, and clear instructions for your loved ones.</li>
            <li><strong>Avoiding Probate delays:</strong> Proper beneficiary designations and estate strategies help transfer assets quickly and privately without costly court delays.</li>
            <li><strong>Generational Wealth Transfer:</strong> Life insurance can help transfer wealth directly to beneficiaries, with death benefits generally received income-tax-free, helping support the financial legacy you want to leave for the next generation.</li>
          </ul>
        </div>

        <h2 id="sec-1">1. Defining What Legacy Means Beyond Money</h2>
        <p>Everything you have worked for tells a story. Legacy planning is not reserved exclusively for the wealthy—it is a vital process for any family that wants to ensure their assets, home, business, and personal values pass smoothly to the next generation.</p>
        <p>A well-crafted legacy plan can help reduce family confusion, minimize legal stress, and provide greater financial stability for your heirs.</p>

        <h2 id="sec-2">2. Estate Planning Essentials: Wills, Trusts & Beneficiaries</h2>
        <p>A legal estate plan works alongside your financial products. Primary components include:</p>
        <ul>
          <li><strong>Wills:</strong> Directs how assets are distributed and appoints guardians for minor children.</li>
          <li><strong>Trusts:</strong> Provides private asset control and distribution terms without court supervision.</li>
          <li><strong>Beneficiary Designations:</strong> Direct designations on life insurance and annuities override wills and bypass probate court.</li>
        </ul>

        <h2 id="sec-3">3. Understanding the Impact of Probate Delays</h2>
        <p>Probate is the court-supervised process of authenticating a will and distributing assets. Probate can take anywhere from several months to years, creating stress and legal expenses for surviving family members. When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free.</p>

        <h2 id="sec-4">4. Using Life Insurance for Wealth Transfer</h2>
        <p>Life insurance is one of the most efficient wealth transfer tools available. Death benefit proceeds pass to beneficiaries income-tax-free, providing liquid cash to pay final expenses, estate taxes, or equalize inheritance among children.</p>

        <div class="article-faq-container" id="sec-faq">
          <h2>5. Frequently Asked Questions</h2>
          <div class="faq-accordion-card">
            <div class="faq-question">Do life insurance proceeds go through probate?</div>
            <div class="faq-answer">No. As long as a living beneficiary is designated on the policy, life insurance death benefits pass directly to the named beneficiary outside of the probate court process.</div>
          </div>
          <div class="faq-accordion-card">
            <div class="faq-question">Are life insurance death benefits taxable to beneficiaries?</div>
            <div class="faq-answer">Under IRS Code Section 101(a), life insurance death benefits paid to a named beneficiary are generally received income-tax-free.</div>
          </div>
        </div>

        <div class="edu-disclosure-box">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    # Build TOC HTML
    toc_links_html = ""
    for label, href in toc_items:
        toc_links_html += f'<li><a href="#{href}">{label}</a></li>\n'

    toc_title = "EN ESTA GUÍA" if is_es else "IN THIS GUIDE"
    cta_badge = "CONSULTA GRATUITA" if is_es else "NO-COST CONSULTATION"
    cta_title = "¿Listo para orientación honesta?" if is_es else "Ready for Honest Guidance?"
    cta_text = "Reserve una revisión sin compromiso con un profesional con licencia." if is_es else "Schedule a review with a licensed professional — no pressure, no obligation."
    cta_btn = "Programar Revisión →" if is_es else "Schedule a Review →"
    home_target = "index_es.html#contact" if is_es else "index.html#contact"

    # Assemble World-Class Article Page Structure
    worldclass_html = f"""
    <!-- WORLD-CLASS ARTICLE HERO BANNER -->
    <div class="article-hero-banner">
      <div class="article-hero-container" data-reveal>
        <div class="article-cat-badge">
          <span style="width:6px; height:6px; background:#1D9E75; border-radius:50%;"></span>
          {cat}
        </div>
        <h1 class="article-main-title">{title}</h1>
        
        <div class="article-meta-row">
          <div class="eeat-badge-hero">
            <svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg>
            <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span>
          </div>
          <div style="font-size:13.5px; color:#64748B; font-weight:600;">• {read}</div>
        </div>

        <div class="article-hero-img-wrap" data-reveal data-delay="1">
          <img src="{img}" alt="{title}">
        </div>
      </div>
    </div>

    <!-- 2-COLUMN ARTICLE CONTENT GRID -->
    <div class="article-page-wrapper">
      <div class="article-grid-container">
        
        <!-- LEFT CONTENT COLUMN -->
        <div class="article-content-card" data-reveal>
          {article_body}
        </div>

        <!-- RIGHT STICKY SIDEBAR -->
        <div class="article-sidebar-sticky">
          
          <!-- Widget 1: Table of Contents -->
          <div class="sidebar-card-widget">
            <div class="sidebar-toc-title">📖 {toc_title}</div>
            <ul class="sidebar-toc-list">
              {toc_links_html}
            </ul>
          </div>

          <!-- Widget 2: Consultation CTA Card -->
          <div class="sidebar-card-widget sidebar-cta-widget">
            <span class="scw-badge">{cta_badge}</span>
            <h3>{cta_title}</h3>
            <p>{cta_text}</p>
            <a href="{home_target}" class="scw-btn">{cta_btn}</a>
            <a href="tel:+14696081595" class="scw-phone">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
              Call (469) 608-1595
            </a>
          </div>

          <!-- Widget 3: Trust Badges -->
          <div class="sidebar-card-widget" style="background:#F8FAFC;">
            <div style="font-size:12px; font-weight:800; color:#4A2D7A; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">Why Family First Legacy</div>
            <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Licensed & Insured</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> 24hr Response</li>
              <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Your Privacy Matters</li>
            </ul>
          </div>

        </div>
      </div>
    </div>
"""

    # Clean out any old sections
    html = re.sub(r'<!-- ARTICLE HERO HEADER -->.*?</section>', '', html, flags=re.DOTALL)
    html = re.sub(r'<!-- WORLD-CLASS ARTICLE HERO BANNER -->.*?<!-- MORE ARTICLES', '<!-- MORE ARTICLES', html, flags=re.DOTALL)
    html = re.sub(r'<section id="blog-article"[^>]*>.*?</section>', '', html, flags=re.DOTALL)

    # Inject worldclass_html right before MORE ARTICLES
    if "<!-- MORE ARTICLES" in html:
        html = html.replace("<!-- MORE ARTICLES", f"{worldclass_html}\n    <!-- MORE ARTICLES")
    elif "<!-- CTA BANNER" in html:
        html = html.replace("<!-- CTA BANNER", f"{worldclass_html}\n    <!-- CTA BANNER")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ Upgraded {fname} to World-Class Publication UI")

def main():
    print("=== Applying World-Class Publication UI/UX across All Blog Pages ===")
    files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(files):
        update_article_page(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
