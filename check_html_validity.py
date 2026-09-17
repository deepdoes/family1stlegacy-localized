#!/usr/bin/env python3
"""
check_html_validity.py
Checks index.html and index_es.html for unclosed style/script tags or broken head elements.
"""

import os
from html.parser import HTMLParser

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

class SimpleChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in ["img", "input", "br", "hr", "meta", "link"]:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in ["img", "input", "br", "hr", "meta", "link"]:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            else:
                self.errors.append(f"Mismatched end tag </{tag}>, expected </{self.stack[-1] if self.stack else 'NONE'}>")

for fname in ["index.html", "index_es.html"]:
    fpath = os.path.join(BASE, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for unclosed <style> or <script>
    style_starts = content.count("<style")
    style_ends = content.count("</style>")
    script_starts = content.count("<script")
    script_ends = content.count("</script>")
    
    print(f"[{fname}] <style> starts: {style_starts}, ends: {style_ends}")
    print(f"[{fname}] <script> starts: {script_starts}, ends: {style_ends}")
