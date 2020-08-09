#!/bin/sh

set -e

cd /usr/src/app
python manage.py migrate

exec "$@"