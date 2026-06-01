import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

# Read master index
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    master_content = f.read()

# Extract Header and Footer
nav_end_idx = master_content.find('<!-- HERO SLIDESHOW')
header_part = master_content[:nav_end_idx]

# Inject blog specific CSS into header
blog_css = """
<style>
#blog-article { padding: 140px 0 100px; background: var(--bg); }
.article-header { max-width: 800px; margin: 0 auto 56px; text-align: center; }
.article-badge { display: inline-flex; align-items: center; gap: 8px; font-size: 13px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--amber); margin-bottom: 24px; }
.article-title { font-family: var(--font-head); font-size: clamp(40px, 5vw, 64px); font-weight: 800; line-height: 1.1; letter-spacing: -2px; color: var(--dark); margin-bottom: 24px; }
.article-meta { font-size: 14px; color: var(--muted); font-weight: 500; }
.article-hero-wrap { max-width: 1000px; margin: 0 auto 64px; border-radius: 24px; overflow: hidden; box-shadow: 0 20px 50px rgba(0,0,0,0.1); }
.article-hero-img { width: 100%; aspect-ratio: 21/9; object-fit: cover; display: block; }
.article-body { max-width: 760px; margin: 0 auto; background: var(--white); padding: 64px 80px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
.article-body p { font-size: 18px; line-height: 1.8; color: var(--muted); margin-bottom: 24px; font-weight: 300; }
.article-body h2 { font-family: var(--font-head); font-size: 32px; font-weight: 700; color: var(--dark); margin: 48px 0 24px; letter-spacing: -1px; }
.article-body h3 { font-family: var(--font-head); font-size: 24px; font-weight: 700; color: var(--dark); margin: 32px 0 16px; letter-spacing: -0.5px; }
.article-body ul { margin-bottom: 24px; padding-left: 24px; }
.article-body li { font-size: 18px; line-height: 1.8; color: var(--muted); font-weight: 300; margin-bottom: 12px; }
.article-body blockquote { font-size: 24px; font-style: italic; color: var(--green); border-left: 4px solid var(--amber); padding-left: 24px; margin: 40px 0; }
@media(max-width: 768px) {
  .article-body { padding: 40px 32px; }
}
</style>
"""
header_part = header_part.replace('</head>', blog_css + '\n</head>')

# For footer, find <!-- CTA BANNER -->
cta_idx = master_content.find('<!-- CTA BANNER ──────────────────────────────────────── -->')
footer_part = master_content[cta_idx:]

blogs = [
    {
        "filename": "blog_family_protection.html",
        "category": "Family Protection",
        "title": "Why 60% of Families are Dangerously Underinsured",
        "date": "April 2024 • 5 min read",
        "img": "images/hero_life_insurance_diverse_1777335713599.png",
        "content": """
        <p>In today's unpredictable world, relying solely on employer-provided life insurance is a risk most families cannot afford to take. Studies show that over 60% of American families do not have enough life insurance to replace their primary breadwinner's income, leaving them dangerously exposed to financial ruin if tragedy strikes.</p>
        
        <h2>The Illusion of Employer Coverage</h2>
        <p>Many professionals assume the "1x or 2x salary" policy provided by their employer is sufficient. However, this coverage is almost always a fraction of what is actually needed to pay off a mortgage, cover living expenses, and fund a child's college education. More importantly, employer coverage does not travel with you. If you lose your job or change careers, your coverage vanishes precisely when you might be uninsurable due to age or health changes.</p>
        
        <blockquote>"The biggest mistake families make is assuming the safety net their employer built is meant to catch their family. It's not. It's just a corporate perk."</blockquote>
        
        <h2>How Much Do You Actually Need?</h2>
        <p>Financial experts widely recommend owning an independent life insurance policy with a death benefit equal to 10 to 15 times your annual income. This calculation is known as the DIME method:</p>
        <ul>
            <li><strong>D</strong>ebt: Total outstanding debts (credit cards, auto loans, personal loans).</li>
            <li><strong>I</strong>ncome: Your annual salary multiplied by the number of years your family will need support.</li>
            <li><strong>M</strong>ortgage: The remaining balance on your home.</li>
            <li><strong>E</strong>ducation: The estimated cost of your children's future college tuition.</li>
        </ul>
        
        <h2>The Evolution of Life Insurance: Living Benefits</h2>
        <p>Modern life insurance has evolved drastically. Today, you do not have to die for your policy to pay out. Policies equipped with "Living Benefits" allow you to access a large portion of your death benefit while you are still alive if you suffer a qualifying heart attack, stroke, cancer diagnosis, or chronic illness. This cash can be used to replace lost income, pay for experimental treatments, or simply keep your family afloat.</p>
        
        <h2>Conclusion</h2>
        <p>Don't leave your family's future to chance. Securing an independent, robust life insurance policy is the foundational step of any serious financial plan. Reach out to Family First Legacy today for a free review of your current coverage to ensure your loved ones are truly protected.</p>
        """
    },
    {
        "filename": "blog_retirement.html",
        "category": "Retirement Planning",
        "title": "The Tax Timebomb Hiding in Your 401(k)",
        "date": "April 2024 • 6 min read",
        "img": "images/hero_retirement_diverse_1777335727638.png",
        "content": """
        <p>For decades, Americans have been told that the 401(k) is the ultimate retirement tool. While it is an excellent way to accumulate wealth, especially with an employer match, it comes with a massive, often misunderstood drawback: The Tax Timebomb.</p>
        
        <h2>Understanding Tax-Deferred Risk</h2>
        <p>When you contribute to a traditional 401(k) or IRA, you are using pre-tax dollars. This means you get a tax break today, but you are agreeing to pay taxes on every dollar you withdraw in retirement. The problem? You are deferring the calculation of those taxes to a future date, essentially giving the government a blank check.</p>
        
        <p>With national debt at record highs, many economists believe that tax rates must inevitably rise. If you are a successful saver and build a $1,000,000 portfolio, you don't actually have $1,000,000. Depending on future tax rates, you might only have $700,000 or less.</p>
        
        <blockquote>"Deferring taxes implies you believe taxes will be lower in the future. Given the current economic landscape, is that a bet you are willing to make with your life savings?"</blockquote>
        
        <h2>The Power of Tax-Free Income</h2>
        <p>The wealthy have long understood that it is not about how much money you make; it is about how much money you keep. To defuse the 401(k) timebomb, you must diversify your retirement portfolio with tax-free vehicles.</p>
        <ul>
            <li><strong>Roth Conversions:</strong> Systematically moving money from tax-deferred accounts into Roth accounts where it can grow and be withdrawn tax-free.</li>
            <li><strong>Cash Value Life Insurance:</strong> Utilizing an Indexed Universal Life (IUL) policy. The cash value grows tax-deferred, and you can take tax-free loans against the policy in retirement, creating a completely tax-free income stream.</li>
        </ul>
        
        <h2>Protecting Against Market Volatility</h2>
        <p>Taxes are only half the battle. If you retire right before a major market crash, "Sequence of Returns Risk" can decimate your portfolio. Products like Fixed Indexed Annuities (FIAs) offer a 0% floor, meaning when the stock market crashes, you lose nothing. By combining market protection with tax-free strategies, you can guarantee a stress-free retirement.</p>
        
        <h2>Next Steps</h2>
        <p>It is crucial to analyze your current retirement trajectory and calculate your projected future tax burden. Contact our experts at Family First Legacy to learn how to seamlessly pivot your strategy toward tax-free, protected growth.</p>
        """
    },
    {
        "filename": "blog_education.html",
        "category": "Education Planning",
        "title": "The 529 Trap: Smarter Ways to Fund College",
        "date": "April 2024 • 5 min read",
        "img": "images/hero_education_diverse_1777335740128.png",
        "content": """
        <p>As the cost of higher education continues to skyrocket, parents are desperately looking for ways to save. For years, the default advice has been to open a 529 College Savings Plan. But what happens if your child gets a full scholarship? Or decides to start a business instead of going to college? The 529 can quickly become a trap.</p>
        
        <h2>The Rigid Rules of a 529 Plan</h2>
        <p>A 529 plan allows your money to grow tax-free, but only if it is used for "qualified education expenses." If your child decides not to attend college, and you withdraw the money for any other reason, you will be hit with ordinary income tax plus a harsh 10% penalty on the earnings.</p>
        
        <p>Furthermore, 529 plans are heavily weighed in the Free Application for Federal Student Aid (FAFSA). Having a large 529 balance can significantly reduce the amount of need-based financial aid, grants, and subsidized loans your child qualifies for.</p>
        
        <h2>The Alternative: Indexed Universal Life (IUL)</h2>
        <p>More families are discovering that an Indexed Universal Life (IUL) policy is a vastly superior vehicle for college funding due to its unparalleled flexibility.</p>
        <ul>
            <li><strong>Zero Penalties:</strong> You can access the cash value in an IUL tax-free for ANY reason. If your child doesn't go to college, the money can be used for a down payment on a house, to start a business, or simply to fund your own retirement.</li>
            <li><strong>FAFSA Friendly:</strong> Unlike 529 plans, the cash value inside a life insurance policy is currently not considered an asset on the FAFSA, meaning it won't hurt your child's chances of receiving financial aid.</li>
            <li><strong>Market Protection:</strong> 529 plans are exposed to the stock market. If the market crashes right before tuition is due, your college fund shrinks. IULs have a 0% floor, meaning your principal and locked-in gains are entirely protected from market crashes.</li>
        </ul>
        
        <h2>Setting Your Child Up For Life</h2>
        <p>When you use a juvenile life insurance policy to fund college, you are also giving your child a massive head start in life. They will enter adulthood with a fully funded, permanent life insurance policy that continues to build tax-free wealth long after they graduate.</p>
        
        <h2>Conclusion</h2>
        <p>Don't lock your hard-earned money into a restrictive government plan. Talk to the advisors at Family First Legacy about using flexible, tax-advantaged strategies to guarantee your child's educational future without risking your own financial freedom.</p>
        """
    },
    {
        "filename": "blog_financial_strategy.html",
        "category": "Wealth Building",
        "title": "Mastering the Rule of 72 to Accelerate Wealth",
        "date": "April 2024 • 4 min read",
        "img": "images/financial_strategy_hispanic_1777333606672.png",
        "content": """
        <p>Wealth building is not about luck; it is about mathematics. One of the most powerful and fundamental concepts in finance is compound interest, famously dubbed by Albert Einstein as "the eighth wonder of the world." To harness this power, you must master the Rule of 72.</p>
        
        <h2>What is the Rule of 72?</h2>
        <p>The Rule of 72 is a simple mental math shortcut to determine how long it will take for your money to double at a given annual rate of return. You simply divide the number 72 by your interest rate.</p>
        
        <p>For example, if you have $10,000 invested in an account earning a 4% return:<br>
        <strong>72 ÷ 4 = 18.</strong><br>
        It will take 18 years for your money to double to $20,000.</p>
        
        <p>If you move that money to an account earning 8%:<br>
        <strong>72 ÷ 8 = 9.</strong><br>
        It will take only 9 years for your money to double.</p>
        
        <h2>The Exponential Difference</h2>
        <p>The true power of the Rule of 72 becomes apparent over long periods of time. Let's say you are 29 years old and have $10,000.</p>
        <ul>
            <li>At a 4% return (doubling every 18 years), by age 65, your money will double twice: to $20,000, and then to $40,000.</li>
            <li>At an 8% return (doubling every 9 years), by age 65, your money will double four times: $20,000 > $40,000 > $80,000 > $160,000!</li>
        </ul>
        <p>A mere 4% difference in return results in four times the amount of wealth at retirement.</p>
        
        <h2>Applying the Rule to Debt</h2>
        <p>Unfortunately, the Rule of 72 also works against you when it comes to debt. If you have a credit card with an 18% interest rate (72 ÷ 18 = 4), the amount you owe will double every 4 years if you only make minimum payments. This is why eliminating high-interest debt is the crucial first step in any financial strategy.</p>
        
        <h2>How to Accelerate Your Wealth</h2>
        <p>To maximize your doubling cycles, you need vehicles that offer strong, consistent returns without exposing your principal to devastating market losses that set the clock back. Products like Indexed Universal Life (IUL) allow you to capture upside market potential while guaranteeing you never lose money due to market crashes, keeping your compound interest curve intact.</p>
        
        <h2>Start Doubling Today</h2>
        <p>Every year you wait is a missed doubling cycle. Contact Family First Legacy for a comprehensive Financial Needs Analysis, and let us show you how to optimize your rate of return and accelerate your path to wealth.</p>
        """
    },
    {
        "filename": "blog_legacy.html",
        "category": "Estate Planning",
        "title": "Avoiding the Probate Trap: Will vs. Trust",
        "date": "April 2024 • 5 min read",
        "img": "images/hero_estate_diverse_1777335759302.png",
        "content": """
        <p>Many people believe that drafting a Last Will and Testament is the ultimate act of estate planning. Unfortunately, a Will alone does not keep your family out of court. If you die with only a Will, your estate is almost guaranteed to go through a lengthy, stressful, and expensive legal process known as Probate.</p>
        
        <h2>The Problem with Probate</h2>
        <p>Probate is the legal process of proving a Will is valid, paying off creditors, and distributing assets. Here is why it is widely considered a trap:</p>
        <ul>
            <li><strong>It is Expensive:</strong> Attorney fees, executor fees, and court costs can easily consume 3% to 8% (or more) of your estate's total gross value.</li>
            <li><strong>It is Slow:</strong> Depending on the state, probate can take anywhere from 9 months to over 2 years, during which time your assets are frozen and inaccessible to your family.</li>
            <li><strong>It is Public:</strong> Probate proceedings become public record. Anyone can see what you owned, who you owed, and who inherited what—making your heirs targets for scams.</li>
        </ul>
        
        <h2>The Solution: The Revocable Living Trust</h2>
        <p>To avoid probate entirely, the gold standard of estate planning is the Revocable Living Trust. When you create a Trust, you transfer ownership of your assets (your home, bank accounts, investments) into the name of the Trust. Because the Trust technically owns the assets, and a Trust never dies, there is nothing for the probate court to process when you pass away.</p>
        
        <p>Your appointed "Successor Trustee" simply steps in and distributes the assets to your beneficiaries privately, immediately, and exactly according to your instructions—without paying a dime to the court system.</p>
        
        <h2>Life Insurance and Estate Planning</h2>
        <p>Life insurance is a unique asset because it inherently bypasses probate, provided you have a named, living beneficiary. The death benefit is paid out via private contract, often within weeks of passing. For high-net-worth individuals, an Irrevocable Life Insurance Trust (ILIT) can be used to completely remove the death benefit from the taxable estate, providing tax-free liquidity to pay off potential estate taxes.</p>
        
        <h2>Conclusion</h2>
        <p>Leaving a legacy should be an act of love, not a legal nightmare. Ensure your family receives exactly what you intend, smoothly and privately. Reach out to the experts at Family First Legacy to discuss integrating proper estate planning and Trusts into your financial foundation.</p>
        """
    }
]

for blog in blogs:
    print(f"Generating {blog['filename']}...")
    
    html = f'''
    <section id="blog-article">
      <div class="container">
        <div class="article-header" data-reveal>
          <div class="article-badge"><span class="green-dot"></span>{blog['category']}</div>
          <h1 class="article-title">{blog['title']}</h1>
          <div class="article-meta">{blog['date']}</div>
        </div>
        
        <div class="article-hero-wrap" data-reveal data-delay="1">
          <img src="{blog['img']}" class="article-hero-img" alt="{blog['title']}">
        </div>
        
        <div class="article-body" data-reveal data-delay="2">
          {blog['content']}
        </div>
      </div>
    </section>
    '''
    
    full_html = header_part + html + footer_part
    
    # Fix internal links since this is a subpage
    full_html = re.sub(r'href="#about"', 'href="index.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="index.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="index.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="index.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="index.html#reviews"', full_html)
    full_html = re.sub(r'href="#faq"', 'href="index.html#faq"', full_html)
    
    with open(os.path.join(base_dir, blog['filename']), 'w', encoding='utf-8') as f:
        f.write(full_html)

print("Blog generation complete.")
