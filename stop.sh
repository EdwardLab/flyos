#!/bin/bash
pkill python3
pkill -f "python3 /flyos/main.py"

pkill -f "python3 /flyos/systemapi.py"

pkill -f "ttyd -p 5002 login"

pkill -f "ttyd -p 5005 login"
pkill ttyd
stopvnc_1080


pkill -f "./novnc/utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:5003"

pids=$(pgrep -f "code-server")

for pid in $pids; do
    kill "$pid"
done
service ssh stop