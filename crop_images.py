from PIL import Image
import os

img = Image.open('imagenes_originales/foto_templo_2.jpg')
width, height = img.size

# We want the FULL width for the cause-effect panel.
left = 0
right = 478

# Adjust height blocks exactly 1024 / 6 ~= 170. Let's see:
boxes = [
    (left, 80, right, 220),   # Cap 7
    (left, 220, right, 350),  # Cap 8
    (left, 350, right, 470),  # Cap 9
    (left, 470, right, 590),  # Cap 10
    (left, 590, right, 720),  # Cap 11
    (left, 720, right, 880),  # Cap 12
]

chapters = [
    "07_manos_del_mal",
    "08_pedestal_soberbia",
    "09_frio_egoismo",
    "10_infierno_sombras",
    "11_mirada_desprecio",
    "12_peso_injusticia"
]

for i, box in enumerate(boxes):
    chap = chapters[i]
    crop = img.crop(box)
    out_path = f"{chap}/web/assets/pasaje_original.jpg"
    crop.save(out_path)
    print(f"Saved {out_path}")
