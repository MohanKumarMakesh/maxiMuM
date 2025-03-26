#!/bin/bash
cd /var/www/maximum
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt#!/bin/bash
# Install dependencies
sudo apt update -y
sudo apt install -y python3 python3-venv python3-pip nginx

# Set up the virtual environment
cd /var/www/maximum
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure Nginx
sudo cp /var/www/maximum/scripts/nginx_config /etc/nginx/sites-available/maximum
sudo ln -s /etc/nginx/sites-available/maximum /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl restart nginx