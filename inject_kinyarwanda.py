import os
import re

base_dir = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"
files_to_update = [
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

print("Injecting Kinyarwanda selectors into 13 English source files...")

cycle_old = """              <span class="lt-item">English</span>
              <span class="lt-item">Español</span>
              <span class="lt-item">Português</span>
              <span class="lt-item">Kiswahili</span>"""

cycle_new = """              <span class="lt-item">English</span>
              <span class="lt-item">Español</span>
              <span class="lt-item">Português</span>
              <span class="lt-item">Kiswahili</span>
              <span class="lt-item">Kinyarwanda</span>"""

modal_old = """    <button onclick="window.location.href='index_sw.html'" style="background:#fff; color:var(--dark); border:none; padding:16px; border-radius:12px; font-weight:600; cursor:pointer; font-size:16px; transition:transform 0.2s;">Kiswahili</button>
  </div>"""

modal_new = """    <button onclick="window.location.href='index_sw.html'" style="background:#fff; color:var(--dark); border:none; padding:16px; border-radius:12px; font-weight:600; cursor:pointer; font-size:16px; transition:transform 0.2s;">Kiswahili</button>
    <button onclick="window.location.href='index_rw.html'" style="background:#fff; color:var(--dark); border:none; padding:16px; border-radius:12px; font-weight:600; cursor:pointer; font-size:16px; transition:transform 0.2s;">Kinyarwanda</button>
  </div>"""

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"Warning: File not found {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    updated = False
    
    # 1. Update Navbar Cycle
    if "Kinyarwanda" not in content and cycle_old in content:
        content = content.replace(cycle_old, cycle_new)
        updated = True
        
    # 2. Update Language Modal Buttons
    if "index_rw.html" not in content and modal_old in content:
        content = content.replace(modal_old, modal_new)
        updated = True
        
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Injected Kinyarwanda into {filename}")
    else:
        print(f"ℹ️ Skipped {filename} (already updated or structure mismatch)")

print("\nInjection completed successfully!")
