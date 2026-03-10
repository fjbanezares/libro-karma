import os
import re
from deep_translator import GoogleTranslator

# We want these target languages for the span/p classes:
# "it", "zh-CN", "ar", "ru", "de", "fr", "ja", "pt"
lang_map = {
    "it": "it",
    "zh": "zh-CN",
    "ar": "ar",
    "ru": "ru",
    "de": "de",
    "fr": "fr",
    "ja": "ja",
    "pt": "pt"
}

def translate_es_to_others(es_text):
    es_text = es_text.strip()
    if not es_text:
        return {}
    results = {}
    for code, g_code in lang_map.items():
        try:
            translation = GoogleTranslator(source='es', target=g_code).translate(es_text)
            results[code] = translation
        except Exception as e:
            print(f"Error translating to {code}: {e}")
            results[code] = es_text
    return results

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r') as f:
        content = f.read()

    # We want to find cases of <span class="es">TEXT</span> and <p class="es">TEXT</p>
    # and if they ONLY have an <en> counterpart right after, we append the others.
    # WAIT: index.html has a lot of spans. Chapters have spans and ps.

    # 1. Process spans
    # Regex for finding consecutive ES and EN spans.
    span_pattern = re.compile(r'<span class="es">(.*?)</span>\s*<span class="en">.*?</span>', re.DOTALL)
    
    def span_replacer(match):
        es_text = match.group(1)
        full_match = match.group(0)
        # If it's already translated (menu/sidebar), skip. We know Sidebar is translated entirely already because we wrote 10 languages explicitly. 
        # But this regex will catch them if they only have es/en. If they have all 10, the regex only matches the es/en part, which is dangerous!
        # Let's ensure there isn't a <span class="it"> right after.
        return full_match

    # A better approach: we only translate specific structure.
    # e.g., the story blocks in chapters: <p class="es">...</p>\n<p class="en">...</p>
    p_pattern = re.compile(r'(<p class="es">(.*?)</p>\s*<p class="en">.*?</p>)(\s*</div>)', re.DOTALL)

    def p_replacer(match):
        full_match = match.group(1)
        es_text = match.group(2)
        end_div = match.group(3)

        # Check if already translated
        if '<p class="it">' in full_match:
            return match.group(0)

        translations = translate_es_to_others(es_text)
        new_blocks = ""
        for code, text in translations.items():
            new_blocks += f'\n                <p class="{code}">{text}</p>'
        
        return full_match + new_blocks + end_div

    new_content = p_pattern.sub(p_replacer, content)

    # 2. Process morals: <span class="es">...</span>\n<span class="en">...</span> inside div class="moral"
    moral_pattern = re.compile(r'(<div class="moral.*?">.*?<span class="es">(.*?)</span>\s*<span class="en">.*?</span>)(\s*</div>)', re.DOTALL)

    def moral_replacer(match):
        full_match = match.group(1)
        es_text = match.group(2)
        end_div = match.group(3)

        if '<span class="it">' in full_match:
             return match.group(0)

        translations = translate_es_to_others(es_text)
        new_blocks = ""
        for code, text in translations.items():
            new_blocks += f'\n                <span class="{code}">{text}</span>'
        
        return full_match + new_blocks + end_div

    new_content = moral_pattern.sub(moral_replacer, new_content)

    # 3. Process index.html chapter titles/subtitles inside cards
    # <span class="es">Capítulo 0</span> ...
    # It's better to just translate the chapter descriptions in index.html specifically.
    
    with open(filepath, 'w') as f:
        f.write(new_content)

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]

for c in chapters:
    filepath = f"{c}/web/index.html"
    if os.path.exists(filepath):
        process_file(filepath)

print("Translation of chapters finished.")
