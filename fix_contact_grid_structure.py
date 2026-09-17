#!/usr/bin/env python3
"""
fix_contact_grid_structure.py
Fixes premature closing of <div class="contact-grid"> across all .html files
so <div class="contact-left"> and <div class="contact-right"> remain side-by-side inside <div class="contact-grid">.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_contact_grid():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in html_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Fix 4 extra </div> tags right before <div class="contact-right"
        pattern = r'(<div class="ci-label">(?:Horario de oficina|Office Hours).*?</div>\s*</div>\s*</div>\s*)</div>\s*</div>\s*</div>\s*(<div class="contact-right")'
        replacement = r'\1</div>\n</div>\n\2'

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Generic pattern for any extra </div> before contact-right
        pattern_generic = r'(<div class="contact-info-list".*?)\n</div>\s*</div>\s*</div>\s*(<div class="contact-right")'
        # Let's cleanly replace the contact section structure in all Spanish pages using regex
        if fname.endswith("_es.html"):
            # Ensure contact-right is inside contact-grid
            content = re.sub(
                r'</div>\s*</div>\s*</div>\s*</div>\s*<div class="contact-right"',
                '</div>\n</div>\n</div>\n<div class="contact-right"',
                content
            )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

    print("  ✓ Fixed contact-grid structural HTML hierarchy across all pages.")

if __name__ == "__main__":
    fix_contact_grid()
