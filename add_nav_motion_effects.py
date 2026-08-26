#!/usr/bin/env python3
"""
add_nav_motion_effects.py
Injects high-end motion effects for main menu mouse hover and active states across all HTML pages:
- Elevates menu items on hover (-2px)
- Glowing gradient underline bar on hover & active items
- Spring bounce chevron 180° rotation
- Submenu item slide right on hover (+6px with purple highlight)
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

NAV_MOTION_CSS = """
/* ─────────────────────────────────────────────────────────────
   PREMIUM NAVIGATION HOVER & ACTIVE MOTION EFFECTS
───────────────────────────────────────────────────────────── */
.nav-links > li > a:not(.nav-cta),
.nav-dropdown-toggle {
  position: relative;
  transition: color 0.3s cubic-bezier(0.25, 1, 0.5, 1), transform 0.3s cubic-bezier(0.25, 1, 0.5, 1) !important;
}

/* Elevate link slightly on mouse hover */
.nav-links > li > a:not(.nav-cta):hover,
.nav-dropdown-wrap:hover .nav-dropdown-toggle {
  transform: translateY(-2px);
  color: var(--amber-lt, #E8C170) !important;
}

#nav.stuck .nav-links > li > a:not(.nav-cta):hover,
#nav.stuck .nav-dropdown-wrap:hover .nav-dropdown-toggle {
  color: var(--purple, #4a2d7a) !important;
}

/* Glowing underline indicator bar on hover */
.nav-links > li > a:not(.nav-cta)::after,
.nav-dropdown-toggle::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  width: 0;
  height: 2.5px;
  background: linear-gradient(90deg, var(--green, #1d9e75), var(--amber, #d9aa43));
  border-radius: 4px;
  transform: translateX(-50%);
  transition: width 0.35s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.35s ease;
  opacity: 0;
  box-shadow: 0 2px 8px rgba(29, 158, 117, 0.5);
}

.nav-links > li > a:not(.nav-cta):hover::after,
.nav-dropdown-wrap:hover .nav-dropdown-toggle::after {
  width: 80%;
  opacity: 1;
}

/* Active Menu Item Glow Dot & Underline */
.nav-links > li > a.nav-active:not(.nav-cta)::after,
.nav-links > li > a.pill-active:not(.nav-cta)::after {
  width: 80% !important;
  opacity: 1 !important;
  background: var(--amber, #d9aa43) !important;
  box-shadow: 0 0 10px rgba(217, 170, 67, 0.7) !important;
}

.nav-links > li > a.nav-active:not(.nav-cta),
.nav-links > li > a.pill-active:not(.nav-cta) {
  font-weight: 700 !important;
}

/* Submenu Item Motion Effects */
.nav-dropdown a {
  position: relative;
  transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important;
}

.nav-dropdown a:hover {
  transform: translateX(6px) !important;
  padding-left: 26px !important;
  background: rgba(74, 45, 122, 0.06) !important;
  color: var(--purple, #4a2d7a) !important;
}

/* Chevron Rotation with Spring Physics */
.nav-dropdown-toggle svg.chevron {
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
}

.nav-dropdown-wrap:hover .nav-dropdown-toggle svg.chevron {
  transform: rotate(180deg) scale(1.2) !important;
}
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "PREMIUM NAVIGATION HOVER & ACTIVE MOTION EFFECTS" in content:
        print(f"  ✓ Motion effects already present in {filename}")
        return

    if "</style>" in content:
        content = content.replace("</style>", NAV_MOTION_CSS + "\n</style>", 1)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Injected nav motion effects into {filename}")

def main():
    print("=== Injecting Premium Nav Motion Effects Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
