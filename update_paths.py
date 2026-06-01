import glob
import os

base_dir = '/Users/deepankarakasajoo/Downloads/Family1stLegacy'
files = glob.glob(os.path.join(base_dir, 'family1stlegacy_v2_16*.html'))

old_path = 'file:///Users/deepankarakasajoo/.gemini/antigravity/brain/602b004a-02d2-476a-ac91-ae1443a469bc/'
new_path = 'images/'

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_path in content:
        content = content.replace(old_path, new_path)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated paths in {os.path.basename(filepath)}")
