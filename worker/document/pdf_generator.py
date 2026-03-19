"""Generate a formatted PDF document from OCR results using ReportLab."""

import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generate_pdf(text: str, output_dir: str, filename: str = "result.pdf") -> str:
    """
    Create a PDF with the OCR text using ReportLab.
    Each double-newline-separated block becomes a paragraph.
    Returns the file path.
    """
    path = os.path.join(output_dir, filename)
    doc = SimpleDocTemplate(path, pagesize=A4)
    styles = getSampleStyleSheet()

    story = [
        Paragraph("Digitized Document", styles["Title"]),
        Spacer(1, 14),
    ]

    for paragraph in text.split("\n\n"):
        para = paragraph.strip()
        if para:
            # Replace newlines inside a paragraph with <br/> for ReportLab
            html_para = para.replace("\n", "<br/>")
            story.append(Paragraph(html_para, styles["Normal"]))
            story.append(Spacer(1, 8))

    doc.build(story)
    return path
