import os
import sys
import json
import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup

base_dir = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
files = [
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

def translate_mymemory(text, langpair="en|rw"):
    url = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(text)}&langpair={langpair}"
    
    # Retry up to 3 times in case of network issues
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
            )
            with urllib.request.urlopen(req, timeout=12) as response:
                data = json.loads(response.read().decode('utf-8'))
                translated = data.get('responseData', {}).get('translatedText', '')
                if translated:
                    # Clean up HTML entities
                    translated = translated.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#039;", "'").replace("&amp;", "&")
                    return translated
        except Exception as e:
            print(f"MyMemory Error on attempt {attempt + 1}: {e}")
            sys.stdout.flush()
            time.sleep(2.0)
            
    return None

def extract_blocks_with_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    blocks = []
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
            
            visible_text = element.get_text().strip()
            if len(visible_text) > 1 and any(c.isalpha() for c in visible_text):
                # Skip language switcher modal and cycle elements
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
                
                blocks.append({
                    'element': element,
                    'text': visible_text,
                    'html': element.decode_contents().strip()
                })
    return blocks

print("Starting Premium Kinyarwanda Swahili-Cleanup Pipeline...")
sys.stdout.flush()

for filename in files:
    en_path = os.path.join(base_dir, filename)
    sw_path = os.path.join(base_dir, filename.replace('.html', '_sw.html'))
    rw_path = os.path.join(base_dir, filename.replace('.html', '_rw.html'))
    
    if not os.path.exists(en_path) or not os.path.exists(sw_path) or not os.path.exists(rw_path):
        print(f"Skipping {filename} - one of the files is missing.")
        sys.stdout.flush()
        continue
        
    print(f"\n========================================\nAnalyzing {filename} Kinyarwanda Page...")
    sys.stdout.flush()
    
    en_blocks = extract_blocks_with_html(en_path)
    sw_blocks = extract_blocks_with_html(sw_path)
    
    # Reload Kinyarwanda with BeautifulSoup to perform in-place modification
    with open(rw_path, 'r', encoding='utf-8') as f:
        rw_soup = BeautifulSoup(f.read(), 'html.parser')
        
    # We must re-extract the blocks from rw_soup to have exact elements in the DOM tree
    rw_blocks = []
    candidate_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'option', 'button', 'a', 'span', 'cite', 'div']
    for tag_name in candidate_tags:
        for element in rw_soup.find_all(tag_name):
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
            if ancestor_translating or (element.parent and element.parent.name in ['script', 'style', 'head', 'title', 'meta', '[document]']):
                continue
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
                rw_blocks.append({
                    'element': element,
                    'text': visible_text
                })
                
    min_len = min(len(en_blocks), len(sw_blocks), len(rw_blocks))
    print(f"Aligning {min_len} blocks for translation comparison...")
    sys.stdout.flush()
    
    fixes_made = 0
    for i in range(min_len):
        en_text = en_blocks[i]['text']
        en_html = en_blocks[i]['html']
        sw_text = sw_blocks[i]['text']
        rw_text = rw_blocks[i]['text']
        
        # Check if the block is identical in Swahili and Kinyarwanda
        if sw_text == rw_text:
            # Check if this is not just an administrative string (email, domain, number)
            is_valid_candidate = True
            if "@" in en_text or en_text.startswith("http") or en_text.endswith(".html") or en_text.endswith(".com"):
                is_valid_candidate = False
            if en_text in ["A+", "Licensed & Insured", "24hr Response", "100% Private", "Subscribe"]:
                pass
                
            if is_valid_candidate:
                print(f"  -> Translating Swahili block {i} ('{sw_text[:35]}...') back to Kinyarwanda...")
                print(f"     Original English: '{en_text[:40]}...'")
                sys.stdout.flush()
                
                # We translate the original English fragment to preserve high-fidelity HTML structures
                translated = translate_mymemory(en_html, "en|rw")
                if translated:
                    print(f"     Translation: '{translated[:40]}...'")
                    sys.stdout.flush()
                    
                    # Perform DOM replacement
                    target_el = rw_blocks[i]['element']
                    target_el.clear()
                    frag_soup = BeautifulSoup(translated, 'html.parser')
                    target_el.append(frag_soup)
                    fixes_made += 1
                else:
                    print("     Failed to get translation, keeping current.")
                    sys.stdout.flush()
                
                time.sleep(0.4) # polite pacing
                
    if fixes_made > 0:
        print(f"Saving fully Kinyarwanda-synchronized page to {rw_path}...")
        sys.stdout.flush()
        with open(rw_path, 'w', encoding='utf-8') as f:
            f.write(str(rw_soup))
    else:
        print("No Swahili fallbacks needed fixing on this page.")
        sys.stdout.flush()

print("\n🎉 Premium Kinyarwanda Swahili-Cleanup Pipeline Completed Successfully!")
sys.stdout.flush()
