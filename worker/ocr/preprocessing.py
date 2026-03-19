"""Image preprocessing utilities for TrOCR input."""

from PIL import Image, ImageFilter


def to_rgb(image: Image.Image) -> Image.Image:
    """Convert any image mode to RGB."""
    if image.mode != "RGB":
        return image.convert("RGB")
    return image


def resize_for_trocr(image: Image.Image, target_height: int = 384) -> Image.Image:
    """Scale image to target height while preserving aspect ratio."""
    w, h = image.size
    if h == target_height:
        return image
    ratio = target_height / h
    return image.resize((int(w * ratio), target_height), Image.LANCZOS)


def denoise(image: Image.Image) -> Image.Image:
    """Apply a gentle median filter to reduce noise."""
    return image.filter(ImageFilter.MedianFilter(size=3))


def preprocess(image: Image.Image) -> Image.Image:
    """Full preprocessing pipeline: RGB → denoise → resize."""
    image = to_rgb(image)
    image = denoise(image)
    image = resize_for_trocr(image)
    return image
