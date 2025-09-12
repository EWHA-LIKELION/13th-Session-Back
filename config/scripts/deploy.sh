#!/bin/sh
set -eu

APP_DIR="/home/ubuntu/srv/ubuntu"
CD="docker compose"
PROJ="-p ubuntu"
FILE="-f $APP_DIR/docker-compose.prod.yml"

cd "$APP_DIR"
echo "[i] PWD=$(pwd)"

$CD $FILE $PROJ config | sed -n '1,120p'

echo "== BUILD WEB =="
# 로그를 파일로 저장하되 종료코드 정확히 받기
if ! $CD $FILE $PROJ build web --no-cache --progress=plain > build.log 2>&1; then
  echo "[X] BUILD FAILED"
  tail -n 120 build.log || true
  exit 1
fi
tail -n 20 build.log || true

echo "== UP =="
if ! $CD $FILE $PROJ up -d; then
  echo "[X] UP FAILED"
  $CD $FILE $PROJ ps || true
  $CD $FILE $PROJ logs --no-color --tail=200 || true
  exit 1
fi

$CD $FILE $PROJ ps
$CD $FILE $PROJ logs web --no-color --tail=200 || true
$CD $FILE $PROJ logs nginx --no-color --tail=200 || true
echo "[✓] Deploy done."
