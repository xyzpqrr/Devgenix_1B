# Use a slim Python base image
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory to root of container
WORKDIR /

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy your whole project into container root
COPY . .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Pre-download bge-small model into image for offline use
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('BAAI/bge-small-en')"

# Entrypoint
CMD ["python", "main.py"]
