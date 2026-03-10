import os
import re

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

ui_1_12 = {
    "cap_0": {"es": "El Despertar", "en": "The Awakening", "it": "Il Risveglio", "zh": "觉醒", "ar": "الصحوة", "ru": "Пробуждение", "de": "Das Erwachen", "fr": "L'Éveil", "ja": "目覚め", "pt": "O Despertar"},
    "cap_1": {"es": "Fuerza Física", "en": "Physical Strength", "it": "Forza Fisica", "zh": "体力", "ar": "القوة البدنية", "ru": "Физическая сила", "de": "Physische Kraft", "fr": "Force Physique", "ja": "体力", "pt": "Força Física"},
    "cap_2": {"es": "Espejos Rotos", "en": "Broken Mirrors", "it": "Specchi Rotti", "zh": "破镜", "ar": "مرايا مكسورة", "ru": "Разбитые зеркала", "de": "Zerbrochene Spiegel", "fr": "Miroirs Brisés", "ja": "割れた鏡", "pt": "Espelhos Quebrados"},
    "cap_3": {"es": "Siembra Silenciosa", "en": "Silent Sowing", "it": "Semina Silenziosa", "zh": "默默播种", "ar": "بذر صامت", "ru": "Тихий посев", "de": "Stilles Säen", "fr": "Semis Silencieux", "ja": "静かな種まき", "pt": "Semeadeira Silenciosa"},
    "cap_4": {"es": "Hilo de la Vida", "en": "Thread of Life", "it": "Filo della Vita", "zh": "生命之线", "ar": "خيط الحياة", "ru": "Нить жизни", "de": "Faden des Lebens", "fr": "Fil de la Vie", "ja": "命の糸", "pt": "Fio da Vida"},
    "cap_5": {"es": "Sombras Mentales", "en": "Mental Shadows", "it": "Ombre Mentali", "zh": "心理阴影", "ar": "ظلال عقلية", "ru": "Ментальные тени", "de": "Mentale Schatten", "fr": "Ombres Mentales", "ja": "精神の影", "pt": "Sombras Mentais"},
    "cap_6": {"es": "Veneno Dulce", "en": "Sweet Poison", "it": "Dolce Veleno", "zh": "甜蜜的毒药", "ar": "ثعبان الروح", "ru": "Сладкий яд", "de": "Süßes Gift", "fr": "Doux Poison", "ja": "甘い毒", "pt": "Veneno Doce"},
    "cap_7": {"es": "Manos del Mal", "en": "Hands of Evil", "it": "Mani del Male", "zh": "邪恶之手", "ar": "أيدي الشر", "ru": "Руки зла", "de": "Hände des Bösen", "fr": "Mains du Mal", "ja": "悪の手", "pt": "Mãos do Mal"},
    "cap_8": {"es": "Soberbia", "en": "Pride", "it": "Superbia", "zh": "傲慢", "ar": "كبرياء", "ru": "Гордыня", "de": "Hochmut", "fr": "Orgueil", "ja": "傲慢", "pt": "Soberba"},
    "cap_9": {"es": "Egoísmo", "en": "Greed", "it": "Egoismo", "zh": "自私", "ar": "أنانية", "ru": "Эгоизм", "de": "Egoismus", "fr": "Égoïsme", "ja": "利己主義", "pt": "Egoísmo"},
    "cap_10": {"es": "Infierno", "en": "Hell", "it": "Inferno", "zh": "地狱", "ar": "جحيم", "ru": "Ад", "de": "Hölle", "fr": "Enfer", "ja": "地獄", "pt": "Inferno"},
    "cap_11": {"es": "Desprecio", "en": "Contempt", "it": "Disprezzo", "zh": "蔑视", "ar": "احتقار", "ru": "Презрение", "de": "Verachtung", "fr": "Mépris", "ja": "軽蔑", "pt": "Desprezo"},
    "cap_12": {"es": "Injusticia", "en": "Injustice", "it": "Ingiustizia", "zh": "不公", "ar": "ظلم", "ru": "Несправедливость", "de": "Ungerechtigkeit", "fr": "Injustice", "ja": "不正", "pt": "Injustiça"},
}

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
    if not os.path.exists(filepath): return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update lang selector block exactly matching anything in lang-selector-elegant entirely
    content = re.sub(
        r'<div class="lang-selector-elegant">[\s\S]*?</div>\s*</div>\s*</div>',
        lang_selector_html.strip() + '\n        </div>',
        content
    )
    # the second replacement might be needed if there is no third </div>:
    content = re.sub(
        r'<div class="lang-selector-elegant">[\s\S]*?</div>\s*</div>(?=\s*<a class="top-linktree-subtle")',
        lang_selector_html.strip(),
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
            
            titles = "".join([f'<span class="{l}">{ui_1_12[f"cap_{i}"][l]}</span>' for l in langs])
            
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
            
            href_match = re.search(r'href="([^"]+)"', m.group(1))
            href = href_match.group(1) if href_match else ""
            
            new_card = f'''<!-- Capítulo {i} -->
                <a href="{href}" class="chapter-card">
                    <img src="{img_src}" alt="Capítulo {i}">
                    <div class="card-content">
                        <span class="card-num">{card_num_html}</span>
                        <h2 class="card-title">{titles}</h2>
                    </div>
                </a>'''
            
            content = content.replace(m.group(1), new_card)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filepath} quickly!")

update_library("index.html")
update_library("biblioteca/index.html")
