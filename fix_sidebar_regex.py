import os
import re

ui_translations = {
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

def build_spans(data_dict):
    out = []
    # Force 10 languages
    order = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
    for lang in order:
        text = data_dict[lang]
        out.append(f'<span class="{lang}">{text}</span>')
    return "".join(out)

sidebar_regexes = [
    (r'<span[^>]*class="es"[^>]*>\s*Biblioteca\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Library\s*</span>', build_spans(ui_translations["biblioteca"])),
    (r'<span[^>]*class="es"[^>]*>\s*El Despertar\s*</span>\s*<span[^>]*class="en"[^>]*>\s*The Awakening\s*</span>', build_spans(ui_translations["cap_0"])),
    (r'<span[^>]*class="es"[^>]*>\s*Fuerza Física\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Physical\s*Strength\s*</span>', build_spans(ui_translations["cap_1"])),
    (r'<span[^>]*class="es"[^>]*>\s*Espejos Rotos\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Broken Mirrors\s*</span>', build_spans(ui_translations["cap_2"])),
    (r'<span[^>]*class="es"[^>]*>\s*Siembra Silenciosa\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Silent\s*Sowing\s*</span>', build_spans(ui_translations["cap_3"])),
    (r'<span[^>]*class="es"[^>]*>\s*Hilo de la Vida\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Thread of Life\s*</span>', build_spans(ui_translations["cap_4"])),
    (r'<span[^>]*class="es"[^>]*>\s*Sombras Mentales\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Mental Shadows\s*</span>', build_spans(ui_translations["cap_5"])),
    (r'<span[^>]*class="es"[^>]*>\s*Veneno Dulce\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Sweet Poison\s*</span>', build_spans(ui_translations["cap_6"])),
    (r'<span[^>]*class="es"[^>]*>\s*Manos del Mal\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Hands of Evil\s*</span>', build_spans(ui_translations["cap_7"])),
    (r'<span[^>]*class="es"[^>]*>\s*Soberbia\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Pride\s*</span>', build_spans(ui_translations["cap_8"])),
    (r'<span[^>]*class="es"[^>]*>\s*Egoísmo\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Greed\s*</span>', build_spans(ui_translations["cap_9"])),
    (r'<span[^>]*class="es"[^>]*>\s*Infierno\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Hell\s*</span>', build_spans(ui_translations["cap_10"])),
    (r'<span[^>]*class="es"[^>]*>\s*Desprecio\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Contempt\s*</span>', build_spans(ui_translations["cap_11"])),
    (r'<span[^>]*class="es"[^>]*>\s*Injusticia\s*</span>\s*<span[^>]*class="en"[^>]*>\s*Injustice\s*</span>', build_spans(ui_translations["cap_12"])),
]

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]
files = [f"{c}/web/index.html" for c in chapters] + ["index.html", "biblioteca/index.html"]

def fix_sidebar(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We first replace spans that are ALREADY 10 languages back to something simpler just to ensure
    # we don't accidentally double them if some match the regex or are partially broken.
    # But wait, our regex strictly looks for an ES span followed by an EN span.
    # So if there are 10 spans, it won't match. No, wait... it might match the first two and leave the rest!
    # To fix this, we should find ALL spans inside the <i>#</i>...</a> and replace them.
    
    # Let's do a more robust approach:
    # Within <nav class="sidebar-nav"> ... </nav>, replace the spans inside each <a> tag.
    
    nav_match = re.search(r'<nav class="sidebar-nav">([\s\S]*?)</nav>', content)
    if not nav_match: return
    nav_content = nav_match.group(1)
    
    # Let's just blindly apply the regexes, but to ensure we don't leave cruft,
    # let's strip ALL spans inside each link first, except we need to know WHICH one it is!
    # The safest way is to capture `<i>...</i>` and replace everything after it inside the `<a>` with the mapped spans.
    
    # Let's map chapters index to their item:
    items_ordered = [
        ("<i>☰</i>", ui_translations["biblioteca"]),
        ("<i>0</i>", ui_translations["cap_0"]),
        ("<i>1</i>", ui_translations["cap_1"]),
        ("<i>2</i>", ui_translations["cap_2"]),
        ("<i>3</i>", ui_translations["cap_3"]),
        ("<i>4</i>", ui_translations["cap_4"]),
        ("<i>5</i>", ui_translations["cap_5"]),
        ("<i>6</i>", ui_translations["cap_6"]),
        ("<i>7</i>", ui_translations["cap_7"]),
        ("<i>8</i>", ui_translations["cap_8"]),
        ("<i>9</i>", ui_translations["cap_9"]),
        ("<i>10</i>", ui_translations["cap_10"]),
        ("<i>11</i>", ui_translations["cap_11"]),
        ("<i>12</i>", ui_translations["cap_12"]),
    ]
    
    new_nav_content = nav_content
    for i_tag, ui_dict in items_ordered:
        # Find <i>x</i> followed by any amount of spans until </a>
        # Replace the spans with build_spans(ui_dict)
        pattern = re.compile(re.escape(i_tag) + r'\s*(<span[\s\S]*?)</a>', re.IGNORECASE)
        new_nav_content = pattern.sub(f'{i_tag}{build_spans(ui_dict)}</a>', new_nav_content)
    
    content = content.replace(nav_content, new_nav_content)
    
    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Fixed sidebar menu correctly in {filepath}")

for path in files:
    fix_sidebar(path)

