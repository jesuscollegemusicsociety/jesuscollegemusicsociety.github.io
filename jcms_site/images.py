from pathlib import Path
from PIL import Image
import shutil

WIDTHS = [100, 200, 400, 800, 1600]
QUALITY = 90


def load_images(app):
    src = Path(app.root_path) / "images"
    dst = Path(app.root_path) / "static/dist/images"

    if dst.exists():
        shutil.rmtree(dst)

    for width in WIDTHS:
        (dst / f"{width}w").mkdir(parents=True, exist_ok=True)

    for img_path in src.iterdir():
        with Image.open(img_path) as img:
            for width in WIDTHS:
                ratio = width / img.width
                height = int(img.height * ratio)
                resized = img.resize((width, height), Image.Resampling.LANCZOS)
                out_path = (dst / f"{width}w" / img_path.stem).with_suffix(".webp")
                resized.save(out_path, "WEBP", quality=QUALITY)

        print(f"Processed {img_path.relative_to(src)}")

    app.jinja_env.globals["image_widths"] = WIDTHS
