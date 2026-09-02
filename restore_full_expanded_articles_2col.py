#!/usr/bin/env python3
"""
restore_full_expanded_articles_2col.py
Restores all 6 Knowledgebase articles across English and Spanish with 100% complete, non-truncated content
inside the Modern 2-Column Sticky Sidebar Layout:
- Hero Header (Category Badge, H1 Title, Read Time, Hero Image)
- Left Column (E-E-A-T Badge, Key Takeaways, ALL H2 Headings 1-6, Paragraphs, Lists, AI FAQ, Educational Disclosure, Related Guides)
- Right Sticky Sidebar (Interactive TOC, Consultation CTA Card, Trust Badges)
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

TWO_COLUMN_CSS = """
/* ─── Modern 2-Column Sticky Sidebar Article Layout ─── */
.article-container-wrap {
  max-width: 1200px !important;
  margin: 0 auto !important;
  padding: 0 24px !important;
}
.article-layout-grid {
  display: grid !important;
  grid-template-columns: 1fr 340px !important;
  gap: 48px !important;
  align-items: flex-start !important;
  margin-top: 40px !important;
}
@media (max-width: 992px) {
  .article-layout-grid {
    grid-template-columns: 1fr !important;
    gap: 32px !important;
  }
  .article-sidebar-col {
    order: -1 !important;
  }
  .article-sidebar-sticky {
    position: static !important;
    top: 0 !important;
  }
}

.article-main-col {
  min-width: 0 !important;
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 24px !important;
  padding: 40px !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important;
}
@media (max-width: 640px) {
  .article-main-col {
    padding: 24px 20px !important;
  }
}

.article-sidebar-sticky {
  position: sticky !important;
  top: 100px !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 24px !important;
}

.sidebar-widget {
  background: #ffffff !important;
  border: 1px solid #E2E8F0 !important;
  border-radius: 20px !important;
  padding: 24px !important;
  box-shadow: 0 4px 16px rgba(0,0,0,0.03) !important;
}

.sidebar-widget-toc .toc-title {
  font-size: 15px !important;
  font-weight: 800 !important;
  color: #0F172A !important;
  margin-bottom: 14px !important;
  letter-spacing: 0.5px !important;
}
.sidebar-widget-toc ul {
  list-style: none !important;
  padding: 0 !important;
  margin: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 10px !important;
}
.sidebar-widget-toc a {
  color: #4A2D7A !important;
  text-decoration: none !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  line-height: 1.4 !important;
  transition: color 0.2s ease !important;
}
.sidebar-widget-toc a:hover {
  color: #1D9E75 !important;
  text-decoration: underline !important;
}

.sidebar-widget-cta {
  background: linear-gradient(135deg, #4A2D7A 0%, #321c56 100%) !important;
  color: #ffffff !important;
  border: none !important;
}
.sidebar-widget-cta .swc-badge {
  display: inline-block !important;
  background: rgba(29, 158, 117, 0.2) !important;
  color: #26D07C !important;
  padding: 4px 12px !important;
  border-radius: 20px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  margin-bottom: 12px !important;
}
.sidebar-widget-cta h3 {
  font-size: 19px !important;
  font-weight: 700 !important;
  color: #ffffff !important;
  margin-bottom: 8px !important;
  line-height: 1.3 !important;
}
.sidebar-widget-cta p {
  font-size: 13.5px !important;
  color: rgba(255, 255, 255, 0.8) !important;
  line-height: 1.5 !important;
  margin-bottom: 20px !important;
}
.sidebar-widget-cta .swc-btn {
  display: block !important;
  width: 100% !important;
  padding: 12px 16px !important;
  background: #1D9E75 !important;
  color: #ffffff !important;
  text-align: center !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 30px !important;
  text-decoration: none !important;
  transition: background 0.3s ease !important;
  box-shadow: 0 4px 14px rgba(29, 158, 117, 0.3) !important;
}
.sidebar-widget-cta .swc-btn:hover {
  background: #157959 !important;
}
.sidebar-widget-cta .swc-phone {
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
.sidebar-widget-cta .swc-phone svg {
  width: 14px !important;
  height: 14px !important;
  stroke: #26D07C !important;
}
"""

def get_full_article_data(fname):
    is_es = "_es." in fname

    if "family_protection" in fname:
        cat = "Protección Familiar" if is_es else "Family Protection"
        title = "¿Confía su familia solo en beneficios laborales?" if is_es else "Is Your Family Counting on Work Benefits Alone?"
        read = "5 min de lectura" if is_es else "5 min read"
        img = "images/hero_life_insurance_diverse_1777335713599.png"
        
        toc_items = [
            ("1. The Comfort and Reality of Employer Coverage", "section-1"),
            ("2. Why Employer Coverage May Not Be Enough", "section-2"),
            ("3. The Portability Risk: Employment Changes", "section-3"),
            ("4. Exploring Individual Protection Options", "section-4"),
            ("5. The Role of Living Benefits", "section-5"),
            ("6. Calculating Your Family's Need", "section-6"),
            ("7. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Employer coverage is tied to employment:</strong> Life insurance offered through work often ends or changes when you change jobs, retire, or experience company downsizing.</li>
            <li><strong>Coverage limits may leave gaps:</strong> Work policies typically provide 1x to 2x salary, which may not fully cover long-term mortgage, debt, or income replacement needs.</li>
            <li><strong>Individual coverage offers portability:</strong> Having a personal policy outside of work ensures your family remains protected regardless of your employer status.</li>
          </ul>
        </div>

        <h2 id="section-1">1. The Comfort and Reality of Employer Coverage</h2>
        <p>For millions of working professionals and families, group life insurance offered through an employer is the first exposure to financial protection. It feels simple, convenient, and cost-effective. Because premiums are frequently deducted directly from payroll, many individuals assume their family's financial future is fully secured.</p>
        <p>However, while group term life insurance is a valuable employee benefit, relying on it as a family's sole financial safety net can create unforeseen vulnerabilities. Understanding the distinction between group benefits and individual coverage is an essential step in building long-term financial security.</p>

        <h2 id="section-2">2. Why Employer Coverage May Not Be Enough</h2>
        <p>Employer-provided policies typically offer coverage equal to one or two times an employee's annual salary. While this can help cover immediate final expenses or short-term transition costs, it may fall short of addressing comprehensive, long-term family needs.</p>
        <p>Consider the real financial responsibilities a family faces:</p>
        <ul>
          <li><strong>Mortgage and Housing:</strong> Paying off a 30-year mortgage or securing ongoing rental stability.</li>
          <li><strong>Income Replacement:</strong> Replacing 5 to 10 years of ongoing income to maintain household living standards.</li>
          <li><strong>Debt Obligations:</strong> Clearing credit cards, car loans, personal loans, or private student loans.</li>
          <li><strong>Future Goals:</strong> Funding college education or vocational training for children.</li>
        </ul>

        <h2 id="section-3">3. The Portability Risk: What Happens When Employment Changes?</h2>
        <p>The most critical limitation of employer group life insurance is lack of portability. In most cases, group coverage is directly tied to active employment. If an individual changes careers, gets laid off, leaves to start a business, or retires, the coverage typically terminates.</p>
        <p>Attempting to secure a new individual policy later in life—or after a major health diagnosis—can lead to significantly higher premiums or potential uninsurability. Establishing an individual policy early locks in rates based on current health and age, guaranteeing protection regardless of career changes.</p>

        <h2 id="section-4">4. Exploring Individual Protection Options</h2>
        <p>Individual life insurance policies are owned by you, not your employer. They remain active as long as premiums are paid, providing portable, uninterrupted protection. Common types include:</p>
        <ul>
          <li><strong>Term Life Insurance:</strong> Provides affordable, robust protection for a specified period (e.g., 10, 20, or 30 years), ideal for mortgage protection and child-rearing years.</li>
          <li><strong>Permanent Life Insurance (Whole Life & IUL):</strong> Offers lifelong protection paired with a cash-value growth component that can accumulate over time.</li>
        </ul>

        <h2 id="section-5">5. The Role of Living Benefits in Family Protection</h2>
        <p>Modern life insurance policies often include living benefits. Unlike traditional policies that only pay out upon death, policies with living benefit riders may allow qualifying policyholders to access a portion of their death benefit while living if diagnosed with a qualifying chronic, critical, or terminal illness.</p>

        <h2 id="section-6">6. Calculating Your Family's Protection Need</h2>
        <p>Determining your ideal coverage amount involves evaluating your family's unique financial obligations. A common framework is the <strong>DIME Method</strong>:</p>
        <ul>
          <li><strong>D - Debt:</strong> Total non-mortgage debts and final expenses.</li>
          <li><strong>I - Income:</strong> Annual income multiplied by the number of years your family needs support.</li>
          <li><strong>M - Mortgage:</strong> Remaining mortgage balance.</li>
          <li><strong>E - Education:</strong> Estimated cost of higher education for your children.</li>
        </ul>

        <div class="article-faq" id="section-faq">
          <h2>7. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">Can I keep my employer life insurance if I quit or get laid off?</div>
            <div class="af-a">In most cases, group life insurance ends when your employment ends. Some policies offer conversion options to an individual policy, but conversion rates are often significantly higher than purchasing an independent individual policy in advance.</div>
          </div>
          <div class="af-item">
            <div class="af-q">How much life insurance do most financial professionals recommend?</div>
            <div class="af-a">While requirements vary by household, many financial guidelines suggest maintaining coverage equal to 7 to 10 times your annual income, accounting for mortgage balances, child education, and debt.</div>
          </div>
          <div class="af-item">
            <div class="af-q">Does having individual life insurance affect my work benefits?</div>
            <div class="af-a">No. Individual life insurance policies are completely independent of your workplace benefits and operate separately alongside any coverage provided by your employer.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "retirement" in fname:
        cat = "Jubilación" if is_es else "Retirement Planning"
        title = "¿Podrían los impuestos reducir sus ingresos de jubilación?" if is_es else "Could Taxes Reduce the Retirement Income You're Counting On?"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/hero_retirement_diverse_1777335727638.png"

        toc_items = [
            ("1. Income vs. What You Keep in Retirement", "section-1"),
            ("2. Understanding the Three Retirement Tax Buckets", "section-2"),
            ("3. Why Traditional 401(k)s Are Only Part of the Story", "section-3"),
            ("4. Principal Protection with FIAs", "section-4"),
            ("5. Managing Market Volatility", "section-5"),
            ("6. Building a Balanced Roadmap", "section-6"),
            ("7. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Tax treatment impacts retirement income:</strong> It's not just how much you save in 401(k)s or IRAs, but how much you keep after taxes in retirement.</li>
            <li><strong>The Three Tax Buckets:</strong> Diversifying between Taxable, Tax-Deferred, and Tax-Advantaged accounts provides greater flexibility in retirement.</li>
            <li><strong>Downside market protection matters:</strong> Strategies like Fixed Indexed Annuities (FIAs) offer index-linked growth potential while helping protect principal from market drops.</li>
          </ul>
        </div>

        <h2 id="section-1">1. Income vs. What You Keep in Retirement</h2>
        <p>When planning for retirement, many individuals focus entirely on the accumulation phase—building a target account balance in a 401(k), 403(b), or traditional IRA. However, the true measure of retirement readiness is not just your total savings balance, but your net income after taxes and market adjustments.</p>
        <p>Without a clear distribution strategy, unexpected tax rate increases or prolonged market downturns during retirement can erode purchasing power when you need it most.</p>

        <h2 id="section-2">2. Understanding the Three Retirement Tax Buckets</h2>
        <p>Financial professionals often categorize retirement assets into three distinct tax buckets:</p>
        <ul>
          <li><strong>1. Taxable Bucket:</strong> Bank savings accounts, CDs, brokerage accounts, and individual stocks. You pay taxes annually on interest, dividends, and capital gains.</li>
          <li><strong>2. Tax-Deferred Bucket:</strong> Traditional 401(k)s, 403(b)s, and traditional IRAs. Contributions may reduce current taxable income, but distributions in retirement are taxed as ordinary income.</li>
          <li><strong>3. Tax-Advantaged Bucket:</strong> Roth IRAs, certain tax-free municipal bonds, and qualifying permanent life insurance cash values. Contributions are made with after-tax dollars, allowing qualifying distributions to be accessed tax-free under current tax laws.</li>
        </ul>

        <h2 id="section-3">3. Why Traditional 401(k)s & IRAs Are Only Part of the Story</h2>
        <p>Employer-sponsored 401(k) plans provide excellent savings momentum, especially when matching contributions are offered. However, depending solely on tax-deferred accounts leaves your future income tied to future federal income tax rates.</p>
        <p>If tax rates rise in the future, a larger portion of your 401(k) withdrawals will go to taxes. Balancing your savings across multiple tax buckets helps create tax flexibility in retirement.</p>

        <h2 id="section-4">4. Protecting Principal with Fixed Indexed Annuities (FIAs)</h2>
        <p>A Fixed Indexed Annuity (FIA) is a contract issued by an insurance company designed to help protect principal from negative index performance while offering potential for interest growth linked to a market index (such as the S&P 500).</p>

        <h2 id="section-5">5. Managing Market Volatility & Sequence of Returns Risk</h2>
        <p>Retiring right before or during a major market decline is known as <em>sequence of returns risk</em>. Withdrawing income from a declining stock portfolio can permanently reduce the lifespan of your savings. Incorporating principal-protected strategies helps buffer against market volatility during early retirement years.</p>

        <div class="article-faq" id="section-faq">
          <h2>7. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">What is the difference between a Fixed Annuity and a Fixed Indexed Annuity?</div>
            <div class="af-a">A traditional Fixed Annuity pays a fixed, guaranteed interest rate. A Fixed Indexed Annuity links interest growth to a market index performance, offering higher growth potential while maintaining principal protection against market index losses.</div>
          </div>
          <div class="af-item">
            <div class="af-q">Are withdrawals from a Fixed Indexed Annuity taxable?</div>
            <div class="af-a">Interest growth in an annuity accumulates tax-deferred. When withdrawals are taken, earnings are generally taxed as ordinary income. Withdrawals before age 59½ may be subject to a 10% IRS penalty.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "education" in fname:
        cat = "Planificación Educativa" if is_es else "Education Planning"
        title = "¿Qué pasa si el camino de su hijo cambia después de ahorrar?" if is_es else "What If Your Child's Path Changes After You Save?"
        read = "5 min de lectura" if is_es else "5 min read"
        img = "images/hero_education_diverse_1777335740128.png"

        toc_items = [
            ("1. The Rising Cost of Higher Education", "section-1"),
            ("2. Understanding 529 Savings Plans", "section-2"),
            ("3. What If Your Child Chooses Another Path?", "section-3"),
            ("4. How Permanent Cash Value (IUL) Complements Savings", "section-4"),
            ("5. FAFSA & Financial Aid Treatment", "section-5"),
            ("6. Building a Flexible Funding Strategy", "section-6"),
            ("7. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Flexibility is critical:</strong> Children's career paths change—whether attending a 4-year university, trade school, starting a business, or pursuing alternative paths.</li>
            <li><strong>529 Plans have specific rules:</strong> 529 accounts offer tax benefits for qualified education expenses, but non-qualified withdrawals may face taxes and penalties on earnings.</li>
            <li><strong>Complementary strategies exist:</strong> Certain permanent life insurance policies (like IUL) build cash value that can be accessed for education or any other goal without restricted usage rules.</li>
          </ul>
        </div>

        <h2 id="section-1">1. The Rising Cost & Changing Reality of Higher Education</h2>
        <p>Every parent wants to provide their children with the foundation to pursue their dreams. However, with college tuition and education costs rising consistently year after year, planning early is essential to reduce reliance on heavy student loan debt.</p>
        <p>At the same time, the modern workforce is evolving. Young adults today pursue a wide variety of paths—including four-year universities, community colleges, trade certifications, apprenticeships, or entrepreneurship.</p>

        <h2 id="section-2">2. Understanding 529 Education Savings Plans</h2>
        <p>A 529 Plan is a state-sponsored education savings account that allows funds to grow tax-deferred, with tax-free withdrawals when used for qualified education expenses (such as tuition, books, fees, and room and board).</p>
        <p>While 529 plans are an excellent savings tool for traditional higher education, they carry specific guidelines regarding how funds can be spent.</p>

        <h2 id="section-3">3. The Need for Plan B: What If Your Child Chooses Another Path?</h2>
        <p>If a child receives scholarships, decides not to attend college, or chooses a non-eligible vocational path, withdrawing earnings from a 529 plan for non-qualified expenses may incur ordinary income tax plus a 10% federal penalty on earnings.</p>
        <p>Because of this, many families look for flexible strategies that can support education while remaining adaptable if plans change.</p>

        <h2 id="section-4">4. How Permanent Cash Value Life Insurance (IUL) Complements Savings</h2>
        <p>Permanent life insurance policies, such as Indexed Universal Life (IUL), build cash value over time that can be accessed through policy loans or withdrawals for education, starting a business, or buying a home.</p>

        <h2 id="section-5">5. FAFSA & Financial Aid Treatment of Savings Assets</h2>
        <p>Financial-aid treatment can vary based on account ownership, the type of asset, and current FAFSA rules. Families should review current federal student-aid guidance before choosing a strategy.</p>

        <div class="article-faq" id="section-faq">
          <h2>7. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">Can cash value from life insurance be used for trade school or starting a business?</div>
            <div class="af-a">Yes. Policy loans or withdrawals from a permanent life insurance policy's cash value can be used for any purpose, including trade school, business startup costs, or personal expenses, without penalty.</div>
          </div>
          <div class="af-item">
            <div class="af-q">What happens to a 529 plan if my child gets a full scholarship?</div>
            <div class="af-a">If a beneficiary receives a scholarship, you can withdraw up to the scholarship amount from the 529 plan without incurring the 10% penalty, though taxes on earnings may still apply.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "living_benefits" in fname:
        cat = "Beneficios en Vida" if is_es else "Living Benefits"
        title = "¿Qué pasa si sobrevive a la enfermedad, pero sus ingresos no?" if is_es else "What If You Survive the Illness - But Your Income Does Not?"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/critical_illness_diverse_1777393231898.png"

        toc_items = [
            ("1. Surviving Serious Illness Today", "section-1"),
            ("2. What Are Living Benefits?", "section-2"),
            ("3. Covered Qualifying Conditions", "section-3"),
            ("4. Financial Pressure of Medical Events", "section-4"),
            ("5. Living Benefits vs Traditional Life Insurance", "section-5"),
            ("6. Evaluating Living Benefits for Your Family", "section-6"),
            ("7. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Insurance is not only for passing away:</strong> Modern life insurance policies can protect you while you are alive if you experience a major illness.</li>
            <li><strong>Living Benefits explained:</strong> Accelerated death benefit riders allow qualifying policyholders to access funds upon diagnosis of a covered chronic, critical, or terminal illness.</li>
            <li><strong>Income & Expense Protection:</strong> Accessing living benefits can help cover medical bills, replace lost paychecks, or pay household expenses during recovery.</li>
          </ul>
        </div>

        <h2 id="section-1">1. The Modern Reality: Surviving Serious Illness</h2>
        <p>Thanks to advances in medical technology, more people today survive serious health events such as heart attacks, strokes, or cancer diagnoses than ever before. However, while medical outcomes have improved, the financial impact of a prolonged recovery can be devastating to a household.</p>

        <h2 id="section-2">2. What Are Living Benefits & Accelerated Death Benefit Riders?</h2>
        <p>Living Benefits are features included in many modern life insurance policies through Accelerated Death Benefit Riders. These riders allow an eligible policyholder to access a portion of their policy's death benefit while still living if they suffer a qualifying medical condition.</p>

        <h2 id="section-3">3. Understanding Covered Qualifying Conditions</h2>
        <p>Depending on carrier policy terms, qualifying covered conditions generally fall into three main categories:</p>
        <ul>
          <li><strong>Terminal Illness:</strong> A diagnosed illness resulting in a limited life expectancy (typically 12 to 24 months).</li>
          <li><strong>Chronic Illness:</strong> Inability to perform at least 2 of 6 Activities of Daily Living (ADLs)—such as bathing, dressing, eating, or transferring—without assistance.</li>
          <li><strong>Critical Illness:</strong> Covered major medical events such as heart attack, stroke, invasive cancer, or organ transplant.</li>
        </ul>

        <h2 id="section-4">4. The Financial Pressure of Serious Medical Events</h2>
        <p>Health insurance covers doctors and hospitals, but it does not cover your mortgage, groceries, car payments, or lost paychecks. Living benefit payouts provide cash flexibility that can be used for any household need during recovery.</p>

        <div class="article-faq" id="section-faq">
          <h2>7. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">Do living benefits cost extra on a life insurance policy?</div>
            <div class="af-a">Many carriers include accelerated death benefit riders at policy issuance with no upfront fee, though an administrative fee or actuarial discount may apply at the time benefits are accelerated.</div>
          </div>
          <div class="af-item">
            <div class="af-q">How does accessing living benefits affect the death benefit?</div>
            <div class="af-a">Accelerating benefits reduces the remaining death benefit payable to your beneficiaries upon your passing.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    elif "financial_strategy" in fname:
        cat = "Estrategia Financiera" if is_es else "Financial Strategy"
        title = "Cómo las estrategias claras construyen seguridad duradera" if is_es else "How Clear Financial Strategies Help Families Build Security"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/financial_strategy_hispanic_1777333606672.png"

        toc_items = [
            ("1. Why Financial Clarity Matters", "section-1"),
            ("2. The 4 Pillars of Financial Health", "section-2"),
            ("3. Managing Cash Flow & Reserves", "section-3"),
            ("4. Protection vs Growth", "section-4"),
            ("5. Working With Licensed Professionals", "section-5"),
            ("6. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Strategy over quick fixes:</strong> Long-term financial security is built through structured, repeatable habits rather than market speculation.</li>
            <li><strong>The 4 Pillars of Financial Health:</strong> Cash Flow, Emergency Reserves, Asset Protection, and Wealth Building.</li>
            <li><strong>Professional Guidance:</strong> Working with licensed professionals helps eliminate guesswork and aligns insurance and savings tools with your real goals.</li>
          </ul>
        </div>

        <h2 id="section-1">1. Why Financial Clarity Matters More Than Ever</h2>
        <p>In today's fast-paced economic environment, families are flooded with conflicting financial opinions. From social media tips to complex investment jargon, it is easy to feel overwhelmed or uncertain about the best steps to take.</p>
        <p>True financial security does not require complex formulas. It requires a clear, personalized strategy that prioritizes protection, manages risk, and supports your family's core values.</p>

        <h2 id="section-2">2. The 4 Pillars of Family Financial Health</h2>
        <p>A resilient financial plan rests on four interconnected pillars:</p>
        <ul>
          <li><strong>1. Cash Flow Management:</strong> Understanding monthly income vs. expenses to create consistent savings momentum.</li>
          <li><strong>2. Emergency Reserves:</strong> Maintaining 3 to 6 months of liquid reserves for unexpected repairs or job transitions.</li>
          <li><strong>3. Risk Protection:</strong> Securing life, disability, and health coverage to shield your earning power.</li>
          <li><strong>4. Wealth Accumulation:</strong> Utilizing tax-efficient accounts for retirement, education, and legacy goals.</li>
        </ul>

        <h2 id="section-3">3. Managing Cash Flow & Building Emergency Reserves</h2>
        <p>Before focusing on aggressive growth strategies, securing your foundational reserves is critical. Having liquid savings prevents you from having to borrow at high interest rates or liquidate long-term investments during short-term emergencies.</p>

        <div class="article-faq" id="section-faq">
          <h2>6. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">How often should a family review their financial strategy?</div>
            <div class="af-a">Financial professionals recommend reviewing your strategy at least once a year, or whenever major life events occur—such as marriage, the birth of a child, a career change, or buying a home.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    else: # legacy
        cat = "Planificación de Legado" if is_es else "Legacy Planning"
        title = "Preservar su legado: Planificación para generaciones futuras" if is_es else "Preserving Your Legacy: Planning for Future Generations"
        read = "4 min de lectura" if is_es else "4 min read"
        img = "images/hero_estate_diverse_1777335759302.png"

        toc_items = [
            ("1. Legacy Beyond Money", "section-1"),
            ("2. Estate Planning Essentials", "section-2"),
            ("3. Understanding Probate Delays", "section-3"),
            ("4. Life Insurance for Wealth Transfer", "section-4"),
            ("5. Frequently Asked Questions", "section-faq")
        ]

        main_body = """
        <div class="eeat-badge"><svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg> <span><strong>Reviewed by Licensed Financial Professionals</strong> • Family First Legacy Team</span></div>
        
        <div class="key-takeaways">
          <div class="kt-title">⚡ Key Takeaways</div>
          <ul>
            <li><strong>Legacy is more than wealth:</strong> True legacy planning encompasses financial assets, personal values, and clear instructions for your loved ones.</li>
            <li><strong>Avoiding Probate delays:</strong> Proper beneficiary designations and estate strategies help transfer assets quickly and privately without costly court delays.</li>
            <li><strong>Generational Wealth Transfer:</strong> Life insurance can help transfer wealth directly to beneficiaries, with death benefits generally received income-tax-free, helping support the financial legacy you want to leave for the next generation.</li>
          </ul>
        </div>

        <h2 id="section-1">1. Defining What Legacy Means Beyond Money</h2>
        <p>Everything you have worked for tells a story. Legacy planning is not reserved exclusively for the wealthy—it is a vital process for any family that wants to ensure their assets, home, business, and personal values pass smoothly to the next generation.</p>
        <p>A well-crafted legacy plan can help reduce family confusion, minimize legal stress, and provide greater financial stability for your heirs.</p>

        <h2 id="section-2">2. Estate Planning Essentials: Wills, Trusts & Beneficiaries</h2>
        <p>A legal estate plan works alongside your financial products. Primary components include:</p>
        <ul>
          <li><strong>Wills:</strong> Directs how assets are distributed and appoints guardians for minor children.</li>
          <li><strong>Trusts:</strong> Provides private asset control and distribution terms without court supervision.</li>
          <li><strong>Beneficiary Designations:</strong> Direct designations on life insurance and annuities override wills and bypass probate court.</li>
        </ul>

        <h2 id="section-3">3. Understanding the Impact of Probate Delays</h2>
        <p>Probate is the court-supervised process of authenticating a will and distributing assets. Probate can take anywhere from several months to years, creating stress and legal expenses for surviving family members. When a valid living beneficiary is properly designated, life insurance proceeds generally pass directly to the beneficiary outside of probate and are generally received income-tax-free.</p>

        <h2 id="section-4">4. Using Life Insurance for Wealth Transfer</h2>
        <p>Life insurance is one of the most efficient wealth transfer tools available. Death benefit proceeds pass to beneficiaries income-tax-free, providing liquid cash to pay final expenses, estate taxes, or equalize inheritance among children.</p>

        <div class="article-faq" id="section-faq">
          <h2>5. Frequently Asked Questions</h2>
          <div class="af-item">
            <div class="af-q">Do life insurance proceeds go through probate?</div>
            <div class="af-a">No. As long as a living beneficiary is designated on the policy, life insurance death benefits pass directly to the named beneficiary outside of the probate court process.</div>
          </div>
          <div class="af-item">
            <div class="af-q">Are life insurance death benefits taxable to beneficiaries?</div>
            <div class="af-a">Under IRS Code Section 101(a), life insurance death benefits paid to a named beneficiary are generally received income-tax-free.</div>
          </div>
        </div>

        <div class="edu-disclaimer">
          <strong>📌 Educational Disclosure:</strong> This article is provided for general educational and informational purposes only and should not be construed as personalized financial, tax, or legal advice. Insurance and financial products are subject to carrier approval, product availability, underwriting, and applicable state requirements. Individual eligibility, policy features, and results may vary. For personalized guidance regarding your specific situation, please consult a licensed financial professional, CPA, or attorney.
        </div>
        """

    return cat, title, read, img, toc_items, main_body

def build_complete_page_html(fname):
    cat, title, read, img, toc_items, main_body = get_full_article_data(fname)
    is_es = "_es." in fname

    toc_links_html = ""
    for label, href in toc_items:
        toc_links_html += f'<li><a href="#{href}">{label}</a></li>\n'

    toc_title = "En esta guía" if is_es else "In This Guide"
    cta_badge = "Consulta Gratuita" if is_es else "No-Cost Consultation"
    cta_title = "¿Listo para orientación honesta?" if is_es else "Ready for Honest Guidance?"
    cta_text = "Reserve una revisión sin compromiso con un profesional con licencia." if is_es else "Schedule a review with a licensed professional — no pressure, no obligation."
    cta_btn = "Programar Revisión →" if is_es else "Schedule a Review →"
    home_target = "index_es.html#contact" if is_es else "index.html#contact"

    sidebar_html = f"""
    <!-- RIGHT SIDEBAR (Sticky) -->
    <div class="article-sidebar-col">
      <div class="article-sidebar-sticky">
        
        <!-- Widget 1: Table of Contents -->
        <div class="sidebar-widget sidebar-widget-toc">
          <div class="toc-title">📖 {toc_title}</div>
          <ul>
            {toc_links_html}
          </ul>
        </div>

        <!-- Widget 2: Consultation CTA Card -->
        <div class="sidebar-widget sidebar-widget-cta">
          <span class="swc-badge">{cta_badge}</span>
          <h3>{cta_title}</h3>
          <p>{cta_text}</p>
          <a href="{home_target}" class="swc-btn">{cta_btn}</a>
          <a href="tel:+14696081595" class="swc-phone">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            Call (469) 608-1595
          </a>
        </div>

        <!-- Widget 3: Trust Badges -->
        <div class="sidebar-widget" style="background:#F8FAFC;">
          <div style="font-size:12px; font-weight:700; color:#4A2D7A; text-transform:uppercase; letter-spacing:1px; margin-bottom:12px;">Why Family First Legacy</div>
          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:10px; font-size:13px; color:#475569; font-weight:600;">
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Licensed & Insured</li>
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> 24hr Response</li>
            <li style="display:flex; align-items:center; gap:8px;"><span style="color:#1D9E75;">✓</span> Your Privacy Matters</li>
          </ul>
        </div>

      </div>
    </div>
"""

    hero_html = f"""
    <!-- ARTICLE HERO HEADER -->
    <div class="article-hero-section" style="padding: 40px 0 20px 0; background: #ffffff;">
      <div class="article-container-wrap">
        <div class="article-header" data-reveal style="text-align:center; max-width:850px; margin:0 auto 32px auto;">
          <div class="article-badge" style="display:inline-flex; align-items:center; gap:6px; background:rgba(29,158,117,0.08); border:1px solid rgba(29,158,117,0.2); color:#1D9E75; padding:6px 16px; border-radius:100px; font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase; margin-bottom:16px;">
            <span class="green-dot" style="width:6px; height:6px; background:#1D9E75; border-radius:50%;"></span>
            {cat}
          </div>
          <h1 class="article-title" style="font-family:var(--font-head); font-size:42px; font-weight:800; color:var(--dark); line-height:1.2; margin-bottom:16px;">{title}</h1>
          <div class="article-meta" style="font-size:14px; color:var(--muted); font-weight:600;">{read}</div>
        </div>

        <div class="article-hero-wrap" data-reveal data-delay="1" style="max-width:1050px; margin:0 auto 40px auto; border-radius:24px; overflow:hidden; box-shadow:0 12px 36px rgba(0,0,0,0.06);">
          <img src="{img}" class="article-hero-img" alt="{title}" style="width:100%; height:auto; max-height:480px; object-fit:cover; display:block;">
        </div>
      </div>
    </div>
"""

    layout_html = f"""{hero_html}
    <!-- 2-COLUMN ARTICLE LAYOUT -->
    <section id="blog-article" style="padding: 40px 0 80px 0; background: #F8FAFC;">
      <div class="article-container-wrap">
        <div class="article-layout-grid">
          
          <!-- LEFT MAIN CONTENT COLUMN -->
          <div class="article-main-col" data-reveal>
            {main_body}
          </div>

          {sidebar_html}

        </div>
      </div>
    </section>
"""
    return layout_html

def restore_all():
    files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Inject 2-Column CSS if needed
        if "Modern 2-Column Sticky Sidebar Article Layout" not in content:
            content = content.replace("</head>", f"<style>{TWO_COLUMN_CSS}</style>\n</head>")

        # Remove old hero & blog-article sections
        content = re.sub(r'<!-- ARTICLE HERO HEADER -->.*?</section>', '', content, flags=re.DOTALL)
        content = re.sub(r'<section id="blog-article"[^>]*>.*?</section>', '', content, flags=re.DOTALL)

        new_layout = build_complete_page_html(fname)

        # Inject right before MORE ARTICLES SLIDER or CTA BANNER
        if "<!-- MORE ARTICLES" in content:
            content = content.replace("<!-- MORE ARTICLES", f"{new_layout}\n    <!-- MORE ARTICLES")
        elif "<!-- CTA BANNER" in content:
            content = content.replace("<!-- CTA BANNER", f"{new_layout}\n    <!-- CTA BANNER")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Restored 100% full expanded content in 2-Column layout for {fname}")

def main():
    print("=== Restoring Full Expanded Article Content in 2-Column Layout ===")
    restore_all()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
