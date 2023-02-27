task: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic
web: gunicorn core.wsgi:application --log-file -
