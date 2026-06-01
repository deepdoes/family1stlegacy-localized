import sys
import os
import json
import urllib.request
import time
from bs4 import BeautifulSoup, NavigableString, Comment

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
        'sw': 'Swahili (neutral, clear and professional)'
    }
    target_lang_desc = lang_names.get(lang, lang)

    system_prompt = (
        "You are a professional, expert financial services and insurance translator. "
        f"Your task is to translate a list of English text strings from a premium financial planning website into {target_lang_desc}. "
        "CRITICAL: You must return the EXACT same number of translated strings as the input array. Do not combine, omit, or split strings. Each input string must map directly to its corresponding output string at the exact same index."
    )
    
    user_prompt = f"""Translate the following JSON array of English text strings from a WFG-affiliated financial planning website into {target_lang_desc}.

Guidelines:
1. Provide a professional, natural, premium, high-fidelity translation suitable for an elite financial advisory firm. Do not translate literally if it sounds mechanical; use the correct industry terminology in the target language.
2. Keep WFG-specific terminology natural (e.g., 'Financial Needs Analysis', 'Indexed Universal Life', 'Living Benefits') using their standard localized equivalents in the target language.
3. Keep brand names like 'Family First Legacy', 'World Financial Group', 'WFG' intact unless they have standard localized equivalents.
4. Keep the output as a valid JSON array of strings, where each element corresponds exactly to the input text index.

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
        "model": "llama-3.1-8b-instant",
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
        "temperature": 0.2
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
        print(f"\n--- Translating to {lang} via Groq Llama-3.3 ---")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 1. Find meaningful text nodes
        texts_to_translate = []
        nodes_to_translate = []
        
        for element in soup.descendants:
            if isinstance(element, NavigableString) and not isinstance(element, Comment):
                parent = element.parent
                if parent and parent.name not in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                    text = str(element).strip()
                    # Only translate strings with alphabetic characters and length > 1
                    if len(text) > 1 and any(c.isalpha() for c in text):
                        texts_to_translate.append(text)
                        nodes_to_translate.append(element)
        
        print(f"Found {len(texts_to_translate)} text nodes to translate.")
        if not texts_to_translate:
            continue
            
        # 2. Batch translate using Groq
        chunk_size = 8 # Small chunk sizes to stay 100% free of array mismatch errors and run extremely fast
        translated_texts = []
        
        for i in range(0, len(texts_to_translate), chunk_size):
            chunk = texts_to_translate[i:i+chunk_size]
            print(f"Translating chunk {i//chunk_size + 1}/{(len(texts_to_translate)-1)//chunk_size + 1}...")
            
            res = translate_batch_groq(chunk, lang, api_key)
            if res:
                translated_texts.extend(res)
            else:
                print("Fallback: Using original text for this chunk due to translation failure.")
                translated_texts.extend(chunk)
                
            time.sleep(0.4) # rate limit friendly
            
        # 3. Replace text in the DOM tree
        for idx, node in enumerate(nodes_to_translate):
            if idx < len(translated_texts) and translated_texts[idx]:
                node.replace_with(translated_texts[idx])
        
        # 4. Update language selectors to navigate to compiled pages
        for btn in soup.find_all('button', onclick=True):
            if 'setLanguage' in btn['onclick']:
                btn_lang = btn['onclick'].split("'")[1]
                if btn_lang == 'en':
                    base_name = os.path.basename(filepath)
                    btn['onclick'] = f"window.location.href = '{base_name}'"
                else:
                    base_name = os.path.basename(filepath).replace('.html', f'_{btn_lang}.html')
                    btn['onclick'] = f"window.location.href = '{base_name}'"

        # 5. Update local links to point to their translated counterparts
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html'):
                a['href'] = href.replace('.html', f'_{lang}.html')
            elif '.html#' in href:
                a['href'] = href.replace('.html#', f'_{lang}.html#')

        # 6. Override client language selectors (prevent language modal popup if already translated)
        scripts = soup.find_all('script')
        for s in scripts:
            if s.string and "localStorage.getItem('lang_selected')" in s.string:
                s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
                
        # 7. Save file
        out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
        print(f"Saving translated page to {out_name}...")
        with open(out_name, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    api_key = get_groq_key()
    if not api_key:
        print("Error: GROQ_API_KEY could not be found. Please ensure it is set in .env.local.")
        sys.exit(1)
        
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # We will translate all 13 core files (main pages, blogs, and legal documents)!
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
    
    print(f"Starting Groq Llama-3.3 Translation Engine across {len(files_to_translate)} pages...")
    for filename in files_to_translate:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"Warning: File not found {filepath}")
        else:
            translate_html_groq(filepath, ['es', 'pt', 'sw'], api_key)
            
    print("\n🎉 Groq AI Translation Pipeline Completed Successfully!")
