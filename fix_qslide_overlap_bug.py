#!/usr/bin/env python3
"""
fix_qslide_overlap_bug.py
Fixes the Real Questions slide overlapping bug by enforcing strict display controls:
- Non-active slides (.q-slide:not(.active)): display: none !important; opacity: 0; visibility: hidden; pointer-events: none;
- Active slide (.q-slide.active): display: flex !important; opacity: 1; visibility: visible; pointer-events: auto;
This guarantees that ONLY ONE active slide is rendered at any time, with zero text overlapping or ghosting on mobile or desktop!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SLIDE_STRICT_CSS = """
/* ─── Strict Q&A Slide Display & Mobile Polish (Prevents Text Overlapping) ─── */
.q-slide {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
}
.q-slide.active {
  display: flex !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  position: relative !important;
  width: 100% !important;
  height: 100% !important;
}

@media (max-width: 900px) {
  .qa-dashboard-grid {
    grid-template-columns: 1fr !important;
    gap: 24px !important;
  }
  .qa-selectors-list {
    max-height: 240px !important;
    overflow-y: auto !important;
    padding-right: 6px !important;
  }
  .qa-display-card-stage {
    min-height: auto !important;
    height: auto !important;
    overflow: hidden !important;
    margin-bottom: 48px !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06) !important;
  }
  .q-slide.active {
    padding: 24px 20px !important;
    height: auto !important;
    min-height: auto !important;
  }
  .q-slide h3 {
    font-size: 20px !important;
    line-height: 1.4 !important;
    margin-bottom: 14px !important;
  }
  .q-slide p {
    font-size: 14.5px !important;
    line-height: 1.65 !important;
  }
  .q-slide .btn {
    margin-top: 20px !important;
    width: 100% !important;
    text-align: center !important;
    justify-content: center !important;
  }
}
"""

def remove_previous_bad_css(content):
    # Strip any previous broken mobile QA CSS injection if present
    content = re.sub(r'/\* ─── Mobile UI/UX Polish for Real Questions & Guidance Section ─── \*/.*?</style>', '</style>', content, flags=re.DOTALL)
    content = re.sub(r'/\* ─── Strict Q&A Slide Display & Mobile Polish \(Prevents Text Overlapping\) ─── \*/.*?</style>', '</style>', content, flags=re.DOTALL)
    return content

def apply_fix():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        content = remove_previous_bad_css(content)
        content = content.replace("</head>", f"<style>{SLIDE_STRICT_CSS}</style>\n</head>")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✓ Fixed slide display overlap bug in {fname}")

def main():
    print("=== Fixing Q&A Slide Overlapping Bug Across All HTML Files ===")
    apply_fix()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
