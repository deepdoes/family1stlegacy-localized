import sys
import os
from bs4 import BeautifulSoup, NavigableString, Comment
from deep_translator import GoogleTranslator
import time

def translate_html(filepath, target_langs):
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    for lang in target_langs:
        print(f"\n--- Translating to {lang} ---")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # We need to find all text nodes that actually contain text
        texts_to_translate = []
        nodes_to_translate = []
        
        for element in soup.descendants:
            if isinstance(element, NavigableString) and not isinstance(element, Comment):
                parent = element.parent
                if parent and parent.name not in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                    text = str(element).strip()
                    if len(text) > 1 and any(c.isalpha() for c in text): # Only translate meaningful text
                        texts_to_translate.append(text)
                        nodes_to_translate.append(element)
        
        print(f"Found {len(texts_to_translate)} text nodes to translate.")
        
        # Batch translation (deep_translator supports lists but sometimes fails on large lists, let's do chunks of 50)
        translator = GoogleTranslator(source='en', target=lang)
        chunk_size = 50
        translated_texts = []
        
        for i in range(0, len(texts_to_translate), chunk_size):
            chunk = texts_to_translate[i:i+chunk_size]
            try:
                res = translator.translate_batch(chunk)
                translated_texts.extend(res)
                print(f"Translated chunk {i//chunk_size + 1}/{(len(texts_to_translate)-1)//chunk_size + 1}")
                time.sleep(1) # Be nice to the API
            except Exception as e:
                print(f"Error translating chunk: {e}")
                # Fallback to individual
                for text in chunk:
                    try:
                        translated_texts.append(translator.translate(text))
                    except:
                        translated_texts.append(text)
        
        # Replace in tree
        for i, node in enumerate(nodes_to_translate):
            if i < len(translated_texts) and translated_texts[i]:
                node.replace_with(translated_texts[i])
        
        # Also need to update the links in the modal
        # Since it's static files now, we should update the language buttons
        for btn in soup.find_all('button', onclick=True):
            if 'setLanguage' in btn['onclick']:
                btn_lang = btn['onclick'].split("'")[1]
                if btn_lang == 'en':
                    # If English, they should go back to the base file
                    base_name = os.path.basename(filepath)
                    btn['onclick'] = f"window.location.href = '{base_name}'"
                else:
                    base_name = os.path.basename(filepath).replace('.html', f'_{btn_lang}.html')
                    btn['onclick'] = f"window.location.href = '{base_name}'"

        # Update internal links to point to localized versions
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html'):
                a['href'] = href.replace('.html', f'_{lang}.html')
            elif '.html#' in href:
                a['href'] = href.replace('.html#', f'_{lang}.html#')

        # And hide the modal if we are already on a localized page
        scripts = soup.find_all('script')
        for s in scripts:
            if s.string and "localStorage.getItem('lang_selected')" in s.string:
                s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
                
        # Write out
        out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
        print(f"Saving to {out_name}...")
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
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
    
    for filename in files_to_translate:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
        else:
            translate_html(filepath, ['es', 'pt', 'sw'])
