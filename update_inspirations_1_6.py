import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

common_titles = {
    "es": "La Inspiración Original", "en": "The Original Inspiration"
}
common_descs = {
    "es": "La historia que hemos relatado en este capítulo está inspirada por el pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía adjunta.",
    "en": "The story we have related in this chapter is inspired by the passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the attached photograph."
}

intro_texts = {
    "es": "Como se puede apreciar en el pasaje extraído del mural, la causa y su efecto kármico están descritos originalmente en vietnamita y con una breve traducción al inglés. A continuación, te ofrecemos la traducción y el análisis en tu idioma:",
    "en": "As can be seen in the passage extracted from the mural, the cause and its karmic effect are originally described in Vietnamese with a brief English translation. Below, we offer the translation and analysis in your language:"
}

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

for code, g_code in lang_map.items():
    common_titles[code] = get_trans(common_titles["es"], code, g_code)
    common_descs[code] = get_trans(common_descs["es"], code, g_code)
    intro_texts[code] = get_trans(intro_texts["es"], code, g_code)

def translate_es(text_es):
    d = {"en": get_trans(text_es, "en", "en")}
    for code, g_code in lang_map.items():
        d[code] = get_trans(text_es, code, g_code)
    return d

data = {
    "01_esfuerzo_desinteresado": {
        "vn": "Nhân: Yêu thích lao động giúp đời.<br>Quả: Sức mạnh cường tráng.",
        "en_t": "Cause: Work willingly and being helpful.<br>Effect: Brings perfect physical health.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Trabajar de buena gana y ayudar a los demás.<br>Efecto: Gran fuerza e impecable salud física.",
        "an": "El altruismo físico se cristaliza en la fortaleza de nuestro propio ser. Cada gota de sudor invertida en aliviar la carga de nuestro prójimo, lejos de agotarnos en el tiempo, retorna en nuestra complexión celular otorgándonos esa robustez y vitalidad inquebrantable a la que tanto aspiramos en vidas futuras o realidades solapadas."
    },
    "02_fidelidad_y_familia": {
        "vn": "Nhân: Đa tình, dâm đãng.<br>Quả: Rối loạn giới tính, gia đình con cháu tan vỡ.",
        "en_t": "Cause: Being lustful and promiscuous.<br>Effect: Brings sex disorder and a broken family.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Ser lujurioso y promiscuo rompiendo familias ajenas.<br>Efecto: Atrae desórdenes sexuales y el quiebre de tu propia familia.",
        "an": "La deslealtad narcisista, que busca la saciedad destruyendo los cimientos afectivos, condena al alma a sufrir el mismo y doloroso desarraigo. Jugar con los sentimientos y la intimidad de los demás nos sitúa, inexorablemente, frente al espejo de la profunda soledad y la desunión del propio linaje, obligándonos a cosechar la frialdad que una vez esparcimos."
    },
    "03_generosidad_y_prosperidad": {
        "vn": "Nhân: Bố thí giúp người.<br>Quả: Sung túc mọi người yêu thương.",
        "en_t": "Cause: Doing many charitable activities.<br>Effect: Brings prosperity and love of others.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Hacer obras de caridad ayudando a las personas.<br>Efecto: Atrae inmensa prosperidad económica y el amor de todos.",
        "an": "El apego nunca ha multiplicado lo nuestro, sino que lo estanca. El universo es un vasto océano donde el soltar desinteresadamente abre por fuerza los canales receptivos. Quien sabe compartir con su hermano necesitado las migajas hoy, siembra el código de acceso a la abundancia, donde no solo la riqueza material lo sigue de vuelta, sino también el valioso abrazo desinteresado y amor de los que lo rodean."
    },
    "04_respeto_por_la_vida": {
        "vn": "Nhân: Làm nghề sát sanh.<br>Quả: Yểu mạng, đẻ sinh nơi có chiến tranh.",
        "en_t": "Cause: Working as a slaughterer in the previous life.<br>Effect: Brings rebirth of short-life and in war zones.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Haber trabajado como un verdugo matarife impío en una vida anterior.<br>Efecto: Conlleva un renacer frágil con vida corta y en zona de guerras cruentas.",
        "an": "No se puede sesgar brutalmente y a destajo la existencia temblorosa de una criatura asumiendo que esa energía no te salpicará. El menosprecio por el pulso de la viña divina te abocará, más temprano que tarde, a ser arrojado al terror incesante de la batalla y sobrevivir a la pavorosa realidad de la guerra y la impotencia. Una pedagogía dura y asfixiante impuesta al alma de hielo para que encienda un destello de empatía hacia toda forma de vida."
    },
    "05_pureza_mental": {
        "vn": "Nhân: Thương làm phim viết sách đồi trụy.<br>Quả: Điên loạn, khổ đau, gia đình đổ vỡ.",
        "en_t": "Cause: Producing pornographic books, movies.<br>Effect: Brings mental illness, misery, and a broken family.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Producir libros, películas morbosas u obscenas contaminando a la sociedad.<br>Efecto: Atrae severa enfermedad mental, histeria, miseria y familia destruida.",
        "an": "Volcar inmundicia, vulgaridad y oscuridad en el estanque diáfano del pensamiento colectivo es un sabotaje contra el avance puro de la consciencia humana. Semejante nube negra de desesperanza no se dispersa sino que, debido al efecto bumerán perfecto del karma, vuelve para hospedarse densamente como esquizofrenias latentes y severos tormentos paralizantes en los pasadizos de nuestra propia psiquis."
    },
    "06_sobriedad_y_claridad": {
        "vn": "Nhân: Mời người sử dụng các chất gây say nghiện.<br>Quả: Mất ngủ, ngu dốt, điên loạn.",
        "en_t": "Cause: Offering addictive substances to others.<br>Effect: Brings sleeplessness, foolishness, and mental disorders.",
        "es_t": "<strong>Traducción Recreada:</strong><br>Causa: Ofrecer, vender o invitar al uso de sustancias adictivas o venenosas a otros.<br>Efecto: Atrae insomnio permanente, merma de la inteligencia, necedad y locura desorientadora.",
        "an": "Diluir el juicio sagrado, la voluntad de un tercero, sedándolo para la ruina en pos de mero y codicioso enriquecimiento es adueñarnos de su capacidad cerebral y amnesia perjudicial temporal. Como las leyes energéticas impiden deudas sin saldar, asimilamos en paralelo ese oscuro desvarío como un tormento neurótico; padeciendo de insomnios crónicos irrefrenables y nublando nuestra brillantez e inspiración hasta la impotencia para empujarnos ávidamente a revalorizar por contraste la sobriedad divina de una mente limpia e intacta."
    }
}

chapters = [
    "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad"
]

for chap in chapters:
    print(f"Translating components for {chap}...")
    d = data[chap]
    
    d["es_t_full"] = {"es": d["es_t"]}
    d["es_t_full"].update(translate_es(d["es_t"]))
    
    d["an_full"] = {"es": f'<strong>Análisis:</strong> {d["an"]}'}
    d["an_full"].update(translate_es(f'<strong>Análisis:</strong> {d["an"]}'))

def build_inspiration_block(chap):
    d = data[chap]
    
    titles = "".join([f'<h3 class="{k}" style="color: var(--gold); text-align: center; margin-bottom: 2rem; font-family: \'Cinzel\', serif;">{v}</h3>\n' for k,v in common_titles.items()])
    descs = "".join([f'<p class="{k}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">{v}</p>\n' for k,v in common_descs.items()])
    
    intros = "".join([f'<p class="{k}" style="color: #bbb; margin-bottom: 1.5rem; font-style: italic;">{v}</p>\n' for k,v in intro_texts.items()])
    
    vn_html = f'<p style="color: #fff; font-style: italic; margin-bottom: 2rem; font-family: \'EB Garamond\', serif; font-size: 1.2rem;"><strong>🇻🇳 Tiếng Việt:</strong><br>{d["vn"]}</p>'
    
    mural_trans = "".join([f'<p class="{k}" style="color: #fff; margin-bottom: 1.5rem; background: rgba(197, 160, 89, 0.1); padding: 1rem; border-left: 3px solid var(--gold);">{v}</p>\n' for k,v in d["es_t_full"].items()])
    
    analysis = "".join([f'<p class="{k}" style="color: #aaa; margin: 0 0 1rem 0; line-height: 1.6;">{v}</p>\n' for k,v in d["an_full"].items()])
    
    html = f"""
            <div class="original-inspiration fade-in" style="margin-top: 5rem; padding-top: 3rem; border-top: 1px solid rgba(197, 160, 89, 0.3);">
                {titles}
                {descs}
                <center>
                    <img src="assets/pasaje_original.jpg" alt="Tranh Nhân Quả Original" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); margin-bottom: 2rem;">
                </center>
                <div class="translation-box" style="background: rgba(0, 0, 0, 0.4); padding: 2rem; border-radius: 12px; border-left: 4px solid var(--gold); max-width: 800px; margin: 0 auto;">
                    {intros}
                    {vn_html}
                    <p style="color: #ddd; margin-bottom: 1.5rem;"><strong>🇬🇧 English Translation:</strong><br>{d["en_t"]}</p>
                    {mural_trans}
                    <hr style="border-color: rgba(197, 160, 89, 0.2); margin-block: 2rem;">
                    {analysis}
                </div>
            </div>"""
    return html

def inject(chapter):
    filepath = f"{chapter}/web/index.html"
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    
    # Check if .original-inspiration already exists. If yes, replace it.
    if '<div class="original-inspiration' in content:
        content = re.sub(r'<div class="original-inspiration[^>]*>([\s\S]*?)<div class="translation-box"[^>]*>([\s\S]*?)</div>\s*</div>', build_inspiration_block(chapter).strip(), content, flags=re.IGNORECASE)
    else:
        # Insert before Linktree or before </main>
        block = build_inspiration_block(chapter)
        # Look for <div class="linktree-subtle
        if '<div class="linktree-subtle' in content:
            content = re.sub(r'(\s*<div class="linktree-subtle)', r'\n            ' + block + r'\1', content)
        else:
            content = re.sub(r'(\s*</main>)', r'\n            ' + block + r'\1', content)
    
    with open(filepath, "w") as f:
        f.write(content)
        print(f"Injected original inspiration into {chapter}")

for chap in chapters:
    inject(chap)
