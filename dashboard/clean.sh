#!/bin/bash
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