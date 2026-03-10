import os
import re
import json

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

ui_1_12 = {
    # Sidebar standard names
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
    "biblioteca": {"es": "Biblioteca", "en": "Library", "it": "Libreria", "zh": "图书馆", "ar": "مكتبة", "ru": "Библиотека", "de": "Bibliothek", "fr": "Bibliothèque", "ja": "図書館", "pt": "Biblioteca"},
}

with open("chapters_13_18_data.json", "r", encoding="utf-8") as f:
    cdata = json.load(f)

for ch in ["13_amor_y_respeto", "14_peso_deudores", "15_desperdicio_y_escasez", "16_adiccion_y_ceguera", "17_orfandad_filial", "18_pereza_laboral"]:
    num = ch.split("_")[0]
    ui_1_12[f"cap_{num}"] = {l: cdata[ch]["title"][l] for l in langs}

def get_spans(d):
    return "".join(f'<span class="{l}">{d[l]}</span>' for l in langs)

menu_items = [
    ("biblioteca", "index.html", "<i>☰</i>", get_spans(ui_1_12["biblioteca"])),
    ("00", "00_introduccion/web/index.html", "<i>0</i>", get_spans(ui_1_12["cap_0"])),
    ("01", "01_esfuerzo_desinteresado/web/index.html", "<i>1</i>", get_spans(ui_1_12["cap_1"])),
    ("02", "02_fidelidad_y_familia/web/index.html", "<i>2</i>", get_spans(ui_1_12["cap_2"])),
    ("03", "03_generosidad_y_prosperidad/web/index.html", "<i>3</i>", get_spans(ui_1_12["cap_3"])),
    ("04", "04_respeto_por_la_vida/web/index.html", "<i>4</i>", get_spans(ui_1_12["cap_4"])),
    ("05", "05_pureza_mental/web/index.html", "<i>5</i>", get_spans(ui_1_12["cap_5"])),
    ("06", "06_sobriedad_y_claridad/web/index.html", "<i>6</i>", get_spans(ui_1_12["cap_6"])),
    ("07", "07_manos_del_mal/web/index.html", "<i>7</i>", get_spans(ui_1_12["cap_7"])),
    ("08", "08_pedestal_soberbia/web/index.html", "<i>8</i>", get_spans(ui_1_12["cap_8"])),
    ("09", "09_frio_egoismo/web/index.html", "<i>9</i>", get_spans(ui_1_12["cap_9"])),
    ("10", "10_infierno_sombras/web/index.html", "<i>10</i>", get_spans(ui_1_12["cap_10"])),
    ("11", "11_mirada_desprecio/web/index.html", "<i>11</i>", get_spans(ui_1_12["cap_11"])),
    ("12", "12_peso_injusticia/web/index.html", "<i>12</i>", get_spans(ui_1_12["cap_12"])),
    ("13", "13_amor_y_respeto/web/index.html", "<i>13</i>", get_spans(ui_1_12["cap_13"])),
    ("14", "14_peso_deudores/web/index.html", "<i>14</i>", get_spans(ui_1_12["cap_14"])),
    ("15", "15_desperdicio_y_escasez/web/index.html", "<i>15</i>", get_spans(ui_1_12["cap_15"])),
    ("16", "16_adiccion_y_ceguera/web/index.html", "<i>16</i>", get_spans(ui_1_12["cap_16"])),
    ("17", "17_orfandad_filial/web/index.html", "<i>17</i>", get_spans(ui_1_12["cap_17"])),
    ("18", "18_pereza_laboral/web/index.html", "<i>18</i>", get_spans(ui_1_12["cap_18"]))
]

def build_nav(is_root):
    nav_lines = ['<nav class="sidebar-nav">']
    for id, path, icon, spans in menu_items:
        prefix = "" if is_root else "../../"
        if id == "biblioteca":
            prefix = "" if is_root else "../../"
            p = prefix + path
        else:
            p = prefix + path
        
        # The JS `updateActiveNavLink` handles `active` class, so no need here unless explicitly done by the user template.
        nav_lines.append(f'            <div class="nav-item"><a href="{p}" class="nav-link">{icon}{spans}</a></div>')
    nav_lines.append('        </nav>')
    return "\n".join(nav_lines)

nav_root = build_nav(True)
nav_deep = build_nav(False)

# 1) Update all HTMLs with complete sidebar config
all_htmls = ["index.html", "linktree.html"]
for c_path in [c for c in os.listdir() if os.path.isdir(c) and re.match(r'^\d\d_', c)]:
    all_htmls.append(f"{c_path}/web/index.html")

for path in all_htmls:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        is_root = ("/" not in path)
        new_nav = nav_root if is_root else nav_deep
        
        new_content = re.sub(r'<nav class="sidebar-nav">[\s\S]*?</nav>', new_nav, content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
print("Updated all sidebars identically and perfectly.")

# 2) Fix index.html cards (append 13-18 to library-grid) array
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Only append if Chapter 13 card is not there!
if '<!-- Capítulo 13 -->' not in idx_content:
    romans = {"13": "XIII", "14": "XIV", "15": "XV", "16": "XVI", "17": "XVII", "18": "XVIII"}
    new_chapters = [
        "13_amor_y_respeto", "14_peso_deudores", "15_desperdicio_y_escasez",
        "16_adiccion_y_ceguera", "17_orfandad_filial", "18_pereza_laboral"
    ]
    
    cards_html = ""
    for ch in new_chapters:
        num = ch.split("_")[0]
        titles = "".join([f'<span class="{l}">{cdata[ch]["title"][l]}</span>' for l in langs])
        # Check image logic (art.jpg or hero.jpg)
        img_name = "art.jpg" if os.path.exists(f"{ch}/web/assets/art.jpg") else "hero.jpg"
        
        cards_html += f'''
                <!-- Capítulo {num} -->
                <a href="{ch}/web/index.html" class="chapter-card">
                    <img src="{ch}/web/assets/{img_name}" alt="Capítulo {num}">
                    <div class="card-content">
                        <span class="card-num">
                            {''.join(f'<span class="{l}">CAPÍTULO {romans[num]}</span>' if l in ['es','pt'] else f'<span class="{l}">CHAPTER {romans[num]}</span>' if l == 'en' else f'<span class="{l}">CAPITOLO {romans[num]}</span>' if l == 'it' else f'<span class="{l}">第{romans[num]}章</span>' if l in ['zh','ja'] else f'<span class="{l}">الفصل {romans[num]}</span>' if l == 'ar' else f'<span class="{l}">ГЛАВА {romans[num]}</span>' if l == 'ru' else f'<span class="{l}">KAPITEL {romans[num]}</span>' if l == 'de' else f'<span class="{l}">CHAPITRE {romans[num]}</span>' for l in langs)}
                        </span>
                        <h2 class="card-title">{titles}</h2>
                    </div>
                </a>
'''
    # We replace the closing </div> of <div class="library-grid"> with cards + closing tag
    
    # We can match `<a href="12_peso_injusticia/web/index.html"[^>]*>[\s\S]*?</a>\s*</div>`
    pattern = r'(<a href="12_peso_injusticia/web/index\.html"[^>]*class="chapter-card"[^>]*>[\s\S]*?</a>\s*)(</div>\s*</div>\s*</main>)'
    
    idx_content = re.sub(pattern, lambda m: m.group(1) + cards_html + m.group(2), idx_content)
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(idx_content)
    print("Added chapters 13-18 to library index!")
else:
    print("Chapters 13-18 already exist in library index.")
