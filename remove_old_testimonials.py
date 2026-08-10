#!/usr/bin/env python3
"""
remove_old_testimonials.py
Removes the old dummy testimonial section (<section id="testimonial">...</section>)
from all HTML files so only the compliant "Real Questions. Clear Guidance." section remains.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def remove_testimonial_section(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    pattern = r'<!-- TESTIMONIAL \(featured slideshow\).*?--!?>\s*<section id="testimonial">.*?</section>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

    pattern2 = r'<section id="testimonial">.*?</section>'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Removed dummy testimonials from {os.path.basename(filepath)}")
    else:
        print(f"  CLEAN: {os.path.basename(filepath)}")

def main():
    print("=== Removing Dummy Testimonial Sections Across All HTML Files ===")
    html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
    for filepath in html_files:
        remove_testimonial_section(filepath)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
