import sys
import os
import json
import urllib.request
import time
from bs4 import BeautifulSoup, Comment

def get_groq_key():
    # Try finding the API key in the main CafeOS environment file
    env_path = "/Users/deepankarakasajoo/Downloads/ZeroFeeOrder-MVP-main/.env.local"
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("GROQ_API_KEY="):
                    # Strip any surrounding quotes or spacing
                    val = line.split("=", 1)[1].strip()
                    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                        val = val[1:-1]
                    return val
    return os.environ.get("GROQ_API_KEY")

def translate_batch_groq(texts, lang, api_key):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    # Map target language code to native names for better prompt context
    lang_names = {
        'es': 'Spanish (neutral, premium financial tone)',
        'pt': 'Portuguese (Brazilian, professional financial tone)',
        'sw': 'Swahili (neutral, clear and professional)',
        'rw': 'Kinyarwanda (clear, professional, natural financial tone)'
    }
    target_lang_desc = lang_names.get(lang, lang)

    system_prompt = (
        "You are a professional, expert financial services and insurance translator. "
        f"Your task is to translate a list of English text or HTML fragments from a premium financial planning website into {target_lang_desc}. "
        "CRITICAL: Keep all HTML tags (like <br/>, <strong>, <a>, <span>) exactly as they are. Do not remove, split, or modify any HTML tags. Only translate the text inside and around them. "
        "CRITICAL: You must return the EXACT same number of translated fragments as the input array. Do not combine, omit, or split items. Each input element must map directly to its corresponding output element at the exact same index."
    )
    
    user_prompt = f"""Translate the following JSON array of HTML/text strings from a WFG-affiliated financial planning website into {target_lang_desc}.
    
Guidelines:
1. Provide a professional, natural, premium, high-fidelity translation suitable for an elite financial advisory firm. Do not translate literally if it sounds mechanical; use the correct industry terminology in the target language.
2. Keep WFG-specific terminology natural (e.g., 'Financial Needs Analysis' -> 'Análisis de Necesidades Financieras', 'Indexed Universal Life' -> 'Indexed Universal Life (IUL)', 'Living Benefits' -> 'Beneficios en Vida') using their standard localized equivalents in the target language.
3. Keep brand names like 'Family First Legacy', 'World Financial Group', 'WFG' intact unless they have standard localized equivalents.
4. Keep all HTML tags (like <br/>, <strong>, <a>) unchanged in position and name.
5. Keep the output as a valid JSON array of strings, where each element corresponds exactly to the input text index.

Input JSON:
{json.dumps(texts)}

You must respond with a valid JSON object in this exact schema (containing a "translations" key with the array of translated strings):
{{
  "translations": [
     "translated_string_1",
     "translated_string_2",
     ...
  ]
}}
"""
    
    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "response_format": { "type": "json_object" },
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.15
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    # Try with up to 5 retries with backoff in case of transient limits
    backoff = 5.0
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                text_response = res_data['choices'][0]['message']['content']
                parsed = json.loads(text_response.strip())
                translated = parsed.get("translations", [])
                
                if isinstance(translated, list) and len(translated) == len(texts):
                    return translated
                print(f"Mismatch in returned size (Expected {len(texts)}, Got {len(translated)}). Retrying...")
        except Exception as e:
            if hasattr(e, 'read'):
                try:
                    err_body = e.read().decode('utf-8')
                    print(f"API Error details: {err_body}")
                except:
                    pass
            print(f"API Error on attempt {attempt + 1}: {e}")
            if "429" in str(e):
                print(f"Rate limited (429). Backing off for {backoff} seconds...")
                time.sleep(backoff)
                backoff *= 2.0
            else:
                time.sleep(2)
    
    return None

def translate_html_groq(filepath, target_langs, api_key):
    print(f"\n========================================\nReading {os.path.basename(filepath)}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    for lang in target_langs:
        out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
        if os.path.exists(out_name):
            print(f"Skipping {lang} for {os.path.basename(filepath)} - output file already exists.")
            continue
            
        print(f"\n--- Translating to {lang} via block-level Groq Engine ---")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 1. Extract block-level elements that contain visible text
        elements_to_translate = []
        html_fragments = []
        
        # Tags we want to translate as whole blocks (including inner tags like <br/>, <strong>, etc.)
        candidate_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'option', 'button', 'a', 'span', 'cite', 'div']
        
        for tag_name in candidate_tags:
            for element in soup.find_all(tag_name):
                # If div, only translate if it contains direct text or only inline tags, not other main blocks
                if element.name == 'div':
                    if any(child.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div', 'section'] for child in element.find_all()):
                        continue
                
                # Check if this element is nested inside another element that we are already translating
                ancestor_translating = False
                parent = element.parent
                while parent:
                    if parent.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'option', 'button', 'a', 'span', 'cite']:
                        ancestor_translating = True
                        break
                    # If inside a div that we are translating, skip as well
                    if parent.name == 'div':
                        if not any(c.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'div', 'section'] for c in parent.find_all()):
                            ancestor_translating = True
                            break
                    parent = parent.parent
                    
                if ancestor_translating:
                    continue
                    
                # Exclude administrative and non-visible blocks
                if element.parent and element.parent.name in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                    continue
                
                # Get raw inner content to preserve HTML tags
                inner_html = element.decode_contents().strip()
                visible_text = element.get_text().strip()
                
                # Only translate if there's actual alphabetic text
                if len(visible_text) > 1 and any(c.isalpha() for c in visible_text):
                    # Do not translate language switcher modal buttons or cycles
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
        if not html_fragments:
            continue
            
        # 2. Batch translate
        chunk_size = 6 # Small batch size is extremely safe for rate limits and payload limits
        translated_fragments = []
        
        for i in range(0, len(html_fragments), chunk_size):
            chunk = html_fragments[i:i+chunk_size]
            print(f"Translating chunk {i//chunk_size + 1}/{(len(html_fragments)-1)//chunk_size + 1}...")
            
            res = translate_batch_groq(chunk, lang, api_key)
            if res:
                translated_fragments.extend(res)
            else:
                print("Batch translation failed. Attempting item-by-item fallback translation...")
                # Rate limit friendly sleep
                time.sleep(4.0)
                for item in chunk:
                    item_res = translate_batch_groq([item], lang, api_key)
                    if item_res and len(item_res) == 1:
                        translated_fragments.append(item_res[0])
                    else:
                        print(f"Fallback item failed, keeping original: {item[:30]}...")
                        translated_fragments.append(item)
                    time.sleep(4.0)
                
            time.sleep(3.5) # rate limit friendly
            
        # 3. Replace content inside the elements
        for idx, element in enumerate(elements_to_translate):
            if idx < len(translated_fragments) and translated_fragments[idx]:
                # Clear and insert new parsed translation structure (preserves HTML formatting)
                element.clear()
                # Parse fragment back
                frag_soup = BeautifulSoup(translated_fragments[idx], 'html.parser')
                element.append(frag_soup)
        
        # 4. Update language selector buttons in the modal to point to the correct localized versions of the current page!
        current_base = os.path.basename(filepath).replace('.html', '') # e.g. "family_protection"
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

        # 6. Override client language selectors (prevent language modal popup if already translated)
        scripts = soup.find_all('script')
        for s in scripts:
            if s.string and "localStorage.getItem('lang_selected')" in s.string:
                s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
                
        # 7. Save file
        print(f"Saving translated page to {out_name}...")
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    api_key = get_groq_key()
    if not api_key:
        print("Error: GROQ_API_KEY could not be found. Please ensure it is set in .env.local.")
        sys.exit(1)
        
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
    
    print(f"Starting Tag-Preserving Block-level Groq Translation Engine across {len(files_to_translate)} pages...")
    for filename in files_to_translate:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"Warning: File not found {filepath}")
        else:
            translate_html_groq(filepath, ['es', 'pt', 'sw', 'rw'], api_key)
            
    print("\n🎉 Tag-Preserving Block-level Groq Translation Pipeline Completed Successfully!")
