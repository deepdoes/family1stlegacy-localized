#!/usr/bin/env python3
"""
update_navbar_dropdown_behavior.py
Updates src/components/layout/Navbar.tsx so dropdown links (like Services) render as interactive buttons
preventing page navigation on click/tap, opening on mouseover (hover) on desktop, and toggling on touch devices.
"""

import os

NAVBAR_TSX = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy/src/components/layout/Navbar.tsx"

def update():
    with open(NAVBAR_TSX, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Link rendering when dropdown exists
    old_code = """                  <Link
                    href={item.href}
                    className={`text-sm font-medium transition-colors hover:text-purple-600 flex items-center gap-1 ${
                      isStuck ? "text-gray-700" : "text-white/90"
                    }`}
                  >
                    {item.label}
                    {item.dropdown && <ChevronDown className="w-3.5 h-3.5 opacity-70 group-hover:rotate-180 transition-transform" />}
                  </Link>"""

    new_code = """                  {item.dropdown ? (
                    <button
                      type="button"
                      onClick={(e) => { e.preventDefault(); e.stopPropagation(); }}
                      className={`text-sm font-medium transition-colors hover:text-purple-600 flex items-center gap-1 bg-transparent border-none cursor-pointer ${
                        isStuck ? "text-gray-700" : "text-white/90"
                      }`}
                    >
                      {item.label}
                      <ChevronDown className="w-3.5 h-3.5 opacity-70 group-hover:rotate-180 transition-transform" />
                    </button>
                  ) : (
                    <Link
                      href={item.href}
                      className={`text-sm font-medium transition-colors hover:text-purple-600 flex items-center gap-1 ${
                        isStuck ? "text-gray-700" : "text-white/90"
                      }`}
                    >
                      {item.label}
                    </Link>
                  )}"""

    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(NAVBAR_TSX, "w", encoding="utf-8") as f:
            f.write(content)
        print("  ✓ Successfully updated Navbar.tsx dropdown trigger behavior")
    else:
        print("  ⚠ Could not find exact code block in Navbar.tsx")

if __name__ == "__main__":
    update()
