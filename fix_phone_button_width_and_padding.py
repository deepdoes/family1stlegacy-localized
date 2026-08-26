#!/usr/bin/env python3
"""
fix_phone_button_width_and_padding.py
Fixes the top-right mobile call button (.mobile-nav-call-btn) stretching too wide across the header:
- Sets flex: 0 0 auto !important, width: auto !important, max-width: fit-content !important, height: 34px !important.
- Compact padding: 6px 14px !important with white-space: nowrap !important.
- Ensures elegant, perfectly proportioned pill hugging top-right corner without stretching.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

PHONE_BTN_FIX_CSS = """
  /* Mobile Call Button - Compact & Non-Stretching Pill */
  .mobile-nav-call-btn {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 6px !important;
    padding: 6px 14px !important;
    height: 34px !important;
    width: auto !important;
    max-width: fit-content !important;
    flex: 0 0 auto !important;
    flex-shrink: 0 !important;
    border-radius: 20px !important;
    font-family: var(--font-head, sans-serif) !important;
    font-size: 12px !important;
    font-weight: 700 !important;
    text-decoration: none !important;
    margin: 0 !important;
    margin-left: auto !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08) !important;
    white-space: nowrap !important;
    box-sizing: border-box !important;
  }
"""

def update_file(filename):
    fpath = os.path.join(BASE, filename)
    if not os.path.exists(fpath):
        return

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace existing .mobile-nav-call-btn block inside @media (max-width: 768px)
    pattern_btn = r'\.mobile-nav-call-btn \s* \{ [^}]* \}'
    if re.search(pattern_btn, content, flags=re.VERBOSE):
        content = re.sub(pattern_btn, PHONE_BTN_FIX_CSS.strip(), content, flags=re.VERBOSE)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ Fixed mobile call button width in {filename}")

def main():
    print("=== Fixing Top Mobile Call Button Width Across All Pages ===")
    html_files = [f for f in os.listdir(BASE) if f.endswith(".html") and not f.startswith("v1")]
    for fname in sorted(html_files):
        update_file(fname)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
