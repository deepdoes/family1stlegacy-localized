import sys
import os
import json
import urllib.request
import time
from bs4 import BeautifulSoup, NavigableString, Comment

def get_antigravity_endpoint():
    # Antigravity provides a local inference endpoint for built‑in models
    # Adjust if your deployment uses a different host/port
    return os.getenv('ANTIGRAVITY_ENDPOINT', 'http://localhost:8000/v1/chat/completions')

def get_antigravity_key():
    # Antigravity authentication token, if required (optional)
    return os.getenv('ANTIGRAVITY_API_KEY')

def translate_batch_oss(texts, lang, endpoint, api_key=None):
    # Map target language code to description for prompt clarity
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
1. Provide a professional, natural, premium, high‑fidelity translation suitable for an elite financial advisory firm. Do not translate literally if it sounds mechanical; use the correct industry terminology in the target language.
2. Keep WFG‑specific terminology natural (e.g., 'Financial Needs Analysis', 'Indexed Universal Life', 'Living Benefits') using their standard localized equivalents in the target language.
3. Keep brand names like 'Family First Legacy', 'World Financial Group', 'WFG' intact unless they have standard localized equivalents.
4. Return a JSON object with a single key "translations" containing an array of translated strings in the same order.

Input JSON:
{json.dumps(texts)}

Output example:
{{"translations": ["...", "..."]}}
"""
    data = {
        "model": "gpt-oss-120b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"}
    }
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(endpoint, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                content = res_data['choices'][0]['message']['content']
                parsed = json.loads(content.strip())
                translated = parsed.get('translations', [])
                if isinstance(translated, list) and len(translated) == len(texts):
                    return translated
                print(f"Size mismatch (expected {len(texts)}, got {len(translated)}). Retrying…")
        except Exception as e:
            print(f"API error on attempt {attempt+1}: {e}")
            time.sleep(2)
    return None

def translate_html_oss(filepath, target_langs):
    print(f"\n=== Translating {os.path.basename(filepath)} ===")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    endpoint = get_antigravity_endpoint()
    api_key = get_antigravity_key()
    for lang in target_langs:
        print(f"--- Translating to {lang} with GPT‑OSS 120B ---")
        soup = BeautifulSoup(html_content, 'html.parser')
        # 1. Find text nodes
        texts_to_translate = []
        nodes_to_translate = []
        for element in soup.descendants:
            if isinstance(element, NavigableString) and not isinstance(element, Comment):
                parent = element.parent
                if parent and parent.name not in ['script', 'style', 'head', 'title', 'meta', '[document]']:
                    text = str(element).strip()
                    if len(text) > 1 and any(c.isalpha() for c in text):
                        texts_to_translate.append(text)
                        nodes_to_translate.append(element)
        if not texts_to_translate:
            continue
        # 2. Batch translate
        chunk_size = 40
        translated_texts = []
        for i in range(0, len(texts_to_translate), chunk_size):
            chunk = texts_to_translate[i:i+chunk_size]
            print(f"Translating chunk {i//chunk_size + 1}/{(len(texts_to_translate)-1)//chunk_size + 1}")
            res = translate_batch_oss(chunk, lang, endpoint, api_key)
            if res:
                translated_texts.extend(res)
            else:
                print("Fallback – using original text for this chunk.")
                translated_texts.extend(chunk)
            time.sleep(1)
        # 3. Replace text in DOM
        for idx, node in enumerate(nodes_to_translate):
            if idx < len(translated_texts) and translated_texts[idx]:
                node.replace_with(translated_texts[idx])
        # 4. Update language selector buttons
        for btn in soup.find_all('button', onclick=True):
            if 'setLanguage' in btn['onclick']:
                btn_lang = btn['onclick'].split("'")[1]
                base_name = os.path.basename(filepath)
                if btn_lang == 'en':
                    btn['onclick'] = f"window.location.href = '{base_name}'"
                else:
                    btn['onclick'] = f"window.location.href = '{base_name}'.replace('.html', f'_{btn_lang}.html')"
        # 5. Update internal links
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.endswith('.html'):
                a['href'] = href.replace('.html', f'_{lang}.html')
            elif '.html#' in href:
                a['href'] = href.replace('.html#', f'_{lang}.html#')
        # 6. Disable language modal popup on already translated pages
        for s in soup.find_all('script'):
            if s.string and "localStorage.getItem('lang_selected')" in s.string:
                s.string = s.string.replace("if (!localStorage.getItem('lang_selected')) {", "if (false) {")
        # 7. Write out translated file
        out_name = f"{filepath.rsplit('.', 1)[0]}_{lang}.html"
        print(f"Saving translated page to {out_name}")
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
    print(f"Starting GPT‑OSS 120B translation for {len(files_to_translate)} pages…")
    for filename in files_to_translate:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
        translate_html_oss(filepath, ['es', 'pt', 'sw'])
    print("\n✅ Translation pipeline completed.")
