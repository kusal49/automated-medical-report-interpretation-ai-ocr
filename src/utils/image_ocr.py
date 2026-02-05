from paddleocr import PaddleOCR
import numpy as np
from PIL import Image
import streamlit as st

ocr = PaddleOCR(
    use_angle_cls=False,
    lang="en"
)

MAX_ALLOWED_SIDE = 2000  # STRICT LIMIT


def extract_text_from_image(image_file):
    image = Image.open(image_file).convert("RGB")
    width, height = image.size
    max_side = max(width, height)

    # ❌ HARD BLOCK LARGE IMAGES
    if max_side > MAX_ALLOWED_SIDE:
        st.error(
            f"❌ Image too large ({width}×{height}).\n\n"
            f"Please resize the image so the longest side is **≤ {MAX_ALLOWED_SIDE}px** "
            "and upload again."
        )
        return None  # important: stop pipeline

    image_np = np.array(image)

    with st.spinner("🔍 Extracting text from image…"):
        result = ocr.ocr(image_np)

    if not result:
        return ""

    return "\n".join(word[1][0] for line in result for word in line)
