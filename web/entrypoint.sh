sleep 30

python manage.py makemigrations --no-input

python manage.py migrate --no-input

python manage.py collectstatic --no-input

exec gunicorn server.wsgi:application -c gunicorn_conf.py --reload
