#!/usr/bin/env python3
"""
fix_logo_links_across_all_subpages.py
Updates top-left navbar logo and footer logo links across all subpages and blog pages:
- English subpages: href="index.html"
- Spanish subpages: href="index_es.html"
- Leaves homepage index.html as href="#" (or index.html) for scroll-to-top behavior.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def fix_logos():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        # Skip homepage index files (their logo scrolls to top #)
        if fname in ["index.html", "index_es.html", "index_pt.html", "index_rw.html", "index_sw.html"]:
            continue

        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        home_target = "index_es.html" if "_es." in fname else "index.html"

        # Regex patterns to replace nav-logo links pointing to # or #hero
        new_content = re.sub(r'<a\s+href="#"\s+class="nav-logo"', f'<a href="{home_target}" class="nav-logo"', content)
        new_content = re.sub(r'<a\s+class="nav-logo"\s+href="#"', f'<a class="nav-logo" href="{home_target}"', new_content)
        new_content = re.sub(r'<a\s+href="#hero"\s+class="nav-logo"', f'<a href="{home_target}" class="nav-logo"', new_content)

        # Footer logo link fix if needed
        new_content = re.sub(r'<a\s+href="#"\s+class="nav-logo"\s+style="text-decoration:none"', f'<a href="{home_target}" class="nav-logo" style="text-decoration:none"', new_content)

        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  ✓ Fixed navbar and footer logo links (pointing to {home_target}) in {fname}")

def main():
    print("=== Fixing Top-Left Navbar & Footer Logo Links Across All Subpages ===")
    fix_logos()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
