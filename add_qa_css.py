#!/usr/bin/env python3
"""
add_qa_css.py
Injects the missing Real Questions Interactive Dashboard CSS rules into index_es.html and all HTML files.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

QA_CSS = """
/* Real Questions Interactive Dashboard styles */
.qa-dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 40px;
  align-items: flex-start;
  margin-top: 40px;
}
@media (max-width: 900px) {
  .qa-dashboard-grid {
    grid-template-columns: 1fr;
  }
  .qa-selectors-list {
    max-height: 320px !important;
  }
}
.qa-selectors-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-height: 520px;
  overflow-y: auto;
  padding: 8px 8px 8px 4px;
}
.qa-selectors-list::-webkit-scrollbar {
  width: 6px;
}
.qa-selectors-list::-webkit-scrollbar-track {
  background: rgba(0,0,0,0.02);
  border-radius: 10px;
}
.qa-selectors-list::-webkit-scrollbar-thumb {
  background: rgba(29, 158, 117, 0.2);
  border-radius: 10px;
}
.qa-selectors-list::-webkit-scrollbar-thumb:hover {
  background: rgba(29, 158, 117, 0.4);
}
.q-card {
  cursor: pointer;
  padding: 20px 24px;
  border-radius: 16px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: #ffffff;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: hidden;
  flex-shrink: 0;
}
.q-card:hover {
  background: rgba(0, 0, 0, 0.01);
  border-color: rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}
.q-card.active {
  border-color: var(--green) !important;
  background: rgba(29, 158, 117, 0.05) !important;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.6);
}
.q-card::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: var(--green);
  transform: scaleY(0);
  transition: transform 0.3s ease;
}
.q-card.active::before {
  transform: scaleY(1);
}
.q-slide {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.4s ease, transform 0.4s ease;
  transform: translateY(10px);
}
.q-slide.active {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '.qa-dashboard-grid' in content:
        print(f"  CLEAN: {os.path.basename(filepath)}")
        return

    content = content.replace('</style>', QA_CSS.strip() + '\n</style>', 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Added Real Questions CSS to {os.path.basename(filepath)}")

def main():
    print("=== Injecting Real Questions Dashboard CSS Across All HTML Files ===")
    html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
    for filepath in html_files:
        update_file(filepath)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
