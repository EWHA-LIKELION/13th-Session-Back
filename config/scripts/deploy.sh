#!/usr/bin/env bash
set -euo pipefail

APP_DIR="/home/ubuntu/srv/ubuntu"
CD="docker compose"   # v2 기준, v1 쓰면 'docker-compose'로 교체
PROJ="-p ubuntu"
FILE="-f $APP_DIR/docker-compose.prod.yml"

cd "$APP_DIR"
echo "[i] PWD=$(pwd)"

# 0) 참고: compose config 최종 확인
$CD $FILE $PROJ config | sed -n '1,120p'

# 1) 빌드(캐시·예쁜로그 끄고 실패 지점 그대로 노출)
echo "== BUILD WEB =="
if ! $CD $FILE $PROJ build web --no-cache --progress=plain | tee build.log ; then
  echo "[X] BUILD FAILED (exit $?)"
  tail -n 120 build.log
  exit 1
fi

# 2) 컨테이너 기동
echo "== UP =="
if ! $CD $FILE $PROJ up -d ; then
  echo "[X] UP FAILED (exit $?)"
  $CD $FILE $PROJ ps
  $CD $FILE $PROJ logs --no-color --tail=200
  exit 1
fi

# 3) 상태 및 초기 로그
$CD $FILE $PROJ ps
$CD $FILE $PROJ logs web --no-color --tail=200 || true
$CD $FILE $PROJ logs nginx --no-color --tail=200 || true
echo "[✓] Deploy done."
