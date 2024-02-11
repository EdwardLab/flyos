import os
from config import *
#basic
os.system("""
adb start-server
""")
os.system('hostname ' + hostname)
#clean
def logs_check():
    files = [
        "/flyos/logs/flyos_main.py",
        "/flyos/logs/flyos_systemapi.log",
        "/flyos/logs/ttyd.log",
        "/flyos/logs/vnc.log",
        "/flyos/logs/novnc.log"
    ]
    threshold = 1000

    for file in files:
        try:
            size = os.path.getsize(file) / 1024 
            if size > threshold:
                os.remove(file)
        except FileNotFoundError:
            pass
logs_check()
# dashboard service
if boot_dashboard:
    if dashboard_server == 'dev':
        os.system("""
        nohup python3 /flyos/main.py >> /flyos/logs/flyos_main.log 2>&1 &
        """)
    if dashboard_server == 'gunicorn':
        if server_enable_ssl:
            os.system(f"""
            nohup gunicorn -b {dashboard_host_addr}:{server_port} --chdir /flyos main:app --certfile={ssl_cert_path} --keyfile={ssl_key_path} >> /flyos/logs/flyos_main.log 2>&1 &
            """)
        else:
            os.system(f"""
            nohup gunicorn -b {dashboard_host_addr}:{server_port} --chdir /flyos main:app >> /flyos/logs/flyos_main.log 2>&1 &
            """)

# SSH and shell service
if boot_ssh:
    os.system(f"""
    nohup ttyd -p {terminal_port} login >> /flyos/logs/ttyd.log 2>&1 &
    nohup ttyd -p {android_terminal_port} android_shell >> /flyos/logs/ttyd_android.log 2>&1 &
    nohup /etc/init.d/ssh start >> /flyos/logs/ssh.log 2>&1 &
    """)
# VNC service
if boot_default_vnc:
    os.system(f"""
    rm -rf /tmp/.X{vnc_default_port}-lock
    rm -rf /tmp/.X11-unix/X{vnc_default_port}
    nohup vncserver :{vnc_default_port} -geometry {vnc_default_geometry} -localhost {vnc_default_localhost} >> /flyos/logs/vnc_default.log 2>&1 &
    """)
if boot_vnc_1920x1080:
    os.system("""
    rm -rf /tmp/.X1-lock
    rm -rf /tmp/.X11-unix/X1
    nohup vncserver :2 -geometry 1920x1080 -localhost no >> /flyos/logs/vnc_1920x1080.log 2>&1 &
    """)
if boot_vnc:
    os.system(f"""
    nohup /flyosext/novnc/utils/novnc_proxy --vnc localhost:590{vnc_default_port} --listen {novnc_proxy_addr}:{vnc_port} >> /flyos/logs/novnc.log 2>&1 &
    """)
# App service
if boot_code_server:
    os.system("""
    nohup code-server >> /flyos/logs/code_server.log 2>&1 &
    """)

if boot_jupyter:
    os.system(f"""
    nohup python3 -m jupyter notebook --no-browser --allow-root --ip={jupyter_host_addr} --port={jupyter_notebook_port} --notebook-dir=/ >> /flyos/logs/jupyter.log 2>&1 &
    """)

if boot_file_browser:
    os.system(f"""
    nohup /usr/local/bin/filebrowser -p {file_browser_port} -a {file_browser_addr} -r {file_browser_listen_dir} -d /flyosext/filebrowser/filebrowser.db >> /flyos/logs/file_browser.log 2>&1 &
    """)

if boot_runscripts:
    # boot scripts
    os.system('nohup find /boot/scripts -name "*.sh" -exec bash {} \; >> /flyos/logs/boot_scripts.log 2>&1 &')