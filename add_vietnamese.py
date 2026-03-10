import os
import re
import time
import json
from deep_translator import GoogleTranslator

# Folders to scan
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
    fp = os.path.join(d, "web", "index.html")
    if os.path.exists(fp): files_to_process.append(fp)
    # Also check index.html / linktree in root
    if d == ".":
        if os.path.exists("index.html"): files_to_process.append("index.html")
        if os.path.exists("linktree.html"): files_to_process.append("linktree.html")
    if d == "biblioteca":
        if os.path.exists("biblioteca/index.html"): files_to_process.append("biblioteca/index.html")

print(f"Found {len(files_to_process)} HTML files to inject Vietnamese.")

# Translation cache
t_cache = {}
CACHE_FILE = "vi_translation_cache.json"
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        t_cache = json.load(f)

def get_vi_trans(text_es):
    if text_es in t_cache:
        return t_cache[text_es]
    
    for i in range(5):
        try:
            res = GoogleTranslator(source='es', target='vi').translate(text_es)
            t_cache[text_es] = res
            return res
        except Exception as e:
            time.sleep(2)
    return text_es

# We need a highly robust regex to capture from <TAG class="es"> up to <TAG class="pt">.
# Because the contents inside <TAG class="es"> could contain HTML (like <i> or <strong>),
# we use `.*?` for the text.

pat = re.compile(
    r'(?P<whole><(?P<tag>[a-zA-Z1-6]+)\s+class="es"(?P<attrs>[^>]*)>(?P<text>.*?)</(?P=tag)>'
    r'[\s\S]*?'
    r'<(?P=tag2>sameas_tag_placeholder)\s+class="pt"[^>]*>.*?</(?P=tag3>sameas_tag_placeholder)>)',
    # wait, python re module doesn't easily support backreferencing dynamically for different groups in one pass 
    # without compiling per match or using complex syntax if the tag varies.
    # Actually, (?P=tag) requires the EXACT same string. So we just use (?P=tag) again!
)

# A better approach: 
# Find ALL <TAG class="pt" ...> in the file. 
# Oh wait, we need the SPANISH text to translate!
# Okay, so we find <... class="es" ...> TEXT </...>.
# Then we find the VERY NEXT <... class="pt" ...> TEXT </...>.
# BUT wait! If we do it like this, what if they aren't right next to each other? They always are.

# Let's write a block-level regex since they are perfectly grouped:
pat = re.compile(r'(<(?P<tag>[a-zA-Z1-6]+)\s+class="es"(?P<attrs>[^>]*)>(?P<text>.*?)</(?P=tag)>[\s\S]*?<(?P=tag2>[a-zA-Z1-6]+)\s+class="pt"[^>]*>.*?</(?P=tag3>[a-zA-Z1-6]+)>)')

def replacer(match):
    whole = match.group(1)
    tag = match.group('tag')
    attrs = match.group('attrs')
    text_es = match.group('text')
    tag_pt = match.group('tag2')
    
    # Check if there's already a class="vi" right after this block? No, our regex stops at `</pt_tag>`. 
    # But what if there's a nested structure? Unlikely in our flat spans/p.
    # Check if 'class="vi"' is in the `whole` text (just in case) - shouldn't be.
    
    # Only translate if tag == tag_pt 
    if tag != tag_pt:
        return whole # Safety

    trans = get_vi_trans(text_es)
    
    # Extract indentation of the pt tag to format it beautifully
    pt_split = whole.split('<' + tag + ' class="pt"')
    if len(pt_split) == 2:
        last_newlines = pt_split[0].split('\n')
        indent = "\n" + last_newlines[-1] if not last_newlines[-1].strip() else "\n"
    else:
        indent = "\n"
        
    vi_tag = f'<{tag} class="vi"{attrs}>{trans}</{tag}>'
    
    return whole + indent + vi_tag

for fp in files_to_process:
    with open(fp, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Dropdown
    if 'data-lang="vi"' not in html and 'data-lang="pt"' in html:
        # insert vi option after pt option
        pt_opt = r'<div class="lang-opt" data-lang="pt" onclick="setLanguage\(\'pt\'\)"><span class="flag">🇵🇹</span> Português</div>'
        vi_opt = r'<div class="lang-opt" data-lang="vi" onclick="setLanguage(\'vi\')"><span class="flag">🇻🇳</span> Tiếng Việt</div>'
        html = re.sub(f'({pt_opt})', r'\1\n                    ' + vi_opt, html)

    # 2. Add language to the chapter content via replacer!
    # BUT first, what if it's already translated?
    # Actually, we can just split the file if it doesn't have vi.
    if '<span class="vi">' not in html and '<p class="vi">' not in html and '<h' not in html: pass # well...
    
    new_html, count = pat.subn(replacer, html)
    
    # 3. Save
    with open(fp, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Injected {count} Vietnamese blocks in {fp}")

# Save Cache
with open(CACHE_FILE, "w") as f:
    json.dump(t_cache, f, ensure_ascii=False, indent=2)

print("Vietnamese translation complete!")
