"""
TrOCR inference via HuggingFace Inference API.

No local model download required.
Model: microsoft/trocr-small-handwritten
  - Free via HuggingFace Inference API (30,000 req/month)
  - ~270 MB if ever loaded locally (vs 1.3 GB for trocr-base)
"""

import io

import httpx
from PIL import Image

HF_API_URL = (
    "https://api-inference.huggingface.co/models/"
    "microsoft/trocr-small-handwritten"
)


def predict(image: Image.Image, hf_token: str) -> str:
    """
    Run TrOCR inference on a PIL image via HuggingFace Inference API.

    Args:
        image:     PIL Image (RGB) to recognize
        hf_token:  HuggingFace API token (free at huggingface.co/settings/tokens)

    Returns:
        Predicted text string.
    """
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)

    headers = {"Authorization": f"Bearer {hf_token}"}
    response = httpx.post(
        HF_API_URL,
        headers=headers,
        content=buf.read(),
        timeout=60.0,
    )
    response.raise_for_status()

    result = response.json()
    if isinstance(result, list) and result:
        return result[0].get("generated_text", "")
    return ""
