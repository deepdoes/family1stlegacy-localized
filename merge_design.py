import re
import os

# 1. Load the main homepage (master template)
with open('/Users/deepankarakasajoo/Downloads/family1stlegacy_v2_16.html', 'r', encoding='utf-8') as f:
    master_content = f.read()

# Split master template
hero_idx = master_content.find('<!-- HERO SLIDESHOW ──────────────────────────────────── -->')
footer_idx = master_content.find('<!-- FOOTER ──────────────────────────────────────────── -->')

header_part = master_content[:hero_idx]
footer_part = master_content[footer_idx:]

# 2. Load the content file (to get its specific styles and progress nav + pages)
with open('/Users/deepankarakasajoo/Downloads/family_first_legacy_website.html', 'r', encoding='utf-8') as f:
    src_content = f.read()

# Extract the <style> block from src_content
style_match = re.search(r'<style>(.*?)</style>', src_content, re.DOTALL)
src_style = style_match.group(1) if style_match else ""

# Replace the :root in src_style with our dark theme adaptation
dark_root = """
    :root {
      --navy: #ffffff;
      --navy-mid: #e0e0e0;
      --navy-soft: #cccccc;
      --gold: #c9a84c;
      --gold-light: #e8c97a;
      --gold-pale: #2a2515;
      --teal: #1d9e75;
      --teal-light: #0a1f18;
      --red-soft: #2a1111;
      --red-mid: #e24b4a;
      --amber-soft: #2a1f0a;
      --amber-mid: #ef9f27;
      --purple-soft: #1a1738;
      --purple-mid: #7f77dd;
      --white: #12121a;
      --off-white: #0a0a0f;
      --gray-100: #1a1a24;
      --gray-200: #2a2a35;
      --gray-400: #666677;
      --gray-600: #a0a0b0;
      --text-primary: #ffffff;
      --text-secondary: rgba(255,255,255,0.7);
      --text-muted: rgba(255,255,255,0.4);
      --shadow-sm: 0 4px 12px rgba(0,0,0,0.5);
      --shadow-md: 0 8px 24px rgba(0,0,0,0.6);
    }
"""
src_style = re.sub(r':root\s*\{.*?\}', dark_root, src_style, flags=re.DOTALL)

# Inject the src_style into the header_part right before </head>
header_part = header_part.replace('</head>', f'<style>\n{src_style}\n</style>\n</head>')

# Extract the 4 pages from src_content
p0 = src_content.find('<div class="page active" id="page-0">')
p1 = src_content.find('<div class="page" id="page-1">')
p2 = src_content.find('<div class="page" id="page-2">')
p3 = src_content.find('<div class="page" id="page-3">')
main_end = src_content.find('</main>')

pages = [
    src_content[p0:p1].strip(),
    src_content[p1:p2].strip(),
    src_content[p2:p3].strip(),
    src_content[p3:main_end].strip()
]

# Ensure all pages have 'active' class
pages[0] = pages[0].replace('<div class="page active" id="page-0">', '<div class="page active" id="page-0" style="padding-top: 40px;">')
pages[1] = pages[1].replace('<div class="page" id="page-1">', '<div class="page active" id="page-1" style="padding-top: 40px;">')
pages[2] = pages[2].replace('<div class="page" id="page-2">', '<div class="page active" id="page-2" style="padding-top: 40px;">')
pages[3] = pages[3].replace('<div class="page" id="page-3">', '<div class="page active" id="page-3" style="padding-top: 40px;">')

file_names = [
    'family_protection.html',
    'retirement_planning.html',
    'education_planning.html',
    'financial_strategy.html'
]

titles = ["Family protection", "Retirement planning", "Education planning", "Financial strategy"]

def build_nav(active_idx):
    nav = '<nav class="progress-nav" id="progress-nav" style="position: sticky; top: 0; z-index: 90; margin-top: 75px;">\n'
    for i in range(4):
        cls = "prog-step"
        if i == active_idx:
            cls += " active"
        elif i < active_idx:
            cls += " done"
        nav += f'    <div class="{cls}" onclick="window.location.href=\'{file_names[i]}\'" id="ps{i}"><div class="ps-num">0{i+1}</div><div class="ps-title">{titles[i]}</div><div class="ps-check">✓ Completed</div></div>\n'
    nav += '  </nav>'
    return nav

# Generate the 4 files
for i in range(4):
    out_name = os.path.join('/Users/deepankarakasajoo/Downloads', file_names[i])
    
    # We construct the final HTML
    # 1. header_part (which has the global nav, language switcher, styles)
    # 2. progress-nav (built for this specific page)
    # 3. <main class="main"> 
    # 4. the page content
    # 5. </main>
    # 6. footer_part
    
    # Wait, the main homepage nav has "fixed" position or something.
    # The progress nav should sit below it.
    
    full_html = header_part + build_nav(i) + '\n<main class="main">\n' + pages[i] + '\n</main>\n\n' + footer_part
    
    # Fix the hash links in the top nav for these subpages.
    # Since we are not on the homepage, href="#about" won't work. It should be href="family1stlegacy_v2_16.html#about"
    full_html = re.sub(r'href="#about"', 'href="family1stlegacy_v2_16.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="family1stlegacy_v2_16.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="family1stlegacy_v2_16.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="family1stlegacy_v2_16.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="family1stlegacy_v2_16.html#reviews"', full_html)
    
    # But for "Get Started ->" linking to #contact, maybe keep it to the homepage contact
    full_html = re.sub(r'href="#contact"', 'href="family1stlegacy_v2_16.html#contact"', full_html)

    # Also, we need to update the logo link to go back to homepage
    full_html = full_html.replace('class="nav-logo" href="#"', 'class="nav-logo" href="family1stlegacy_v2_16.html"')

    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Generated {out_name}")

