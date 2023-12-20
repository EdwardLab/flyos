from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
import netifaces as ni
import socket
import requests
import psutil
import sys
import os
sys.path.append('/flyos')
from tools import *
import config
import tools
if config.show_motd == False:
    sys.exit()
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def check_port_open(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        
        if result == 0:
            return True
        else:
            return False
    except socket.error:
        return False
    finally:
        sock.close()
def get_local_ip():
    try:
        interfaces = ni.interfaces()
        for interface in interfaces:
            if interface.startswith('wlan') or interface.startswith('eth'):
                addresses = ni.ifaddresses(interface)
                if ni.AF_INET in addresses:
                    return addresses[ni.AF_INET][0]['addr']
        return '127.0.0.1'
    except Exception:
        return '127.0.0.1'


ip_address = get_local_ip()
console = Console()
console.print(
f'''
The FlyOS Project
Version: {tools.get_version()}
* Documentation and Help: https://flyos.us/
* Report bugs and suggestions: https://github.com/xingyujie/flyos/issues/

Network Information:
LAN IP address: {ip_address}   

Device usage:
CPU Usage: {get_cpu_usage()}%
Memory Usage: {get_memory_usage()}%
Disk Usage: {get_disk_usage()}%

''')
is_flyos_started = check_port_open(server_port)
print("Dashboard Status:")
if is_flyos_started:
    console.print('FlyOS Dashboard is started and the status is ok!', style='bold green')
    console.print(f'* FlyOS Web Dashboard: http://{ip_address}:{server_port}', style='bold green')
else:
    console.print('* WARNING: FlyOS Dashboard is not started, please check the service status!', style='bold yellow')