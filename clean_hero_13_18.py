import os
import glob

chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]

for ch in chapters:
    # 1. delete hero.png
    png_path = f"{ch}/web/assets/hero.png"
    if os.path.exists(png_path):
        os.remove(png_path)
        print(f"Deleted {png_path}")
    
    # 2. replace hero.png with hero.jpg in index.html
    # Also fix alt="Karma XII"
    html_path = f"{ch}/web/index.html"
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
        
        html = html.replace('hero.png', 'hero.jpg')
        # We can also fix the Alt tags, but just replacing the extension is the main priority.
        # Oh, let's fix Karma XII to Karma XIII, XIV..
        romans = {"13": "XIII", "14": "XIV", "15": "XV", "16": "XVI", "17": "XVII", "18": "XVIII"}
        roman = romans[ch[:2]]
        html = html.replace('Karma XII', f'Karma {roman}')
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Updated {html_path}")

print("Done cleaning up legacy hero.png")
