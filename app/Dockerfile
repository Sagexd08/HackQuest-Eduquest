FROM python:3.9-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    PORT=5000

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs directory
RUN mkdir -p logs && \
    chmod -R 777 logs

# Expose port
EXPOSE 5000

# Set the entrypoint to use gunicorn
ENTRYPOINT ["gunicorn"]

# Configure the CMD to set gunicorn parameters
CMD ["--bind", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "--log-level", "info", "app:app"]
