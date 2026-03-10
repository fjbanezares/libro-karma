import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

# Old substrings to replace at the bottom
old_es = "sobre el proyecto y colaborar"
new_es = "sobre el proyecto o colaborar"

old_en = "about the project and collaborate"
new_en = "about the project or collaborate"

# Need to accurately translate the new strings for all
new_dict = {
    "es": "Si quieres conocer más sobre el proyecto o colaborar, accede a nuestro",
    "en": "If you want to know more about the project or collaborate, access our"
}

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

for code, g_code in lang_map.items():
    new_dict[code] = get_trans(new_dict["es"], code, g_code)

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]
files = [f"{c}/web/index.html" for c in chapters] + ["index.html"]

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # 1. Replace the bottom text exactly
    # We will just replace the entire linktree-subtle block contents to be perfectly sure.
    linktree_html = f"""
            <div class="linktree-subtle fade-in" style="margin-top: 6rem; padding: 3rem 0; border-top: 1px solid rgba(197, 160, 89, 0.2); text-align: center;">
"""
    depth = "../../" if "index.html" != filepath else ""
    for code in ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]:
        linktree_html += f'                <p class="{code}" style="color: #999; font-style: italic; margin-bottom: 1.5rem;">{new_dict[code]} <a href="{depth}linktree.html" style="color: var(--gold); text-decoration: none; border-bottom: 1px dotted var(--gold); padding-bottom: 2px; transition: all 0.3s ease;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'var(--gold)\'">Linktree</a>.</p>\n'
    linktree_html += """            </div>"""

    # Sub the old block
    content = re.sub(r'<div class="linktree-subtle.*</div>', linktree_html.strip(), content, flags=re.DOTALL)

    # 2. Add subtle Linktree button below language selector
    # We find `<div class="lang-selector-elegant">...</div>` inside `<div class="top-header-controls">`
    # and add the button right after the elegant div, and we set top-header-controls to flex-direction: column to stack them.
    # Wait! the simplest way is to just find `</div>\n        </div>\n\n        <header`
    # meaning the end of `top-header-controls` block.
    
    # We can inject a linktree button if it's not already there.
    if "top-linktree-subtle" not in content:
        # replace the beginning of top-header-controls to add flex-direction column if not present
        if '<div class="top-header-controls"' in content and '<div class="lang-selector-elegant">' in content:
            # Let's insert a small text link right after `</div>` of `.lang-selector-elegant`
            # Look for `<div class="lang-selector-elegant">...</div>` block
            # Actually, `</div>\n        </div>\n\n        <header` is safe.
            # Let's add it right before `</div>\n\n        <header`
            subtle_button = f"""
                <a class="top-linktree-subtle" href="{depth}linktree.html" style="font-family: 'Cinzel', serif; font-size: 0.75rem; color: rgba(255,255,255,0.4); text-decoration: none; letter-spacing: 2px; margin-top: 8px; transition: color 0.3s;" onmouseover="this.style.color='var(--gold)'" onmouseout="this.style.color='rgba(255,255,255,0.4)'">LINKTREE</a>
"""
            # find <div class="top-header-controls"> and change it to include style
            # to let the contents stack vertically aligned to the right.
            content = content.replace('<div class="top-header-controls">', '<div class="top-header-controls" style="flex-direction: column; align-items: flex-end; justify-content: center; gap: 0;">')
            
            # Now we find the end of `lang-selector-elegant`. It's hard with regex to balance tags.
            # Instead, we find `<header class="mobile-header">` and go up two `</div>`.
            content = content.replace('</div>\n        </div>\n\n        <header class="mobile-header">', f'</div>\n{subtle_button}        </div>\n\n        <header class="mobile-header">')

    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Processed {filepath}")

for f in files:
    process_file(f)
