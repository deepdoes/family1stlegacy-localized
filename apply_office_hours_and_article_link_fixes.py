#!/usr/bin/env python3
"""
apply_office_hours_and_article_link_fixes.py
1. Updates Saturday office hours across all HTML files from 'Sat: 10am – 4pm' to 'Sat: 10am – 6pm' (or 'Sat: 2pm – 6pm' as requested).
2. Fixes article action buttons on blog pages (href="#contact") by pointing them to 'index.html#contact'
   so that clicking "Schedule a No-Cost Review" or "Get Started Free" from any article page smoothly lands on the contact form!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_office_hours():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    
    old_hours = "Sat: 10am – 4pm"
    new_hours = "Sat: 10am – 6pm"

    old_hours_2 = "Sat: 10am - 4pm"
    
    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False
        if old_hours in content:
            content = content.replace(old_hours, new_hours)
            updated = True
        if old_hours_2 in content:
            content = content.replace(old_hours_2, new_hours)
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated Saturday office hours to '{new_hours}' in {fname}")

def fix_article_action_buttons():
    blog_files = [f for f in os.listdir(BASE) if f.startswith("blog_") and f.endswith(".html")]
    
    for fname in sorted(blog_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Is Spanish blog?
        home_target = "index_es.html#contact" if "_es." in fname else "index.html#contact"

        # Replace href="#contact" inside article body button (e.g. Schedule a No-Cost Review)
        new_content = re.sub(r'href="#contact"', f'href="{home_target}"', content)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  ✓ Fixed article action button links (pointing to {home_target}) in {fname}")

def main():
    print("=== Applying Saturday Office Hours & Article Action Button Fixes ===")
    fix_office_hours()
    fix_article_action_buttons()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
