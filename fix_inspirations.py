import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

intro_texts = {
    "es": "Como se puede apreciar en el pasaje extraído del mural, la causa y su efecto kármico están descritos originalmente en vietnamita y con una breve traducción al inglés. A continuación, te ofrecemos su traducción detallada en los distintos idiomas:",
    "en": "As can be seen in the passage extracted from the mural, the cause and its karmic effect are originally described in Vietnamese with a brief English translation. Below, we offer the detailed translation in different languages:",
    "it": "Come si può vedere nel passaggio estratto dal murale, la causa e il suo effetto karmico sono originariamente descritti in vietnamita con una breve traduzione in inglese. Di seguito offriamo la traduzione dettagliata in diverse lingue:"
}

def get_trans(text_es, lang_code, g_code):
    try:
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

# We fill intro_texts via API dynamically or manually
for code, g_code in lang_map.items():
    if code not in intro_texts:
        intro_texts[code] = get_trans(intro_texts['es'], code, g_code)

def translate_analysis(es_text):
    results = {}
    for code, g_code in lang_map.items():
        results[code] = get_trans(es_text, code, g_code)
    return results

# Translations of the cause/effect from the mural per chapter:
mural_trans = {
    "07_manos_del_mal": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Usar las manos para actos malvados.<br>Efecto: Renace como una especie sin manos.",
                         "en": "<strong>Recreated Translation:</strong><br>Cause: Using hands to do evil things.<br>Effect: Brings rebirth as species without hands."},
    "08_pedestal_soberbia": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser arrogante e irrespetuoso con los demás.<br>Efecto: Trae bajo estatus social.",
                             "en": "<strong>Recreated Translation:</strong><br>Cause: Being arrogant and disrespectful towards others.<br>Effect: Brings low social status."},
    "09_frio_egoismo": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser tacaño y no ayudar en la vida anterior.<br>Efecto: Renace como un pobre abandonado.",
                        "en": "<strong>Recreated Translation:</strong><br>Cause: Being stingy and unhelpful in the previous life.<br>Effect: Brings rebirth as a poor and neglected."},
    "10_infierno_sombras": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Ser un ladrón y asesino en la vida anterior.<br>Efecto: Trae renacimiento en el infierno y sufrimiento por fuego y cuchillos.",
                            "en": "<strong>Recreated Translation:</strong><br>Cause: Being a thief and murderer in the previous life.<br>Effect: Brings rebirth into hell and suffering from fire and knives."},
    "11_mirada_desprecio": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Mirar a los demás con desprecio.<br>Efecto: Trae enfermedades graves y soledad.",
                            "en": "<strong>Recreated Translation:</strong><br>Cause: Looking down on others.<br>Effect: Brings severe disease and loneliness."},
    "12_peso_injusticia": {"es": "<strong>Traducción Recreada:</strong><br>Causa: Tratar mal a los empleados.<br>Efecto: Conduce a un rápido final de las bendiciones y a la pobreza.",
                           "en": "<strong>Recreated Translation:</strong><br>Cause: Treating employees poorly.<br>Effect: Brings a quick end to blessing and poverty."}
}

for chap_k, d in mural_trans.items():
    es_t = d["es"]
    for code, g_code in lang_map.items():
        if code not in d:
             d[code] = get_trans(es_t, code, g_code)

chapters = ["07_manos_del_mal", "08_pedestal_soberbia", "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"]

common_titles = {
    "es": "La Inspiración Original", "en": "The Original Inspiration", "it": "L'Ispirazione Originale", 
    "zh": "最初的灵感", "ar": "الإلهام الأصلي", "ru": "Оригинальное вдохновение", 
    "de": "Die Ursprüngliche Inspiration", "fr": "L'Inspiration Originale", 
    "ja": "元のインスピレーション", "pt": "A Inspiração Original"
}

common_descs = {
    "es": "La historia que hemos generado para este capítulo está inspirada por este pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía original.",
}
for code, g_code in lang_map.items():
    common_descs[code] = get_trans(common_descs['es'], code, g_code)
common_descs["en"] = get_trans(common_descs['es'], "en", "en")


def process_chapter(chap):
    filepath = f"{chap}/web/index.html"
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the entire original-inspiration block
    oi_match = re.search(r'<div class="original-inspiration[^>]*>([\s\S]*?)<div class="translation-box"[^>]*>([\s\S]*?)</div>\s*</div>', content, re.IGNORECASE)
    if not oi_match:
        print(f"Could not find original-inspiration block in {chap}!")
        return
    
    # We will completely rewrite original-inspiration!
    # But we need the existing Vietnamese text and Spanish/English Analysis if any.
    vietnamese_match = re.search(r'<p[^>]*>(\s*<strong>🇻🇳 Tiếng Việt:</strong>[\s\S]*?)</p>', content)
    vietnamese_html = ""
    if vietnamese_match:
        vietnamese_html = f'<p style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;">{vietnamese_match.group(1)}</p>'

    an_es_match = re.search(r'<p class="es"([^>]*)><strong>Análisis:</strong>(.*?)</p>', content, re.DOTALL)
    es_an_text = an_es_match.group(2).strip() if an_es_match else "Un análisis de las causas representadas."
    
    an_trans = translate_analysis(f"<strong>Análisis:</strong> {es_an_text}")
    
    an_en_match = re.search(r'<p class="en".*?>(.*?)</p>', content, re.DOTALL)
    en_an_html = ""
    if an_en_match:
        # Check if it has 'Analysis:'
        if "Analysis:" in an_en_match.group(1):
            en_an_html = f'<p class="en" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{an_en_match.group(1)}</p>'

    # construct the new block
    all_titles = "".join([f'<h3 class="{k}" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: \'Cinzel\', serif;">{v}</h3>\n' for k,v in common_titles.items()])
    all_descs = "".join([f'<p class="{k}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">{v}</p>\n' for k,v in common_descs.items()])
    
    intros = "".join([f'<p class="{k}" style="color: #bbb; margin-bottom: 1.5rem; font-style: italic;">{v}</p>\n' for k,v in intro_texts.items()])
    m_trans = "".join([f'<p class="{k}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197, 160, 89, 0.1); padding: 1rem; border-left: 3px solid var(--gold);">{v}</p>\n' for k,v in mural_trans[chap].items()])
    
    an_es_html = f'<p class="es" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;"><strong>Análisis:</strong> {es_an_text}</p>\n'
    if not en_an_html:
        en_an_html = f'<p class="en" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{get_trans("<strong>Análisis:</strong> "+es_an_text, "en", "en")}</p>\n'
    
    an_others_html = "".join([f'<p class="{k}" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{v}</p>\n' for k,v in an_trans.items()])

    replacement = f"""
            <div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197, 160, 89, 0.3);">
                {all_titles}
                {all_descs}
                <center>
                    <img src="assets/pasaje_original.jpg" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                <div class="translation-box" style="background: rgba(0, 0, 0, 0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">
                    {intros}
                    {vietnamese_html}
                    {m_trans}
                    <hr style="border-color: rgba(197, 160, 89, 0.2); margin-block: 2rem;">
                    {an_es_html}
                    {en_an_html}
                    {an_others_html}
                </div>
            </div>
    """

    # Do a big sub
    new_content = re.sub(r'<div class="original-inspiration[^>]*>([\s\S]*?)<div class="translation-box"[^>]*>([\s\S]*?)</div>\s*</div>', replacement.strip(), content, flags=re.IGNORECASE)

    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {chap} successfully.")
    else:
        print(f"Failed to match block in {chap}.")

for chap in chapters:
    process_chapter(chap)
