#!/usr/bin/env python3
"""
set_saturday_hours_10am_2pm.py
Updates Saturday office hours across all HTML files to:
"Mon–Fri: 9am – 7pm · Sat: 10am – 2pm"
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def update_hours():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    
    old_target = "Sat: 10am – 6pm"
    new_target = "Sat: 10am – 2pm"
    
    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if old_target in content:
            content = content.replace(old_target, new_target)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Updated Saturday office hours to '{new_target}' in {fname}")

def main():
    print("=== Updating Saturday Office Hours to 10am - 2pm Across All Pages ===")
    update_hours()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
