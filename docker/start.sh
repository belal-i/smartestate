#!/bin/bash

cd /app

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server/beat/worker/flower)"
    exit 1
fi

PROCESS_TYPE=$1

# This failed to install when building the image...
# pip install gunicorn
if [ "$PROCESS_TYPE" = "server" ]; then
    if [ "$DJANGO_DEBUG" = "true" ]; then
        gunicorn \
            --reload \
            --bind 0.0.0.0:8000 \
            --workers 2 \
            --worker-class eventlet \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            smartestate.wsgi
    else
        gunicorn \
            --bind 0.0.0.0:8000 \
            --workers 2 \
            --worker-class eventlet \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            smartestate.wsgi
    fi
elif [ "$PROCESS_TYPE" = "beat" ]; then
    celery \
        --app dockerapp.celery_app \
        beat \
        --loglevel INFO \
        --scheduler django_celery_beat.schedulers:DatabaseScheduler
elif [ "$PROCESS_TYPE" = "flower" ]; then
    celery \
        --app dockerapp.celery_app \
        flower \
        --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}" \
        --loglevel INFO
elif [ "$PROCESS_TYPE" = "worker" ]; then
    celery \
        --app dockerapp.celery_app \
        worker \
        --loglevel INFO
fi
