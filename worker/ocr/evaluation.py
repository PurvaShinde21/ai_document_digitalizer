"""
CER (Character Error Rate) and WER (Word Error Rate) evaluation
using the jiwer library.

Install: pip install jiwer
"""

from jiwer import cer, wer


def character_error_rate(reference: str, hypothesis: str) -> float:
    """
    Compute Character Error Rate (CER).
    CER = (substitutions + insertions + deletions) / total characters in reference
    Lower is better. 0.0 = perfect, 1.0 = completely wrong.
    """
    return cer(reference, hypothesis)


def word_error_rate(reference: str, hypothesis: str) -> float:
    """
    Compute Word Error Rate (WER).
    WER = (substitutions + insertions + deletions) / total words in reference
    Lower is better. 0.0 = perfect.
    """
    return wer(reference, hypothesis)


def evaluate(reference: str, hypothesis: str) -> dict:
    """Return a dict with both CER and WER for a prediction pair."""
    return {
        "cer": round(character_error_rate(reference, hypothesis), 4),
        "wer": round(word_error_rate(reference, hypothesis), 4),
    }
