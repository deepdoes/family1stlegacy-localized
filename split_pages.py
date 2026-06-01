import os

filename = '/Users/deepankarakasajoo/Downloads/family_first_legacy_website.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the boundaries
p0 = content.find('<div class="page active" id="page-0">')
p1 = content.find('<div class="page" id="page-1">')
p2 = content.find('<div class="page" id="page-2">')
p3 = content.find('<div class="page" id="page-3">')
main_end = content.find('</main>')

header_html = content[:p0]
footer_html = content[main_end:]

pages = [
    content[p0:p1].strip(),
    content[p1:p2].strip(),
    content[p2:p3].strip(),
    content[p3:main_end].strip()
]

# Ensure all pages have 'active' class
pages[0] = pages[0].replace('<div class="page active" id="page-0">', '<div class="page active" id="page-0">')
pages[1] = pages[1].replace('<div class="page" id="page-1">', '<div class="page active" id="page-1">')
pages[2] = pages[2].replace('<div class="page" id="page-2">', '<div class="page active" id="page-2">')
pages[3] = pages[3].replace('<div class="page" id="page-3">', '<div class="page active" id="page-3">')

# Strip out the goTo() javascript from the footer
import re
footer_html = re.sub(r'function goTo\(stepIndex\) \{.*?\n\s*\n', '', footer_html, flags=re.DOTALL)
footer_html = re.sub(r'// Make prog-step clicks work.*?\}\);', '', footer_html, flags=re.DOTALL)

file_names = [
    'family_protection.html',
    'retirement_planning.html',
    'education_planning.html',
    'financial_strategy.html'
]

# Build the nav string function
def build_nav(active_idx):
    nav = '<nav class="progress-nav" id="progress-nav">\n'
    titles = ["Family protection", "Retirement planning", "Education planning", "Financial strategy"]
    for i in range(4):
        # Determine class
        cls = "prog-step"
        if i == active_idx:
            cls += " active"
        elif i < active_idx:
            cls += " done"
        
        nav += f'    <div class="{cls}" onclick="window.location.href=\'{file_names[i]}\'" id="ps{i}"><div class="ps-num">0{i+1}</div><div class="ps-title">{titles[i]}</div><div class="ps-check">✓ Completed</div></div>\n'
    nav += '  </nav>'
    return nav

for i in range(4):
    out_name = os.path.join('/Users/deepankarakasajoo/Downloads', file_names[i])
    
    # Replace the progress-nav block in the header
    new_header = re.sub(r'<nav class="progress-nav" id="progress-nav">.*?</nav>', build_nav(i), header_html, flags=re.DOTALL)
    
    full_html = new_header + pages[i] + '\n\n  ' + footer_html
    
    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        print(f"Generated {out_name}")

