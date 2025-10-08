import re
import os
from re import Match
import pillow_heif
from PIL import Image
from pillow_heif import register_heif_opener

HEX_RE = re.compile(r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$')

register_heif_opener()

RESAMPLE = Image.Resampling.LANCZOS

def check_color(color: str) -> Match[str] | None:
    if not isinstance(color, str):
        raise TypeError("Invalid color")

    return HEX_RE.match(color)

def open_image(path: str) -> Image.Image:
    ext = os.path.splitext(path)[1].lower()
    try:
        img = Image.open(path)
        return img.convert("RGB")
    except Exception:
        if ext in [".heic", ".heif"]:
            if pillow_heif.is_supported(path):
                im = pillow_heif.open_heif(path, convert_hdr_to_8bit=False)
                return im.to_pillow().convert("RGB")
            else:
                raise ValueError("Unsupported HEIF format: " + path)
        else:
            raise


def resize_image(img):
    max_width = 120

    aspect_ratio = 0.55

    new_height = int(max_width * img.height / img.width * aspect_ratio)

    return img.resize((max_width, new_height), RESAMPLE)