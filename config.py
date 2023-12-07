# FlyOS Project by DigitalPlat Team (created by Edward Hsing)
# FlyOS dashboard dashboard configuration file
# Do not edit variable if unfamiliar (DELETING ANY VARIABLE WILL CRASH THE SERVER!); it affects server functionality

# True for Enable, False for Disable

# Basic configuration
hostname = "flyos"   # Linux hostname
show_motd = True   # Display device information on FlyOS bash login
notavailable_tips = False   # Enable GEOIP to detect FlyOS cloud service availability; disable to reduce dashboard loading time
log_message = True   # Send notification messages on dashboard login or security operations; disable to stop notifications

# SSL conf (for gunicorn)
server_enable_ssl = True
ssl_cert_path = '/flyosext/ssl/default.crt'
ssl_key_path = '/flyosext/ssl/default.key'

# Server configuration
dashboard_host_addr = '0.0.0.0' # Allows all devices (0.0.0.0), local only (127.0.0.1), or specify allowed IP address
dashboard_server = 'dev'
jupyter_host_addr = '0.0.0.0'
novnc_proxy_addr = '0.0.0.0'

# dashboard configuration
dashboard_menu_timeout = 10000

# Port configuration
server_port = 5000  # Dashboard listening port
terminal_port = 5002
vnc_port = 5003
code_server_port = 5004
android_terminal_port = 5005
jupyter_notebook_port = 5996
android_screen_port_web = 5007

# VNC
android_screen_port_vnc = 3
android_screen_vnc_conf = '-geometry 1280x720 -xstartup /flyosext/android/scrcpy.sh -localhost no'
vnc_default_port = 1
vnc_1920x1080_port = 2
vnc_default_geometry = '1920x1080'
vnc_default_localhost = 'no'

# Boot configuration (services on FlyOS boot)
boot_default_vnc = True
boot_vnc_1920x1080 = True
boot_dashboard = True   # Dashboard and API service
boot_ssh = True   # SSH and WebSSH Service
boot_vnc = True   # VNC and WebVNC Service
boot_code_server = True   # Application service (e.g., VSCode and Jupyter Notebook)
boot_jupyter = True   # Jupyter service

# Developer options
dev_server_debug = True
#, ssl_context=("/flyosext/ssl/default.crt", "/flyosext/ssl/default.key")'