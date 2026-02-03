import cv2
import numpy as np

def preprocess_image(input_image_path: str, output_image_path: str):
    img = cv2.imread(input_image_path)

    if img is None:
        raise RuntimeError("Failed to load image")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction
    gray = cv2.medianBlur(gray, 3)

    # Binarization (critical for dot-matrix / fax invoices)
    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imwrite(output_image_path, thresh)
    return output_image_path
