#!/bin/bash
apt update
apt upgrade -y
apt clean
apt autoremove -y
rm -rf logs/*
rm -rf /root/.bash_history
rm -rf /var/lib/apt/lists/*
rm -rf /root/.cache/*
echo > /flyos/files/pwd.conf
rm -rf /flyos/files/setup/setup_lock
rm -rf /root/.mozilla/firefox-esr
rm -rf /flyos/logs/*
rm -rf /root/.cache
rm -rf /root/.vnc/*.log
rm -rf /root/.vnc/*.pid
rm -rf /var/log/*
rm -rf /var/tmp/*
rm -rf /tmp/*
rm -rf /flyos/nohup.out
rm -rf /boot/scripts/*
rm -rf /flyos/.ipynb_checkpoints
rm -rf /root/.local/share/code-server
rm -rf /root/.local/share/jupyter
echo > /flyos/files/token/token
echo > /flyos/files/temp/otp
echo root:flyospwd | chpasswd
echo flyos:userpassword | chpasswd
cp /flyos/config.py /flyos/files/backup/config.py