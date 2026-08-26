#!/usr/bin/env python3
"""
upgrade_subpage_cta_banners.py
Upgrades the basic CTA banner across all subpages to match the high-converting,
premium glassmorphism CTA banner from index.html.
Removes internal developer jargon 'Call to Action' and replaces it with professional eyebrow tags.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

PREMIUM_CTA_TEMPLATE = """<!-- CTA BANNER ──────────────────────────────────────── -->
<section id="cta-banner">
  <div class="cta-scanline"></div>
  <div class="cta-orb cta-orb-1"></div>
  <div class="cta-orb cta-orb-2"></div>
  <div class="cta-orb cta-orb-3"></div>
  <div class="container">
    <div class="cta-inner">
      <div class="cta-left">
        <div class="cta-badge" data-reveal>
          <span class="cta-badge-dot"></span>
          <span>{EYEBROW}</span>
        </div>
        <div class="cta-text">
          <h2 data-reveal data-delay="1">{HEADING}</h2>
          <p data-reveal data-delay="2">{SUBTEXT}</p>
        </div>
      </div>
      <div class="cta-right" data-reveal="right" data-delay="2">
        <div class="cta-actions">
          <a href="index.html#contact" class="btn-white">
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            Schedule a No-Cost Review
          </a>
          <a href="tel:+14696081595" class="btn-outline-white">
            <svg viewBox="0 0 24 24"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            Call (469) 608-1595
          </a>
        </div>
        <div class="cta-stats">
          <div class="cts-item">
            <div class="cts-num">24hr</div>
            <div class="cts-lbl">Response</div>
          </div>
          <div class="cts-item">
            <div class="cts-num">No-Cost</div>
            <div class="cts-lbl">Consultation</div>
          </div>
          <div class="cts-item">
            <div class="cts-num">100%</div>
            <div class="cts-lbl">Licensed Professionals</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>"""

PAGES_CONFIG = [
    (
        "estate_planning.html",
        "PROTECT YOUR LEGACY",
        "Protect the People and Values<br>That <em>Matter Most.</em>",
        "Estate and legacy planning can help your wishes be clearly known and your loved ones better prepared. Ask questions, compare options, and plan with clarity — no pressure."
    ),
    (
        "family_protection.html",
        "TAKE THE NEXT STEP",
        "Know What Protects Your Family<br>Before <em>Life Changes.</em>",
        "Ask questions, review your protection options, and decide with clarity — no pressure, no obligation."
    ),
    (
        "retirement_planning.html",
        "RETIRE WITH CLARITY",
        "Your Retirement Deserves<br>a <em>Clear Plan.</em>",
        "Planning for retirement is about more than just saving money. Ask questions, understand your income options, and build a strategy with confidence."
    ),
    (
        "education_planning.html",
        "INVEST IN THEIR FUTURE",
        "Build a Flexible Foundation<br>for Their <em>Education.</em>",
        "Explore flexible savings and growth strategies tailored to your child's future goals. Request a no-cost review today."
    ),
    (
        "financial_strategy.html",
        "BUILD YOUR STRATEGY",
        "Take Control of Your<br>Financial <em>Future.</em>",
        "Customized financial strategies designed around your family's unique goals, cash flow, and protection needs."
    ),
    (
        "business_strategies.html",
        "PROTECT YOUR BUSINESS",
        "Ensure Business Continuity<br>& <em>Key-Person Protection.</em>",
        "Plan for business stability, key-person coverage, and smooth succession. Schedule a consultation with our team."
    ),
    (
        "opportunity.html",
        "JOIN OUR TEAM",
        "Build a Purpose-Driven Career<br>in <em>Financial Services.</em>",
        "Help families protect their financial future while building a rewarding career with ongoing mentorship and growth."
    )
]

def main():
    print("=== Upgrading Subpage CTA Banners to Premium Glassmorphism Design ===")

    for fname, eyebrow, heading, subtext in PAGES_CONFIG:
        fpath = os.path.join(BASE, fname)
        if not os.path.exists(fpath):
            print(f"❌ File not found: {fname}")
            continue

        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Build replacement html
        new_cta = PREMIUM_CTA_TEMPLATE.format(
            EYEBROW=eyebrow,
            HEADING=heading,
            SUBTEXT=subtext
        )

        # Replace old subpage cta section
        pattern = r'<section class="subpage-cta"[^>]*>.*?</section>'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, new_cta, content, flags=re.DOTALL)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Upgraded CTA banner in {fname}")
        elif '<section id="cta-banner">' in content:
            # Check if it already has old eyebrow
            content = re.sub(r'<span>Call to Action</span>', f'<span>{eyebrow}</span>', content)
            content = re.sub(r'Call to Action', eyebrow, content)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated eyebrow in {fname}")
        else:
            print(f"  ⚠️ Could not find CTA section in {fname}")

    print("=== Done! ===")

if __name__ == "__main__":
    main()
