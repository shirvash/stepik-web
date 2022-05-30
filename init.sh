#!/bin/bash

sudo pip3 install -r requirements.txt

sudo rm -f /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf


sudo rm /etc/gunicorn.d/gunicorn-hello.conf
sudo rm /etc/gunicorn.d/gunicorn-ask.conf
sudo ln -sf /home/box/web/etc/gunicorn-hello.conf /etc/gunicorn.d/gunicorn-hello.conf
sudo ln -sf /home/box/web/etc/gunicorn-ask.conf /etc/gunicorn.d/gunicorn-ask.conf



python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py makemigrations qa
python3 /home/box/web/ask/manage.py migrate

python3  /home/box/web/ask/manage.py loaddata initial.json

bash restartServers.sh
