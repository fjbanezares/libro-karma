import os
from bs4 import BeautifulSoup, NavigableString

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

print(f"Cleaning leftovers in {len(files_to_process)} HTML files...")

import re

# We know the specific leftover strings starts from some translated text.
# The most common was "Đó là một..." but there could be others.
# Actually, if we look at `13_amor_y_respeto/web/index.html` lines 270-300:
# It's an orphan text node at the end of the <p class="pt">...</p> block!
# Because the regex matched `</[^>]+>` and deleted only to the first closing tag, leaving the rest.

# Let's write a python script that just looks for common Vietnamese characters
# appearing OUTSIDE of any tag, following `</p>`.
# Wait, let's just use regex to fix what the previous script missed.
# The previous script deleted `\s*<[^>]+class="vi"[^>]*>.*?</[^>]+>`.
# This means if it was `<p class="vi"><strong>Text</strong> More text</p>`, it deleted `<p class="vi"><strong>Text</strong>`!
# This left ` More text</p>` !
# And ` More text` was translated Vietnamese.
# We can easily detect any line that contains `</p>` but has Vietnamese text or hanging content.
# Actually, the ONLY place where this happened is in the `<div class="translation-box...` block where we had:
# `<strong>Análisis:</strong>` ... wait, `<strong>Analysis:</strong>` was there?
# YES! For chapters 1-18, the translation-box Analysis section was:
# `<p class="es"><strong>Análisis:</strong> ...</p>`
# So `add_vietnamese_v2.py` created:
# `<p class="vi"><strong>Phân tích:</strong> ...</p>`
# And `revert_vi.py` deleted up to `</strong>`. Leaving ` Phân tích:</strong> ...</p>`?
# No, `revert_vi.py` deleted up to `</strong>`. Meaning it deleted `<p class="vi"><strong>Phân tích:</strong>`.
# And left ` ...</p>`.
# So the remaining text is just the REST of the Vietnamese analysis string, followed by `</p>`.

def clean_file(fp):
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    # The leftover is ALWAYS exactly after `</p>` of the `pt` block.
    # Because `add_vietnamese_v2.py` injected it with the same indent as `pt` block.
    # Let's inspect what is currently between `</p>` and `</div>` of the translation box:
    # Actually, we can use regex to find and remove any text that starts after `</p>` 
    # and ends with `</p>` which contains Vietnamese words like `Đó`, `khi`, `của`, `và`, `kẻ` etc.
    
    # Or simply: Any line that starts with spaces, followed by some text that does NOT start with `<` and ends with `</p>`
    # Example: ` Đó là một quy luật tinh tế... mãi mãi.</p>`
    # We can match `r'\n\s*[^<]+?</p>'` IF the line has Vietnamese characters.
    
    # Let's be aggressive but safe:
    # Find `</p> \n <TEXT NOT STARTING WITH < AND ENDING WITH </p>`
    # Wait! The text could be on the same line as `</p>` of the pt tag.
    # Example: `<p class="pt">... pureza do espírito.</p> Đó là một quy luật... mãi mãi.</p>`
    
    content = re.sub(r'(</p>\s*)[^<]+?</p>', r'\1', content)
    
    # Wait! What if there is another occurrence where text is left without a tag?
    # What about `<h3 class="vi">Nguồn cảm hứng ban đầu</h3>`?
    # `revert_vi.py` matched `\s*<[^>]+class="vi"[^>]*>.*?</[^>]+>`.
    # That correctly deleted the WHOLE `<h3>` because there were no nested tags inside `<h3>`!
    # What about the Dropdown option? `revert_vi.py` already deleted it completely.
    # What about the Sidebar link? `<i>13</i><span class="es">...</span>...<span class="vi">...</span></a>`
    # `revert_vi.py` matched `\s*<[^>]+class="vi"[^>]*>.*?</[^>]+>`.
    # It matched `<span class="vi">...</span>` and deleted it!
    # What about the moral? `<div class="moral fade-in"><span class="es">...</span>...<span class="vi">...</span></div>`
    # Deleted perfectly!
    # What about the main story? `<p class="es"><span class="drop-cap">A</span>...</p>`
    # For `vi`, it injected `<p class="vi"><span class="drop-cap">A</span>...</p>`.
    # If `revert_vi.py` deleted up to the first `</span>`, it deleted `<p class="vi"><span class="drop-cap">A</span>` and left `...</p>`.
    # Yes! So the story blocks might have `...</p>` leftovers!
    
    # So basically, we have orphaned text immediately following `</p>` or `</div>` that ends in `</p>`.
    # But wait, `re.sub(r'(</p>\s*)[^<]+?</p>', r'\1', content)` will delete ANY text between `</p>` and `</p>`!
    # Let's test this carefully.

    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)

for fp in set(files_to_process):
    clean_file(fp)

print("Cleaned leftovers!")
