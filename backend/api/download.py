import os

from fastapi import APIRouter, HTTPException, Path
from fastapi.responses import FileResponse

from config import settings
from services.queue_service import get_job

router = APIRouter()

MIME_TYPES: dict[str, str] = {
    "txt": "text/plain",
    "docx": (
        "application/vnd.openxmlformats-officedocument"
        ".wordprocessingml.document"
    ),
    "pdf": "application/pdf",
}


@router.get(
    "/download/{job_id}/{fmt}",
    summary="Download the digitized output file",
)
async def download_file(
    job_id: str = Path(..., description="Job ID returned from /api/upload"),
    fmt: str = Path(..., pattern="^(txt|docx|pdf)$", description="Output format"),
):
    """
    Download the processed file in TXT, DOCX, or PDF format.
    Only available after job status is 'completed'.
    """
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found.")
    if job["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail=f"Job is not completed yet. Current status: {job['status']}",
        )
    if fmt not in job.get("output_formats", []):
        raise HTTPException(
            status_code=404,
            detail=f"Format '{fmt}' not available for this job.",
        )

    file_path = os.path.join(settings.OUTPUT_DIR, job_id, f"result.{fmt}")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Output file missing on disk.")

    return FileResponse(
        path=file_path,
        media_type=MIME_TYPES[fmt],
        filename=f"digitized_{job_id[:8]}.{fmt}",
    )
