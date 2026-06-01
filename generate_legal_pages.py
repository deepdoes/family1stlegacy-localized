import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

# Read master index
with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
    master_content = f.read()

# Extract Header and Footer
nav_end_idx = master_content.find('<!-- HERO SLIDESHOW')
header_part = master_content[:nav_end_idx]

# Inject legal specific CSS into header
legal_css = """
<style>
#legal-page { padding: 140px 0 100px; background: var(--bg); }
.legal-header { max-width: 800px; margin: 0 auto 56px; text-align: center; }
.legal-title { font-family: var(--font-head); font-size: clamp(40px, 5vw, 64px); font-weight: 800; line-height: 1.1; letter-spacing: -2px; color: var(--dark); margin-bottom: 24px; }
.legal-meta { font-size: 14px; color: var(--muted); font-weight: 500; }
.legal-body { max-width: 800px; margin: 0 auto; background: var(--white); padding: 64px 80px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); }
.legal-body p { font-size: 16px; line-height: 1.8; color: var(--muted); margin-bottom: 24px; font-weight: 400; }
.legal-body h2 { font-family: var(--font-head); font-size: 28px; font-weight: 700; color: var(--dark); margin: 48px 0 16px; letter-spacing: -1px; }
.legal-body ul { margin-bottom: 24px; padding-left: 24px; }
.legal-body li { font-size: 16px; line-height: 1.8; color: var(--muted); font-weight: 400; margin-bottom: 8px; }
@media(max-width: 768px) {
  .legal-body { padding: 40px 32px; }
}
</style>
"""
header_part = header_part.replace('</head>', legal_css + '\n</head>')

# For footer, find <!-- CTA BANNER -->
cta_idx = master_content.find('<!-- CTA BANNER ──────────────────────────────────────── -->')
footer_part = master_content[cta_idx:]

pages = [
    {
        "filename": "privacy.html",
        "title": "Privacy Policy",
        "date": "Last Updated: January 2026",
        "content": """
        <p>Family First Legacy ("we", "us", or "our") respects your privacy and is committed to protecting it through our compliance with this Privacy Policy. This policy describes the types of information we may collect from you or that you may provide when you visit the website family1stlegacy.com.</p>
        
        <h2>Information We Collect</h2>
        <p>We collect several types of information from and about users of our Website, including information:</p>
        <ul>
            <li>By which you may be personally identified, such as name, postal address, e-mail address, telephone number ("personal information");</li>
            <li>That is about you but individually does not identify you; and/or</li>
            <li>About your internet connection, the equipment you use to access our Website, and usage details.</li>
        </ul>
        
        <h2>How We Use Your Information</h2>
        <p>We use information that we collect about you or that you provide to us, including any personal information:</p>
        <ul>
            <li>To present our Website and its contents to you.</li>
            <li>To provide you with information, products, or services that you request from us.</li>
            <li>To fulfill any other purpose for which you provide it.</li>
            <li>To carry out our obligations and enforce our rights arising from any contracts entered into between you and us.</li>
            <li>To notify you about changes to our Website or any products or services we offer or provide though it.</li>
        </ul>
        
        <h2>Disclosure of Your Information</h2>
        <p>We may disclose aggregated information about our users, and information that does not identify any individual, without restriction. We do not sell, trade, or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with advance notice.</p>
        
        <h2>Changes to Our Privacy Policy</h2>
        <p>It is our policy to post any changes we make to our privacy policy on this page. If we make material changes to how we treat our users' personal information, we will notify you through a notice on the Website home page.</p>
        
        <h2>Contact Information</h2>
        <p>To ask questions or comment about this privacy policy and our privacy practices, contact us at: info@family1stlegacy.com</p>
        """
    },
    {
        "filename": "terms.html",
        "title": "Terms of Service",
        "date": "Last Updated: January 2026",
        "content": """
        <p>These Terms of Service ("Terms") govern your use of the Family First Legacy website (family1stlegacy.com). By accessing or using our website, you agree to be bound by these Terms. If you disagree with any part of the terms, then you may not access the website.</p>
        
        <h2>1. Services Provided</h2>
        <p>Family First Legacy provides information related to financial services, life insurance, retirement planning, education planning, and estate preservation. We are an independent financial services agency. The information provided on this website does not constitute tax, legal, or professional financial advice.</p>
        
        <h2>2. Use of the Website</h2>
        <p>You may use our website only for lawful purposes and in accordance with these Terms. You agree not to use the website:</p>
        <ul>
            <li>In any way that violates any applicable federal, state, local, or international law or regulation.</li>
            <li>For the purpose of exploiting, harming, or attempting to exploit or harm minors in any way by exposing them to inappropriate content, asking for personally identifiable information, or otherwise.</li>
            <li>To transmit, or procure the sending of, any advertising or promotional material, including any "junk mail", "chain letter", "spam", or any other similar solicitation.</li>
        </ul>
        
        <h2>3. Intellectual Property Rights</h2>
        <p>The website and its entire contents, features, and functionality (including but not limited to all information, software, text, displays, images, video, and audio, and the design, selection, and arrangement thereof) are owned by Family First Legacy, its licensors, or other providers of such material and are protected by United States and international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.</p>
        
        <h2>4. Disclaimer of Warranties</h2>
        <p>Your use of the website, its content, and any services or items obtained through the website is at your own risk. The website, its content, and any services or items obtained through the website are provided on an "as is" and "as available" basis, without any warranties of any kind, either express or implied.</p>
        
        <h2>5. Limitation on Liability</h2>
        <p>In no event will Family First Legacy, its affiliates, or their licensors, service providers, employees, agents, officers, or directors be liable for damages of any kind, under any legal theory, arising out of or in connection with your use, or inability to use, the website, any websites linked to it, any content on the website or such other websites, including any direct, indirect, special, incidental, consequential, or punitive damages.</p>
        
        <h2>6. Governing Law</h2>
        <p>All matters relating to the Website and these Terms, and any dispute or claim arising therefrom or related thereto (in each case, including non-contractual disputes or claims), shall be governed by and construed in accordance with the internal laws of the State of Texas without giving effect to any choice or conflict of law provision or rule.</p>
        """
    }
]

for page in pages:
    print(f"Generating {page['filename']}...")
    
    html = f'''
    <section id="legal-page">
      <div class="container">
        <div class="legal-header" data-reveal>
          <h1 class="legal-title">{page['title']}</h1>
          <div class="legal-meta">{page['date']}</div>
        </div>
        
        <div class="legal-body" data-reveal data-delay="1">
          {page['content']}
        </div>
      </div>
    </section>
    '''
    
    full_html = header_part + html + footer_part
    
    # Fix internal links
    full_html = re.sub(r'href="#about"', 'href="index.html#about"', full_html)
    full_html = re.sub(r'href="#services"', 'href="index.html#services"', full_html)
    full_html = re.sub(r'href="#process"', 'href="index.html#process"', full_html)
    full_html = re.sub(r'href="#opportunity"', 'href="index.html#opportunity"', full_html)
    full_html = re.sub(r'href="#reviews"', 'href="index.html#reviews"', full_html)
    full_html = re.sub(r'href="#faq"', 'href="index.html#faq"', full_html)
    full_html = re.sub(r'href="#blog"', 'href="index.html#blog"', full_html)
    
    with open(os.path.join(base_dir, page['filename']), 'w', encoding='utf-8') as f:
        f.write(full_html)

print("Legal pages generation complete.")
