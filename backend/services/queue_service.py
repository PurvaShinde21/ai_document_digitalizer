import json
import uuid
from datetime import datetime, timezone

import redis

from config import settings
from models.job_model import JobStatus

_redis_client = None


def get_redis() -> redis.Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.from_url(settings.REDIS_URL, decode_responses=True)
    return _redis_client


def create_job(filename: str, file_type: str) -> str:
    """Create a new job entry in Redis. Returns the job_id."""
    job_id = str(uuid.uuid4())
    job_data = {
        "job_id": job_id,
        "status": JobStatus.PENDING.value,
        "filename": filename,
        "file_type": file_type,
        "output_formats": json.dumps([]),
        "error": "",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    r = get_redis()
    r.hset(f"job:{job_id}", mapping=job_data)
    r.expire(f"job:{job_id}", 60 * 60 * 24)  # auto-expire after 24 hours
    return job_id


def get_job(job_id: str) -> dict | None:
    """Fetch job data from Redis. Returns None if not found."""
    r = get_redis()
    data = r.hgetall(f"job:{job_id}")
    if not data:
        return None
    # Deserialize the JSON list back to a Python list
    data["output_formats"] = json.loads(data.get("output_formats", "[]"))
    return data


def update_job_status(
    job_id: str,
    status: JobStatus,
    error: str = "",
    output_formats: list | None = None,
) -> None:
    """Update job status (and optionally output_formats) in Redis."""
    r = get_redis()
    updates = {"status": status.value, "error": error or ""}
    if output_formats is not None:
        updates["output_formats"] = json.dumps(output_formats)
    r.hset(f"job:{job_id}", mapping=updates)
