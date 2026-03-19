from fastapi import APIRouter, BackgroundTasks, File, HTTPException, UploadFile

from services.file_service import get_output_dir, save_upload, validate_file
from services.ocr_service import run_ocr_pipeline
from services.queue_service import create_job

router = APIRouter()


@router.post("/upload", summary="Upload a document for OCR processing")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
):
    """
    Accept an image (JPEG, PNG, TIFF, WebP) or PDF.
    Returns a job_id immediately. Processing runs in the background.
    Poll /api/status/{job_id} to track progress.
    """
    content = await file.read()

    try:
        validate_file(file, content)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    file_type = "pdf" if file.content_type == "application/pdf" else "image"

    # Create Redis job entry
    job_id = create_job(filename=file.filename, file_type=file_type)

    # Persist file to disk
    file_path = await save_upload(job_id, file.filename, content)
    out_dir = get_output_dir(job_id)

    # Non-blocking: OCR runs after response is sent
    background_tasks.add_task(run_ocr_pipeline, job_id, file_path, out_dir)

    return {
        "job_id": job_id,
        "status": "pending",
        "message": "File uploaded successfully. Processing started.",
    }
