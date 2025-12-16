FROM python:3.11-slim

# 1. System deps (keep minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Set workdir
WORKDIR /app

# 3. Install deps separately (layer caching, bitch)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy app
COPY . .

# 5. Expose port
EXPOSE 8000

# 6. Run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
