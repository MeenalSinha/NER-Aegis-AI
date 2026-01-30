# NER-Aegis AI - Production Dockerfile
# Multi-stage build for optimized container size

# Stage 1: Builder
FROM python:3.10-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.10-slim

# Set metadata
LABEL maintainer="NER-Aegis AI Team"
LABEL description="Landslide Risk Intelligence System for Northeast India"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Create non-root user for security
RUN groupadd -r aegis && useradd -r -g aegis aegis

# Set working directory
WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/aegis/.local

# Copy application files
COPY --chown=aegis:aegis app.py .
COPY --chown=aegis:aegis logic/ ./logic/
COPY --chown=aegis:aegis requirements.txt .
COPY --chown=aegis:aegis README.md .

# Create directory for data persistence
RUN mkdir -p /app/data && chown -R aegis:aegis /app/data

# Switch to non-root user
USER aegis

# Update PATH
ENV PATH=/home/aegis/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Expose port
EXPOSE 8501

# Run application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
