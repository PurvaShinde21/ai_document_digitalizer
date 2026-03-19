import os

import aiofiles
from fastapi import UploadFile

from config import settings

# Allowed MIME types and their extensions
ALLOWED_TYPES: dict[str, str] = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/tiff": ".tiff",
    "image/webp": ".webp",
    "application/pdf": ".pdf",
}


def validate_file(file: UploadFile, content: bytes) -> None:
    """Raise ValueError if file type or size is invalid."""
    if file.content_type not in ALLOWED_TYPES:
        raise ValueError(
            f"Unsupported file type: '{file.content_type}'. "
            f"Allowed formats: JPEG, PNG, TIFF, WebP, PDF."
        )
    if len(content) > settings.max_upload_bytes:
        raise ValueError(
            f"File size exceeds limit of {settings.MAX_UPLOAD_SIZE_MB} MB."
        )


async def save_upload(job_id: str, filename: str, content: bytes) -> str:
    """Persist uploaded file to disk. Returns the absolute file path."""
    upload_dir = os.path.join(settings.UPLOAD_DIR, job_id)
    os.makedirs(upload_dir, exist_ok=True)
    # Sanitize filename to avoid path traversal
    safe_name = os.path.basename(filename)
    file_path = os.path.join(upload_dir, safe_name)
    async with aiofiles.open(file_path, "wb") as f:
        await f.write(content)
    return file_path


def get_output_dir(job_id: str) -> str:
    """Return (and create) the output directory for a job."""
    output_dir = os.path.join(settings.OUTPUT_DIR, job_id)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
