import os
import re
import json

new_chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]

all_chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
] + new_chapters

files = [f"{c}/web/index.html" for c in all_chapters] + ["index.html"]

with open("chapters_13_18_data.json", "r", encoding='utf8') as f:
    cdata = json.load(f)

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]

new_nav_html = ""
for ch in new_chapters:
    ch_num = ch.split("_")[0]
    title_spans = "".join([f'<span class="{l}">{cdata[ch]["title"][l]}</span>' for l in langs])
    new_nav_html += f'            <div class="nav-item"><a href="../../{ch}/web/index.html" class="nav-link"><i>{ch_num}</i>{title_spans}</a></div>\n'

for fpath in files:
    if not os.path.exists(fpath): continue
    with open(fpath, "r", encoding='utf8') as f:
        html = f.read()

    # If already injected, skip
    if "13_amor_y_respeto" not in html and "sidebar-nav" in html:
        # For index.html, depth is different
        depth = "../../" if fpath != "index.html" else ""
        
        # Build the exact injected content replacing depth if needed
        to_inject = new_nav_html
        if depth == "":
            to_inject = to_inject.replace("../../", "")
            
        # We need to insert this right after `12_peso_injusticia... </div>`
        html = re.sub(r'(<div class="nav-item"><a href="[^"]*12_peso_injusticia[^>]*>[\s\S]*?</a></div>\s*)', r'\1' + to_inject, html)

    # For the newly copied chapters (13 to 18), they might have `.nav-link active` class still stuck on "12" or whatever copy they came from.
    # Let's cleanly reset `nav-link active` -> `nav-link` everywhere, 
    # then ONLY set it for the current chapter.
    
    if "index.html" != fpath:
        # Strip all actives
        html = html.replace('class="nav-link active"', 'class="nav-link"')
        # Add active to the current
        current_ch = fpath.split("/")[0]
        # Match the link of the current chapter
        pat = rf'(<a href="\.\./\.\./{current_ch}/web/index\.html" class="nav-link")'
        html = re.sub(pat, r'\1 active', html)

    with open(fpath, "w", encoding='utf8') as f:
        f.write(html)
    print("Updated sidebar for", fpath)

print("Sidebars all updated.")
