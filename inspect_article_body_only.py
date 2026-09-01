#!/usr/bin/env python3
"""
inspect_article_body_only.py
Extracts strictly the article text content inside the blog body (excluding headers, footers, forms, scripts)
to give an exact word count and paragraph breakdown of each article.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

blog_files = [
    "blog_family_protection.html",
    "blog_retirement.html",
    "blog_education.html",
    "blog_living_benefits.html",
    "blog_financial_strategy.html",
    "blog_legacy.html"
]

def analyze_article_text(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract content between blog-content-wrapper or article body
    match = re.search(r'<div class="blog-content-body"[^>]*>(.*?)</div>\s*<div style="margin-top:32px;">', html, flags=re.DOTALL)
    if not match:
        match = re.search(r'<div class="blog-body"[^>]*>(.*?)</div>\s*<!-- CTA BANNER', html, flags=re.DOTALL)
    
    if not match:
        return {"words": 0, "h2": 0, "p": 0}

    body_html = match.group(1)
    
    clean_text = re.sub(r'<[^>]+>', ' ', body_html)
    words = [w for w in clean_text.split() if len(w) > 1]
    
    h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', body_html, flags=re.DOTALL)
    p_matches = re.findall(r'<p[^>]*>(.*?)</p>', body_html, flags=re.DOTALL)

    return {
        "words": len(words),
        "h2_count": len(h2_matches),
        "p_count": len(p_matches),
        "h2_titles": [re.sub(r'<[^>]+>', '', h).strip() for h in h2_matches]
    }

def main():
    print("=== Analyzing Article Content Depth ===")
    for bfile in blog_files:
        path = os.path.join(BASE, bfile)
        stats = analyze_article_text(path)
        if stats:
            print(f"\n📄 {bfile}:")
            print(f"   • Word Count: {stats['words']} words")
            print(f"   • Section Headings (H2): {stats['h2_count']}")
            print(f"   • Paragraphs: {stats['p_count']}")
            print("   • Subheadings:")
            for h2 in stats['h2_titles']:
                print(f"     - {h2}")

if __name__ == "__main__":
    main()
