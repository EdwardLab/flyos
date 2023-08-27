#!/bin/bash
apt clean
apt autoremove -y
rm -rf logs/*
rm -rf /root/.bash_history
rm -rf /var/lib/apt/lists/*
rm -rf /root/.cache/*
echo > /flyos/files/pwd.conf