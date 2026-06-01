import sys
import os
import json
import urllib.request
import time
from bs4 import BeautifulSoup, NavigableString, Comment

def get_openai_key():
    # 1. Try finding in the current directory's .env.local
    local_env = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env.local")
    if os.path.exists(local_env):
        with open(local_env, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("OPENAI_API_KEY="):
                    return line.split("=", 1)[1].strip()
    # 2. Try finding the API key in the main CafeOS environment
    env_path = "/Users/deepankarakasajoo/Downloads/ZeroFeeOrder-MVP-main/.env.local"
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith("OPENAI_API_KEY="):
                    return line.split("=", 1)[1].strip()
    # 3. Try standard environment variables
    return os.environ.get("OPENAI_API_KEY")

def translate_batch_openai(texts, lang, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    
    # Map target language code to native names for better prompt context
    lang_names = {
        'es': 'Spanish (neutral, premium financial tone)',
        'pt': 'Portuguese (Brazilian, professional financial tone)',
        'sw': 'Swahili (neutral, clear and professional)'
    }
    target_lang_desc = lang_names.get(lang, lang)

    system_prompt = (
        "You are a professional, expert financial services and insurance translator. "
        f"Your task is to translate a list of English text strings from a premium financial planning website into {target_lang_desc}."
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
        "model": "gpt-4o-mini",
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
        'Authorization': f'Bearer {api_key}'
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    # Try with up to 3 retries in case of transient API limits
    for attempt in range(3):
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
            time.sleep(2)
    
    return None

def translate_html_openai(filepath, target_langs, api_key):
    print(f"\n========================================\nReading {os.path.basename(filepath)}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    for lang in target_langs:
        print(f"\n--- Translating to {lang} via OpenAI ChatGPT ---")
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
            
        # 2. Batch translate using OpenAI
        chunk_size = 40 # Standard chunk size for cost-effectiveness and precision
        translated_texts = []
        
        for i in range(0, len(texts_to_translate), chunk_size):
            chunk = texts_to_translate[i:i+chunk_size]
            print(f"Translating chunk {i//chunk_size + 1}/{(len(texts_to_translate)-1)//chunk_size + 1}...")
            
            res = translate_batch_openai(chunk, lang, api_key)
            if res:
                translated_texts.extend(res)
            else:
                print("Fallback: Using original text for this chunk due to translation failure.")
                translated_texts.extend(chunk)
                
            time.sleep(1.0) # rate limit friendly
            
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
    api_key = get_openai_key()
    if not api_key:
        print("Error: OPENAI_API_KEY could not be found. Please set OPENAI_API_KEY in your .env.local or shell environment.")
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
    
    print(f"Starting OpenAI ChatGPT Translation Engine across {len(files_to_translate)} pages...")
    for filename in files_to_translate:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"Warning: File not found {filepath}")
        else:
            translate_html_openai(filepath, ['es', 'pt', 'sw'], api_key)
            
    print("\n🎉 OpenAI ChatGPT Translation Pipeline Completed Successfully!")
