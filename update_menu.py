import os
import re

# We will define a list of (spanish_text, english_text, dict_of_translations)
translations = {
    # Dropdown Menu Template Replacement inside each HTML
    "lang_menu_replacement": """
                <button class="lang-current-trigger">
                    <span class="flag">🇪🇸</span> <span class="es">Castellano</span> <span class="en">English</span>
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
""",
}

def replace_lang_menu(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the block between <button class="lang-current-trigger"> and </div></div> (the end of lang-selector-elegant)
    pattern = r'<button class="lang-current-trigger">.*?</button>\s*<div class="lang-dropdown-menu">.*?</div>'
    # Wait, simple string replace is safer if it matches exactly. Let's use re.sub
    new_content = re.sub(r'<button class="lang-current-trigger">[\s\S]*?</button>[\s\S]*?<div class="lang-dropdown-menu">[\s\S]*?</div>', translations["lang_menu_replacement"], content)
    
    with open(filepath, 'w') as f:
        f.write(new_content)

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
        replace_lang_menu(path)
        print("Updated menu in", path)
