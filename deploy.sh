#!/bin/bash
alembic revision --autogenerate -m "Create initial tables"
alembic upgrade head
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app