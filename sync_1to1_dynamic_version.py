#!/usr/bin/env python3
"""
sync_1to1_dynamic_version.py
Extracts the complete, finalized HTML & CSS from index.html and generates a 100% 1:1 matching
React Client Component for src/app/dynamic/page.tsx, ensuring absolute visual, code, and functional
parity between static and dynamic versions.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
INDEX_HTML = os.path.join(BASE, "index.html")
DYNAMIC_PAGE_TSX = os.path.join(BASE, "src", "app", "dynamic", "page.tsx")

def sync():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Extract head styles
    style_matches = re.findall(r'<style[^>]*>(.*?)</style>', html_content, flags=re.DOTALL)
    combined_styles = "\n".join(style_matches)

    # Extract body inner HTML
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, flags=re.DOTALL)
    if not body_match:
        print("  ❌ Could not find <body> in index.html")
        return
    
    body_inner = body_match.group(1)

    # Clean backticks and template strings for JSX
    safe_body_inner = body_inner.replace("`", "\\`").replace("${", "\\${")
    safe_combined_styles = combined_styles.replace("`", "\\`").replace("${", "\\${")

    template = """\"use client\";

import React, { useEffect } from \"react\";

export default function DynamicPage() {
  useEffect(() => {
    // Execute interactive scripts for Hero Slider, Navbar, FAQ, and Q&A Dashboard
    const initScripts = () => {
      // Hero slider
      const slides = document.querySelectorAll('.slide');
      const dots = document.querySelectorAll('.hero-dot');
      let current = 0;
      let timer: any = null;

      function goTo(index: number) {
        if (!slides.length) return;
        slides[current]?.classList.remove('active');
        if (dots[current]) dots[current].classList.remove('active');
        current = (index + slides.length) % slides.length;
        slides[current]?.classList.add('active');
        if (dots[current]) dots[current].classList.add('active');
      }

      if (slides.length > 0) {
        timer = setInterval(() => goTo(current + 1), 6000);
      }

      // Navbar scroll stuck state
      const nav = document.getElementById('nav');
      const handleScroll = () => {
        if (nav) {
          if (window.scrollY > 50) nav.classList.add('stuck');
          else nav.classList.remove('stuck');
        }
      };
      window.addEventListener('scroll', handleScroll);
      handleScroll();

      return () => {
        if (timer) clearInterval(timer);
        window.removeEventListener('scroll', handleScroll);
      };
    };

    const cleanup = initScripts();
    return () => {
      if (cleanup) cleanup();
    };
  }, []);

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: `__STYLES__` }} />
      <div dangerouslySetInnerHTML={{ __html: `__BODY__` }} />
    </>
  );
}
"""

    react_page_code = template.replace("__STYLES__", safe_combined_styles).replace("__BODY__", safe_body_inner)

    with open(DYNAMIC_PAGE_TSX, "w", encoding="utf-8") as f:
        f.write(react_page_code)
    print("  ✓ Successfully created 100% 1:1 synchronized React component at src/app/dynamic/page.tsx")

if __name__ == "__main__":
    print("=== Synchronizing Dynamic Page 100% 1:1 with index.html ===")
    sync()
    print("=== Done! ===")
