FROM python:3.12.7-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["shiny", "run", "--host", "0.0.0.0", "--port", "8000", "app.py"]