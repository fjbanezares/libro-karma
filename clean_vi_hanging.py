import os
import re

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia",
    "13_amor_y_respeto", "14_peso_deudores", "15_desperdicio_y_escasez", "16_adiccion_y_ceguera",
    "17_orfandad_filial", "18_pereza_laboral"
]
files = [f"{c}/web/index.html" for c in chapters] + ["index.html", "biblioteca/index.html", "linktree.html"]

for fp in files:
    if not os.path.exists(fp): continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # The leftover strings come after `</p>` and have no starting tag or start with <br>
    # They ALWAYS end with </p> because that was the end of the <p class="vi"> block.
    # Looking for: </p> followed by any spaces, then any text containing Vietnamese words or <br>, followed by </p>.
    # Instead of complex regex, let's just find `</p>` followed by `<br>Nhân:` or `<br>Nguyên nhân:` or `Đó là một`
    # Or just `</p>` followed by anything that is NOT `<` or `\s+<` up to `</p>`.
    
    # Wait, `<p class="pt">...</p><br>Nguyên nhân: ...</p>`
    # The regex `(</p>\s*)(?!<)[\s\S]*?</p>` would match `</p>` then ANY char that doesn't start with `<` then up to `</p>`.
    # Let's test this carefully.
    
    # Actually, simpler: just remove any `<br>Nguyên nhân:.*?</p>`, `<br>Nhân:.*?</p>`, `Đó.*?</p>`, etc.
    # Let's use a regex to match the orphaned text pattern specifically:
    content = re.sub(r'(</p>\s*)<br>(Nguyên nhân|Nhân):[\s\S]*?</p>', r'\1', content)
    content = re.sub(r'(</p>\s*)(Đó|Đây|Như|Vì|Bởi|Kẻ|Ai)[\s\S]*?</p>', r'\1', content)

    # Let me also fix line 75 in 15_desperdicio_y_escasez where 
    # `<div class="lang-opt" data-lang="pt" onclick="setLanguage('pt')"><span class="flag">🇵🇹</span> Português</div> Tiếng Việt</div>`
    # Wait! " Tiếng Việt</div>" is dangling in line 75!
    content = re.sub(r' Tiếng Việt</div>', '', content)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

print("Cleaned up hanging Vietnamese elements.")
