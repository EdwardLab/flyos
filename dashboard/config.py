# FlyOS Project by DigitalPlat Team (created by Edward Hsing)
# FlyOS dashboard dashboard configuration file
# If you don't know what it is, don't modify the configuration file randomly. Please make sure you know what you're doing (DELETING ANY VARIABLE WILL CRASH THE SERVER!)

# True for Enable, False for Disable

# Basic configuration
hostname = "localhost"   # Linux hostname
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
novnc_proxy_addr = '0.0.0.0'
file_browser_addr = '0.0.0.0'
file_browser_listen_dir = '/'

# Port configuration
server_port = 5000  # Dashboard listening port
terminal_port = 5002
vnc_port = 5003
code_server_port = 5004
android_terminal_port = 5005
android_screen_port_web = 5007
file_browser_port = 5008
wine_port_web = 5009
userspace_ttyd_port = 5010

# VNC
android_screen_port_vnc = 3
android_screen_vnc_conf = '-geometry 1280x720 -xstartup /flyosext/android/scrcpy.sh -localhost no'
vnc_default_port = 1
vnc_1920x1080_port = 2
vnc_default_geometry = '1920x1080'
vnc_default_localhost = 'no'
wine_port_vnc = 4

# Userspace config
userspace_vnc_login_user = 'root' # Default: user 'flyos' in userspace
userspace_ttyd = True


# Boot configuration (services on FlyOS boot)
boot_userspace = True
boot_userspace_ssh = True
boot_default_vnc = True
boot_vnc_1920x1080 = False
boot_dashboard = True   # Dashboard and API service
boot_ssh = True   # SSH and WebSSH Service
boot_vnc = True   # VNC and WebVNC Service
boot_code_server = True   # Code Server
boot_file_browser = True # File Browser Service
boot_runscripts = True # Execute the script under /boot/scripts directory at boot startup

# Developer options
dev_server_debug = True

# Dashboard plugin
dashboard_float_monitoring_refresh_time = '2000' # 2000 ms refresh

# FlyOS Container Config
container_ttyd_port_gen_range_min = 55000
container_ttyd_port_gen_range_max = 56000
# Web Terminal Auth (recommended)
container_ttyd_auth_enable = False # When logging into the container web terminal, ask for credentials
container_ttyd_auth_user = 'admin'
container_ttyd_auth_password = 'admin'
container_ttyd_one_client = True # Only allow one connection, disconnecting when close terminal or exit shell (recommended, for safety)

