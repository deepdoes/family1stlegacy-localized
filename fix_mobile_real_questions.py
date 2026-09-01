#!/usr/bin/env python3
"""
fix_mobile_real_questions.py
Enhances the UI/UX of the 'Real Questions & Guidance' section (#reviews) on mobile devices:
1. Removes vertical clipping/chopping on mobile by letting .qa-display-card-stage auto-expand to fit 100% of answer text.
2. Compacts the question list height (max-height: 240px) on mobile.
3. Optimizes mobile padding and typography inside .q-slide.
4. Adds bottom margin breathing room (margin-bottom: 40px) so the floating mobile bottom bar never covers the CTA button.
5. Adds auto-smooth-scroll in selectQuestion() on mobile devices so tapping a question automatically focuses on the full answer!
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

MOBILE_QA_CSS = """
/* ─── Mobile UI/UX Polish for Real Questions & Guidance Section ─── */
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
    overflow: visible !important;
    margin-bottom: 48px !important;
    border-radius: 20px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06) !important;
  }
  .q-slide {
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

def apply_fix():
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]

    for fname in sorted(html_files):
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False

        # 1. Inject Mobile CSS
        if "Mobile UI/UX Polish for Real Questions" not in content:
            content = content.replace("</head>", f"<style>{MOBILE_QA_CSS}</style>\n</head>")
            updated = True

        # 2. Update selectQuestion JavaScript to include smooth auto-scroll on mobile
        old_js = """function selectQuestion(idx) {
  const slides = document.querySelectorAll('.q-slide');
  const cards = document.querySelectorAll('.q-card');
  if(!slides.length || !cards.length) return;
  
  slides.forEach((s, i) => {
    if(i === idx) {
      s.classList.add('active');
    } else {
      s.classList.remove('active');
    }
  });
  
  cards.forEach((c, i) => {
    if(i === idx) {
      c.classList.add('active');
    } else {
      c.classList.remove('active');
    }
  });
}"""

        new_js = """function selectQuestion(idx) {
  const slides = document.querySelectorAll('.q-slide');
  const cards = document.querySelectorAll('.q-card');
  if(!slides.length || !cards.length) return;
  
  slides.forEach((s, i) => {
    if(i === idx) {
      s.classList.add('active');
    } else {
      s.classList.remove('active');
    }
  });
  
  cards.forEach((c, i) => {
    if(i === idx) {
      c.classList.add('active');
    } else {
      c.classList.remove('active');
    }
  });

  if (window.innerWidth <= 900) {
    const stage = document.querySelector('.qa-display-card-stage');
    if (stage) {
      stage.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
  }
}"""

        if old_js in content:
            content = content.replace(old_js, new_js)
            updated = True

        if updated:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✓ Applied Real Questions mobile UI/UX fix to {fname}")

def main():
    print("=== Applying Mobile UI/UX Polish for Real Questions & Guidance Section ===")
    apply_fix()
    print("=== Done! ===")

if __name__ == "__main__":
    main()
