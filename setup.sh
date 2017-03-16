#!/bin/bash

# Docker, Django, Gunicorn, Postgresql Environment Installer
#
# This script will install everything required for our server.


###############################################################################
# Install prerequisites
###############################################################################

# Install Python
sudo apt-get install python3

# Install virtualenv
sudo pip install virtualenv

# Install docker-compose
sudo pip install docker-compose

###############################################################################
# Configure virtualenv
###############################################################################

# Setup virtualenv

virtualenv venv
source venv/bin/activate

cp ./drivers/geckodriver ~/bin/

docker-compose build
docker-compose up -d db
docker-compose up -d