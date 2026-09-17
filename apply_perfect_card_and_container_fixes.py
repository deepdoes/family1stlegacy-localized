#!/usr/bin/env python3
import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# List of root HTML files to update
html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html') and os.path.isfile(os.path.join(BASE_DIR, f))]

print(f"Found {len(html_files)} HTML files to process.")

OLD_CONTAINER_OVERRIDE = """.container, .article-container-wrap, .article-hero-container, .article-grid-container {
  max-width: 100% !important;
  box-sizing: border-box !important;
}"""

NEW_CONTAINER_OVERRIDE = """.container {
  width: 100% !important;
  max-width: 1200px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  box-sizing: border-box !important;
}

.article-hero-container,
.article-grid-container,
.article-container-wrap,
.article-faq-container {
  width: 100% !important;
  max-width: 1040px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  box-sizing: border-box !important;
}"""

# 1. Update Container Max Width overrides in all HTML files
for fname in html_files:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Fix the max-width 100% override if present
    if OLD_CONTAINER_OVERRIDE in content:
        content = content.replace(OLD_CONTAINER_OVERRIDE, NEW_CONTAINER_OVERRIDE)
        modified = True

    # Also check variations with regex
    regex_override = re.compile(
        r'\.container,\s*\.article-container-wrap,\s*\.article-hero-container,\s*\.article-grid-container\s*\{\s*max-width:\s*100%\s*!important;\s*box-sizing:\s*border-box\s*!important;\s*\}',
        re.DOTALL
    )
    if regex_override.search(content):
        content = regex_override.sub(NEW_CONTAINER_OVERRIDE, content)
        modified = True

    # 2. Homepage fixes for index*.html
    if fname.startswith('index'):
        # Fix .blog-card CSS rule flex basis
        old_flex = "flex: 0 0 calc((100% - 64px) / 3.15);"
        new_flex = "flex: 0 0 280px; width: 280px; max-width: 85vw;"
        if old_flex in content:
            content = content.replace(old_flex, new_flex)
            modified = True

        # Fix .blog-slider-track .blog-card CSS block
        old_track_card = """.blog-slider-track .blog-card {
  width: 280px !important;
  max-width: 85vw !important;
  flex-shrink: 0 !important;
}"""
        new_track_card = """.blog-slider-track .blog-card,
.blog-slider .blog-card {
  width: 280px !important;
  max-width: 85vw !important;
  flex: 0 0 280px !important;
  flex-shrink: 0 !important;
}"""
        if old_track_card in content:
            content = content.replace(old_track_card, new_track_card)
            modified = True

        # Fix inline styles on blog-card HTML tags in slider track
        def replace_card_tag(match):
            tag = match.group(0)
            if 'style=' not in tag:
                return tag.replace('class="blog-card"', 'class="blog-card" style="flex:none;"')
            return tag

        content = re.sub(r'<a\s+[^>]*class="blog-card"[^>]*>', replace_card_tag, content)

        # Fix blog card inner padding / title / excerpt if needed
        if '.bc-content { padding: 32px;' in content:
            content = content.replace('.bc-content { padding: 32px;', '.bc-content { padding: 24px 24px 28px 24px;')
            modified = True

    # Save changes if file was modified
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    if modified:
        print(f"Updated layout fixes in {fname}")

print("Completed updating HTML files.")
