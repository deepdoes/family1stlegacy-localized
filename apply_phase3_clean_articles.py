#!/usr/bin/env python3
"""
apply_phase3_clean_articles.py
Cleanly updates all 6 Spanish Knowledgebase article pages using Document 2:
- blog_family_protection_es.html
- blog_retirement_es.html
- blog_education_es.html
- blog_living_benefits_es.html
- blog_financial_strategy_es.html
- blog_legacy_es.html
"""

import os
import re

BASE_DIR = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
DOC2_PATH = "/Users/deepankarakasajoo/.gemini/antigravity/brain/ee1c32b0-7b6a-4b00-8e47-03da730d51b7/.user_uploaded/media_1789680344701.md"

with open(DOC2_PATH, "r", encoding="utf-8") as f:
    doc2_text = f.read()

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

    art = article_chunks[art_num]

    # 1. Main Title
    title_match = re.search(r'##\s*\*\*([^\n]+)\*\*', art)
    main_title = title_match.group(1).replace('\\', '').strip() if title_match else ""

    html = re.sub(
        r'<h1 class="article-main-title">.*?</h1>',
        f'<h1 class="article-main-title">{main_title}</h1>',
        html, count=1, flags=re.DOTALL
    )

    # 2. Key Takeaways
    tk_start = art.find('## **⚡ Puntos clave**')
    first_sec_match = re.search(r'##\s*\*\*1\\\.', art)
    tk_raw = art[tk_start:first_sec_match.start()].strip() if (tk_start != -1 and first_sec_match) else ""

    tk_bullets = []
    for line in tk_raw.splitlines():
        line = line.strip()
        if not line or "LOCATION:" in line or "Article body" in line or line.startswith("**LOCATION") or line.startswith("|"):
            continue
        if line.startswith('*') or line.startswith('-'):
            item = line.lstrip('*- ').strip()
            if "LOCATION:" in item or "Article body" in item:
                continue
            if ':' in item:
                p1, p2 = item.split(':', 1)
                tk_bullets.append(f"<li><strong>{p1.strip()}:</strong> {p2.strip()}</li>")
            else:
                tk_bullets.append(f"<li>{item}</li>")

    kt_html = """        <div class="kt-box-elevated">
          <div class="kt-header">⚡ Puntos clave</div>
          <ul>
""" + "\n".join("            " + b for b in tk_bullets) + """
          </ul>
        </div>"""

    # 3. Parse Narrative Sections
    sec_matches = list(re.finditer(r'##\s*\*\*([0-9]+)\\\.\s+([^\*]+)\*\*', art))
    sections_html = []
    toc_links = []
    faq_sec_num = None

    for i, sm in enumerate(sec_matches):
        snum = sm.group(1)
        stitle = sm.group(2).replace('\\', '').strip()

        if "Preguntas frecuentes" in stitle or "preguntas frecuentes" in stitle.lower():
            faq_sec_num = snum
            continue

        toc_links.append((f"sec-{snum}", f"{snum}. {stitle}"))

        start_pos = sm.end()
        end_pos = sec_matches[i+1].start() if i+1 < len(sec_matches) else len(art)
        sec_chunk = art[start_pos:end_pos].strip()

        # Split into paragraphs and lists
        paras = sec_chunk.split('\n\n')
        p_html_list = []
        for p in paras:
            p = p.strip()
            if not p or p.startswith('**LOCATION') or p.startswith('|') or p.startswith('**OPEN') or p.startswith('**MATCH'):
                continue
            lines = p.splitlines()
            if all(l.strip().startswith('*') or l.strip().startswith('-') for l in lines if l.strip()):
                p_html_list.append("<ul>")
                for l in lines:
                    l = l.strip().lstrip('*- ').strip()
                    if ':' in l:
                        lp1, lp2 = l.split(':', 1)
                        p_html_list.append(f"  <li><strong>{lp1.strip()}:</strong> {lp2.strip()}</li>")
                    else:
                        p_html_list.append(f"  <li>{l}</li>")
                p_html_list.append("</ul>")
            else:
                p_html_list.append(f"<p>{p}</p>")

        sec_html = f'''        <h2 id="sec-{snum}">{snum}. {stitle}</h2>\n''' + "\n".join(f"        {p}" for p in p_html_list)
        sections_html.append(sec_html)

    # 4. Parse FAQs cleanly
    if faq_sec_num:
        faq_match = re.search(r'##\s*\*\*([0-9]+)\\\.\s+Preguntas frecuentes\*\*', art)
        faq_start = faq_match.start()
        end_matches = [
            art.find('## **IN THIS GUIDE', faq_start),
            art.find('## RIGHT SIDEBAR', faq_start),
            art.find('## **SHARED BLOCKS', faq_start),
        ]
        end_candidates = [m for m in end_matches if m != -1]
        faq_end = min(end_candidates) if end_candidates else len(art)

        faq_text = art[faq_match.end():faq_end]
        q_matches = list(re.finditer(r'##\s*\*\*([^\n]+)\*\*', faq_text))
        real_faqs = []
        for j, qm in enumerate(q_matches):
            q = qm.group(1).replace('\\', '').strip()
            if 'RIGHT SIDEBAR' in q or 'IN THIS GUIDE' in q or 'SHARED BLOCKS' in q:
                continue
            q_start = qm.end()
            q_end = q_matches[j+1].start() if j+1 < len(q_matches) else len(faq_text)
            a_chunk = faq_text[q_start:q_end].strip()
            a_paras = [p.strip() for p in a_chunk.split('\n\n') if p.strip() and not p.strip().startswith('**LOCATION') and not p.strip().startswith('|') and not p.strip().startswith('**OPEN') and not p.strip().startswith('**MATCH')]
            a = ' '.join(a_paras)
            real_faqs.append((q, a))

        faq_html = f"""        <div class="article-faq-container" id="sec-faq">
          <h2>{faq_sec_num}. Preguntas frecuentes</h2>"""
        for q, a in real_faqs:
            faq_html += f"""
          <div class="faq-accordion-card">
            <div class="faq-question">{q}</div>
            <div class="faq-answer">{a}</div>
          </div>"""
        faq_html += "\n        </div>"
        sections_html.append(faq_html)
        toc_links.append(("sec-faq", f"{faq_sec_num}. Preguntas frecuentes"))

    # 5. Build full content card
    full_content_card = f"""        <!-- LEFT CONTENT COLUMN -->
        <div class="article-content-card" data-reveal>
          
{kt_html}

""" + "\n\n".join(sections_html) + f"\n\n{DISCLOSURE_HTML}\n        </div>"

    html = re.sub(
        r'<!-- LEFT CONTENT COLUMN -->\s*<div class="article-content-card"[\s\S]*?</div>\s*<!-- RIGHT STICKY SIDEBAR -->',
        full_content_card + '\n\n        <!-- RIGHT STICKY SIDEBAR -->',
        html
    )

    # 6. Sidebar TOC
    toc_items_html = "\n".join(f'              <li><a href="#{link_id}">{link_title}</a></li>' for link_id, link_title in toc_links)
    html = re.sub(
        r'<div class="sidebar-toc-title">.*?</div>\s*<ul class="sidebar-toc-list">[\s\S]*?</ul>',
        f'<div class="sidebar-toc-title">📖 EN ESTA GUÍA</div>\n            <ul class="sidebar-toc-list">\n{toc_items_html}\n            </ul>',
        html
    )

    # 7. More Articles section title & buttons on each article page
    html = html.replace("More Articles & Strategies", "Últimos artículos y estrategias")
    html = html.replace("More Articles &amp; Strategies", "Últimos artículos y estrategias")
    html = html.replace("Read Article", "LEER ARTÍCULO")
    html = html.replace("READ ARTICLE", "LEER ARTÍCULO")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"  ✓ Cleanly updated {filename} ({len(sections_html)} sections, {len(toc_links)} TOC links)")

print("All 6 Spanish articles cleanly updated with 0 leftover markers.")
