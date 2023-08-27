import os
from config import *
#basic
os.system("""
adb start-server
""")
os.system('hostname ' + hostname)
#clean
os.system("""
#!/bin/bash
logs_check() {
    files=("/flyos/logs/flyos_main.py" "/flyos/logs/flyos_systemapi.log" "/flyos/logs/ttyd.log" "/flyos/logs/vnc.log" "/flyos/logs/novnc.log")
    threshold=1000

    for file in "${files[@]}"; do
        size=$(du -k "$file" | cut -f1)
        if [[ $size -gt $threshold ]]; then
            rm -f "$file"
        fi
    done
}
logs_check
cd
""")
# dashboard service
if boot_dashboard:
    os.system("""
    nohup python3 /flyos/main.py >> /flyos/logs/flyos_main.log 2>&1 &
    nohup python3 /flyos/systemapi.py >> /flyos/logs/flyos_systemapi.log 2>&1 &
    """)
# SSH and shell service
if boot_ssh:
    os.system("""
    nohup ttyd -p 5002 login >> /flyos/logs/ttyd.log 2>&1 &
    nohup ttyd -p 5005 android_shell >> /flyos/logs/ttyd_android.log 2>&1 &
    nohup /etc/init.d/ssh start >> /flyos/logs/ssh.log 2>&1 &
    """)
# VNC service
if boot_vnc:
    os.system("""
    nohup startvnc_1080 >> /flyos/logs/vnc.log 2>&1 &
    nohup /flyosext/novnc/utils/novnc_proxy --vnc localhost:5902 --listen 0.0.0.0:5003 >> /flyos/logs/novnc.log 2>&1 &
    """)
# App service
if boot_app:
    os.system("""
    nohup code-server >> /flyos/logs/code_server.log 2>&1 &
    nohup jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=5006 --notebook-dir=/ >> /flyos/logs/code_server.log 2>&1 &
    """)