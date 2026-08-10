#!/usr/bin/env python3
"""
fix_select_question_js.py
Injects top-level selectQuestion(idx) and switchRqCard(idx) functions into all HTML files.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SELECT_QUESTION_JS = """
function selectQuestion(idx) {
  var slides = document.querySelectorAll('.q-slide');
  var cards = document.querySelectorAll('.q-card');
  if (slides.length && cards.length) {
    slides.forEach(function(s, i) {
      if (i === idx) {
        s.classList.add('active');
      } else {
        s.classList.remove('active');
      }
    });
    cards.forEach(function(c, i) {
      if (i === idx) {
        c.classList.add('active');
      } else {
        c.classList.remove('active');
      }
    });
  }
}
var switchRqCard = selectQuestion;
window.selectQuestion = selectQuestion;
window.switchRqCard = selectQuestion;
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old script injection if present
    content = re.sub(r'<script>\s*window\.selectQuestion = function.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── Real Questions Selector JavaScript ──.*?</script>', '', content, flags=re.DOTALL)

    if 'function selectQuestion(' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'<script>\n{SELECT_QUESTION_JS.strip()}\n</script>\n</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Injected global selectQuestion JS into {os.path.basename(filepath)}")

def main():
    print("=== Injecting global selectQuestion JS Across All HTML Files ===")
    html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
    for filepath in html_files:
        update_file(filepath)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
