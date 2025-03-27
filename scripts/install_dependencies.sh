#!/bin/bash

# Update package lists
sudo apt update -y

# Install required packages
sudo apt install -y python3 python3-venv python3-pip nginx

# Ensure Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx installation failed. Exiting."
    exit 1
fi

# Start and enable Nginx service
sudo systemctl start nginx
sudo systemctl enable nginx

# Create the application directory if it doesn't exist
sudo mkdir -p /var/www/maximum
sudo chown -R $USER:$USER /var/www/maximum

# Set up the virtual environment
cd /var/www/maximum/src || exit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure Nginx
sudo cp /var/www/maximum/scripts/nginx_config /etc/nginx/sites-available/maximum
sudo ln -sf /etc/nginx/sites-available/maximum /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default
sudo systemctl restart nginx