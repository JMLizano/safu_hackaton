#! /bin/bash

# OS dependencies
apt get update
apt-get install -yq \
    git build-essential python python-dev python3 python3-dev python-pip libffi-dev \
    libssl-dev make supervisor

# Get the code
# cd /opt
# git clone https://github.com/JMLizano/safu_hackaton.git 
# cd safu_hackaton/
# git checkout safu_api

# pip from apt is out of date, so make it update itself and install virtualenv.
pip install --upgrade pip virtualenv
# Install app deps
make install

# Create user that will run the app
useradd -m -d /home/pythonapp pythonapp
chown -R pythonapp:pythonapp /opt/safu_hackaton


# Configure supervisor to start gunicorn inside of our virtualenv and run the
# application.
cat >/etc/supervisor/conf.d/safu-api.conf << EOF
[program:safuapi]
directory=/opt/safu_hackaton
command=pipenv run gunicorn -b :80 autoapp:app
autostart=true
autorestart=true
user=pythonapp
environment = 
    DATABASE_URL=mysql+pymysql://${DB_USER}:${DB_PASS}@${DB_HOST}/safu
EOF

supervisorctl reread
supervisorctl update