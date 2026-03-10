import os
import re
from deep_translator import GoogleTranslator

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

def get_trans(text_es, lang_code, g_code):
    try:
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

def generate_spans(es_text, en_text):
    results = {"es": es_text, "en": en_text}
    for code, g_code in lang_map.items():
        results[code] = get_trans(es_text, code, g_code)
    
    html = "\n".join([f'                    <span class="{k}">{v}</span>' for k,v in results.items()])
    return html

chapters = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^(0[0-9]|1[0-2])_', d)]

for chap in sorted(chapters):
    filepath = os.path.join(chap, "web", "index.html")
    if not os.path.exists(filepath): continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find hero-content block
    m_content = re.search(r'<div class="hero-content">([\s\S]*?)</div>\s*</section>', content)
    if not m_content:
        continue
    
    hero_inner = m_content.group(1)
    
    # Exract Chapter Num
    m_num = re.search(r'<div class="chapter-num">\s*<span class="es">(.*?)</span>\s*<span class="en">(.*?)</span>\s*</div>', hero_inner)
    # Extract Chapter Title
    m_title = re.search(r'<h1 class="chapter-title">\s*<span class="es">(.*?)</span>\s*<span class="en">(.*?)</span>\s*</h1>', hero_inner)
    # Extract Subtitle
    m_sub = re.search(r'<p class="subtitle">\s*<span class="es">(.*?)</span>\s*<span class="en">(.*?)</span>\s*</p>', hero_inner)

    # We only process if it ONLY has es and en
    # Let's check if it already has <span class="it">
    if '<span class="it">' in hero_inner:
        print(f"Already updated {chap}")
        continue
    
    if m_num and m_title:
        num_html = f'''<div class="chapter-num">
{generate_spans(m_num.group(1), m_num.group(2))}
                </div>'''
        
        title_html = f'''<h1 class="chapter-title">
{generate_spans(m_title.group(1), m_title.group(2))}
                </h1>'''
        
        sub_html = ""
        if m_sub:
            sub_html = f'''<p class="subtitle">
{generate_spans(m_sub.group(1), m_sub.group(2))}
                </p>'''
        
        new_hero_inner = f"""
                {num_html}
                {title_html}
                {sub_html}
            """
        new_content = content[:m_content.start(1)] + new_hero_inner + content[m_content.end(1):]
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {chap} successfully.")
    else:
        print(f"Could not parse hero section in {chap}")
