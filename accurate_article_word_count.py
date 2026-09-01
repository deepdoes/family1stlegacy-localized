#!/usr/bin/env python3
"""
accurate_article_word_count.py
Parses the exact <div class="article-main-col"> content of all blog files to measure word count and reading time.
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

def analyze(fname):
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    match = re.search(r'<div class="article-main-col"[^>]*>(.*?)</div>\s*<!-- RIGHT SIDEBAR', html, flags=re.DOTALL)
    if not match:
        match = re.search(r'<div class="article-main-col"[^>]*>(.*?)</div>', html, flags=re.DOTALL)

    if not match:
        return 0, 0, 0

    body = match.group(1)
    clean = re.sub(r'<[^>]+>', ' ', body)
    words = [w for w in clean.split() if len(w) > 0]
    
    h2_matches = re.findall(r'<h2[^>]*>', body)
    p_matches = re.findall(r'<p[^>]*>', body)

    return len(words), len(h2_matches), len(p_matches)

def main():
    print("=== Article Content Length Audit ===")
    print(f"{'Article':<32} | {'Word Count':<12} | {'Headings (H2)':<15} | {'Paragraphs':<10} | {'Read Time'}")
    print("-" * 85)
    for b in blog_files:
        w, h, p = analyze(b)
        read_time = f"{max(1, round(w / 200))} min read"
        print(f"{b:<32} | {w:<12} | {h:<15} | {p:<10} | {read_time}")

if __name__ == "__main__":
    main()
