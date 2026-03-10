import os
import re

all_dirs = [
    ".", "biblioteca", "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia",
    "13_amor_y_respeto", "14_peso_deudores", "15_desperdicio_y_escasez", "16_adiccion_y_ceguera",
    "17_orfandad_filial", "18_pereza_laboral"
]

files_to_process = []
for d in all_dirs:
    fp = os.path.join(d, "web", "index.html") if d != "." else "index.html"
    if os.path.exists(fp): files_to_process.append(fp)
    if d == ".":
        for ff in ["biblioteca/index.html", "linktree.html"]:
            if os.path.exists(ff) and ff not in files_to_process: files_to_process.append(ff)

vi_opt_pat = re.compile(r'\s*<(?:div|span|a|button)[^>]*?class="vi"[^>]*>.*?</(?:div|span|a|button)>', flags=re.DOTALL)
vi_opt_pat_2 = re.compile(r'\s*<[^>]+class="lang-opt"[^>]+data-lang="vi"[^>]*>.*?</[^>]+>', flags=re.DOTALL)
vi_opt_pat_3 = re.compile(r'\s*<[^>]+class="vi"[^>]*>.*?</[^>]+>', flags=re.DOTALL)

for fp in set(files_to_process):
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()

    # Clean the translation
    html = vi_opt_pat_2.sub('', html)
    html = vi_opt_pat_3.sub('', html)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Reverted all VI injections!")
