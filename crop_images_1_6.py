from PIL import Image
import os

img_path = "imagenes_originales_/foto_1_6.jpg"
img = Image.open(img_path)

# Approximate coordinates for the 6 rows (left column pairs)
# Format: (left, top, right, bottom)
# Total size: 478x1024
boxes = {
    "01_esfuerzo_desinteresado": (55, 110, 385, 245),
    "02_fidelidad_y_familia": (50, 245, 385, 365),
    "03_generosidad_y_prosperidad": (50, 365, 385, 485),
    "04_respeto_por_la_vida": (45, 485, 385, 605),
    "05_pureza_mental": (40, 610, 385, 735),
    "06_sobriedad_y_claridad": (30, 740, 385, 875),
}

for chapter, box in boxes.items():
    crop_img = img.crop(box)
    target_dir = f"{chapter}/web/assets"
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "pasaje_original.jpg")
    crop_img.save(target_path, quality=95)
    print(f"Saved {target_path}")

print("Cropping complete.")
