import os
from PIL import Image, ImageDraw, ImageFont
import random


def create_placeholder(name, filename):
    width = 600
    height = 400
    color = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))

    img = Image.new("RGB", (width, height), color=color)
    d = ImageDraw.Draw(img)

    # Try to load a font, fallback to default
    try:
        font = ImageFont.truetype("Arial", 40)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text position (approximate centering)
    text = name
    bbox = d.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) / 2, (height - text_height) / 2)

    d.text(position, text, fill=(255, 255, 255), font=font)

    path = os.path.join("store/static/store/images", filename)
    img.save(path)
    print(f"Generated {path}")


candies = {
    "Chocolate Bar": "chocolate_bar.png",
    "Gummy Bears": "gummy_bears.png",
    "Lollipop": "lollipop.png",
    "Jelly Beans": "jelly_beans.png",
    "Caramel": "caramel.png",
    "Sour Patch Kids": "sour_patch_kids.png",
    "Peppermint": "peppermint.png",
    "Dark Chocolate": "dark_chocolate.png",
}

os.makedirs("store/static/store/images", exist_ok=True)

for name, filename in candies.items():
    create_placeholder(name, filename)
