import pytesseract
from PIL import Image

def run_ocr(image_path: str, output_text_path: str):
    img = Image.open(image_path)

    config = "--oem 1 --psm 6"

    text = pytesseract.image_to_string(
        img,
        lang="eng",
        config=config
    )

    with open(output_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return text
