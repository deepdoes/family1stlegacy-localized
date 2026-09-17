#!/usr/bin/env python3
"""
find_unclosed_style.py
Finds which <style> block is missing a closing </style> tag in index.html and index_es.html.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

def find_unclosed(fname):
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all <style> positions and </style> positions
    styles = [m.start() for m in re.finditer(r'<style', content, re.IGNORECASE)]
    end_styles = [m.start() for m in re.finditer(r'</style>', content, re.IGNORECASE)]

    print(f"=== {fname} ===")
    for i, s_pos in enumerate(styles):
        # find closest </style> after s_pos
        next_ends = [e for e in end_styles if e > s_pos]
        next_start = styles[i+1] if i+1 < len(styles) else len(content)
        if not next_ends or next_ends[0] > next_start:
            snippet = content[s_pos:s_pos+200]
            print(f"  ❌ Unclosed <style> at pos {s_pos}:\n{snippet}\n")

if __name__ == "__main__":
    find_unclosed("index.html")
    find_unclosed("index_es.html")
