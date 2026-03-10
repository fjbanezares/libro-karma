import os
import shutil

chapters = [
    "13_amor_y_respeto",
    "14_peso_deudores",
    "15_desperdicio_y_escasez",
    "16_adiccion_y_ceguera",
    "17_orfandad_filial",
    "18_pereza_laboral"
]

images = {
    "13_amor_y_respeto": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_13_juxtaposition_1773108905919.png",
    "14_peso_deudores": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_14_juxtaposition_1773108944598.png",
    "15_desperdicio_y_escasez": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_15_juxtaposition_1773108981284.png",
    "16_adiccion_y_ceguera": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_16_juxtaposition_1773109018575.png",
    "17_orfandad_filial": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_17_juxtaposition_1773109057613.png",
    "18_pereza_laboral": "/Users/fjbanezares/.gemini/antigravity/brain/786ec5d2-344e-439c-94a9-35c2afec7d1f/karma_18_juxtaposition_1773109097200.png"
}

for ch in chapters:
    hero_path = f"{ch}/web/assets/hero.jpg"
    art_path = f"{ch}/web/assets/art.jpg"
    
    # 1. Verify if we need to copy hero -> art
    # If art doesn't exist, we rename hero to art
    if os.path.exists(hero_path) and not os.path.exists(art_path):
        # We rename the old beautiful scene to art.jpg
        shutil.move(hero_path, art_path)
        print(f"Moved {hero_path} -> {art_path}")
    elif os.path.exists(hero_path) and os.path.exists(art_path):
        # Already moved? Wait, let's just make sure.
        pass

    # 2. Copy the new juxtaposition image to hero.jpg
    new_hero_src = images[ch]
    shutil.copy(new_hero_src, hero_path)
    print(f"Copied juxtaposition {new_hero_src} -> {hero_path}")

print("Assets distribution complete.")
