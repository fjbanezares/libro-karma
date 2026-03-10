import os
import re
import time
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}
langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        for i in range(5):
            try:
                return GoogleTranslator(source='es', target=g_code).translate(text_es)
            except Exception as e:
                print(f"Retrying {lang_code}... attempt {i+1} error: {e}")
                time.sleep(3)
        return text_es
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

def trans_dict(text_es):
    d = {"es": text_es, "en": get_trans(text_es, "en", "en")}
    for code, g_code in lang_map.items():
        d[code] = get_trans(text_es, code, g_code)
    return d

chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]

morals_es = {
    "13_amor_y_respeto": "Quien siembra consideración, cosecha una belleza inquebrantable.",
    "14_peso_deudores": "Las deudas del alma ahogan más que las deudas del bolsillo.",
    "15_desperdicio_y_escasez": "La abundancia jamás perdona a quien desprecia el pan.",
    "16_adiccion_y_ceguera": "Apagar tu luz propia hoy, garantiza nacer en la penumbra mañana.",
    "17_orfandad_filial": "Rechazar a quien te dio la vida desgarra los hilos de tu propio destino.",
    "18_pereza_laboral": "El tiempo robado a la labor digna oxida irremediablemente el porvenir."
}

print("Translating specific morals...")
translated_morals = {}
for ch in chapters:
    translated_morals[ch] = trans_dict(morals_es[ch])

for ch in chapters:
    fpath = f"{ch}/web/index.html"
    if not os.path.exists(fpath): continue

    with open(fpath, "r", encoding='utf8') as f:
        html = f.read()

    # 1. Update the Moral Block
    moral_html = '<div class="moral fade-in">\n'
    for l in langs:
        moral_html += f'                <span class="{l}">{translated_morals[ch][l]}</span>\n'
    moral_html += '            </div>'

    html = re.sub(r'<div class="moral fade-in">[\s\S]*?</div>', moral_html, html)

    # 2. Extract final-art if it exists at the bottom
    art_block_match = re.search(r'(<div class="final-art fade-in".*?</div>)\s*', html, flags=re.DOTALL)
    art_html = ""
    if art_block_match:
        art_html = art_block_match.group(1)
        html = html.replace(art_block_match.group(0), '') # Remove it from current place
    else:
        # Recreate if it got lost
        art_html = """
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/art.jpg" alt="Obra de Arte Karma" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>
        """
        
    # We must insert art_html JUST BEFORE the moral_html
    # meaning replace '<div class="moral fade-in">' with art_html + '\n<div class="moral fade-in">'
    if 'class="final-art' not in html:  # prevents double injection if something went wrong
        html = html.replace('<div class="moral fade-in">', art_html + '\n\n            <div class="moral fade-in">')

    with open(fpath, "w", encoding='utf8') as f:
        f.write(html)
    print(f"Updated moral and art order for {fpath}")

print("Refactor completed.")
