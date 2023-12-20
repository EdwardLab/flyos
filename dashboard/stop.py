import os
from tools import *
# Terminate Python3 processes
os.system("pkill python3")

# Terminate specific Python scripts
os.system("pkill -f 'python3 /flyos/main.py'")
os.system("pkill -f 'python3 /flyos/systemapi.py'")

# Terminate processes running ttyd and stopvnc_1080
os.system("pkill -f 'ttyd -p 5002 login'")
os.system("pkill -f 'ttyd -p 5005 login'")
os.system("pkill ttyd")
os.system(f"vncserver -kill {vnc_default_port}")
os.system(f"vncserver -kill {vnc_1920x1080_port}")

# Terminate novnc_proxy
os.system("pkill -f './novnc/utils/novnc_proxy --vnc localhost:5901 --listen 0.0.0.0:5003'")

# Terminate code-server processes
os.system("""
pids=$(pgrep -f "code-server")

for pid in $pids; do
    kill "$pid"
done
""")

# Stop SSH service
os.system("service ssh stop")

# File Browser
os.system('pkill -f "/usr/local/bin/filebrowser"')