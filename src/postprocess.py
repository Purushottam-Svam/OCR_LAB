import re

def clean_ocr_text(raw_text_path: str, cleaned_text_path: str):
    with open(raw_text_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Normalize whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Common OCR corrections
    replacements = {
        "1NV0ICE": "INVOICE",
        "0RD": "ORD",
        "TOTAl": "TOTAL",
        "SHP": "SHIP",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    with open(cleaned_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return text
