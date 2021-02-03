#!/bin/bash

#sudo pip3 uninstall -y django 
#sudo pip3 install django==1.9.4


sudo service mysql restart


sudo mysql -uroot -e "CREATE DATABASE IF NOT EXISTS myproject CHARACTER SET utf8 COLLATE utf8_unicode_ci;"


sudo rm -f /etc/nginx/sites-enabled/test.conf
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf


sudo rm /etc/gunicorn.d/hello.py
sudo rm /etc/gunicorn.d/ask.py
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask.py /etc/gunicorn.d/ask.py

cd /home/box/web
python3 ask/manage.py makemigrations
python3 ask/manage.py migrate

bash restartServers.sh
