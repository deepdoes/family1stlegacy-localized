#!/usr/bin/env python3
"""
inspect_article_lengths.py
Compares the blog article lengths (word count, headings, paragraphs) between v1/ original files
and current root blog files to determine if any content was trimmed or how deep they currently are.
"""

import os
import re
from bs4 import BeautifulSoup

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
V1_DIR = os.path.join(BASE, "v1")

blog_files = [
    "blog_family_protection.html",
    "blog_retirement.html",
    "blog_education.html",
    "blog_living_benefits.html",
    "blog_financial_strategy.html",
    "blog_legacy.html"
]

def analyze_file(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract article container content
    match = re.search(r'<article[^>]*>(.*?)</article>', html, flags=re.DOTALL)
    if not match:
        match = re.search(r'<div class="blog-body"[^>]*>(.*?)</div>\s*<!-- CTA BANNER', html, flags=re.DOTALL)
    
    text_content = match.group(1) if match else html
    
    # Strip HTML tags to get pure text word count
    clean_text = re.sub(r'<[^>]+>', ' ', text_content)
    words = clean_text.split()
    h2_count = len(re.findall(r'<h2[^>]*>', text_content))
    p_count = len(re.findall(r'<p[^>]*>', text_content))
    
    return {
        "words": len(words),
        "h2_count": h2_count,
        "p_count": p_count
    }

def compare():
    print(f"{'Article File':<30} | {'Current Words':<15} | {'V1 Words':<15} | {'Difference'}")
    print("-" * 75)

    for bfile in blog_files:
        curr_path = os.path.join(BASE, bfile)
        v1_path = os.path.join(V1_DIR, bfile)

        curr_stats = analyze_file(curr_path)
        v1_stats = analyze_file(v1_path)

        curr_w = curr_stats['words'] if curr_stats else 'N/A'
        v1_w = v1_stats['words'] if v1_stats else 'N/A'
        
        diff = ""
        if isinstance(curr_w, int) and isinstance(v1_w, int):
            diff = f"{curr_w - v1_w:+d} words"
        elif v1_w == 'N/A':
            diff = "New article"

        print(f"{bfile:<30} | {str(curr_w):<15} | {str(v1_w):<15} | {diff}")

if __name__ == "__main__":
    compare()
