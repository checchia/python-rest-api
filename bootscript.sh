#!/bin/sh

echo "-------------------------------------------"
echo "Pre-requisites - "
echo "1. apt-get update && apt-get upgrade"
echo "2. apt-get install nginx"
echo "3. Create a new site and enable it"
echo "4. server -> listen 80 / to 127.0.0.1:8000"
echo "5. Restart nginx service"
echo "6. Install php5-fpm package"
echo "-------------------------------------------"

echo "-------------------------------------------"
echo "Update nginx default site"
cp config/default /etc/nginx/sites-enabled/default

echo "Restart nginx. This would reverse proxy port 80 to this Python config management tool listening on 8000"
sudo service nginx restart

echo "Deploy PHP home page to document root"
cp index.php /var/www/html/index.php

echo "Restart PHP service"
sudo service php5-fpm restart
echo "-------------------------------------------"

echo "Config tool untar'ed at ~/staging/config-tool"
cd ~/staging/config-tool

echo "Install virtual environment and activate it"
pip3 install virtualenv
python3 -m venv env
source env/bin/activate

echo "Install all the requirements for config tool app within the virtual environment"
pip3 install -r requirements.txt

echo "Install gunicorn for launching the app"
pip3 install gunicorn
echo "-------------------------------------------"

echo "Launch configuration tool app - gunicorn with (2 * #cores + 1 = 3) workers"
gunicorn -w 3 run:app &

