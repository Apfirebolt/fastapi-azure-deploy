# <module-path> is the relative path to the folder that contains the module
# that contains wsgi.py; <module> is the name of the folder containing wsgi.py.
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
alembic revision --autogenerate -m "Initial tables"
alembic upgrade head


