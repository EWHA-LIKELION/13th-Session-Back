FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1 PIP_DISABLE_PIP_VERSION_CHECK=1 PIP_NO_CACHE_DIR=1 PIP_ROOT_USER_ACTION=ignore
WORKDIR /app

# 런타임 라이브러리
RUN apk add --no-cache \
    openssl \
    libffi \
    libjpeg-turbo \
    zlib \
    mariadb-connector-c

# 의존성 설치
COPY requirements.txt /app/requirements.txt
RUN apk add --no-cache --virtual .build-deps \
      build-base libffi-dev openssl-dev jpeg-dev zlib-dev \
      mariadb-connector-c-dev pkgconf \
 && python -m pip install --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r /app/requirements.txt \
 && apk del .build-deps

# ★ 앱 소스 먼저 복사
COPY . /app/

# ★ 복사된 파일에 권한 부여 (절대경로 추천)
RUN test -f /app/config/docker/entrypoint.prod.sh \
 && chmod +x /app/config/docker/entrypoint.prod.sh
