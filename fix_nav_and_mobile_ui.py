#!/usr/bin/env python3
"""
fix_nav_and_mobile_ui.py
1. Fixes the Language Switcher Button & Dropdown UI (horizontal inline flex button, pill badges for language codes, active checkmarks).
2. Fixes the Nav Pill sliding animation bug so the pill locks onto 'Services' (and other links) 
   without sliding back to 'About' when hovering over dropdowns or language switchers.
3. Injects a comprehensive Mobile UI/UX CSS overhaul across ALL pages (English & Spanish), 
   fixing multi-column squishing, horizontal overflow, card clipping, header overlap, and typography scaling.
"""

import os
import glob
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# --- Complete Global Style Overhaul (Nav Pill, Language Dropdown, & Mobile UI/UX) ---
GLOBAL_OVERHAUL_CSS = """
/* ─── LANGUAGE SWITCHER PREMIUM UI FIXES ─── */
#nav .lang-switcher {
  position: relative !important;
  display: inline-flex !important;
  align-items: center !important;
}
#nav .lang-btn {
  display: inline-flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  height: 36px !important;
  padding: 0 14px !important;
  border-radius: 20px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  letter-spacing: 0.5px !important;
  cursor: pointer !important;
  white-space: nowrap !important;
  font-family: var(--font-body) !important;
  transition: all 0.2s ease !important;
}
#nav:not(.stuck) .lang-btn {
  background: rgba(255,255,255,0.12) !important;
  border: 1px solid rgba(255,255,255,0.3) !important;
  color: #FFFFFF !important;
}
#nav.stuck .lang-btn {
  background: rgba(74,45,122,0.08) !important;
  border: 1px solid rgba(74,45,122,0.2) !important;
  color: #0A0A0F !important;
}
#nav .lang-btn svg { width: 14px !important; height: 14px !important; flex-shrink: 0 !important; }
#nav .lang-btn .lang-chevron { width: 10px !important; height: 10px !important; transition: transform 0.2s !important; }
#nav .lang-switcher.open .lang-chevron { transform: rotate(180deg) !important; }

#nav .lang-dropdown {
  position: absolute !important;
  top: calc(100% + 10px) !important;
  right: 0 !important;
  background: #FFFFFF !important;
  border: 1px solid #E8E4EF !important;
  border-radius: 16px !important;
  padding: 8px !important;
  min-width: 195px !important;
  box-shadow: 0 16px 40px rgba(32,18,56,0.18) !important;
  z-index: 10000 !important;
}
#nav .lang-dropdown a {
  display: flex !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 10px !important;
  padding: 10px 14px !important;
  border-radius: 10px !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: #222222 !important;
  text-decoration: none !important;
  transition: background 0.15s ease, color 0.15s ease !important;
  white-space: nowrap !important;
}
#nav .lang-dropdown a span:first-child {
  background: rgba(74,45,122,0.08) !important;
  color: #4A2D7A !important;
  padding: 2px 7px !important;
  border-radius: 6px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  letter-spacing: 0.5px !important;
  min-width: 28px !important;
  text-align: center !important;
}
#nav .lang-dropdown a:hover {
  background: #EDE6F5 !important;
  color: #4A2D7A !important;
}
#nav .lang-dropdown a.active {
  font-weight: 700 !important;
  color: #4A2D7A !important;
  background: rgba(74,45,122,0.05) !important;
}
#nav .lang-dropdown a .lang-check {
  margin-left: auto !important;
  font-size: 13px !important;
  color: #4A2D7A !important;
}

/* ─── COMPREHENSIVE MOBILE RESPONSIVE OVERHAUL (max-width: 768px) ─── */
@media (max-width: 768px) {
  /* Layout & Container Padding */
  body { overflow-x: hidden !important; }
  .nav-bar { padding: 0 16px !important; height: 70px !important; }
  .page-hero { padding: 120px 0 60px !important; }
  .hero-content { padding: 0 20px !important; text-align: left !important; }
  
  /* Typography Scaling for Mobile */
  .t-h1 { font-size: clamp(28px, 7vw, 38px) !important; letter-spacing: -1px !important; line-height: 1.15 !important; }
  .t-h2 { font-size: clamp(22px, 6vw, 30px) !important; letter-spacing: -0.5px !important; line-height: 1.2 !important; }
  .t-h3 { font-size: clamp(18px, 5vw, 22px) !important; }
  .t-lead, .slide-sub, p.t-body { font-size: 15px !important; line-height: 1.6 !important; }
  
  /* Stack 2-Column Grids & Card Grids Vertically */
  div[style*="grid-template-columns"], 
  div[style*="minmax"],
  div[style*="repeat("],
  .tiles-grid, 
  #rq-preview-grid,
  .hero-content > div[style*="display:flex"],
  div[style*="display:grid"] {
    grid-template-columns: 1fr !important;
    flex-direction: column !important;
    gap: 20px !important;
  }

  /* Reset Card Grid Column Spans on Mobile */
  .expect-card,
  div[style*="grid-column:span 2"],
  div[style*="grid-column: span 2"] {
    grid-column: span 1 !important;
    grid-column: auto !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 24px 20px !important;
  }
  
  /* Reset Desktop Margins & Borders */
  .tiles-grid { margin-top: 20px !important; padding: 0 20px !important; }
  .tile-card { padding: 24px !important; width: 100% !important; box-sizing: border-box !important; }
  
  /* Fix Featured Cards & Q&A Interactive Component */
  #rq-featured-box { padding: 24px !important; border-radius: 20px !important; }
  #rq-featured-box > div { grid-template-columns: 1fr !important; gap: 24px !important; }
  #rq-card-display { padding: 24px !important; min-height: auto !important; }
  #rq-preview-grid { grid-template-columns: 1fr !important; }
  
  /* Fix Vertical Lines & Dividers Overlapping Text */
  div[style*="border-left"], 
  div[style*="border-right"] {
    border-left: none !important;
    border-right: none !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
  }

  /* Section Spacing */
  section { padding: 60px 0 !important; }
  div[style*="padding:0 32px"], 
  div[style*="padding: 0 32px"],
  div[style*="padding:0 48px"] {
    padding: 0 20px !important;
  }

  /* Buttons on Mobile */
  .btn, .btn-cta, a[class*="btn"] {
    width: 100% !important;
    justify-content: center !important;
    text-align: center !important;
    box-sizing: border-box !important;
    margin-bottom: 8px !important;
  }

  /* Mobile Header & Logo Fix */
  .nav-logo img { height: 45px !important; width: auto !important; }
  .mobile-menu-header { padding: 20px !important; }
  .mobile-menu-logo { height: 40px !important; }
}
"""

# --- Fixed Nav Pill JavaScript ---
FIXED_NAV_PILL_JS = """
  // Fixed Fluid Nav Pill Animation
  const pill = document.querySelector('.nav-pill');
  if (pill) {
    const mainLinks = document.querySelectorAll('.nav-links > li > a:not(.nav-cta), .nav-links .nav-dropdown-toggle, .nav-links .lang-btn');
    let activeLink = document.querySelector('.nav-links > li > a.nav-active:not(.nav-cta), .nav-links > li > a.pill-active:not(.nav-cta)');

    function movePill(el) {
      if (!el) {
        pill.style.opacity = '0';
        return;
      }
      mainLinks.forEach(l => l.classList.remove('pill-active'));
      el.classList.add('pill-active');
      pill.style.opacity = '1';
      pill.style.width = el.offsetWidth + 'px';
      pill.style.transform = `translateX(${el.offsetLeft}px)`;
    }

    if (activeLink) movePill(activeLink);

    // Attach listeners to root <li> items
    document.querySelectorAll('.nav-links > li').forEach(li => {
      const targetLink = li.querySelector('a:not(.no-pill), button.lang-btn') || li.querySelector('a');
      if (!targetLink) return;

      li.addEventListener('mouseenter', () => movePill(targetLink));
      li.addEventListener('mouseleave', () => {
        const currentActive = document.querySelector('.nav-links > li > a.nav-active:not(.nav-cta)');
        movePill(currentActive || null);
      });
    });
  }
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace or update Nav Pill JavaScript
    if 'movePill' in content:
        pattern = r'// Fluid Nav Pill Animation.*?links\.forEach\(link => \{.*?\}\);\s*\}\s*\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, FIXED_NAV_PILL_JS.strip(), content, flags=re.DOTALL)
        else:
            pattern2 = r'// Fixed Fluid Nav Pill Animation.*?\}\);\s*\}\s*\}'
            if re.search(pattern2, content, flags=re.DOTALL):
                content = re.sub(pattern2, FIXED_NAV_PILL_JS.strip(), content, flags=re.DOTALL)

    # 2. Inject or Update Overhaul CSS
    if 'LANGUAGE SWITCHER PREMIUM UI FIXES' in content:
        content = re.sub(r'/\* ─── LANGUAGE SWITCHER PREMIUM UI FIXES ─── \*/.*?</style>', GLOBAL_OVERHAUL_CSS.strip() + '\n</style>', content, flags=re.DOTALL)
    elif 'LANGUAGE SWITCHER & NAV PILL FIXES' in content:
        content = re.sub(r'/\* ─── LANGUAGE SWITCHER & NAV PILL FIXES ─── \*/.*?</style>', GLOBAL_OVERHAUL_CSS.strip() + '\n</style>', content, flags=re.DOTALL)
    elif 'COMPREHENSIVE MOBILE RESPONSIVE OVERHAUL' in content:
        content = re.sub(r'/\* ─── COMPREHENSIVE MOBILE RESPONSIVE OVERHAUL.*? \*/.*?</style>', GLOBAL_OVERHAUL_CSS.strip() + '\n</style>', content, flags=re.DOTALL)
    else:
        content = content.replace('</style>', GLOBAL_OVERHAUL_CSS.strip() + '\n</style>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {os.path.basename(filepath)}")
    else:
        print(f"  CLEAN: {os.path.basename(filepath)}")


def main():
    print("=== Applying Global Nav Pill, Language Dropdown & Mobile UI/UX Overhaul ===")
    html_files = sorted(glob.glob(os.path.join(BASE, "*.html")))
    for filepath in html_files:
        update_file(filepath)
    print("=== Done! ===")

if __name__ == "__main__":
    main()
