web: gunicorn codex_project.wsgi
worker: celery -A codex_project worker --loglevel=info -P eventlet -E