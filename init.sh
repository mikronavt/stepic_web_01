#!/usr/bin/env bash
#sudo apt-get update
#sudo apt-get install nginx
cd /home/box/web
mkdir public
mkdir uploads
cd public
mkdir css
mkdir img
mkdir js
cd /
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart