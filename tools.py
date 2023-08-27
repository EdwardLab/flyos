import subprocess
import psutil
import os
import requests
import netifaces as ni
from config import *
from sysconf import *
from werkzeug.security import generate_password_hash, check_password_hash
import random
PASSWORDS_FILE = "/flyos/files/pwd.conf"
def check_password(password):
    with open(PASSWORDS_FILE, "r") as file:
        stored_password_hash = file.read().strip()
        if check_password_hash(stored_password_hash, password):
            return True
    return False
def run_system(cmd):
    results = os.popen(cmd).read()
    return results
def get_device_storage():
    result = subprocess.run(['df', '/'], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')
    if len(output_lines) >= 2:
        storage_info = output_lines[1].split()
        if len(storage_info) >= 5:
            available_space = int(storage_info[3]) / (1024 * 1024)
            return round(available_space, 2)
    storage = get_device_storage()
    if storage is not None:
        return "{:.2f} GB".format(storage)
    else:
        return "Failed to retrieve device storage information."
def get_kernel_version():
    result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
    return result.stdout.strip()


def check_ssh_process():
    ssh_process_running = False
    try:
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                if "ssh" in process_name.lower():
                    ssh_process_running = True
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except:
        return "Stopped"
    if ssh_process_running:
        return "Running"
    else:
        return "Stopped"
    
def check_vnc_process():
    vnc_process_running = False
    for proc in psutil.process_iter():
        try:
            process_name = proc.name()
            if "vnc" in process_name.lower():
                vnc_process_running = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    if vnc_process_running:
        return "Running"
    else:
        return "Stopped"
def check_codeserver_process():
    try:
        output = subprocess.check_output(["pgrep", "-f", "code-server"])
        if len(output.strip().splitlines()) > 0:
            return "Running"
        else:
            return "Stopped"
    except subprocess.CalledProcessError:
        return "Stopped"
def check_ttyd_process():
    ssh_process_running = False
    try:
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                if "ttyd" in process_name.lower():
                    ssh_process_running = True
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    except:
        return "Stopped"
    if ssh_process_running:
        return "Running"
    else:
        return "Stopped"
def flyos_framework_status():
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        output_lines = result.stdout.strip().split('\n')[1:]
        devices = [line.split('\t')[0] for line in output_lines if line.endswith('device')]
        
        if devices:
            return True
        else:
            return False
    
    except subprocess.CalledProcessError as e:
        return 'Error: ' + e

def battery_status():
    battery_capacity = os.popen('cat /sys/class/power_supply/battery/capacity').read()
    battery_status = os.popen('cat /sys/class/power_supply/battery/status').read()
    status = f"{battery_capacity} {battery_status}"
    return status

def check_country():
    timeout = 10
    if notavailable_tips == False:
        result = 'true'
    else:
        try:
            url = 'http://geoip.digitalplat.org/api/check-country'
            response = requests.get(url, timeout=timeout)
            result = response.text
            return result
        except Exception as e:
            print("Exception in check_country:", str(e))
def get_local_ip():
    try:
        interfaces = ni.interfaces()
        for interface in interfaces:
            if interface.startswith('wlan') or interface.startswith('eth'):
                addresses = ni.ifaddresses(interface)
                if ni.AF_INET in addresses:
                    return addresses[ni.AF_INET][0]['addr']
        return '127.0.0.1'
    except Exception as e:
        return '127.0.0.1'
def get_version():
    fullver = f"{os_ver}_{os_build_channel}"
    if cust_build != "":
        fullver = fullver + "_" + cust_build
    return fullver
def send_android_msg(title, msg, msg_id):
    command = f'adb shell "su -lp 2000 -c \\"cmd notification post -S bigtext -t \'{title}\' \'{msg_id}\' \'{msg}\'\\""'
    os.system(command)