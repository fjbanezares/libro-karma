import os
import re
from deep_translator import GoogleTranslator

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

ui_1_12 = {
    "cap_0": {"es": "El Despertar de la Ley", "en": "The Awakening of Law"},
    "cap_1": {"es": "Fuerza Física", "en": "Physical Strength"},
    "cap_2": {"es": "Espejos Rotos", "en": "Broken Mirrors"},
    "cap_3": {"es": "Siembra Silenciosa", "en": "Silent Sowing"},
    "cap_4": {"es": "Hilo de la Vida", "en": "Thread of Life"},
    "cap_5": {"es": "Sombras Mentales", "en": "Mental Shadows"},
    "cap_6": {"es": "Veneno Dulce", "en": "Sweet Poison"},
    "cap_7": {"es": "Manos del Mal", "en": "Hands of Evil"},
    "cap_8": {"es": "Soberbia", "en": "Pride"},
    "cap_9": {"es": "Egoísmo", "en": "Greed"},
    "cap_10": {"es": "Infierno", "en": "Hell"},
    "cap_11": {"es": "Desprecio", "en": "Contempt"},
    "cap_12": {"es": "Injusticia", "en": "Injustice"},
}
ui_desc = {
    "cap_0": {"es": "Una introducción a la ley de causa y efecto."},
    "cap_1": {"es": "El esfuerzo desinteresado y el vigor del alma."},
    "cap_2": {"es": "La fragmentación del alma y la familia."},
    "cap_3": {"es": "La generosidad y el fruto de la abundancia."},
    "cap_4": {"es": "El respeto sagrado por cada latido divino."},
    "cap_5": {"es": "La pureza de la mente sobre el miedo."},
    "cap_6": {"es": "El valor de la claridad sobre la confusión."},
    "cap_7": {"es": "Cómo las acciones oscuras atan las manos."},
    "cap_8": {"es": "La venda dorada de la superioridad."},
    "cap_9": {"es": "La soledad de un corazón que no da."},
    "cap_10": {"es": "El fuego eterno de la culpa."},
    "cap_11": {"es": "La enfermedad como eco de la soberbia."},
    "cap_12": {"es": "El poder malgastado y la ruina material."},
}

for i in range(13):
    d = ui_1_12[f"cap_{i}"]
    text = d["es"]
    for l in langs:
        if l not in d:
            tcode = lang_map.get(l, l)
            try:
                d[l] = GoogleTranslator(source='es', target=tcode).translate(text)
            except:
                d[l] = text

for i in range(13):
    d = ui_desc[f"cap_{i}"]
    text = d["es"]
    for l in langs:
        if l not in d:
            tcode = lang_map.get(l, l)
            try:
                d[l] = GoogleTranslator(source='es', target=tcode).translate(text)
            except:
                d[l] = text

lang_selector_html = """
            <div class="lang-selector-elegant">
                <button class="lang-current-trigger">
                    <span class="flag">🇪🇸</span> <span class="es">Castellano</span>
                </button>
                <div class="lang-dropdown-menu">
                    <div class="lang-opt" data-lang="es" onclick="setLanguage('es')"><span class="flag">🇪🇸</span> Castellano</div>
                    <div class="lang-opt" data-lang="en" onclick="setLanguage('en')"><span class="flag">🇬🇧</span> English</div>
                    <div class="lang-opt" data-lang="it" onclick="setLanguage('it')"><span class="flag">🇮🇹</span> Italiano</div>
                    <div class="lang-opt" data-lang="zh" onclick="setLanguage('zh')"><span class="flag">🇨🇳</span> 中文</div>
                    <div class="lang-opt" data-lang="ar" onclick="setLanguage('ar')"><span class="flag">🇦🇪</span> العربية</div>
                    <div class="lang-opt" data-lang="ru" onclick="setLanguage('ru')"><span class="flag">🇷🇺</span> Русский</div>
                    <div class="lang-opt" data-lang="de" onclick="setLanguage('de')"><span class="flag">🇩🇪</span> Deutsch</div>
                    <div class="lang-opt" data-lang="fr" onclick="setLanguage('fr')"><span class="flag">🇫🇷</span> Français</div>
                    <div class="lang-opt" data-lang="ja" onclick="setLanguage('ja')"><span class="flag">🇯🇵</span> 日本語</div>
                    <div class="lang-opt" data-lang="pt" onclick="setLanguage('pt')"><span class="flag">🇵🇹</span> Português</div>
                </div>
            </div>
"""

def update_library(filepath):
    prefix = "" if "/" not in filepath else "../../"
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update lang selector
    content = re.sub(
        r'<div class="lang-selector-elegant">[\s\S]*?</div>\s*</div>\s*</div>',
        lang_selector_html.strip() + '\n        </div>',
        content
    )

    # 2. Re-render cards 0-12
    romans = {"0": "0", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", 
              "7": "VII", "8": "VIII", "9": "IX", "10": "X", "11": "XI", "12": "XII"}
    
    for i in range(13):
        # find the card for chapter i
        pattern = re.compile(rf'(<!-- Capítulo {i} -->\s*<a href="[^"]+" class="chapter-card">\s*<img src="([^"]+)" alt="Capítulo {i}">\s*<div class="card-content">[\s\S]*?</div>\s*</a>)')
        m = pattern.search(content)
        if m:
            img_src = m.group(2)
            
            # build the new card HTML
            titles = "".join([f'<span class="{l}">{ui_1_12[f"cap_{i}"][l]}</span>' for l in langs])
            descs = "".join([f'<span class="{l}">{ui_desc[f"cap_{i}"][l]}</span>' for l in langs])
            
            # build card-num
            def get_chap_str(num, l):
                if num == "0":
                    base = {"es": "CAPÍTULO 0", "en": "CHAPTER 0", "it": "CAPITOLO 0", "zh": "第0章", "ar": "الفصل 0", "ru": "ГЛАВА 0", "de": "KAPITEL 0", "fr": "CHAPITRE 0", "ja": "第0章", "pt": "CAPÍTULO 0"}
                    return base.get(l, f"CHAPTER 0")
                else:
                    if l in ['es','pt']: return f"CAPÍTULO {romans[num]}"
                    elif l == 'en': return f"CHAPTER {romans[num]}"
                    elif l == 'it': return f"CAPITOLO {romans[num]}"
                    elif l in ['zh','ja']: return f"第{romans[num]}章"
                    elif l == 'ar': return f"الفصل {romans[num]}"
                    elif l == 'ru': return f"ГЛАВА {romans[num]}"
                    elif l == 'de': return f"KAPITEL {romans[num]}"
                    elif l == 'fr': return f"CHAPITRE {romans[num]}"
            
            card_num_html = "".join([f'<span class="{l}">{get_chap_str(str(i), l)}</span>' for l in langs])
            
            # Extract href properly from original block
            href_match = re.search(r'href="([^"]+)"', m.group(1))
            href = href_match.group(1) if href_match else ""
            
            new_card = f'''<!-- Capítulo {i} -->
                <a href="{href}" class="chapter-card">
                    <img src="{img_src}" alt="Capítulo {i}">
                    <div class="card-content">
                        <span class="card-num">{card_num_html}</span>
                        <h2 class="card-title">{titles}</h2>
                        <p class="card-desc">
                            {descs}
                        </p>
                    </div>
                </a>'''
            
            content = content.replace(m.group(1), new_card)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath}")

update_library("index.html")
if os.path.exists("biblioteca/index.html"):
    update_library("biblioteca/index.html")
else:
    print("biblioteca/index.html not found.")
