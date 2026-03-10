import os
import shutil
import json
import re
from PIL import Image
from deep_translator import GoogleTranslator

new_chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]
romans = {"13": "XIII", "14": "XIV", "15": "XV", "16": "XVI", "17": "XVII", "18": "XVIII"}

boxes = {
    "13_amor_y_respeto": (55, 105, 385, 235),
    "14_peso_deudores": (55, 240, 385, 365),
    "15_desperdicio_y_escasez": (55, 370, 385, 490),
    "16_adiccion_y_ceguera": (55, 495, 385, 620),
    "17_orfandad_filial": (55, 625, 385, 755),
    "18_pereza_laboral": (55, 760, 385, 890),
}

# 1. Crop images
img = Image.open("imagenes_originales/foto_13_18.jpg")
for ch, box in boxes.items():
    if not os.path.exists(ch):
        shutil.copytree("12_peso_injusticia", ch)
    # the crop
    crp = img.crop(box)
    tar = f"{ch}/web/assets/pasaje_original.jpg"
    crp.save(tar, quality=95)

# 2. Inject
with open("chapters_13_18_data.json", "r", encoding='utf8') as f:
    cdata = json.load(f)

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

for ch in new_chapters:
    fpath = f"{ch}/web/index.html"
    with open(fpath, "r", encoding='utf8') as f:
        html = f.read()

    data = cdata[ch]
    ch_num = ch.split("_")[0]
    roman = romans[ch_num]

    # Replacing CHAPTER titles (like CAPÍTULO XII -> CAPÍTULO XIII)
    # The header has stuff like <p class="chapter-num"><span class="es">CAPÍTULO 12</span>...</p>
    # Actually, let's just replace all instances of matching numbers/romans
    html = html.replace('12</', f'{int(ch_num)}</')
    html = html.replace('XII</', f'{roman}</')
    html = html.replace('12<', f'{int(ch_num)}<')
    html = html.replace('XII<', f'{roman}<')

    # Replace <h1 class="chapter-title">
    t_es = data["title"]["es"]
    html = re.sub(r'(<h1 class="chapter-title">)[\s\S]*?(</h1>)', lambda m: m.group(1) + ''.join([f'<span class="{l}">{data["title"][l]}</span>' for l in langs]) + m.group(2), html)
    
    # Replace `<div class="story-container"> ...` up to `<div class="story-block` (Wait, story container has the main story block)
    # Let's find `<div class="story-block fade-in">` -> the first one is the main story. The second is the Parable.
    
    main_story_html = f"""<div class="story-block fade-in">
                <p class="es"><span class="drop-cap">{data["story"]["es"][0]}</span>{data["story"]["es"][1:]}</p>
"""
    for l in langs[1:]:
        main_story_html += f'                <p class="{l}"><span class="drop-cap">{data["story"][l][0]}</span>{data["story"][l][1:]}</p>\n'
    main_story_html += "            </div>"

    # We need to carefully replace the First story-block
    # Using re.sub with count=1
    html = re.sub(r'<div class="story-block fade-in">.*?</div>', main_story_html, html, count=1, flags=re.DOTALL)

    # Parable replace (the second story-block with different style)
    para_html = f"""<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">
"""
    for l in langs:
        para_html += f'                <h3 class="{l}" style="color: var(--gold); text-align: center; font-family: \'Cinzel\', serif; margin-bottom: 2rem;">{data["parable_title"][l]}</h3>\n'
    for l in langs:
        para_html += f'                <p class="{l}" style="font-style: italic; color: #ddd; line-height: 1.8; text-align: justify; margin-bottom: 1.5rem;">{data["parable_text"][l]}</p>\n'
    para_html += "            </div>"
    
    # regex for the second story-block
    # Wait, the parable is usually styled with `margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;`
    html = re.sub(r'<div class="story-block fade-in" style="margin-top: 3rem; margin-bottom: 2rem; padding: 0 1rem;">.*?</div>', para_html, html, flags=re.DOTALL)

    # Inspiration translation
    insp_html = f"""
                    <p style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: 'EB Garamond', serif; font-size: 1.2rem;"><strong>🇻🇳 Tiếng Việt:</strong><br>{data["vn"]}</p>
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English Translation:</strong><br>{data["en_t"]}</p>
"""
    for l in langs:
        insp_html += f'                    <p class="{l}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197, 160, 89, 0.1); padding: 1rem; border-left: 3px solid var(--gold);">{data["es_t"][l]}</p>\n'
    insp_html += '                    <hr style="border-color: rgba(197, 160, 89, 0.2); margin-block: 2rem;">\n'
    for l in langs:
        insp_html += f'                    <p class="{l}" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{data["analysis"][l]}</p>\n'

    # Re-inject the interior of translation-box
    # First we need to isolate the `translation-box` content starting from `<p style="color: #fff; font-style: italic;...`
    # Replace anything between the intro texts and `</div>` of the translation box
    
    html = re.sub(r'(<p style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;">[\s\S]*?)</div>\s*</div>', insp_html + '\n                </div>\n            </div>', html)

    # Moral text
    # In 12 it was: <div class="moral fade-in"> <h2 ...> <span class="es">La balanza nunca olvida.</span> ... </h2>
    
    # We will just write a default moral like "El universo siempre responde." and translate it.
    def get_trans(text_es, lang_code, g_code):
        try:
            if lang_code == "en": g_code = "en"
            return GoogleTranslator(source='es', target=g_code).translate(text_es)
        except Exception as e:
            return text_es
    lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}
    moral_es = "El universo siempre responde."
    moral_dict = {"es": moral_es, "en": get_trans(moral_es, "en", "en")}
    for code, g_code in lang_map.items():
        moral_dict[code] = get_trans(moral_es, code, g_code)
        
    html = re.sub(r'(<div class="moral fade-in">\s*<h2 style="[^"]*">)[\s\S]*?(</h2>)', lambda m: m.group(1) + ''.join([f'<span class="{l}">{moral_dict[l]}</span>' for l in langs]) + m.group(2), html)


    with open(fpath, "w", encoding='utf8') as f:
        f.write(html)
    print(f"Updated {fpath}")

print("Done part 2!")
