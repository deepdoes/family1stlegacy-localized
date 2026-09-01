#!/usr/bin/env python3
"""
apply_item1_homepage_wording.py
Applies Item #1 wording across all English HTML pages:
1. Contact / Trust Badges: Licensed & Insured • 24hr Response • Your Privacy Matters
2. Newsletter Subtitle: Monthly insights on family protection, financial planning, and preparing for the future. Unsubscribe anytime.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

TRUST_BADGES_HTML = """<div class="contact-trust" data-reveal data-delay="2">
          <span class="ct-chip"><svg viewBox="0 0 24 24"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"/></svg>Licensed &amp; Insured</span>
          <span class="ct-chip"><svg viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>24hr Response</span>
          <span class="ct-chip"><svg viewBox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>Your Privacy Matters</span>
        </div>"""

NEWSLETTER_SUB_HTML = '<div class="fn-sub">Monthly insights on family protection, financial planning, and preparing for the future. Unsubscribe anytime.</div>'

def is_english_file(fname):
    if not fname.endswith(".html") or fname.startswith("v1"):
        return False
    # Filter out language suffixes
    for lang in ["_es.", "_pt.", "_rw.", "_sw."]:
        if lang in fname:
            return False
    return True

def apply_item1():
    english_files = [f for f in os.listdir(BASE) if is_english_file(f)]
    
    for fname in sorted(english_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Replace contact trust badges block
        trust_pattern = r'<div class="contact-trust"[^>]*>.*?</div>'
        if re.search(trust_pattern, content, flags=re.DOTALL):
            content = re.sub(trust_pattern, TRUST_BADGES_HTML, content, flags=re.DOTALL)

        # 2. Replace newsletter subtitle text
        news_pattern = r'<div class="fn-sub">.*?</div>'
        if re.search(news_pattern, content, flags=re.DOTALL):
            content = re.sub(news_pattern, NEWSLETTER_SUB_HTML, content, flags=re.DOTALL)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Applied Item #1 wording to {fname}")

def main():
    print("=== Applying Item #1 Approved Home-Page Wording Across English Pages ===")
    apply_item1()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
