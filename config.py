# The FlyOS Project by: DigitalPlat Team(Edward Hsing)
# This is the FlyOS dashboard control panel configuration file
# If you don't know what this is, please don't edit or delete it, otherwise the server will not work properly

# basic configuration
hostname = "flyos"   # Linux hostname
show_motd = True   # This option controls whether to display device usage and IP information when logging in to Shell (bash)
notavailable_tips = False # Enable can use GEOIP to detect whether the FlyOS cloud service is available in your country and region, if not available, it will start the offline mode and tell you the unavailable message (disable can reduce the loading time of the dashboard)

# port configuration (This option controls the corresponding port of the iframe of the dashboard)
server_port = 5000
vnc_port = 5003
code_server_port = 5004
terminal_port = 5002
android_terminal_port = 5005
jupyter_notebook_port = 5006

# boot configuration
# These configurations define which services are started when the device boots
boot_dashboard = True   # dashboard and API service
boot_ssh = True   # SSH and WebSSH Service
boot_vnc = True   # VNC and WebVNC Service
boot_app = True   # Application service, like: VSCode and Jupyter Notebook