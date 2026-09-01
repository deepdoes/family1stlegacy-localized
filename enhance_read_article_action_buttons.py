#!/usr/bin/env python3
"""
enhance_read_article_action_buttons.py
Enhances the 'READ ARTICLE ->' action button on all blog cards across the website:
- Ensures pointer-events: auto and cursor: pointer for 100% immediate touch responsiveness.
- Adds an explicit, attractive interactive button style (subtle pill background + hover state)
  so users and clients instantly recognize it as a fully functional action button.
"""

import os

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

READ_ARTICLE_CSS_FIX = """
/* ─── Read Article Action Button Touch & Hover Enhancement ─── */
.bc-link {
  margin-top: auto !important;
  font-size: 12px !important;
  font-weight: 700 !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  color: #4A2D7A !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  padding: 8px 16px !important;
  background: rgba(74, 45, 122, 0.06) !important;
  border: 1px solid rgba(74, 45, 122, 0.12) !important;
  border-radius: 30px !important;
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
  cursor: pointer !important;
  pointer-events: auto !important;
  width: fit-content !important;
}
.blog-card:hover .bc-link,
.bc-link:hover {
  background: #4A2D7A !important;
  color: #ffffff !important;
  border-color: #4A2D7A !important;
  box-shadow: 0 4px 12px rgba(74, 45, 122, 0.25) !important;
}
.bc-link svg {
  width: 13px !important;
  height: 13px !important;
  stroke: currentColor !important;
  fill: none !important;
  stroke-width: 2.5 !important;
  transition: transform 0.3s ease !important;
}
.blog-card:hover .bc-link svg,
.bc-link:hover svg {
  transform: translateX(4px) !important;
  stroke: #ffffff !important;
}
"""

def apply_enhancement():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    
    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        if "Read Article Action Button Touch & Hover Enhancement" not in content:
            content = content.replace("</head>", f"<style>{READ_ARTICLE_CSS_FIX}</style>\n</head>")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Added Read Article action button enhancement to {fname}")

def main():
    print("=== Enhancing Read Article Action Buttons Across All Pages ===")
    apply_enhancement()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
