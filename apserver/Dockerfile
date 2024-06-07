# 開発用ステージ
FROM python:3.11.9-slim-bookworm AS developer

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    wget=1.21.3-1+b2 \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ビルドステージ
FROM python:3.11.9-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 本番ステージ
FROM gcr.io/distroless/python3-debian12:nonroot AS production

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
COPY --from=builder /app/ .

EXPOSE 8000
USER nonroot

CMD ["/app/opt/main.py"]
