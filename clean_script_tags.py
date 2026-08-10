#!/usr/bin/env python3
"""
clean_script_tags.py
Fixes duplicate/nested <script> tags and cleanly defines selectQuestion(idx) in all HTML files.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

CLEAN_JS = """
<script>
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
</script>
"""

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all previous broken injections
    content = re.sub(r'<script>\s*<script>.*?</script>\s*</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*<script>', '<script>', content)
    content = re.sub(r'<script>\s*function selectQuestion\(idx\).*?</script>', '', content, flags=re.DOTALL)

    # Insert clean JS before </body>
    content = content.replace('</body>', f'{CLEAN_JS.strip()}\n</body>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Cleaned JS tags in {os.path.basename(filepath)}")

def main():
    print("=== Cleaning Script Tags Across All HTML Files ===")
    html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
    for filepath in html_files:
        clean_file(filepath)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
