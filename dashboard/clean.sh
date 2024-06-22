#!/bin/bash
apt update
apt upgrade -y
apt clean
apt autoremove -y
userspace cmd --cmd 'apt update'
userspace cmd --cmd 'apt upgrade -y'
userspace cmd --cmd 'apt clean'
userspace cmd --cmd 'apt autoremove -y'
rm -rf logs/*
rm -rf /root/.bash_history
rm -rf /container/userspace/root/.bash_history
rm -rf /var/lib/apt/lists/*
rm -rf /container/userspace/var/lib/apt/lists/*
rm -rf /container/userspace/root/.cache/*
echo > /flyos/files/pwd.conf
rm -rf /flyos/files/setup/setup_lock
rm -rf /container/userspace/root/.mozilla/firefox-esr
rm -rf /flyos/logs/*
rm -rf /root/.cache
rm -rf /root/.vnc/*.log
rm -rf /root/.vnc/*.pid
rm -rf /container/userspace/root/.vnc/*.log
rm -rf /container/userspace/root/.vnc/*.pid
rm -rf /var/log/*
rm -rf /container/userspace/var/log/*
rm -rf /var/tmp/*
rm -rf /tmp/*
rm -rf /container/userspace/var/tmp/*
rm -rf /container/userspace/tmp/*
rm -rf /flyos/nohup.out
rm -rf /boot/scripts/*
rm -rf /root/.local/share/code-server
echo > /flyos/files/token/token
echo > /flyos/files/temp/otp
echo root:flyospwd | chpasswd
echo flyos:userpassword | chpasswd
cp /flyos/config.py /flyos/files/backup/config.py
rm -rf /var/cache/apt/*.bin
rm -rf /container/userspace/var/cache/apt/*.bin