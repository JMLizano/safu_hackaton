#! /bin/bash

# OS dependencies
apt get update
apt-get install -yq \
    git build-essential python python-dev python3 python3-dev python-pip libffi-dev \
    libssl-dev make supervisor

# Get the code 
cd /opt/safu_hackaton/
git checkout api_only

# pip from apt is out of date, so make it update itself and install virtualenv.
pip install --upgrade pip virtualenv

# Install app deps
make install

# Create user that will run the app
useradd -m -d /home/pythonapp pythonapp
chown -R pythonapp:pythonapp /opt/safu_hackaton

nohup pipenv run gunicorn -b :80 autoapp:app &