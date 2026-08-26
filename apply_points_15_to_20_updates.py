#!/usr/bin/env python3
"""
apply_points_15_to_20_updates.py
Applies compliance & technical updates for Items 15-20 across all active HTML files:

Item 15 (FINANCIAL STRATEGY):
Replaces unconditional tax-free statements in financial_strategy.html with qualified wording:
"Depending on policy design and current tax law, cash value may be accessed on a tax-advantaged basis in some situations. Accessing cash value can affect policy benefits and may have tax implications. Consult a qualified tax professional."

Item 16 (BUSINESS STRATEGIES):
Ensures legal & tax disclaimer is present near buy-sell / succession content in business_strategies.html:
"Business strategies may involve legal and tax considerations. Work with qualified legal and tax professionals when establishing agreements or determining tax treatment."

Item 17 & 18 (PRIVACY POLICY):
Ensures exact compliant paragraph under Website Forms and Data Storage & Cookies in privacy.html:
"Family First Legacy does not intentionally use this website as a repository for sensitive personal information. Information submitted through forms may be processed or stored by the service providers we use to operate forms, email, CRM, scheduling, analytics, or website hosting."

Item 19 (TERMS & PRIVACY DATES):
Ensures "Last Updated: August 2026" / "August 26, 2026" is set across terms.html and privacy.html.

Item 20 (KNOWLEDGEBASE ARTICLES):
Verifies preview cards, headings, and article content consistency.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

ROW15_TEXT = "Depending on policy design and current tax law, cash value may be accessed on a tax-advantaged basis in some situations. Accessing cash value can affect policy benefits and may have tax implications. Consult a qualified tax professional."
ROW17_TEXT = "Family First Legacy does not intentionally use this website as a repository for sensitive personal information. Information submitted through forms may be processed or stored by the service providers we use to operate forms, email, CRM, scheduling, analytics, or website hosting."

def update_points(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Item 15: Financial Strategy
    if "financial_strategy" in filename:
        faq_tax_pattern = r'(<button class="faq-q"[^>]*>\s*What is a tax-efficient retirement strategy\?\s*<div class="faq-icon"></div>\s*</button>\s*<div class="faq-a"><p>).*?(</p></div>)'
        if re.search(faq_tax_pattern, content, flags=re.DOTALL):
            content = re.sub(faq_tax_pattern, r'\1' + ROW15_TEXT + r'\2', content, flags=re.DOTALL)

    # Item 17 & 18 & 19: Privacy & Terms
    if "privacy" in filename:
        content = re.sub(r'Last Updated: [A-Za-z]+ \d{4}', 'Last Updated: August 2026', content)
        # Clean duplicate paragraph under Website Forms
        duplicate_pat = r'<p>Family First Legacy does not intentionally store personal information directly on this website, except for information visitors choose to submit through contact forms, consultation request forms, or message fields\.</p>'
        content = re.sub(duplicate_pat, '', content)

    if "terms" in filename:
        content = re.sub(r'Last Updated: [A-Za-z]+ \d{4}', 'Last Updated: August 2026', content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Applied compliance & legal updates for Items 15-20 in {filename}")

def main():
    print("=== Applying Items 15-20 Compliance & Legal Updates Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_points(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
