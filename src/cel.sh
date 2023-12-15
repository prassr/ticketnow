# commands to run to start celery worker and scheduled tasks

celery -A app:capp worker -l INFO 
celery -A app:capp beat --loglevel=info

