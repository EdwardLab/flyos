# FlyOS Project by DigitalPlat Team (created by Edward Hsing)
# FlyOS dashboard dashboard configuration file
# Do not edit variable if unfamiliar (DELETING ANY VARIABLE WILL CRASH THE SERVER!); it affects server functionality

# True for Enable, False for Disable

# Basic configuration
hostname = "flyos"   # Linux hostname
show_motd = True   # Display device information on FlyOS bash login
log_message = True   # Send notification messages on dashboard login or security operations; disable to stop notifications

# SSL conf (for gunicorn only)
server_enable_ssl = False
ssl_cert_path = '/flyosext/ssl/default.crt'
ssl_key_path = '/flyosext/ssl/default.key'

# Server configuration
dashboard_host_addr = '0.0.0.0' # Allows all devices (0.0.0.0), local only (127.0.0.1), or specify allowed IP address
dashboard_server = 'dev' # dev or gunicorn, only gunicorn support SSL
server_ip_get_method = 'url_root' # iframe gets server IP, Options: host_spilt, url_root. url_root is recommended, especially reverse proxy
jupyter_host_addr = '0.0.0.0'
novnc_proxy_addr = '0.0.0.0'
file_browser_addr = '0.0.0.0'
file_browser_listen_dir = '/'

# Port configuration
server_port = 5000  # Dashboard listening port
terminal_port = 5002
vnc_port = 5003
code_server_port = 5004
android_terminal_port = 5005
jupyter_notebook_port = 5996
android_screen_port_web = 5007
file_browser_port = 5008
wine_port_web = 5009

# VNC
android_screen_port_vnc = 3
android_screen_vnc_conf = '-geometry 1280x720 -xstartup /flyosext/android/scrcpy.sh -localhost no'
vnc_default_port = 1
vnc_1920x1080_port = 2
vnc_default_geometry = '1280x720'
vnc_default_localhost = 'no'
wine_port_vnc = 4

# Boot configuration (services on FlyOS boot)
boot_default_vnc = True
boot_vnc_1920x1080 = True
boot_dashboard = True   # Dashboard and API service
boot_ssh = True   # SSH and WebSSH Service
boot_vnc = True   # VNC and WebVNC Service
boot_code_server = True   # Application service (e.g., VSCode and Jupyter Notebook)
boot_jupyter = True   # Jupyter service
boot_file_browser = True # File Browser Service
boot_runscripts = True # Execute the script under /boot/scripts directory at boot startup

# Developer options
dev_server_debug = True
