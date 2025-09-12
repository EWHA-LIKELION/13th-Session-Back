#!/usr/bin/env bash
set -eu

APP_DIR="/home/ubuntu/srv/ubuntu"
cd "$APP_DIR"

# compose 최종 확인
sudo docker compose config | sed -n '1,120p'

echo "== BUILD WEB =="
# --progress는 compose 뒤에 둔다
if ! sudo docker compose --progress=plain -f docker-compose.prod.yml -p ubuntu build web --no-cache | tee build.log ; then
  echo "[X] BUILD FAILED"
  tail -n 120 build.log || true
  exit 1
fi

echo "== UP =="
if ! sudo docker compose -f docker-compose.prod.yml -p ubuntu up -d ; then
  echo "[X] UP FAILED"
  sudo docker compose -f docker-compose.prod.yml -p ubuntu ps || true
  sudo docker compose -f docker-compose.prod.yml -p ubuntu logs --no-color --tail=200 || true
  exit 1
fi

sudo docker compose -f docker-compose.prod.yml -p ubuntu ps
sudo docker compose -f docker-compose.prod.yml -p ubuntu logs web --no-color --tail=200 || true
sudo docker compose -f docker-compose.prod.yml -p ubuntu logs nginx --no-color --tail=200 || true
echo "[✓] Deploy done."
