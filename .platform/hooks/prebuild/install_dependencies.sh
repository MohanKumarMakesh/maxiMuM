#!/bin/bash
echo "Installing dependencies..."
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install -r /var/app/current/src/requirements.txt