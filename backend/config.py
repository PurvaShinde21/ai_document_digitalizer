import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ── General ───────────────────────────────────
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    ALLOWED_ORIGINS: list = os.getenv(
        "ALLOWED_ORIGINS", "http://localhost:3000"
    ).split(",")
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "20"))

    # ── Redis (Upstash in prod, local in dev) ─────
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # ── Local Storage ─────────────────────────────
    UPLOAD_DIR: str = os.getenv("UPLOAD_DIR", "storage/uploads")
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "storage/outputs")

    # ── HuggingFace Inference API ─────────────────
    # Get a free token at: https://huggingface.co/settings/tokens
    HF_API_TOKEN: str = os.getenv("HF_API_TOKEN", "")
    # trocr-small-handwritten = ~270 MB (vs 1.3 GB for base) — free API, no local download
    TROCR_MODEL: str = os.getenv(
        "TROCR_MODEL", "microsoft/trocr-small-handwritten"
    )

    @property
    def hf_api_url(self) -> str:
        return f"https://api-inference.huggingface.co/models/{self.TROCR_MODEL}"

    @property
    def max_upload_bytes(self) -> int:
        return self.MAX_UPLOAD_SIZE_MB * 1024 * 1024


settings = Settings()
