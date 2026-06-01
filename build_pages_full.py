import os
import re

base_dir = '/Users/deepankarakasajoo/Downloads/Family1stLegacy'
source_file = '/Users/deepankarakasajoo/Downloads/family_first_legacy_website.html'

with open(os.path.join(base_dir, 'family1stlegacy_v2_16.html'), 'r', encoding='utf-8') as f:
    master_content = f.read()

with open(source_file, 'r', encoding='utf-8') as f:
    source_content = f.read()

hero_idx = master_content.find('<!-- HERO SLIDESHOW ──────────────────────────────────── -->')
header_part = master_content[:hero_idx]
contact_idx = master_content.find('<section id="contact">')
footer_part = master_content[contact_idx:]

extra_css = """
<style>
/* ── Static Hero ── */
.static-hero { position: relative; min-height: 70vh; display: flex; align-items: center; justify-content: center; padding: 120px 20px 80px; background-size: cover; background-position: center; }
.static-hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(to right, rgba(10,10,15,0.95) 0%, rgba(10,10,15,0.7) 100%); z-index: 1; }
.sh-content { position: relative; z-index: 2; max-width: 900px; text-align: center; }
.sh-badge { display: inline-block; font-family: var(--font-body); font-size: 12px; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: var(--green); padding: 6px 16px; border: 1px solid rgba(29,158,117,0.3); border-radius: 30px; margin-bottom: 24px; }
.sh-title { font-family: var(--font-head); font-size: clamp(36px, 5vw, 56px); font-weight: 400; color: #fff; line-height: 1.1; margin-bottom: 24px; }
.sh-sub { font-family: var(--font-body); font-size: clamp(16px, 2vw, 20px); color: rgba(255,255,255,0.7); line-height: 1.6; margin-bottom: 32px; }
.sh-hook { font-family: var(--font-head); font-size: 22px; color: var(--amber); font-style: italic; border-left: 2px solid var(--amber); padding-left: 20px; text-align: left; max-width: 700px; margin: 0 auto; }

/* ── Content Image Injection ── */
.content-image { width: 100%; height: 450px; object-fit: cover; border-radius: 20px; margin: 60px 0 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.6); }

/* ── Dark Mode Overrides for Source Content ── */
.main-content-wrap { max-width: 900px; margin: 0 auto; padding: 60px 20px 120px; color: rgba(255,255,255,0.75); font-size: 18px; line-height: 1.8; }
.main-content-wrap h3 { font-family: var(--font-head); font-size: 32px; color: #fff; margin-bottom: 24px; line-height: 1.25; }
.main-content-wrap h4 { font-family: var(--font-head); font-size: 22px; color: var(--amber); margin-bottom: 16px; }
.community-card, .story-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 40px; margin: 40px 0; }
.community-card { border-left: 4px solid var(--amber); }
.emphasis { color: #fff; font-weight: 600; }
.alert { background: rgba(200,50,50,0.1); border: 1px solid rgba(200,50,50,0.3); padding: 30px; border-radius: 16px; margin: 40px 0; color: #fff; }
.section-label { font-family: var(--font-head); font-size: 14px; text-transform: uppercase; letter-spacing: 2px; color: var(--amber); margin: 80px 0 30px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; }
.probate-steps { margin: 40px 0; }
.probate-step { display: flex; gap: 24px; margin-bottom: 30px; }
.prob-circle { width: 40px; height: 40px; border-radius: 50%; background: var(--green); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; flex-shrink:0; }
.prob-body { background: rgba(255,255,255,0.02); padding: 24px; border-radius: 16px; flex-grow: 1; border: 1px solid rgba(255,255,255,0.05); }
.dur { display: inline-block; margin-top: 12px; font-size: 13px; color: var(--amber); font-weight: bold; text-transform: uppercase; }
.illness-grid, .mistake-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 40px 0; }
@media(max-width:768px) { .illness-grid, .mistake-cols { grid-template-columns: 1fr; } }
.illness-card, .mistake-col { background: rgba(255,255,255,0.03); padding: 30px; border-radius: 16px; border: 1px solid rgba(255,255,255,0.08); }
.dis-table { width: 100%; border-collapse: collapse; margin: 40px 0; font-size: 16px; }
.dis-table-hdr { margin-bottom: 20px; }
.dis-cols { display: flex; background: rgba(255,255,255,0.05); font-weight: bold; color:#fff; }
.dis-col-h { flex: 1; padding: 16px; border: 1px solid rgba(255,255,255,0.1); }
.dis-row { display: flex; }
.dis-cell { flex: 1; padding: 16px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.01); }
.income-impact { margin: 40px 0; }
.impact-row { display: flex; gap: 20px; align-items: center; margin-bottom: 20px; }
.impact-month { width: 100px; font-weight: bold; color: var(--amber); }
.impact-bar-wrap { flex-grow: 1; background: rgba(255,255,255,0.03); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08); }
.bar-track { height: 12px; background: rgba(0,0,0,0.5); border-radius: 6px; margin: 10px 0; overflow: hidden; }
.bar-fill { height: 100%; background: var(--amber); }
.bar-teal { background: var(--green); }
.bar-orange { background: #b05c28; }
.bar-red { background: #992323; }
hr.divider { border: none; height: 1px; background: rgba(255,255,255,0.1); margin: 60px 0; }
.mistake-q { margin-top: 24px; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 12px; text-align: center; font-style: italic; color:#fff; }
.belief-list, .reality-list { margin-left: 20px; }
.belief-list li, .reality-list li { margin-bottom: 10px; }
</style>
"""
header_part = header_part.replace('</head>', extra_css + '\n</head>')

# Define pages and their specific images
pages_meta = [
    {
        "id": "page-0",
        "filename": "family_protection.html",
        "badge": "Family Protection",
        "hero_img": "images/hero_life_insurance_diverse_1777335713599.png",
        "replacements": [
            ("<h3>Picture this: You're gone.", '<img class="content-image" src="images/probate_trap_diverse_1777393105349.png">\n<h3>Picture this: You\'re gone.'),
            ("<h3>You don't have to die", '<img class="content-image" src="images/chronic_illness_diverse_1777393119808.png">\n<h3>You don\'t have to die'),
            ("<h3>One phone call.", '<img class="content-image" src="images/critical_illness_diverse_1777393231898.png">\n<h3>One phone call.'),
            ('<div class="mistake-header">', '<img class="content-image" src="images/costly_mistake_diverse_1777393245000.png">\n<div class="mistake-header">')
        ]
    },
    {
        "id": "page-1",
        "filename": "retirement_planning.html",
        "badge": "Retirement Planning",
        "hero_img": "images/hero_retirement_diverse_1777335727638.png",
        "replacements": [
            ("<h3>We grew up believing", '<img class="content-image" src="images/market_volatility_diverse_1777393133743.png">\n<h3>We grew up believing'),
            ("<h3>If you have $500,000", '<img class="content-image" src="images/tax_timebomb_diverse_1777393258870.png">\n<h3>If you have $500,000')
        ]
    },
    {
        "id": "page-2",
        "filename": "education_planning.html",
        "badge": "Education Planning",
        "hero_img": "images/hero_education_diverse_1777335740128.png",
        "replacements": [
            ("<h3>Every parent wants", '<img class="content-image" src="images/college_savings_diverse_1777393273467.png">\n<h3>Every parent wants')
        ]
    },
    {
        "id": "page-3",
        "filename": "financial_strategy.html",
        "badge": "Financial Strategy",
        "hero_img": "images/hero_business_diverse_1777335776243.png",
        "replacements": [
            ("<h3>Wealth is not an accident.", '<img class="content-image" src="images/wealth_transfer_diverse_1777393288351.png">\n<h3>Wealth is not an accident.')
        ]
    }
]

def extract_page_content(page_id):
    start_str = f'<div class="page" id="{page_id}">'
    if start_str not in source_content:
        start_str = f'<div class="page active" id="{page_id}">'
    
    start_idx = source_content.find(start_str)
    if start_idx == -1: return ""
    
    # Find next page or end of main
    next_idx = source_content.find('<div class="page', start_idx + 10)
    if next_idx == -1:
        next_idx = source_content.find('</main>', start_idx)
        
    return source_content[start_idx:next_idx]

for meta in pages_meta:
    raw_html = extract_page_content(meta['id'])
    
    # 1. Extract Hero Data
    title_match = re.search(r'<h1>(.*?)</h1>', raw_html)
    sub_match = re.search(r'<p class="hero-sub">(.*?)</p>', raw_html)
    hook_match = re.search(r'<p class="hero-hook">(.*?)</p>', raw_html)
    
    title = title_match.group(1) if title_match else ""
    sub = sub_match.group(1) if sub_match else ""
    hook = hook_match.group(1) if hook_match else ""
    
    # 2. Extract Stats
    stats_html = ""
    stat_block = re.search(r'<div class="stat-row">(.*?)</div>\s*<div class="community-card', raw_html, re.DOTALL)
    if stat_block:
        stats = re.findall(r'<div class="stat-card"><div class="stat-num">(.*?)</div><div class="stat-label">(.*?)</div></div>', stat_block.group(1))
        stats_html = '''
        <section id="numbers" style="padding: 60px 0; background: var(--dark); border-bottom: 1px solid rgba(255,255,255,0.05);">
          <div class="container-full">
            <div class="numbers-grid">
        '''
        for num, label in stats:
            stats_html += f'''
              <div class="number-item on" style="opacity: 1; transform: none;">
                <div class="ni-num">{num}</div>
                <div class="ni-label">{label}</div>
              </div>
            '''
        stats_html += '''
            </div>
          </div>
        </section>
        '''
    
    # 3. Extract the body content (everything after stat-row)
    body_start = raw_html.find('<div class="community-card')
    if body_start == -1: body_start = raw_html.find('<div class="story-card')
    
    body_content_raw = raw_html[body_start:]
    # Remove the closing </div> of the page wrapper if present
    body_content_raw = re.sub(r'</div>\s*$', '', body_content_raw)
    
    # 4. Apply image injections
    for old, new in meta['replacements']:
        body_content_raw = body_content_raw.replace(old, new)
        
    # Wrap body in dark theme wrapper
    body_html = f'''
    <div style="background: var(--dark); padding-top: 40px;">
      <div class="main-content-wrap">
        {body_content_raw}
      </div>
    </div>
    '''
    
    # Build full Hero
    hero_html = f'''
    <section class="static-hero" style="background-image:url('{meta['hero_img']}');">
      <div class="sh-content">
        <div class="sh-badge">{meta['badge']}</div>
        <h1 class="sh-title">{title}</h1>
        <p class="sh-sub">{sub}</p>
        <div class="sh-hook">{hook}</div>
      </div>
    </section>
    '''
    
    full_html = header_part + hero_html + stats_html + body_html + footer_part
    
    # Fix links
    full_html = re.sub(r'href="#about"', 'href="family1stlegacy_v2_16.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="family1stlegacy_v2_16.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="family1stlegacy_v2_16.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="family1stlegacy_v2_16.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="family1stlegacy_v2_16.html#reviews"', full_html)
    full_html = full_html.replace('class="nav-logo" href="#"', 'class="nav-logo" href="family1stlegacy_v2_16.html"')

    out_name = os.path.join(base_dir, meta['filename'])
    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Generated {out_name} with full content.")
