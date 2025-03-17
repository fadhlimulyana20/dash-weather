#!/bin/sh

python -m celery -A core worker --loglevel=info