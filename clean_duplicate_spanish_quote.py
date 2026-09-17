#!/usr/bin/env python3
"""
clean_duplicate_spanish_quote.py
Removes duplicate quote box in about-content on index_es.html so it matches index.html master 1:1.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
FPATH = os.path.join(BASE, "index_es.html")

with open(FPATH, "r", encoding="utf-8") as f:
    html = f.read()

# Remove duplicate about-pull in about-content
html = re.sub(
    r'(<div class="about-content">.*?<a class="btn btn-green".*?</a>)\s*<div class="about-pull".*?</div>',
    r'\1',
    html,
    flags=re.DOTALL
)

# Remove about-pull between paragraph and button if present
html = re.sub(
    r'<div class="about-pull" data-delay="3" data-reveal="">\s*<p>“Hacemos más que ofrecer seguros:.*?</cite>\s*</div>\s*',
    '',
    html,
    flags=re.DOTALL
)

with open(FPATH, "w", encoding="utf-8") as f:
    f.write(html)

print("  ✓ Cleaned duplicate quote box on index_es.html")
