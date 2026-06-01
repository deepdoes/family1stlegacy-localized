import os
from bs4 import BeautifulSoup

base_dir = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
files_to_sync = [
    'index.html',
    'family_protection.html',
    'retirement_planning.html',
    'education_planning.html',
    'financial_strategy.html',
    'estate_planning.html',
    'blog_family_protection.html',
    'blog_retirement.html',
    'blog_education.html',
    'blog_financial_strategy.html',
    'blog_legacy.html',
    'privacy.html',
    'terms.html'
]

translations = {
    'en': {
        'title': 'Select Your Language',
        'desc': 'Choose a language to view the Family First Legacy website.',
        'cycle': ['English', 'Español', 'Português', 'Kiswahili', 'Kinyarwanda'],
        'buttons': {
            'en': 'English',
            'es': 'Español',
            'pt': 'Português',
            'sw': 'Kiswahili',
            'rw': 'Kinyarwanda'
        }
    },
    'es': {
        'title': 'Seleccione su idioma',
        'desc': 'Elija un idioma para ver el sitio web de Family First Legacy.',
        'cycle': ['Inglés', 'Español', 'Portugués', 'Kiswahili', 'Kinyarwanda'],
        'buttons': {
            'en': 'Inglés',
            'es': 'Español',
            'pt': 'Portugués',
            'sw': 'Kiswahili',
            'rw': 'Kinyarwanda'
        }
    },
    'pt': {
        'title': 'Selecione o seu idioma',
        'desc': 'Escolha um idioma para ver o site da Family First Legacy.',
        'cycle': ['Inglês', 'Espanhol', 'Português', 'Kiswahili', 'Kinyarwanda'],
        'buttons': {
            'en': 'Inglês',
            'es': 'Espanhol',
            'pt': 'Português',
            'sw': 'Kiswahili',
            'rw': 'Kinyarwanda'
        }
    },
    'sw': {
        'title': 'Chagua Lugha Yako',
        'desc': 'Chagua lugha ili kuona tovuti ya Family First Legacy.',
        'cycle': ['Kiingereza', 'Kihispania', 'Kireno', 'Kiswahili', 'Kinyarwanda'],
        'buttons': {
            'en': 'Kiingereza',
            'es': 'Kihispania',
            'pt': 'Kireno',
            'sw': 'Kiswahili',
            'rw': 'Kinyarwanda'
        }
    },
    'rw': {
        'title': 'Hitamo Ururimi Rwawe',
        'desc': 'Hitamo ururimi kugira ngo urebe urubuga rwa Family First Legacy.',
        'cycle': ['Icyongereza', 'Ikihiyipaniya', 'Igiportugali', 'Igiswahili', 'Kinyarwanda'],
        'buttons': {
            'en': 'Icyongereza',
            'es': 'Ikihiyipaniya',
            'pt': 'Igiportugali',
            'sw': 'Igiswahili',
            'rw': 'Kinyarwanda'
        }
    }
}

print("Starting Instant Language Selector Sync across all compiled pages...")

for filename in files_to_sync:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Warning: English source file not found {filepath}")
        continue
        
    current_base = filename.replace('.html', '')
    
    # Check translated files
    for lang in ['es', 'pt', 'sw', 'rw']:
        lang_filepath = os.path.join(base_dir, f"{current_base}_{lang}.html")
        if not os.path.exists(lang_filepath):
            # File might not be translated yet, skip for now
            continue
            
        print(f"Syncing selectors for {current_base}_{lang}.html...")
        
        with open(lang_filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        # 1. Update Navbar Selector
        nav_lang = soup.find('a', class_='nav-lang')
        if nav_lang:
            cycle = translations[lang]['cycle']
            new_nav_lang = BeautifulSoup(f"""
            <a href="#" class="nav-lang no-pill" onclick="showLanguageModal(event)" title="Switch Language">
              <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
              <span class="lang-text-cycle">
                <span class="lt-item">{cycle[0]}</span>
                <span class="lt-item">{cycle[1]}</span>
                <span class="lt-item">{cycle[2]}</span>
                <span class="lt-item">{cycle[3]}</span>
                <span class="lt-item">{cycle[4]}</span>
              </span>
            </a>
            """, 'html.parser')
            nav_lang.replace_with(new_nav_lang)
            
        # 2. Update Language Selector Modal
        lang_modal = soup.find('div', id='language-modal')
        if lang_modal:
            title = translations[lang]['title']
            desc = translations[lang]['desc']
            btn_texts = translations[lang]['buttons']
            
            # Construct the 5 buttons
            btn_htmls = []
            for blang in ['en', 'es', 'pt', 'sw', 'rw']:
                label = btn_texts[blang]
                if blang == 'en':
                    target_url = f"{current_base}.html"
                else:
                    target_url = f"{current_base}_{blang}.html"
                    
                if blang == lang:
                    # Active button styling (green background)
                    style = "background:var(--green); color:#fff; border:none; padding:16px; border-radius:12px; font-weight:600; cursor:pointer; font-size:16px; transition:transform 0.2s;"
                else:
                    # Non-active button styling (white background)
                    style = "background:#fff; color:var(--dark); border:none; padding:16px; border-radius:12px; font-weight:600; cursor:pointer; font-size:16px; transition:transform 0.2s;"
                    
                btn_htmls.append(f'<button onclick="window.location.href=\'{target_url}\'" style="{style}">{label}</button>')
                
            buttons_grid = "\n    ".join(btn_htmls)
            
            new_modal = BeautifulSoup(f"""
            <div id="language-modal" style="display:none; position:fixed; inset:0; background:rgba(244,242,246,0.85); z-index:99999; backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px); align-items:center; justify-content:center; flex-direction:column; text-align:center;">
              <img src="images/FamilyFirstLogo.png" alt="Family First Legacy" style="max-width:180px; margin-bottom:32px;">
              <h2 style="color:var(--dark); font-family:var(--font-head); font-size:32px; margin-bottom:10px;">{title}</h2>
              <p style="color:var(--muted); font-family:var(--font-body); margin-bottom:40px;">{desc}</p>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; max-width:400px; width:100%; padding:0 20px;">
                {buttons_grid}
              </div>
            </div>
            """, 'html.parser')
            lang_modal.replace_with(new_modal)
            
        with open(lang_filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))

print("\n🎉 All existing localized pages successfully synced and updated!")
