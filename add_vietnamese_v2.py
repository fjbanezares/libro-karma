import os
import re
import time
import json
from deep_translator import GoogleTranslator

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

print(f"Found {len(files_to_process)} HTML files to inject Vietnamese.")

t_cache = {}
CACHE_FILE = "vi_translation_cache.json"
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        t_cache = json.load(f)

def get_vi_trans(text_es):
    if text_es in t_cache:
        return t_cache[text_es]
    
    # Check if empty or only HTML tags without words
    if not text_es.strip() or text_es == "KARMA" or text_es.isdigit() or text_es.startswith("<"):
        # Not quite right to skip tags, but just translate.
        pass
        
    print(f"Translating to vi: {text_es[:30]}...")
    for i in range(5):
        try:
            res = GoogleTranslator(source='es', target='vi').translate(text_es)
            t_cache[text_es] = res
            return res
        except Exception as e:
            time.sleep(3)
    return text_es

pat = re.compile(r'(<(?P<tag>[a-zA-Z1-6]+)\s+class="es"(?P<attrs>[^>]*)>(?P<text>.*?)</(?P=tag)>[\s\S]*?<(?P<tag2>[a-zA-Z1-6]+)\s+class="pt"[^>]*>.*?</(?P=tag2)>)')

def replacer(match):
    whole = match.group(1)
    tag = match.group('tag')
    attrs = match.group('attrs')
    text_es = match.group('text')
    
    # Anti-duplication check: if there's already a .vi element after .pt, abort replacing.
    # But since regex stops at .pt, it doesn't see .vi unless .vi is INSIDE the block, which is impossible.
    # We must ensure we don't duplicate if script runs twice.
    # Actually, we do `with open -> if 'class="vi"' in html: return`. Handled outside.

    trans = get_vi_trans(text_es)
    
    # Beautifully indent
    lines = whole.split('\n')
    if len(lines) > 1:
        # get the indentation of the last line (<tag class="pt"...>)
        last_line_indent = lines[-1][:len(lines[-1])-len(lines[-1].lstrip())]
        vi_tag = f'\n{last_line_indent}<{tag} class="vi"{attrs}>{trans}</{tag}>'
    else:
        vi_tag = f'<{tag} class="vi"{attrs}>{trans}</{tag}>'
        
    return whole + vi_tag

for fp in set(files_to_process):
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()

    # Avoid duplicating translations if already done
    if 'class="vi"' in html:
        print(f"Skipping {fp}, already has vi.")
        continue

    # Update Dropdown Menu
    pt_opt_pat = re.compile(r'(<div class="lang-opt" data-lang="pt".*?</div>)')
    if 'data-lang="vi"' not in html:
        vi_opt = '<div class="lang-opt" data-lang="vi" onclick="setLanguage(\'vi\')"><span class="flag">🇻🇳</span> Tiếng Việt</div>'
        html = pt_opt_pat.sub(r'\1\n                    ' + vi_opt, html)

    # Inject
    new_html, count = pat.subn(replacer, html)
    
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Injected {count} Vietnamese blocks in {fp}")

with open(CACHE_FILE, "w", encoding="utf-8") as f:
    json.dump(t_cache, f, ensure_ascii=False, indent=2)

print("Vietnamese translation complete!")
