#!/usr/bin/env python3
"""
update_sidebar_trust_badges_wording.py
Updates the sidebar trust badges wording across all Knowledgebase article pages and Python scripts:
- FROM: 24hr Response -> TO: 24hr Response
- FROM: Your Privacy Matters -> TO: Your Privacy Matters
- Spanish: Respuesta en 24 horas / Su privacidad importa
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

REPLACEMENTS = [
    ("24hr Response", "24hr Response"),
    ("Your Privacy Matters", "Your Privacy Matters"),
    ("Respuesta en 24 horas", "Respuesta en 24 horas"),
    ("Su privacidad importa", "Su privacidad importa"),
]

def apply_update():
    for root, dirs, files in os.walk(BASE):
        if ".next" in root or "node_modules" in root:
            continue
        for fname in files:
            if fname.endswith(".html") or fname.endswith(".py"):
                fpath = os.path.join(root, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                updated = False
                for old, new in REPLACEMENTS:
                    if old in content:
                        content = content.replace(old, new)
                        updated = True
                
                if updated:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"  ✓ Updated sidebar trust badges in {fname}")

def main():
    print("=== Updating Sidebar Trust Badges Wording ===")
    apply_update()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
