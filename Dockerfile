# === Build stage ===
FROM python:3.11-alpine AS build

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
WORKDIR /app

# 빌드에 필요한 라이브러리(헤더/컴파일러 포함)
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    libjpeg-turbo-dev \
    zlib-dev

# pip 최신화 + 파이썬 패키지 설치
COPY requirements.txt .
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# === Runtime stage ===
FROM python:3.11-alpine AS runtime

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# 런타임에만 필요한 라이브러리
RUN apk add --no-cache \
    libpq \
    libjpeg-turbo \
    zlib \
    tzdata \
    netcat-openbsd

# 빌드 결과(설치된 site-packages 등)와 앱 복사
COPY --from=build /usr/local /usr/local
COPY --from=build /app /app

# 포트/명령은 compose에서 지정 (예: gunicorn)
# EXPOSE 8000
# CMD ["gunicorn", "drfproject.wsgi:application", "-b", "0.0.0.0:8000"]
