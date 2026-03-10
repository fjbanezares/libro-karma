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
    for lang, text in data_dict.items():
        out.append(f'<span class="{lang}">{text}</span>')
    return "".join(out)

sidebar_replacements = [
    (r'<span class="es">Biblioteca</span><span class="en">Library</span>', build_spans(ui_translations["biblioteca"])),
    (r'<span class="es">El Despertar</span><span class="en">The Awakening</span>', build_spans(ui_translations["cap_0"])),
    (r'<span class="es">Fuerza Física</span><span class="en">Physical Strength</span>', build_spans(ui_translations["cap_1"])),
    (r'<span class="es">Espejos Rotos</span><span class="en">Broken Mirrors</span>', build_spans(ui_translations["cap_2"])),
    (r'<span class="es">Siembra Silenciosa</span><span class="en">Silent Sowing</span>', build_spans(ui_translations["cap_3"])),
    (r'<span class="es">Hilo de la Vida</span><span class="en">Thread of Life</span>', build_spans(ui_translations["cap_4"])),
    (r'<span class="es">Sombras Mentales</span><span class="en">Mental Shadows</span>', build_spans(ui_translations["cap_5"])),
    (r'<span class="es">Veneno Dulce</span><span class="en">Sweet Poison</span>', build_spans(ui_translations["cap_6"])),
    (r'<span class="es">Manos del Mal</span><span class="en">Hands of Evil</span>', build_spans(ui_translations["cap_7"])),
    (r'<span class="es">Soberbia</span><span class="en">Pride</span>', build_spans(ui_translations["cap_8"])),
    (r'<span class="es">Egoísmo</span><span class="en">Greed</span>', build_spans(ui_translations["cap_9"])),
    (r'<span class="es">Infierno</span><span class="en">Hell</span>', build_spans(ui_translations["cap_10"])),
    (r'<span class="es">Desprecio</span><span class="en">Contempt</span>', build_spans(ui_translations["cap_11"])),
    (r'<span class="es">Injusticia</span><span class="en">Injustice</span>', build_spans(ui_translations["cap_12"])),
]

def update_sidebar(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    for old, new in sidebar_replacements:
        content = content.replace(old, new)

    # Some cleanup for index.html titles
    content = content.replace(r'<span class="es">Librería del Karma</span>\n                <span class="en">The Karma Library</span>',
                              build_spans({"es": "Librería del Karma", "en": "The Karma Library", "it": "Libreria del Karma", "zh": "因果图书馆", "ar": "مكتبة الكارما", "ru": "Библиотека Кармы", "de": "Karma Bibliothek", "fr": "Bibliothèque du Karma", "ja": "カルマ図書館", "pt": "Biblioteca do Karma"}))

    content = content.replace('<span class="es">CAPÍTULO 0</span><span class="en">CHAPTER 0</span>', build_spans({"es":"CAPÍTULO 0", "en":"CHAPTER 0", "it":"CAPITOLO 0", "zh":"第0章", "ar":"الفصل 0", "ru":"ГЛАВА 0", "de":"KAPITEL 0", "fr":"CHAPITRE 0", "ja":"第0章", "pt":"CAPÍTULO 0"}))
    content = content.replace('<span class="es">CAPÍTULO I</span><span class="en">CHAPTER I</span>', build_spans({"es":"CAPÍTULO I", "en":"CHAPTER I", "it":"CAPITOLO I", "zh":"第一章", "ar":"الفصل الأول", "ru":"ГЛАВА I", "de":"KAPITEL I", "fr":"CHAPITRE I", "ja":"第一章", "pt":"CAPÍTULO I"}))
    content = content.replace('<span class="es">CAPÍTULO II</span><span class="en">CHAPTER II</span>', build_spans({"es":"CAPÍTULO II", "en":"CHAPTER II", "it":"CAPITOLO II", "zh":"第二章", "ar":"الفصل الثاني", "ru":"ГЛАВА II", "de":"KAPITEL II", "fr":"CHAPITRE II", "ja":"第二章", "pt":"CAPÍTULO II"}))
    content = content.replace('<span class="es">CAPÍTULO III</span><span class="en">CHAPTER III</span>', build_spans({"es":"CAPÍTULO III", "en":"CHAPTER III", "it":"CAPITOLO III", "zh":"第三章", "ar":"الفصل الثالث", "ru":"ГЛАВА III", "de":"KAPITEL III", "fr":"CHAPITRE III", "ja":"第三章", "pt":"CAPÍTULO III"}))
    content = content.replace('<span class="es">CAPÍTULO IV</span><span class="en">CHAPTER IV</span>', build_spans({"es":"CAPÍTULO IV", "en":"CHAPTER IV", "it":"CAPITOLO IV", "zh":"第四章", "ar":"الفصل الرابع", "ru":"ГЛАВА IV", "de":"KAPITEL IV", "fr":"CHAPITRE IV", "ja":"第四章", "pt":"CAPÍTULO IV"}))
    content = content.replace('<span class="es">CAPÍTULO V</span><span class="en">CHAPTER V</span>', build_spans({"es":"CAPÍTULO V", "en":"CHAPTER V", "it":"CAPITOLO V", "zh":"第五章", "ar":"الفصل الخامس", "ru":"ГЛАВА V", "de":"KAPITEL V", "fr":"CHAPITRE V", "ja":"第五章", "pt":"CAPÍTULO V"}))
    content = content.replace('<span class="es">CAPÍTULO VI</span><span class="en">CHAPTER VI</span>', build_spans({"es":"CAPÍTULO VI", "en":"CHAPTER VI", "it":"CAPITOLO VI", "zh":"第六章", "ar":"الفصل السادس", "ru":"ГЛАВА VI", "de":"KAPITEL VI", "fr":"CHAPITRE VI", "ja":"第六章", "pt":"CAPÍTULO VI"}))
    content = content.replace('<span class="es">CAPÍTULO VII</span><span class="en">CHAPTER VII</span>', build_spans({"es":"CAPÍTULO VII", "en":"CHAPTER VII", "it":"CAPITOLO VII", "zh":"第七章", "ar":"الفصل السابع", "ru":"ГЛАВА VII", "de":"KAPITEL VII", "fr":"CHAPITRE VII", "ja":"第七章", "pt":"CAPÍTULO VII"}))
    content = content.replace('<span class="es">CAPÍTULO VIII</span><span class="en">CHAPTER VIII</span>', build_spans({"es":"CAPÍTULO VIII", "en":"CHAPTER VIII", "it":"CAPITOLO VIII", "zh":"第八章", "ar":"الفصل الثامن", "ru":"ГЛАВА VIII", "de":"KAPITEL VIII", "fr":"CHAPITRE VIII", "ja":"第八章", "pt":"CAPÍTULO VIII"}))
    content = content.replace('<span class="es">CAPÍTULO IX</span><span class="en">CHAPTER IX</span>', build_spans({"es":"CAPÍTULO IX", "en":"CHAPTER IX", "it":"CAPITOLO IX", "zh":"第九章", "ar":"الفصل التاسع", "ru":"ГЛАВА IX", "de":"KAPITEL IX", "fr":"CHAPITRE IX", "ja":"第九章", "pt":"CAPÍTULO IX"}))
    content = content.replace('<span class="es">CAPÍTULO X</span><span class="en">CHAPTER X</span>', build_spans({"es":"CAPÍTULO X", "en":"CHAPTER X", "it":"CAPITOLO X", "zh":"第十章", "ar":"الفصل العاشر", "ru":"ГЛАВА X", "de":"KAPITEL X", "fr":"CHAPITRE X", "ja":"第十章", "pt":"CAPÍTULO X"}))
    content = content.replace('<span class="es">CAPÍTULO XI</span><span class="en">CHAPTER XI</span>', build_spans({"es":"CAPÍTULO XI", "en":"CHAPTER XI", "it":"CAPITOLO XI", "zh":"第十一章", "ar":"الفصل الحادي عشر", "ru":"ГЛАВА XI", "de":"KAPITEL XI", "fr":"CHAPITRE XI", "ja":"第十一章", "pt":"CAPÍTULO XI"}))
    content = content.replace('<span class="es">CAPÍTULO XII</span><span class="en">CHAPTER XII</span>', build_spans({"es":"CAPÍTULO XII", "en":"CHAPTER XII", "it":"CAPITOLO XII", "zh":"第十二章", "ar":"الفصل الثاني عشر", "ru":"ГЛАВА XII", "de":"KAPITEL XII", "fr":"CHAPITRE XII", "ja":"第十二章", "pt":"CAPÍTULO XII"}))

    with open(filepath, 'w') as f:
        f.write(content)

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]

files = [f"{c}/web/index.html" for c in chapters]
files.append("index.html")

for path in files:
    if os.path.exists(path):
        update_sidebar(path)
        print("Updated sidebar/index in", path)
