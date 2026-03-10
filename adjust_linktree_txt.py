import os
import re
from deep_translator import GoogleTranslator

# Target languages
lang_map = {"it": "it", "zh": "zh-CN", "ar": "ar", "ru": "ru", "de": "de", "fr": "fr", "ja": "ja", "pt": "pt"}

desc_original_es = "La historia que hemos generado para este capítulo está inspirada por este pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía original."
desc_new_es = "La historia que hemos relatado en este capítulo está inspirada por el pasaje de la escena original de los murales «Tranh Nhân Quả» (Ilustraciones del Karma) del Templo Linh Ung en Da Nang, capturado en la fotografía adjunta."

def get_trans(text_es, lang_code, g_code):
    try:
        if lang_code == "en": g_code = "en"
        return GoogleTranslator(source='es', target=g_code).translate(text_es)
    except Exception as e:
        print(f"Error {lang_code}: {e}")
        return text_es

# Translate old descriptions to find and new descriptions to replace
old_descs = {"es": desc_original_es}
new_descs = {"es": desc_new_es}

old_descs["en"] = "The story we generated for this chapter is inspired by this passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the original photograph."
new_descs["en"] = "The story we have related in this chapter is inspired by the passage from the original scene of the \"Tranh Nhân Quả\" (Karma Illustrations) murals at the Linh Ung Temple in Da Nang, captured in the attached photograph."

for code, g_code in lang_map.items():
    # Only translating the new one. The old ones were mapped during `fix_inspirations.py` from `common_descs['es']`.
    # Let's just do a regex replace for the <p class="lang"...> block covering the description to be totally safe.
    new_descs[code] = get_trans(desc_new_es, code, g_code)

# Let's create the linktree text block
linktree_text_es = "Si quieres conocer más sobre el proyecto y colaborar, accede a nuestro"
linktree_dict = {"es": linktree_text_es}
linktree_dict["en"] = "If you want to know more about the project and collaborate, access our"
for code, g_code in lang_map.items():
    linktree_dict[code] = get_trans(linktree_text_es, code, g_code)

linktree_html = f"""
            <div class="linktree-subtle fade-in" style="margin-top: 6rem; padding: 3rem 0; border-top: 1px solid rgba(197, 160, 89, 0.2); text-align: center;">
"""
for code in ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]:
    linktree_html += f'                <p class="{code}" style="color: #999; font-style: italic; margin-bottom: 1.5rem;">{linktree_dict[code]} <a href="../../linktree.html" style="color: var(--gold); text-decoration: none; border-bottom: 1px dotted var(--gold); padding-bottom: 2px; transition: all 0.3s ease;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'var(--gold)\'">Linktree</a>.</p>\n'
linktree_html += """            </div>"""

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

    # 1. Remove Top Header LinkTree icon.
    # Pattern to match the <a href="../../linktree.html" ... >...</a> block
    icon_pattern = r'<a href="(../../)?linktree\.html"[^>]*>[\s\S]*?<svg[\s\S]*?</svg>\s*</a>'
    content = re.sub(icon_pattern, '', content)

    # 2. Add subtle Linktree before </main> if it's not index.html (index has a different structure, although we can just put it at the end)
    if "index.html" in filepath and filepath != "index.html":
        # Remove any existing linktree subtle to avoid dupes
        content = re.sub(r'<div class="linktree-subtle.*</div>', '', content, flags=re.DOTALL)
        content = re.sub(r'</main>', linktree_html + '\n    </main>', content)

    # 3. Replace "hemos generado" descriptions in chapters 7-12
    # We look for <p class="XX" ...>La historia que hemos generado ...</p>
    # Actually, the easiest way is iterating through the translations of new_desc we made and replacing the inner HTML of those specific <p>
    if filepath != "index.html":
        # We need to find the <p ...> block which is right after the title in .original-inspiration
        # Find the block where `class="XX"` and text matches vaguely.
        
        # In reality, it's easier to replace old_descs if we had them or just regex the exact <p> if they match.
        # But wait! I can just find the whole <p class="es" ...>La historia que hemos generado... </p> and replace its content.
        for lang in new_descs:
            if lang == "es":
                # replace <p class="es" ...>La historia que hemos generado...</p>
                content = re.sub(r'(<p class="es"[^>]*>)\s*La historia que hemos generado[^<]*?(</p>)', r'\g<1>' + new_descs["es"] + r'\g<2>', content)
            elif lang == "en":
                content = re.sub(r'(<p class="en"[^>]*>)\s*The story we generated[^<]*?(</p>)', r'\g<1>' + new_descs["en"] + r'\g<2>', content)
            else:
                # for other languages we don't strictly know the exact old text since we dynamically translated it previously.
                # Let's isolate the `.original-inspiration` <h3> blocks, and the <p> blocks that follow.
                pass
        
        # A safer dynamic replace for all languages: The `common_descs` was injected recently. We can regex the exact <p> blocks that have `max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;` inside `original-inspiration`.
        # <p class="it" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">...
        for lang, text in new_descs.items():
            pattern = re.compile(rf'(<p class="{lang}" style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: #ccc;">)[\s\S]*?(</p>)')
            content = pattern.sub(rf'\g<1>{text}\g<2>', content)

    with open(filepath, 'w') as f:
        f.write(content)
        print(f"Processed {filepath}")

for f in files:
    process_file(f)

# Also do it for root index
process_file("index.html")
# For index, we might just append the linktree string at the end of the <div class="container">, near the end. Let's see if index has </main>.
# If we have to, we will do it.
