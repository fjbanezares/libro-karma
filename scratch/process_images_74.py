import os
from PIL import Image
import shutil

# Paths
brain_dir = "/Users/fjbanezares/.gemini/antigravity/brain/0d30a346-2c48-4874-b2b8-c6c36516d8e3"
hero_src = os.path.join(brain_dir, "ch74_hero_1779244690430.png")
art_src = os.path.join(brain_dir, "ch74_art_1779244714157.png")
original_mural_src = "/Users/fjbanezares/libro del karma/imagenes_originales/imagen74.png"

dest_assets_dir = "/Users/fjbanezares/libro del karma/74_complices_del_destino/web/assets"

# Create directories
os.makedirs(dest_assets_dir, exist_ok=True)
print("Created assets directory.")

# 1. Process hero.jpg (Diptych Cause & Effect)
if os.path.exists(hero_src):
    img_hero = Image.open(hero_src)
    # The generated image is square and perfect. Let's save as JPG with quality=92
    hero_dst = os.path.join(dest_assets_dir, "hero.jpg")
    img_hero.convert("RGB").save(hero_dst, "JPEG", quality=92)
    print(f"Processed and saved hero.jpg to {hero_dst}")
else:
    print(f"Error: Hero source not found at {hero_src}")

# 2. Process art.jpg (Circular naive signature)
if os.path.exists(art_src):
    img_art = Image.open(art_src)
    # The image is already square. We can save as JPG with quality=92
    art_dst = os.path.join(dest_assets_dir, "art.jpg")
    img_art.convert("RGB").save(art_dst, "JPEG", quality=92)
    print(f"Processed and saved art.jpg to {art_dst}")
else:
    print(f"Error: Art source not found at {art_src}")

# 3. Copy pasaje_original.png
if os.path.exists(original_mural_src):
    mural_dst = os.path.join(dest_assets_dir, "pasaje_original.png")
    shutil.copy(original_mural_src, mural_dst)
    print(f"Copied original mural image to {mural_dst}")
else:
    print(f"Error: Original mural source not found at {original_mural_src}")

print("Image processing complete!")
