from pdf2image import convert_from_path
from pathlib import Path

def pdf_to_image(pdf_path: str, output_path: str, dpi: int = 400):
    pages = convert_from_path(pdf_path, dpi=dpi)

    if not pages:
        raise RuntimeError("No pages found in PDF")

    image_path = Path(output_path)
    pages[0].save(image_path, "PNG")

    return str(image_path)
