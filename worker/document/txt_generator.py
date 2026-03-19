"""Generate plain-text output from OCR results."""

import os


def generate_txt(text: str, output_dir: str, filename: str = "result.txt") -> str:
    """Write OCR text to a .txt file. Returns the file path."""
    path = os.path.join(output_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path
