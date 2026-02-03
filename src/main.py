from pathlib import Path

from pdf_to_image import pdf_to_image
from preprocess import preprocess_image
from ocr import run_ocr
from postprocess import clean_ocr_text

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PDF = BASE_DIR / "input" / "inv1.pdf"
OUTPUT_DIR = BASE_DIR / "output"

IMAGE_PATH = OUTPUT_DIR / "image.png"
PREPROCESSED_PATH = OUTPUT_DIR / "preprocessed.png"
OCR_RAW_PATH = OUTPUT_DIR / "ocr_raw.txt"
OCR_CLEAN_PATH = OUTPUT_DIR / "ocr_clean.txt"


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("1️⃣ Converting PDF to image...")
    pdf_to_image(str(INPUT_PDF), str(IMAGE_PATH))

    print("2️⃣ Preprocessing image...")
    preprocess_image(str(IMAGE_PATH), str(PREPROCESSED_PATH))

    print("3️⃣ Running Tesseract OCR...")
    run_ocr(str(PREPROCESSED_PATH), str(OCR_RAW_PATH))

    print("4️⃣ Cleaning OCR output...")
    clean_ocr_text(str(OCR_RAW_PATH), str(OCR_CLEAN_PATH))

    print("\n✅ OCR pipeline completed")
    print(f"➡ image: {IMAGE_PATH}")
    print(f"➡ preprocessed: {PREPROCESSED_PATH}")
    print(f"➡ raw OCR: {OCR_RAW_PATH}")
    print(f"➡ cleaned OCR: {OCR_CLEAN_PATH}")


if __name__ == "__main__":
    main()
