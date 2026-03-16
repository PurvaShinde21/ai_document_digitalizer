# AI Handwritten Document Digitizer

> Convert handwritten documents into searchable digital text using AI/ML.

## Overview

This project is a full-stack AI web application that uses **Microsoft TrOCR** (Transformer-based OCR) to recognize handwritten text from uploaded images and PDFs. Users upload a document, the ML pipeline processes it asynchronously, and the result is available for download in **TXT**, **DOCX**, or **PDF** format.

## Architecture

```
User → Next.js Frontend (Vercel)
     → FastAPI Backend (Render)
     → Redis Queue
     → ML Worker (TrOCR Pipeline)
     → Output Storage (S3 / Local)
     → Back to Frontend (Download)
```

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js (React) |
| Backend | FastAPI (Python) |
| ML Model | microsoft/trocr-base-handwritten |
| Queue | Redis (via RQ) |
| Storage | Local → AWS S3 / Cloudflare R2 |
| Deployment | Vercel (frontend) + Render (backend + worker) |

## Project Structure

```
ai-document-digitizer/
├── frontend/       # Next.js UI
├── backend/        # FastAPI REST API
├── worker/         # ML pipeline & Redis worker
├── experiments/    # Dataset loading & evaluation notebooks
├── infrastructure/ # Terraform, K8s, Nginx configs
├── tests/          # pytest test suites
├── scripts/        # Helper shell/Python scripts
└── docker-compose.yml
```

## Getting Started

> Full setup instructions coming in Phase 5 (Docker + local end-to-end).

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/ai-document-digitizer.git
cd ai-document-digitizer

# 2. Copy environment variables
cp .env.example .env
# Edit .env with your real values

# 3. Start all services
docker-compose up --build
```

## Development Phases

| Phase | Description | Status |
|---|---|---|
| 1 | Project scaffold & Git setup | ✅ Complete |
| 2 | FastAPI backend | 🔲 Pending |
| 3 | ML worker & OCR pipeline | 🔲 Pending |
| 4 | Next.js frontend | 🔲 Pending |
| 5 | Docker & local end-to-end | 🔲 Pending |
| 6 | Experiments & evaluation | 🔲 Pending |
| 7 | Tests & CI/CD | 🔲 Pending |
| 8 | Infrastructure (optional) | 🔲 Pending |
| 9 | README & docs | 🔲 Pending |

## License

MIT
