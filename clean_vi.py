import os
from bs4 import BeautifulSoup

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

print(f"Cleaning {len(files_to_process)} HTML files with BeautifulSoup...")

count_removed = 0

for fp in set(files_to_process):
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()

    # Parse with html.parser to preserve formatting as much as possible, though BS4 might alter some indents
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove any element with class="vi"
    vi_elements = soup.find_all(class_="vi")
    for el in vi_elements:
        el.decompose()
        count_removed += 1
        
    # Remove any element with data-lang="vi"
    menu_elements = soup.find_all(attrs={"data-lang": "vi"})
    for el in menu_elements:
        el.decompose()
        count_removed += 1

    # To avoid BeautifulSoup completely reformatting the entire file and losing your exact indentation,
    # wait... BS4 WILL rewrite the entire file's whitespace if we just do str(soup). 
    # Let's NOT use BS4 if we want to preserve exact formatting, we can use it to find the string and then delete it?
    pass

# Wait, instead of BS4 which destroys formatting, let's use a very robust regex that matches balanced tags.
# But we already damaged it with the previous regex that left hanging text!
# So BS4 is the only way to clean the hanging text because the hanging text IS NOT in a tag!
# Wait, my previous `revert_vi.py` script:
# `vi_opt_pat_3 = re.compile(r'\s*<[^>]+class="vi"[^>]*>.*?</[^>]+>', flags=re.DOTALL)`
# That script ALREADY DELETED `<p class="vi"><strong>...</strong>` and left the rest of the text.
# The `html` file now looks like:
# `<p class="pt">...</p> Đó là một quy luật tinh tế... mãi mãi.</p>`
# So `Đó là một quy luật tinh tế... mãi mãi.</p>` is floating around without an open tag!
# BS4 will parse this as text! Let's see how BS4 handles `... mãi mãi.</p>`
pass
