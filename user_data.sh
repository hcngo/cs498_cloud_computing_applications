#!/bin/bash
sudo apt-get update -y
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 -y
sudo pip3 install flask
git clone "https://github.com/hcngo/cs498_cloud_computing_applications.git"
cd cs498_cloud_computing_applications/flaskapp
sudo ln -sT ~/cs498_cloud_computing_applications/flaskapp /var/www/html/flaskapp


