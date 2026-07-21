import os
import sys
import json
import urllib.request
import urllib.parse
import time
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup, NavigableString, Comment

base_dir = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
files_to_translate = [
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

brand_placeholders = {
    "Family First Legacy": "___BRAND_FFL___",
    "World Financial Group": "___BRAND_WFG___",
    "WFG": "___BRAND_WFG_SHORT___"
}

def protect_brands(text):
    for brand, placeholder in brand_placeholders.items():
        text = text.replace(brand, placeholder)
    return text

def restore_brands(text):
    for brand, placeholder in brand_placeholders.items():
        text = text.replace(placeholder, brand)
        text = text.replace(placeholder.lower(), brand)
    return text

def translate_text(text, target_lang):
    if not text.strip() or not any(c.isalpha() for c in text):
        return text
        
    # Check if text is email, URL, phone number, or allowed text
    if "@" in text or "http" in text or text.startswith("+1") or (text.replace("-", "").replace("(", "").replace(")", "").replace(" ", "").isdigit() and len(text) > 5):
        return text

    protected_text = protect_brands(text)
    
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={urllib.parse.quote(protected_text)}"
    
    for attempt in range(5):
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
            )
            with urllib.request.urlopen(req, timeout=8) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                translated_parts = [part[0] for part in res_data[0] if part[0]]
                translated_text = "".join(translated_parts)
                final_text = restore_brands(translated_text)
                return final_text
        except Exception as e:
            # Simple retry backoff
            time.sleep(0.5 + attempt * 0.5)
            
    return text # Fallback

def translate_html_file(filename, target_langs):
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Warning: File not found {filepath}")
        return
        
    print(f"\n========================================\nProcessing: {filename}")
    sys.stdout.flush()
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    for lang in target_langs:
        out_name = f"{filename.rsplit('.', 1)[0]}_{lang}.html"
        out_filepath = os.path.join(base_dir, out_name)
        
        print(f"--- Translating {filename} to {lang} ---")
        sys.stdout.flush()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 1. Collect all valid NavigableStrings
        nodes_to_translate = []
        texts_to_translate = []
        
        for element in soup.descendants:
            if isinstance(element, NavigableString) and not isinstance(element, Comment):
                parent = element.parent
                if parent and parent.name not in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                    text = str(element).strip()
                    if len(text) > 1 and any(c.isalpha() for c in text):
                        is_lang_el = False
                        p = parent
                        while p:
                            if p.name == 'div' and (p.get('id') == 'language-modal' or 'language-modal' in str(p.get('class'))):
                                is_lang_el = True
                                break
                            if p.name == 'a' and ('nav-lang' in str(p.get('class'))):
                                is_lang_el = True
                                break
                            p = p.parent
                        
                        if not is_lang_el:
                            nodes_to_translate.append(element)
                            texts_to_translate.append(str(element))
                            
        print(f"Found {len(nodes_to_translate)} text nodes. Translating in parallel...")
        sys.stdout.flush()
        
        # 2. Parallel translation using ThreadPoolExecutor
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=20) as executor:
            translated_texts = list(executor.map(lambda text: translate_text(text, lang), texts_to_translate))
            
        t1 = time.time()
        print(f"  Finished translation in {t1 - t0:.2f} seconds.")
        sys.stdout.flush()
        
        # 3. Replace in DOM
        for idx, node in enumerate(nodes_to_translate):
            if idx < len(translated_texts) and translated_texts[idx]:
                node.replace_with(translated_texts[idx])
            
        # 4. Update local href links
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html') and not any(href.endswith(f'_{l}.html') for l in ['es', 'pt', 'sw', 'rw']):
                a['href'] = href.replace('.html', f'_{lang}.html')
            elif '.html#' in href:
                parts = href.split('.html#', 1)
                if not any(parts[0].endswith(f'_{l}') for l in ['es', 'pt', 'sw', 'rw']):
                    a['href'] = f"{parts[0]}_{lang}.html#{parts[1]}"
                    
        # 5. Save file
        with open(out_filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    target_languages = ['es', 'pt', 'sw', 'rw']
    print(f"Starting FAST Parallel Google Translate Engine for {len(files_to_translate)} files...")
    sys.stdout.flush()
    
    for filename in files_to_translate:
        translate_html_file(filename, target_languages)
        
    print("\n🎉 Parallel site translation completed successfully!")
    sys.stdout.flush()
