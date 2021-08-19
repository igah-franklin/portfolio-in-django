release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn myresume.wsgi --log-file -