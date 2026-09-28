#!/usr/bin/env python3
"""
update_all_6_spanish_articles_full.py
Parses Document 2 (media_1789680344701.md) and updates all 6 Spanish article pages:
1. blog_family_protection_es.html
2. blog_retirement_es.html
3. blog_education_es.html
4. blog_living_benefits_es.html
5. blog_financial_strategy_es.html
6. blog_legacy_es.html
"""

import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
DOC2_PATH = "/Users/deepankarakasajoo/.gemini/antigravity/brain/ee1c32b0-7b6a-4b00-8e47-03da730d51b7/.user_uploaded/media_1789680344701.md"

with open(DOC2_PATH, "r", encoding="utf-8") as f:
    doc2_text = f.read()

# Split articles
article_chunks = re.split(r'#\s*\*\*ARTÍCULO\s+[0-9]+\s*—', doc2_text)

files_map = [
    ("blog_family_protection_es.html", 1),
    ("blog_retirement_es.html", 2),
    ("blog_education_es.html", 3),
    ("blog_living_benefits_es.html", 4),
    ("blog_financial_strategy_es.html", 5),
    ("blog_legacy_es.html", 6),
]

DISCLOSURE_HTML = """        <div class="edu-disclosure-box">
          <strong>📌 Aviso educativo:</strong> Este artículo se proporciona únicamente con fines educativos e informativos generales y no constituye asesoramiento financiero, legal ni fiscal personalizado. Las opciones y características de las pólizas varían según el estado y la compañía de seguros.
        </div>"""

for filename, art_num in files_map:
    fpath = os.path.join(BASE_DIR, filename)
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    art_text = article_chunks[art_num]

    # 1. Main Title
    title_match = re.search(r'##\s*\*\*([^\n]+)\*\*', art_text)
    if not title_match:
        print(f"Error finding title for {filename}")
        continue
    main_title = title_match.group(1).replace('\\', '').strip()

    # Update H1 in HTML
    html = re.sub(
        r'<h1 class="article-main-title">.*?</h1>',
        f'<h1 class="article-main-title">{main_title}</h1>',
        html, count=1, flags=re.DOTALL
    )

    # Update meta reviewed-by in HTML
    html = re.sub(
        r'<div class="article-meta-row">[\s\S]*?</div>\s*</div>\s*</div>',
        f'''<div class="article-meta-row">
          <div class="eeat-badge-hero">
            <svg viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-5.45 9-12V7l-9-5zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 9z"/></svg>
            Revisado por profesionales financieros con licencia • Equipo de Family First Legacy
          </div>
        </div>
      </div>
    </div>''',
        html, count=1
    )

    # 2. Key Takeaways
    tk_start = art_text.find('## **⚡ Puntos clave**')
    first_sec_match = re.search(r'##\s*\*\*1\\\.', art_text)
    if first_sec_match:
        tk_raw = art_text[tk_start:first_sec_match.start()].strip()
    else:
        tk_raw = ""

    tk_bullets = []
    for line in tk_raw.splitlines():
        line = line.strip()
        if line.startswith('*') or line.startswith('-'):
            item = line.lstrip('*- ').strip()
            # Split bold lead if exists
            if ':' in item:
                parts = item.split(':', 1)
                tk_bullets.append(f"<li><strong>{parts[0].strip()}:</strong> {parts[1].strip()}</li>")
            else:
                tk_bullets.append(f"<li>{item}</li>")

    kt_html = """        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Puntos clave</div>
          <ul>
""" + "\n".join("            " + b for b in tk_bullets) + """
          </ul>
        </div>"""

    # 3. Parse Sections 1..N
    sections_raw = []
    # Find all sections like ## **1\. Title** up to FAQs
    sec_matches = list(re.finditer(r'##\s*\*\*([0-9]+)\\\.\s+([^\*]+)\*\*', art_text))
    
    sections_html = []
    toc_links = []
    faq_sec_num = None

    for i, sm in enumerate(sec_matches):
        sec_num = sm.group(1)
        sec_title = sm.group(2).replace('\\', '').strip()
        
        start_pos = sm.end()
        end_pos = sec_matches[i+1].start() if i+1 < len(sec_matches) else art_text.find('## **IN THIS GUIDE', start_pos)
        if end_pos == -1:
            end_pos = art_text.find('## RIGHT SIDEBAR', start_pos)
        if end_pos == -1:
            end_pos = len(art_text)

        sec_body_raw = art_text[start_pos:end_pos].strip()

        if "Preguntas frecuentes" in sec_title or "preguntas frecuentes" in sec_title.lower():
            # This is the FAQ section!
            faq_sec_num = sec_num
            # Parse FAQ Q&A
            faq_items = []
            faq_chunks = re.split(r'##\s*\*\*([^\n]+)\*\*', sec_body_raw)
            # chunks[0] may be intro, then Q, A, Q, A
            idx = 1
            while idx < len(faq_chunks):
                q_text = faq_chunks[idx].replace('\\', '').strip()
                a_text = faq_chunks[idx+1].strip() if idx+1 < len(faq_chunks) else ""
                # Clean answer paragraphs
                a_paras = [p.strip() for p in a_text.split('\n\n') if p.strip() and not p.strip().startswith('**LOCATION') and not p.strip().startswith('|')]
                a_html = " ".join(a_paras)
                faq_items.append((q_text, a_html))
                idx += 2

            faq_html = f"""        <div class="article-faq-container" id="sec-faq">
          <h2>{sec_num}. Preguntas frecuentes</h2>"""
            for q, a in faq_items:
                faq_html += f"""
          <div class="faq-accordion-card">
            <div class="faq-question">{q}</div>
            <div class="faq-answer">{a}</div>
          </div>"""
            faq_html += "\n        </div>"
            sections_html.append(faq_html)
            toc_links.append((f"sec-faq", f"{sec_num}. Preguntas frecuentes"))
        else:
            # Regular narrative section
            toc_links.append((f"sec-{sec_num}", f"{sec_num}. {sec_title}"))
            
            # Format paragraphs and lists
            paras = sec_body_raw.split('\n\n')
            p_html_list = []
            in_list = False
            curr_list = []

            for p in paras:
                p = p.strip()
                if not p or p.startswith('**LOCATION') or p.startswith('|') or p.startswith('**OPEN') or p.startswith('**MATCH'):
                    continue
                
                # Check bullet points
                lines = p.splitlines()
                if all(l.strip().startswith('*') or l.strip().startswith('-') for l in lines if l.strip()):
                    p_html_list.append("<ul>")
                    for l in lines:
                        l = l.strip().lstrip('*- ').strip()
                        if ':' in l:
                            p1, p2 = l.split(':', 1)
                            p_html_list.append(f"  <li><strong>{p1.strip()}:</strong> {p2.strip()}</li>")
                        else:
                            p_html_list.append(f"  <li>{l}</li>")
                    p_html_list.append("</ul>")
                else:
                    p_html_list.append(f"<p>{p}</p>")

            sec_html = f'''        <h2 id="sec-{sec_num}">{sec_num}. {sec_title}</h2>\n''' + "\n".join(f"        {p}" for p in p_html_list)
            sections_html.append(sec_html)

    # Build entire content card
    full_content_card = f"""        <!-- LEFT CONTENT COLUMN -->
        <div class="article-content-card" data-reveal>
          
{kt_html}

""" + "\n\n".join(sections_html) + f"\n\n{DISCLOSURE_HTML}\n        </div>"

    # Replace content card in HTML
    html = re.sub(
        r'<!-- LEFT CONTENT COLUMN -->\s*<div class="article-content-card"[\s\S]*?</div>\s*<!-- RIGHT STICKY SIDEBAR -->',
        full_content_card + '\n\n        <!-- RIGHT STICKY SIDEBAR -->',
        html
    )

    # 4. Update Sidebar Table of Contents
    toc_items_html = "\n".join(f'              <li><a href="#{link_id}">{link_title}</a></li>' for link_id, link_title in toc_links)
    html = re.sub(
        r'<ul class="sidebar-toc-list">[\s\S]*?</ul>',
        f'<ul class="sidebar-toc-list">\n{toc_items_html}\n            </ul>',
        html
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  ✓ Fully updated {filename} ({len(sections_html)} sections, {len(toc_links)} TOC links)")

print("All 6 Spanish articles successfully updated!")
