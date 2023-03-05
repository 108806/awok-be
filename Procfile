web: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn core.wsgi:application --log-file -
