from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import download, status, upload
from config import settings

app = FastAPI(
    title="AI Document Digitizer API",
    description=(
        "Handwritten document OCR powered by HuggingFace TrOCR "
        "(free-tier, no GPU required). Upload images or PDFs and "
        "download digitized text in TXT, DOCX, or PDF format."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(status.router, prefix="/api", tags=["Status"])
app.include_router(download.router, prefix="/api", tags=["Download"])


# ── Health ────────────────────────────────────────────────────────────────────
@app.get("/", tags=["Health"])
async def root():
    return {"message": "AI Document Digitizer API is running", "version": "1.0.0"}


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok"}
