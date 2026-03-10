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

with open("chapters_13_18_data.json", "r", encoding='utf8') as f:
    cdata = json.load(f)

langs = ["es", "en", "it", "zh", "ar", "ru", "de", "fr", "ja", "pt"]
romans = {"13": "XIII", "14": "XIV", "15": "XV", "16": "XVI", "17": "XVII", "18": "XVIII"}

with open("index.html", "r", encoding='utf8') as f:
    html = f.read()

# For each chapter, we build a chapter-card:
# <a href="13_amor_y_respeto/web/index.html" class="chapter-card fade-in">
#   <div class="card-number">XIII</div>
#   <div class="card-content">
#       <h2><span class="es">...</span>...</h2>
#   </div>
# </a>

new_cards = ""
for ch in new_chapters:
    ch_num = ch.split("_")[0]
    roman = romans[ch_num]
    titles = "".join([f'<span class="{l}">{cdata[ch]["title"][l]}</span>' for l in langs])
    new_cards += f"""
        <a href="{ch}/web/index.html" class="chapter-card fade-in">
            <div class="card-number">{roman}</div>
            <div class="card-content">
                <h2>{titles}</h2>
            </div>
        </a>"""

# Insert the cards right after the Chapter 12 card.
# Search for `href="12_peso_injusticia[...]" [...] </a>`
# and insert new_cards after it.
html = re.sub(r'(<a href="12_peso_injusticia/web/index\.html" class="chapter-card fade-in">[\s\S]*?</a>)', r'\1\n' + new_cards, html)

with open("index.html", "w", encoding='utf8') as f:
    f.write(html)
print("Updated index.html page with cards!")
