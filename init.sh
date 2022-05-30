#!/bin/bash

sudo pip3 install --upgrade django
sudo pip3 install --upgrade gunicorn

sudo rm -f /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo rm /etc/gunicorn.d/test-django
sudo rm /etc/gunicorn.d/test-wsgi
sudo rm /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo ln -sf /home/box/web/etc/gunicorn-wsgi.conf /etc/gunicorn.d/test-wsgi
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/test-django

python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py migrate

bash restartServers.sh
