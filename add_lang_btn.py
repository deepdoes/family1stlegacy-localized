import glob
import re

files = glob.glob('/Users/deepankarakasajoo/Downloads/family1stlegacy_v2_16*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # 1. Add the Language button to nav before nav-cta
    if 'showLanguageModal(' not in content:
        content = re.sub(
            r'(<li>\s*<a[^>]*class="nav-cta"[^>]*>.*?</a>\s*</li>)',
            r'<li><a href="#" onclick="showLanguageModal(event)" style="font-size:20px; text-decoration:none;" title="Switch Language">🌐</a></li>\n        \1',
            content
        )
        changed = True
        
    # 2. Add the showLanguageModal function
    if 'function showLanguageModal' not in content:
        content = content.replace(
            'function setLanguage(lang) {',
            'function showLanguageModal(e) {\n  if(e) e.preventDefault();\n  document.getElementById(\'language-modal\').style.display = \'flex\';\n}\n\nfunction setLanguage(lang) {'
        )
        changed = True
        
    if changed:
        print(f"Updated {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"Skipped {filepath}")
