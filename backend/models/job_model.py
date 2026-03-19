from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class JobStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class JobResponse(BaseModel):
    job_id: str
    status: JobStatus
    filename: str
    file_type: str
    message: str = ""
    output_formats: List[str] = []
    error: Optional[str] = None
    created_at: str
