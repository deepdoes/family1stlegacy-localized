import sys
import os
import json
import urllib.request
import time
from bs4 import BeautifulSoup

def get_gemini_key():
    env_path = "/Users/deepankarakasajoo/Downloads/ZeroFeeOrder-MVP-main/.env.local"
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    val = line.split("=", 1)[1].strip()
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    return val
    return os.environ.get("GEMINI_API_KEY")

def translate_batch_gemini(texts, lang, api_key):
    # Using gemini-1.5-flash for separate, untouched 1,500 RPD daily quota!
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    lang_names = {
        'rw': 'Kinyarwanda (clear, professional, natural financial tone)'
    }
    target_lang_desc = lang_names.get(lang, lang)

    prompt = f"""You are a professional, expert financial services and insurance translator.
Your task is to translate a list of English text or HTML fragments from a premium financial planning website into {target_lang_desc}.

CRITICAL: Keep all HTML tags (like <br/>, <strong>, <a>, <span>) exactly as they are. Do not remove, split, or modify any HTML tags. Only translate the text inside and around them.
Each input element must map directly to its corresponding output element at the exact same index in the returned JSON array.

Input JSON:
{json.dumps(texts)}

Respond with a JSON object in this exact schema (with the "translations" key containing the array of translated strings):
{{
  "translations": [
     "translated_string_1",
     "translated_string_2",
     ...
  ]
}}
"""
    
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    backoff = 4.0
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                text_response = res_data['candidates'][0]['content']['parts'][0]['text'].strip()
                
                if text_response.startswith("```"):
                    if text_response.startswith("```json"):
                        text_response = text_response[7:]
                    else:
                        text_response = text_response[3:]
                    if text_response.endswith("```"):
                        text_response = text_response[:-3]
                    text_response = text_response.strip()
                    
                parsed = json.loads(text_response)
                translated = parsed.get("translations", [])
                
                if isinstance(translated, list) and len(translated) == len(texts):
                    return translated
                print(f"Mismatch in returned size. Retrying...")
                sys.stdout.flush()
        except Exception as e:
            if hasattr(e, 'read'):
                try:
                    err_body = e.read().decode('utf-8')
                    print(f"API Error details: {err_body}")
                except:
                    pass
            print(f"API Error on attempt {attempt + 1}: {e}")
            sys.stdout.flush()
            if "429" in str(e):
                print(f"Rate limited (429). Backing off...")
                sys.stdout.flush()
                time.sleep(backoff)
                backoff *= 2.0
            else:
                time.sleep(2)
    
    return None

def translate_html_gemini(filepath, target_langs, api_key):
    print(f"\n========================================\nReading {os.path.basename(filepath)}...")
    sys.stdout.flush()
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    for lang in target_langs:
        out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
        print(f"\n--- Translating to {lang} via block-level Gemini 1.5 Flash ---")
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
        if html_fragments:
            chunk_size = 15 
            translated_fragments = []
            
            for i in range(0, len(html_fragments), chunk_size):
                chunk = html_fragments[i:i+chunk_size]
                print(f"Translating chunk {i//chunk_size + 1}/{(len(html_fragments)-1)//chunk_size + 1}...")
                sys.stdout.flush()
                
                res = translate_batch_gemini(chunk, lang, api_key)
                if res:
                    translated_fragments.extend(res)
                else:
                    print("Fallback: Using original text for this chunk due to translation failure.")
                    sys.stdout.flush()
                    translated_fragments.extend(chunk)
                    
                time.sleep(2.0) 
                
            for idx, element in enumerate(elements_to_translate):
                if idx < len(translated_fragments) and translated_fragments[idx]:
                    element.clear()
                    frag_soup = BeautifulSoup(translated_fragments[idx], 'html.parser')
                    element.append(frag_soup)
        
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

        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html') and not any(href.endswith(f'_{l}.html') for l in ['es', 'pt', 'sw', 'rw']):
                a['href'] = href.replace('.html', f'_{lang}.html')
            elif '.html#' in href:
                parts = href.split('.html#', 1)
                if not any(parts[0].endswith(f'_{l}') for l in ['es', 'pt', 'sw', 'rw']):
                    a['href'] = f"{parts[0]}_{lang}.html#{parts[1]}"

        scripts = soup.find_all('script')
        for s in scripts:
            if s.string and "localStorage.getItem('lang_selected')" in s.string:
                s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
                
        print(f"Saving translated page to {out_name}...")
        sys.stdout.flush()
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    api_key = get_gemini_key()
    if not api_key:
        print("Error: GEMINI_API_KEY could not be found.")
        sys.exit(1)
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, 'terms.html')
    
    print("Translating the final terms.html to Kinyarwanda (rw) via Gemini 1.5 Flash...")
    sys.stdout.flush()
    translate_html_gemini(filepath, ['rw'], api_key)
    print("\n🎉 Kinyarwanda Terms Page Completed Successfully!")
    sys.stdout.flush()
