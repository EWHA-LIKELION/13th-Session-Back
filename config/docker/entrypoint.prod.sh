#!/usr/bin/env sh
set -e

echo ">>> Apply database migrations"
python manage.py migrate --noinput --settings=drfproject.settings.prod

echo ">>> Collect static files"
python manage.py collectstatic --noinput --settings=drfproject.settings.prod

# 프로덕션에서는 보통 makemigrations 안 합니다. 필요시 주석 해제
# echo ">>> Make migrations (not recommended in prod)"
# python manage.py makemigrations --settings=drfproject.settings.prod

echo ">>> Start app: $@"
exec "$@"
