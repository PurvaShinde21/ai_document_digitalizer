"""Text postprocessing utilities to clean raw OCR output."""

import re


def collapse_spaces(text: str) -> str:
    return re.sub(r" {2,}", " ", text)


def normalize_newlines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def rejoin_hyphenated(text: str) -> str:
    """Rejoin words split across lines with a hyphen."""
    return re.sub(r"(\w)-\n(\w)", r"\1\2", text)


def fix_common_substitutions(text: str) -> str:
    """Fix common OCR character substitution errors."""
    substitutions = {
        r"\b0\b": "O",   # lone zero → capital O (context-dependent)
        r"\bl\b": "I",   # lone lowercase L → capital I
    }
    for pattern, replacement in substitutions.items():
        text = re.sub(pattern, replacement, text)
    return text


def postprocess(text: str) -> str:
    """Apply all postprocessing steps."""
    text = rejoin_hyphenated(text)
    text = collapse_spaces(text)
    text = normalize_newlines(text)
    return text.strip()
