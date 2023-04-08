#!/usr/bin/env bash
# Script that configures Nginx server with some folders and files

# Check if Nginx is installed
if ! command -v nginx &> /dev/null
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
else
	echo "Nginx is already installed"
fi

service nginx start

#Create neccesary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello World!!!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '\tlocation /hbnb_static/ {\n \t\talias /data/web_static/current/;\n\t\}\n' /etc/nginx/sites-available/default
service nginx restart
exit 0
