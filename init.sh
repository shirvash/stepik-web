#!/bin/bash

sudo pip3 install -r requirements.txt

sudo rm -f /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf


sudo rm /etc/gunicorn.d/hello.py
sudo rm /etc/gunicorn.d/ask.py
sudo ln -sf /home/box/web/etc/gunicorn-hello.conf /etc/gunicorn.d/hello
sudo ln -sf /home/box/web/etc/gunicorn-ask.conf /etc/gunicorn.d/ask



python3 /home/box/web/ask/manage.py makemigrations
python3 /home/box/web/ask/manage.py migrate

bash restartServers.sh
