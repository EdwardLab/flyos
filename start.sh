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
cd /flyos
logs_check
nohup python3 /flyos/main.py >> /flyos/logs/flyos_main.log 2>&1 &
nohup python3 /flyos/systemapi.py >> /flyos/logs/flyos_systemapi.log 2>&1 &
nohup ttyd -p 5002 login >> /flyos/logs/ttyd.log 2>&1 &
nohup ttyd -p 5005 adb shell >> /flyos/logs/ttyd_android.log 2>&1 &
nohup startvnc_1080 >> /flyos/logs/vnc.log 2>&1 &
nohup code-server >> /flyos/logs/code_server.log 2>&1 &
nohup ./novnc/utils/novnc_proxy --vnc localhost:5902 --listen 0.0.0.0:5003 >> /flyos/logs/novnc.log 2>&1 &
nohup /etc/init.d/ssh start >> /flyos/logs/ssh.log 2>&1 &