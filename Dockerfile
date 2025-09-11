# ---------- Base ----------
    FROM python:3.11-alpine
    ENV PYTHONUNBUFFERED=1 \
        PIP_DISABLE_PIP_VERSION_CHECK=1 \
        PIP_NO_CACHE_DIR=1
    
    WORKDIR /app
    
    # 런타임 라이브러리 (Pillow/cryptography용)
    RUN apk add --no-cache \
        openssl \
        libffi \
        libjpeg-turbo \
        zlib
    
    # 의존성 먼저 복사 (캐시 최적화)
    COPY requirements.txt /app/requirements.txt
    
    # 빌드시에만 필요한 헤더/툴
    RUN apk add --no-cache --virtual .build-deps \
            build-base \
            libffi-dev \
            openssl-dev \
            jpeg-dev \
            zlib-dev \
        && python -m pip install --upgrade pip setuptools wheel \
        && pip --version \
        && pip install --no-cache-dir -r /app/requirements.txt \
        && apk del .build-deps
    
    # 앱 소스
    COPY . /app/
    
    # 필요시 실행 커맨드/포트
    # EXPOSE 8000
    # CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
    