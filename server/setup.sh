#!/usr/bin/env bash


setup-env() {
    # install fresh packages
    apt update
    apt upgrade -y
    # Install some OS dependencies:
    sudo apt install -y -q build-essential git
    sudo apt install -y -q python3-pip python3-dev python3-venv
    # for gzip support in uwsgi
    sudo apt install --no-install-recommends -y -q libpcre3-dev libz-dev  # for compression
    sudo apt install -y -q nginx
    sudo apt install -y nload  # in/outbound traffic
    # Stop the hackers
    sudo apt install fail2ban -y
}


setup-firewall() {
    ufw allow ssh
    ufw allow http
    ufw allow https
    ufw enable
}


setup-git() {
    # Basic git setup
    git config --global credential.helper cache
    git config --global credential.helper 'cache --timeout=720000'

    # Be sure to put your info here:
    git config --global user.email "vyahello@gmail.com"
    git config --global user.name "Volodymyr Yahello"
}


setup-app-folder() {
    mkdir /webapps
    chmod 777 /webapps
    mkdir /webapps/logs
    mkdir /webapps/logs/billtracker
    mkdir /webapps/logs/billtracker/app_log
    cd /webapps
}


setup-venv() {
    cd /webapps
    python3 -m venv venv
    source /webapps/venv/bin/activate
    pip install --upgrade pip setuptools
    pip install --upgrade httpie glances  # what happens on the server like 'htop'
    pip install --upgrade uwsgi
}


setup-webapp() {
    # clone the repo:
    cd /webapps
    git clone https://github.com/vyahello/billtracker.git
    # Setup the web app:
    cd /webapps/billtracker/
    pip install -r requirements.txt
    python setup.py develop
}


setup-deamon() {
    # Copy and enable the daemon
    cp /webapps/billtracker/server/billtracker.service /etc/systemd/system/billtracker.service

    systemctl start billtracker
    systemctl status billtracker
    systemctl enable billtracker
}


setup-nginx() {
    # CAREFUL HERE. If you are using default, maybe skip this
    rm /etc/nginx/sites-enabled/default

    cp /webapps/billtracker/server/billtracker.nginx /etc/nginx/sites-enabled/billtracker.nginx
    update-rc.d nginx enable
    service nginx restart
}


main() {
    setup-env && \
    setup-firewall && \
    setup-git && \
    setup-app-folder && \
    setup-venv && \
    setup-webapp && \
    setup-deamon && \
    setup-nginx
}


main
