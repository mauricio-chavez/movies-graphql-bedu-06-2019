release: python manage.py migrate --noinput
web: gunicorn movies_app.wsgi:application --log-file -