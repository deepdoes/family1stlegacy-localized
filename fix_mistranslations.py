import os
import re

base_dir = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

# Files list
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

sw_replacements = {
    # Headings
    "Mapenzi dhidi ya Amini": "Wosia dhidi ya Dhamana",
    "Mapenzi dhidi ya<br/><em>Amini.</em>": "Wosia dhidi ya<br/><em>Dhamana.</em>",
    "Mapenzi dhidi ya<br><em>Amini.</em>": "Wosia dhidi ya<br><em>Dhamana.</em>",
    "Wosia dhidi ya Uaminifu": "Wosia dhidi ya Dhamana",
    "Wosia dhidi ya uaminifu": "Wosia dhidi ya Dhamana",
    
    # Testimonials and quotes
    "uaminifu ambao utaacha urithi": "mfuko wa dhamana (trust) utakaowacha urithi",
    "kuamini kwamba mapenzi hayo kuacha urithi": "mfuko wa dhamana (trust) utakaowacha urithi",
    "huduma ya bima ya maisha yote na kuamini kwamba mapenzi hayo kuacha urithi": "sera ya bima ya maisha yote na mfuko wa dhamana (trust) utakaowacha urithi",
    "huduma ya bima ya maisha yote na uaminifu ambao utaacha urithi": "sera ya bima ya maisha yote na mfuko wa dhamana (trust) utakaowacha urithi",
    "Bibi yangu alikufa bila chochote. Niliahidi watoto wangu wangerithi kitu. Family First Legacy ilinisaidia kuweka sera nzima ya maisha na kuamini kwamba mapenzi hayo kuacha urithi kwa vizazi vitatu.": 
        "Bibi yangu alifariki bila kuacha chochote. Niliwaahidi watoto wangu kwamba wangerithi kitu. Family First Legacy ilinisaidia kuanzisha sera ya bima ya maisha yote na mfuko wa dhamana (trust) utakaowacha urithi kwa vizazi vitatu.",
    "Bibi yangu alikufa bila kitu. Niliahidi watoto wangu wangerithi kitu. Family First Legacy ilinisaidia kuweka sera nzima ya maisha na uaminifu ambao utaacha urithi kwa vizazi vitatu.": 
        "Bibi yangu alifariki bila kuacha chochote. Niliwaahidi watoto wangu kwamba wangerithi kitu. Family First Legacy ilinisaidia kuanzisha sera ya bima ya maisha yote na mfuko wa dhamana (trust) utakaowacha urithi kwa vizazi vitatu.",
    
    # Probate and Court concepts
    "kama uaminifu": "kama vile trust/dhamana",
    "hupita majaribio": "huepuka mchakato wa mirathi",
    "bypasses probate": "huepuka mchakato wa mirathi (probate)",
    "unapitia mahakama ya majaribio": "unapitia mchakato wa usimamizi wa mirathi",
    "mahakama ya majaribio": "mahakama ya mirathi",
    "mchakato mrefu, wa umma na wa gharama kubwa wa kisheria unaoitwa probate": "mchakato mrefu, wa umma na wa gharama kubwa wa kisheria unaoitwa usimamizi wa mirathi (probate)",
    "hupita muda wa majaribio": "huepuka mchakato wa mirathi",
    "muda wa majaribio": "mchakato wa mirathi",
}

rw_replacements = {
    # Headings
    "Will vs. Kwizera": "Testama vs. Trust",
    "Ubushake vs. Kwizera": "Testama vs. Trust",
    "Ubushake vs. Kwizera.": "Testama vs. Trust.",
    "Will vs. Kwizera.": "Testama vs. Trust.",
    "Will vs.<br/><em>Kwizera.</em>": "Testama vs.<br/><em>Trust.</em>",
    "Will vs.<br><em>Kwizera.</em>": "Testama vs.<br><em>Trust.</em>",
    "Will vs.<br/><em>Kwizera</em>": "Testama vs.<br/><em>Trust</em>",
    "Will vs.<br><em>Kwizera</em>": "Testama vs.<br><em>Trust</em>",
    "Ubushake vs.<br/><em>Kwizera.</em>": "Testama vs.<br/><em>Trust.</em>",
    "Ubushake vs.<br><em>Kwizera.</em>": "Testama vs.<br><em>Trust.</em>",
    
    # Testimonials and quotes
    "no kwizera bizashoboka usige umurage": "hamwe n'ikigega cy'umurage (trust) kizagira uruhare mu gusiga umurage",
    "no kwizera bizashoboka": "hamwe n'ikigega cy'umurage (trust) kizagira uruhare mu",
    "n'icyizere kizasigira": "n'ikigega cy'umurage (trust) kizasigira",
    "Nyogokuru yapfuye ntacyo. Nasezeranije ko abana banjye bazaragwa ikintu. Family First Legacy yamfashije gushyiraho politiki yubuzima bwose no kwizera bizashoboka usige umurage ibisekuru bitatu.":
        "Nyogokuru yapfuye ntacyo. Nasezeranije ko abana banjye bazaragwa ikintu. Family First Legacy yamfashije gushyiraho politiki y'ubuzima bwose hamwe n'ikigega cy'umurage (trust) kizagira uruhare mu gusiga umurage ku bisekuru bitatu.",
    "Nyogokuru yapfuye nta kintu na kimwe. Nasezeranije ko abana banjye bazaragwa ikintu. Family First Legacy yamfashije gushyiraho politiki y'ubuzima bwose n'icyizere kizasigira umurage ibisekuruza bitatu.":
        "Nyogokuru yapfuye nta kintu na kimwe. Nasezeranije ko abana banjye bazaragwa ikintu. Family First Legacy yamfashije gushyiraho politiki y'ubuzima bwose hamwe n'ikigega cy'umurage (trust) kizasigira umurage ibisekuruza bitatu.",
    
    # Will and Trust concepts
    "Ubushake buracyanyura": "Testama iracyanyura",
    "ubushake bwonyine": "testama yonyine",
    "ufite ubushake gusa": "ufite testama gusa",
    "ubushake bwa nyuma": "testama",
    "gutegura ubushake": "gutegura testama",
    "kugumya ubushake": "kugumya testama",
    "n'ubushake bwawe": "na testama yawe",
    "hamwe n'ubushake": "hamwe na testama",
    "gutegura ubushake bwa nyuma nisezerano": "gutegura testama n'izungura",
    "Ishaka rivuga": "Testama ivuga",
    
    # Trust translation fixes
    "Icyizere cyirengagiza igeragezwa": "Trust yirinda ikibazo cy'izungura (probate)",
    "Icyizere cyirengagiza": "Trust yirinda",
    "Icyizere cyubatswe neza": "Trust yubatswe neza",
    "nk'icyizere": "nka trust",
    "n'icyizere": "na trust",
    "mwizina ryicyizere": "mw'izina rya trust",
    "Iyo uremye Icyizere": "Iyo uremye Trust",
    "Kuberako Ikizere": "Kuberako Trust",
    "kandi Ikizere ntigipfa": "kandi Trust ntigipfa",
    "Igisubizo: Icyizere kizima": "Igisubizo: Revocable Living Trust",
    "Icyizere nikigo": "Trust ni ikigo",
    "Icyizere kizima cyizerwa": "Revocable Living Trust",
    
    # Probate concepts
    "urukiko rwagateganyo": "urukiko rw'izungura (probate)",
    "igeragezwa rwose": "probate rwose",
    "igeragezwa": "probate",
    "kunyura mu igeragezwa": "kunyura mu rubanza rw'izungura (probate)",
    "bypasses probate": "yirinda probate",
    "bypass probate": "yirinda probate",
    
    # Miscellanous
    "Learn More": "Wige byinshi",
    "Timebomb.": "Timebomb. (Ikibazo gikomeye.)",
}

pt_replacements = {
    "A solução: The Revogable Living Trust": "A solução: O Trust Revogável em Vida",
}

# Privacy page contact translations
privacy_contact_original = "To ask questions or comment about this privacy policy and our privacy practices, contact us at: info@family1stlegacy.com"
privacy_contact_translations = {
    "es": "Para hacer preguntas o comentar sobre esta política de privacidad y nuestras prácticas de privacidad, contáctenos en: info@family1stlegacy.com",
    "pt": "Para fazer perguntas ou comentar sobre esta política de privacidade e nossas práticas de privacidade, entre em contato conosco pelo e-mail: info@family1stlegacy.com",
    "sw": "Ili kuuliza maswali au kutoa maoni kuhusu sera hii ya faragha na mazoea yetu ya faragha, wasiliana nasi kwa: info@family1stlegacy.com",
    "rw": "Kugira ngo ubaze ibibazo cyangwa utange ibitekerezo kuri iyi politiki y'ibanga n'imikorere yacu y'ibanga, twandikire kuri: info@family1stlegacy.com"
}

def process_file(filepath, replacements, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    count = 0
    
    # Apply standard replacements
    for src, dest in replacements.items():
        if src in content:
            content = content.replace(src, dest)
            modified = True
            count += 1
            
    # Apply privacy contact translation if it is the privacy page
    if "privacy_" in filepath:
        if privacy_contact_original in content:
            content = content.replace(privacy_contact_original, privacy_contact_translations[lang])
            modified = True
            count += 1
            print(f"  Translated privacy contact details for {lang}")
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Modified {os.path.basename(filepath)} with {count} replacements.")
    return modified

def main():
    print("Starting translation cleanup and accuracy correction...")
    
    modified_files = 0
    for filename in files:
        base_name = filename.rsplit('.', 1)[0]
        
        # 1. Swahili
        sw_path = os.path.join(base_dir, f"{base_name}_sw.html")
        if os.path.exists(sw_path):
            if process_file(sw_path, sw_replacements, "sw"):
                modified_files += 1
                
        # 2. Kinyarwanda
        rw_path = os.path.join(base_dir, f"{base_name}_rw.html")
        if os.path.exists(rw_path):
            if process_file(rw_path, rw_replacements, "rw"):
                modified_files += 1
                
        # 3. Portuguese
        pt_path = os.path.join(base_dir, f"{base_name}_pt.html")
        if os.path.exists(pt_path):
            if process_file(pt_path, pt_replacements, "pt"):
                modified_files += 1
                
        # 4. Spanish (Privacy contact check)
        es_path = os.path.join(base_dir, f"{base_name}_es.html")
        if os.path.exists(es_path):
            if process_file(es_path, {}, "es"):
                modified_files += 1
                
    print(f"\nCompleted! Corrected terms and English leaks in {modified_files} files.")

if __name__ == "__main__":
    main()
