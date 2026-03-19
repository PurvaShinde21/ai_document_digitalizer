# AI Handwritten Document Digitizer

> Convert handwritten documents into searchable digital text using AI — **100% free to run**.

## Architecture

```
User → Next.js Frontend (Vercel, free)
     → FastAPI Backend (Render, 512MB RAM — no model loaded)
       └── BackgroundTask: HuggingFace Inference API (trocr-small-handwritten)
     → Upstash Redis (job status, free tier)
     → Local storage / Cloudflare R2 (file storage)
```

## Project Structure

```
ai-document-digitizer/
├── frontend/               # Next.js UI (Vercel)
│   ├── src/
│   │   ├── components/     # FileUpload, ProgressBar, DownloadButton
│   │   ├── pages/          # index.jsx, results/[jobId].jsx
│   │   └── services/       # api.js (Axios client)
│   └── package.json
│
├── backend/                # FastAPI API (Render)
│   ├── api/                # upload.py, status.py, download.py
│   ├── models/             # job_model.py (Pydantic)
│   ├── services/
│   │   ├── ocr_service.py  # Full pipeline (replaces worker)
│   │   ├── queue_service.py
│   │   └── file_service.py
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── worker/                 # OCR modules (reference / experiments)
│   ├── ocr/                # trocr_model.py, preprocessing.py, etc.
│   └── document/           # txt, docx, pdf generators
│
├── experiments/            # Dataset loading & evaluation notebooks
├── tests/                  # pytest suites
├── docker-compose.yml      # Dev: backend + redis + frontend
├── .env.example
└── README.md
```


## License

MIT
