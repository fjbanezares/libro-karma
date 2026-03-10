import os
import re

chapters = [
    "00_introduccion", "01_esfuerzo_desinteresado", "02_fidelidad_y_familia",
    "03_generosidad_y_prosperidad", "04_respeto_por_la_vida", "05_pureza_mental",
    "06_sobriedad_y_claridad", "07_manos_del_mal", "08_pedestal_soberbia",
    "09_frio_egoismo", "10_infierno_sombras", "11_mirada_desprecio", "12_peso_injusticia"
]

for ch in chapters:
    # We only care about chapters 1-12 for this particular fix
    if ch == "00_introduccion":
        continue
        
    html_path = f"{ch}/web/index.html"
    if not os.path.exists(html_path):
        continue
    
    # Check which image exists to use as secondary image:
    img_name = ""
    if os.path.exists(f"{ch}/web/assets/hero_v1.png"):
        img_name = "hero_v1.png"
    elif os.path.exists(f"{ch}/web/assets/hero.png"):
        img_name = "hero.png"
    elif os.path.exists(f"{ch}/web/assets/hero.jpg"):
        img_name = "hero.jpg"
    elif os.path.exists(f"{ch}/web/assets/art.jpg"):
        img_name = "art.jpg"
        
    if not img_name:
        print(f"Warning: No secondary image found for {ch}")
        continue
        
    # Inject final-art block before `<div class="moral fade-in">` if it's not already there
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "final-art fade-in" not in content and '<div class="moral fade-in">' in content:
        art_block = f"""
            <div class="final-art fade-in" style="text-align: center; margin-top: 4rem; margin-bottom: 2rem;">
                <img src="assets/{img_name}" alt="Obra de Arte Karma" style="max-width: 100%; border-radius: 8px; border: 1px solid var(--gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            </div>
            """
        content = content.replace('<div class="moral fade-in">', art_block.lstrip('\n') + '\n            <div class="moral fade-in">')
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected lovely secondary image into {ch}")
    else:
        print(f"Skipped {ch} - already has final-art or missing moral block.")

