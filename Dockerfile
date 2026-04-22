FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs output

CMD ["python3", "etl_pipeline.py", "--source", "all", "--mode", "full"]
