FROM python:3.11-slim

WORKDIR /app

# poppler-utils is required by pdf2image to convert PDFs → images
RUN apt-get update \
    && apt-get install -y --no-install-recommends poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies first (layer cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create local storage directories (used in development; replaced by R2 in prod)
RUN mkdir -p storage/uploads storage/outputs

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
