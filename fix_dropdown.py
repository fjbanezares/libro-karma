import os
import re

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]
files = [f"{c}/web/index.html" for c in chapters] + ["index.html", "biblioteca/index.html"]

def fix_lang_dropdown(filepath):
    if not os.path.exists(filepath):
        return
    
    with open(filepath, 'r') as f:
        content = f.read()

    # We want to remove the stray div that contains English flag and any extra closing divs.
    # The clean replacement block should be just this inside the nav-header/top-header-controls:
    clean_replacement = """<div class="lang-selector-elegant">
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
        </div>

        <header"""

    # We will use regex to find `<div class="lang-selector-elegant">` up to `<header`
    # replacing the whole block.
    
    pattern = re.compile(r'<div class="lang-selector-elegant">[\s\S]*?<header', re.DOTALL)
    new_content = pattern.sub(clean_replacement, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print("Fixed dropdown in:", filepath)

for path in files:
    fix_lang_dropdown(path)
