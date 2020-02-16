#!/bin/bash
sudo apt-get update -y
sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 -y
sudo pip3 install virtualenv
git clone "https://github.com/hcngo/cs498_cloud_computing_applications.git"
cd cs498_cloud_computing_applications/mp1
virtualenv myprojectenv
source myprojectenv/bin/activate
pip3 install -r requirements.txt
sudo ln -sT ~/cs498_cloud_computing_applications/mp1 /var/www/html/mp1


