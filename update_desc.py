import os
import re
from deep_translator import GoogleTranslator

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

# New correct Spanish description
desc_es = "La historia que hemos relatado en este capítulo está inspirada por el pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la imagen."

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en":
            return "The story we have related in this chapter is inspired by the passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the image."
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

new_descs = {"es": desc_es}
for code, g_code in lang_map.items():
    new_descs[code] = get_trans(desc_es, code, g_code)
new_descs["en"] = get_trans(desc_es, "en", "en")

# We want to replace EVERY <p class="lang" style="...">... old text ...</p> inside original-inspiration block
# Wait, the structure in the HTML is predictable. We can just recreate the title + descs HTML
# and replace the block between `<!-- The title and descs block -->`
# But we don't have markers. We can parse `<h3` up to `<center>` in the original-inspiration div.
# Let's do regex replace for each language paragraph inside `original-inspiration`.
# Actually, it's easier to find `<h3 class="pt"`... and replace everything until `<center>`.

common_titles = {
    "es": "La Inspiración Original", "en": "The Original Inspiration", "it": "L'Ispirazione Originale", 
    "zh": "最初的灵感", "ar": "الإلهام الأصلي", "ru": "Оригинальное вдохновение", 
    "de": "Die Ursprüngliche Inspiration", "fr": "L'Inspiration Originale", 
    "ja": "元のインスピレーション", "pt": "A Inspiração Original"
}
# some titles might be translated slightly differently (e.g. Italian in chaps 1-6 was L'ispirazione originale),
# so let's just replace all <p> above <center> ignoring what was there!

replacement_html = "".join([f'<h3 class="{k}" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: \'Cinzel\', serif;">{v}</h3>\n' for k,v in common_titles.items()])
replacement_html += "".join([f'<p class="{k}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">{v}</p>\n' for k,v in new_descs.items()])

chapters = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d{2}_', d) and "00" not in d]

for chap in chapters:
    filepath = f"{chap}/web/index.html"
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the block inside original inspiration before <center>
    # It starts after <div class="original-inspiration ..."> and ends before <center>
    pattern = re.compile(r'(<div class="original-inspiration fade-in"[^>]*>)\s*(<h3 class="es"[\s\S]*?)(<center>)')
    
    if pattern.search(content):
        content = pattern.sub(r'\1\n' + replacement_html + r'\3', content)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Updated description in {chap}")
    else:
        print(f"Pattern not found in {chap}")
