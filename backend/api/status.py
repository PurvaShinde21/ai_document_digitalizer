from fastapi import APIRouter, HTTPException

from services.queue_service import get_job

router = APIRouter()


@router.get("/status/{job_id}", summary="Get processing status of a job")
async def get_status(job_id: str):
    """
    Returns the current status of an OCR job.

    Status values:
    - pending    → queued, not yet started
    - processing → OCR pipeline is running
    - completed  → finished; outputs are ready for download
    - failed     → an error occurred (see 'error' field)
    """
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail=f"Job '{job_id}' not found.")
    return job
