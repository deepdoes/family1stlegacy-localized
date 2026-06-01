import glob
import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
files = glob.glob(os.path.join(base_dir, '*.html'))

logo_regex = re.compile(r'<div class="logo-mark">.*?</div>\s*<div class="logo-name"[^>]*>.*?</div>', re.DOTALL)
new_logo = r'<img src="images/FamilyFirstLogo.png" alt="Family First Legacy" style="height: 40px; width: auto; object-fit: contain; margin-top: 4px;">'

branding_html = '''
      <div style="text-align: center; margin-top: 40px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.05); font-size: 13px; color: rgba(255,255,255,0.4); display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap;">
        <span>Website created by DFW Branding</span>
        <a href="https://dfwbranding.com" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center;">
          <img src="https://dfwbranding.com/wp-content/uploads/2020/10/DFW-BRANDING-RED-BLACK.png" alt="DFW Branding" style="height: 22px; background: rgba(255,255,255,0.95); padding: 4px 8px; border-radius: 4px; object-fit: contain; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform=''">
        </a>
      </div>
    </div>
  </div>
</footer>
'''

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace logo
    content = logo_regex.sub(new_logo, content)
    
    # 2. Add DFW Branding if not already present
    if 'Website created by DFW Branding' not in content:
        # The footer structure ends with:
        #       </div>
        #     </div>
        #   </div>
        # </footer>
        
        # We will replace the last part of the footer
        content = content.replace('    </div>\n  </div>\n</footer>', branding_html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Updated logos in {os.path.basename(filepath)}")
