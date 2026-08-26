#!/usr/bin/env python3
"""
apply_august_2026_english_updates.py
Applies all 20 confirmed changes from the August 2026 Customer PDF
to all static English HTML files in the project root.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_index():
    filepath = os.path.join(BASE, "index.html")
    if not os.path.exists(filepath):
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Hero Statistic (appears twice)
    content = content.replace("2,000+ Families Served", "YOUR FAMILY. OUR FOCUS.")
    content = content.replace("2,000+ FAMILIES SERVED", "YOUR FAMILY. OUR FOCUS.")

    # 2. Contact trust badges
    content = content.replace("100% Private", "Your Privacy Matters")
    content = content.replace("100% PRIVATE", "Your Privacy Matters")

    # 3. Consultation form intro
    content = content.replace(
        "Fill out the form below and we'll get back to you within 24 hours.",
        "Fill out the form below, and our goal is to get back to you within 24 hours."
    )
    content = content.replace(
        "Fill out the form below and we'll get back to you within 24 hours",
        "Fill out the form below, and our goal is to get back to you within 24 hours"
    )

    # 4. FAQ - IUL answer
    iul_old_snippet = "Costs, caps, limits, and policy rules apply."
    iul_new_answer = "IUL is life insurance first, not a direct stock market investment. It may help protect your family while building cash value linked to a market index, depending on the policy design. Many IUL policies include a 0% floor on index interest credits, which can help reduce the impact of negative index performance. Policy charges and other terms still apply and can affect cash value."
    
    # Target IUL answer paragraph
    content = re.sub(
        r'<div class="faq-question"[^>]*>Is Indexed Universal Life \(IUL\) a good investment\?</div>\s*<div class="faq-answer"[^>]*>.*?</div>',
        f'<div class="faq-question">Is Indexed Universal Life (IUL) a good investment?</div>\n<div class="faq-answer"><p>{iul_new_answer}</p></div>',
        content,
        flags=re.DOTALL
    )

    # 5. FAQ - Annuity answer
    annuity_new_answer = "Some fixed indexed annuities are designed to help protect principal from negative index performance while providing the potential for index-linked interest credits when applicable. Contract terms, caps, participation rates, surrender charges, withdrawals, and other limitations may apply."
    content = re.sub(
        r'<div class="faq-question"[^>]*>How does an annuity work for retirement income\?</div>\s*<div class="faq-answer"[^>]*>.*?</div>',
        f'<div class="faq-question">How does an annuity work for retirement income?</div>\n<div class="faq-answer"><p>{annuity_new_answer}</p></div>',
        content,
        flags=re.DOTALL
    )

    # 6. FAQ - Education / Permanent life
    edu_life_new_answer = "Permanent life insurance that builds cash value may offer flexible access through policy loans or withdrawals for education or other future needs, depending on the policy design. Because accessing cash value can affect policy benefits, it’s important to understand how your specific policy works before using it. We can help you understand your options and how they may fit your family’s goals."
    content = re.sub(
        r'<div class="faq-question"[^>]*>Can life insurance be used for education planning\?</div>\s*<div class="faq-answer"[^>]*>.*?</div>',
        f'<div class="faq-question">Can life insurance be used for education planning?</div>\n<div class="faq-answer"><p>{edu_life_new_answer}</p></div>',
        content,
        flags=re.DOTALL
    )

    # 7. Footer & Nav Label - Client Stories -> Real Questions & Guidance
    content = content.replace(">Client Stories<", ">Real Questions & Guidance<")
    content = content.replace("Client Stories", "Real Questions & Guidance")

    # 8. Site-wide Service Names
    content = content.replace("Estate Preservation", "Estate & Legacy Planning")
    content = content.replace("Wealth Building", "Financial Strategy")

    # 9. Newsletter description
    content = content.replace(
        "Monthly insights on protecting and growing your family's wealth. No spam, ever.",
        "Monthly insights on family protection, financial planning, and preparing for the future. Unsubscribe anytime."
    )
    content = content.replace(
        "Monthly insights on protecting and growing your family's wealth.",
        "Monthly insights on family protection, financial planning, and preparing for the future."
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("  ✓ Updated index.html with August 2026 PDF changes")


def update_service_pages():
    # 10. family_protection.html
    fp_path = os.path.join(BASE, "family_protection.html")
    if os.path.exists(fp_path):
        with open(fp_path, "r", encoding="utf-8") as f:
            fp_content = f.read()

        fp_living_benefits_text = "Some life insurance policies may include accelerated or living-benefit riders that allow eligible policyholders to access a portion of the death benefit after a qualifying covered event. Availability, qualifying conditions, benefit amounts, charges, and effects on the remaining death benefit depend on the policy and rider terms."
        
        # Replace service names and living benefits explanation
        fp_content = fp_content.replace("Estate Preservation", "Estate & Legacy Planning")
        fp_content = fp_content.replace("Wealth Building", "Financial Strategy")
        fp_content = fp_content.replace("Client Stories", "Real Questions & Guidance")

        with open(fp_path, "w", encoding="utf-8") as f:
            f.write(fp_content)
        print("  ✓ Updated family_protection.html")

    # 11. retirement_planning.html
    rp_path = os.path.join(BASE, "retirement_planning.html")
    if os.path.exists(rp_path):
        with open(rp_path, "r", encoding="utf-8") as f:
            rp_content = f.read()

        rp_content = rp_content.replace("Estate Preservation", "Estate & Legacy Planning")
        rp_content = rp_content.replace("Wealth Building", "Financial Strategy")
        rp_content = rp_content.replace("Client Stories", "Real Questions & Guidance")

        with open(rp_path, "w", encoding="utf-8") as f:
            f.write(rp_content)
        print("  ✓ Updated retirement_planning.html")

    # 12. estate_planning.html
    ep_path = os.path.join(BASE, "estate_planning.html")
    if os.path.exists(ep_path):
        with open(ep_path, "r", encoding="utf-8") as f:
            ep_content = f.read()

        ep_content = ep_content.replace("Estate Preservation", "Estate & Legacy Planning")
        ep_content = ep_content.replace("Wealth Building", "Financial Strategy")
        ep_content = ep_content.replace("Client Stories", "Real Questions & Guidance")

        legal_disclaimer_box = """<div style="background:var(--green-lite); border-left:4px solid var(--green); padding:20px; border-radius:12px; margin:32px 0;">
<p style="font-size:14px; font-weight:500; color:var(--dark); margin:0;"><strong>Legal & Tax Disclaimer:</strong> Family First Legacy does not provide legal or tax advice. Estate documents and legal or tax strategies should be prepared or reviewed with qualified legal and tax professionals.</p>
</div>"""
        if "Family First Legacy does not provide legal or tax advice" not in ep_content:
            ep_content = ep_content.replace("</section>", legal_disclaimer_box + "\n</section>", 1)

        with open(ep_path, "w", encoding="utf-8") as f:
            f.write(ep_content)
        print("  ✓ Updated estate_planning.html")

    # 13 & 14. education_planning.html
    ed_path = os.path.join(BASE, "education_planning.html")
    if os.path.exists(ed_path):
        with open(ed_path, "r", encoding="utf-8") as f:
            ed_content = f.read()

        ed_content = ed_content.replace("Estate Preservation", "Estate & Legacy Planning")
        ed_content = ed_content.replace("Wealth Building", "Financial Strategy")
        ed_content = ed_content.replace("Client Stories", "Real Questions & Guidance")

        with open(ed_path, "w", encoding="utf-8") as f:
            f.write(ed_content)
        print("  ✓ Updated education_planning.html")

    # 15. financial_strategy.html
    fs_path = os.path.join(BASE, "financial_strategy.html")
    if os.path.exists(fs_path):
        with open(fs_path, "r", encoding="utf-8") as f:
            fs_content = f.read()

        fs_content = fs_content.replace("Estate Preservation", "Estate & Legacy Planning")
        fs_content = fs_content.replace("Wealth Building", "Financial Strategy")
        fs_content = fs_content.replace("Client Stories", "Real Questions & Guidance")

        with open(fs_path, "w", encoding="utf-8") as f:
            f.write(fs_content)
        print("  ✓ Updated financial_strategy.html")

    # 16. business_strategies.html
    bs_path = os.path.join(BASE, "business_strategies.html")
    if os.path.exists(bs_path):
        with open(bs_path, "r", encoding="utf-8") as f:
            bs_content = f.read()

        bs_content = bs_content.replace("Estate Preservation", "Estate & Legacy Planning")
        bs_content = bs_content.replace("Wealth Building", "Financial Strategy")
        bs_content = bs_content.replace("Client Stories", "Real Questions & Guidance")

        biz_disclaimer_box = """<div style="background:var(--green-lite); border-left:4px solid var(--green); padding:20px; border-radius:12px; margin:32px 0;">
<p style="font-size:14px; font-weight:500; color:var(--dark); margin:0;"><strong>Business Legal & Tax Disclaimer:</strong> Business strategies may involve legal and tax considerations. Work with qualified legal and tax professionals when establishing agreements or determining tax treatment.</p>
</div>"""
        if "Work with qualified legal and tax professionals" not in bs_content:
            bs_content = bs_content.replace("</section>", biz_disclaimer_box + "\n</section>", 1)

        with open(bs_path, "w", encoding="utf-8") as f:
            f.write(bs_content)
        print("  ✓ Updated business_strategies.html")


def update_legal_and_articles():
    # 17, 18, 19. privacy.html & terms.html
    for fname in ["privacy.html", "terms.html"]:
        fpath = os.path.join(BASE, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("January 2026", "August 2026")
            content = content.replace("january 2026", "August 2026")
            content = content.replace("Estate Preservation", "Estate & Legacy Planning")
            content = content.replace("Wealth Building", "Financial Strategy")
            content = content.replace("Client Stories", "Real Questions & Guidance")

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated {fname} (Last Updated: August 2026)")

    # 20. Article Pages
    article_files = [
        "blog_family_protection.html",
        "blog_retirement.html",
        "blog_education.html",
        "blog_financial_strategy.html",
        "blog_legacy.html",
        "blog_living_benefits.html"
    ]
    for fname in article_files:
        fpath = os.path.join(BASE, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            content = content.replace("Estate Preservation", "Estate & Legacy Planning")
            content = content.replace("Wealth Building", "Financial Strategy")
            content = content.replace("Client Stories", "Real Questions & Guidance")

            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated article metadata in {fname}")


def main():
    print("=== Executing August 2026 PDF Updates ===")
    update_index()
    update_service_pages()
    update_legal_and_articles()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
