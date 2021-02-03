#!/bin/bash

echo "Restart NGINX"
sudo service nginx restart

echo "Restart Gunicorn"
sudo service gunicorn restart