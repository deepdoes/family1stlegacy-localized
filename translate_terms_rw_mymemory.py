import sys
import os
import json
import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup

def translate_mymemory(text, langpair="en|rw"):
    url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair={langpair}"
    
    # Retry up to 3 times in case of transient network issues
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                data = json.loads(response.read().decode('utf-8'))
                translated = data.get('responseData', {}).get('translatedText', '')
                if translated:
                    # Clean up HTML entities if any are returned
                    translated = translated.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#039;", "'").replace("&amp;", "&")
                    return translated
        except Exception as e:
            print(f"MyMemory Error on attempt {attempt + 1}: {e}")
            sys.stdout.flush()
            time.sleep(1.5)
            
    return None

def translate_html_mymemory(filepath, lang="rw"):
    print(f"\n========================================\nReading {os.path.basename(filepath)}...")
    sys.stdout.flush()
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
    print(f"\n--- Translating to {lang} via Free MyMemory Translation Engine ---")
    sys.stdout.flush()
    soup = BeautifulSoup(html_content, 'html.parser')
    
    elements_to_translate = []
    html_fragments = []
    candidate_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'option', 'button', 'a', 'span', 'cite', 'div']
    
    for tag_name in candidate_tags:
        for element in soup.find_all(tag_name):
            if element.name == 'div':
                if any(child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div', 'section'] for child in element.find_all()):
                    continue
            
            ancestor_translating = False
            parent = element.parent
            while parent:
                if parent.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'option', 'button', 'a', 'span', 'cite']:
                    ancestor_translating = True
                    break
                if parent.name == 'div':
                    if not any(c.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div', 'section'] for c in parent.find_all()):
                        ancestor_translating = True
                        break
                parent = parent.parent
                
            if ancestor_translating:
                continue
                
            if element.parent and element.parent.name in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                continue
            
            inner_html = element.decode_contents().strip()
            visible_text = element.get_text().strip()
            
            if len(visible_text) > 1 and any(c.isalpha() for c in visible_text):
                is_lang_el = False
                parent = element
                while parent:
                    if parent.name == 'div' and (parent.get('id') == 'language-modal' or 'language-modal' in str(parent.get('class'))):
                        is_lang_el = True
                        break
                    if parent.name == 'a' and ('nav-lang' in str(parent.get('class'))):
                        is_lang_el = True
                        break
                    parent = parent.parent
                
                if is_lang_el:
                    continue
                    
                elements_to_translate.append(element)
                html_fragments.append(inner_html)
    
    print(f"Found {len(html_fragments)} block-level fragments to translate.")
    sys.stdout.flush()
    
    # Translate block-by-block with polite pacing
    translated_fragments = []
    for idx, item in enumerate(html_fragments):
        print(f"Translating block {idx + 1}/{len(html_fragments)}...")
        sys.stdout.flush()
        
        # Parse and translate text, preserving outer/inner HTML structures if simple
        translated_text = translate_mymemory(item)
        if translated_text:
            translated_fragments.append(translated_text)
        else:
            print(f"Fallback: Keeping original text for block {idx + 1}")
            sys.stdout.flush()
            translated_fragments.append(item)
            
        time.sleep(0.35) # polite sleep pacing
        
    # Replace content inside the elements
    for idx, element in enumerate(elements_to_translate):
        if idx < len(translated_fragments) and translated_fragments[idx]:
            element.clear()
            frag_soup = BeautifulSoup(translated_fragments[idx], 'html.parser')
            element.append(frag_soup)
    
    # 4. Update language selector buttons in the modal
    current_base = os.path.basename(filepath).replace('.html', '')
    for btn in soup.find_all('button', onclick=True):
        onclick_str = btn['onclick']
        if 'setLanguage' in onclick_str or 'index_' in onclick_str or 'window.location.href' in onclick_str:
            if "'en'" in onclick_str or "setLanguage('en')" in onclick_str or "index.html" in onclick_str or btn.get_text().strip().lower() in ['english', 'ingliz', 'inglés', 'inglês']:
                btn['onclick'] = f"window.location.href='{current_base}.html'"
            elif "'es'" in onclick_str or "index_es.html" in onclick_str or btn.get_text().strip().lower() in ['español', 'kispaniki', 'espanhol']:
                btn['onclick'] = f"window.location.href='{current_base}_es.html'"
            elif "'pt'" in onclick_str or "index_pt.html" in onclick_str or btn.get_text().strip().lower() in ['português', 'purtukali', 'portugues']:
                btn['onclick'] = f"window.location.href='{current_base}_pt.html'"
            elif "'sw'" in onclick_str or "index_sw.html" in onclick_str or btn.get_text().strip().lower() in ['kiswahili', 'swahili']:
                btn['onclick'] = f"window.location.href='{current_base}_sw.html'"
            elif "'rw'" in onclick_str or "index_rw.html" in onclick_str or btn.get_text().strip().lower() in ['kinyarwanda']:
                btn['onclick'] = f"window.location.href='{current_base}_rw.html'"

    # 5. Update local links to point to their translated counterparts
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.endswith('.html') and not any(href.endswith(f'_{l}.html') for l in ['es', 'pt', 'sw', 'rw']):
            a['href'] = href.replace('.html', f'_{lang}.html')
        elif '.html#' in href:
            parts = href.split('.html#', 1)
            if not any(parts[0].endswith(f'_{l}') for l in ['es', 'pt', 'sw', 'rw']):
                a['href'] = f"{parts[0]}_{lang}.html#{parts[1]}"

    # 6. Override client language selectors
    scripts = soup.find_all('script')
    for s in scripts:
        if s.string and "localStorage.getItem('lang_selected')" in s.string:
            s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
            
    print(f"Saving translated page to {out_name}...")
    sys.stdout.flush()
    with open(out_name, 'w', encoding='utf-8') as f:
        f.write(str(soup))

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, 'terms.html')
    
    print("Translating the final terms.html to Kinyarwanda (rw) via Free MyMemory API...")
    sys.stdout.flush()
    translate_html_mymemory(filepath, 'rw')
    print("\n🎉 Kinyarwanda Terms Page Completed Successfully!")
    sys.stdout.flush()
