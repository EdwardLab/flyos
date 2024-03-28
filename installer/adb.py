# FlyOS Installer
# FlyOS Open Source Project AGPL-3.0 LICENSE
# adb.py Created by: Edward Hsing
import os
import subprocess
#adb call func
def runsys(shell):
    os.system("adb shell " + shell)
def runsys_root(shell):
    os.system("adb shell su -c " + shell)
def popen_sys(shell):
    result = os.popen("adb shell " + shell).read()
    return result
def adb_list():
    devices = os.popen("adb devices").read()
    return devices
def shell():
    os.system('adb shell')
def device_check():
    devices = os.popen("adb devices").read()
    try:
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        output_lines = result.stdout.strip().split('\n')[1:]
        devices = [line.split('\t')[0] for line in output_lines if line.endswith('device')]
        
        if devices:
            return True
        else:
            return False
    
    except subprocess.CalledProcessError:
        print("Error")
def adb_install(files):
    files = os.popen(f"adb install {files}").read()
    return files
def check_device():
    osver = runsys("getprop ro.build.version.release")
    is_root = "#" in runsys("su")
def get_android_version():
    try:
        # Execute adb command to get the Android version
        result = subprocess.run(['adb', 'shell', 'getprop', 'ro.build.version.release'], capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            return output
        else:
            print("Failed to retrieve Android version.")
    except subprocess.CalledProcessError:
        print("Error executing adb command.")
def check_root():
    result = popen_sys("su -c 'echo check_root'")
    if "check_root" in str(result):
        return True
    else:
        return False

def check_data_rw():
    try:
        result = subprocess.run(['adb', 'shell', 'su', '-c', 'touch', '/data/local/test'], capture_output=True, text=True, check=True)
        subprocess.run(['adb', 'shell', 'rm', '/system/test'], capture_output=True, text=True)
        temp = popen_sys('su -c "rm -rf /data/local/test"')
        return True
    except subprocess.CalledProcessError:
        return False

def check_system_rw():
    popen_sys('su -c "mount -o rw,remount /data > /dev/null 2>&1 &"')
    popen_sys('su -c "mount -o rw,remount / > /dev/null 2>&1 &"')
    popen_sys('su -c "mount -o rw,remount /system > /dev/null 2>&1 &"')
    popen_sys('su -c "mount -o rw /dev/block/bootdevice/by-name/system /system > /dev/null 2>&1 &"')
    try:
        result = subprocess.run(['adb', 'shell', 'su', '-c', 'touch', '/system/app/test'], capture_output=True, text=True, check=True)
        subprocess.run(['adb', 'shell', 'rm', '/system/app/test'], capture_output=True, text=True)
        popen_sys('su -c "rm -rf /system/app/test"')
        return True
    except subprocess.CalledProcessError:
        return False

def get_device_architecture():
    command = ['adb', 'shell', 'getprop', 'ro.product.cpu.abi']
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    return output

def get_device_storage():
    result = subprocess.run(['adb', 'shell', 'df', '/data'], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')
    if len(output_lines) >= 2:
        storage_info = output_lines[1].split()
        if len(storage_info) >= 5:
            available_space = int(storage_info[3]) / (1024 * 1024)
            return round(available_space, 2)
    storage = get_device_storage()
    if storage is not None:
        print("Device storage available: {:.2f} GB".format(storage))
    else:
        print("Failed to retrieve device storage information.")

def get_total_ram():
    result = subprocess.run(['adb', 'shell', 'cat', '/proc/meminfo'], capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')
    for line in output_lines:
        if line.startswith('MemTotal:'):
            total_ram = line.split(':')[1].strip().split()[0]
            return round(int(total_ram) / (1024 * 1024),2)
    return None
def check_internet_connection():
    try:
        result = subprocess.run(['adb', 'shell', 'ping', '-c', '1', 'google.com'], capture_output=True, text=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False
def get_kernel_version():
    result = subprocess.run(['adb', 'shell', 'uname', '-a'], capture_output=True, text=True)
    return result.stdout.strip()
def init_install():
    os.system('adb root')
    popen_sys('mount -o rw,remount /data')
    popen_sys('mount -o rw,remount /')
def clear_env():
    current_directory = os.getcwd()
    # List all files in the directory
    files = os.listdir(current_directory)
    # Filter files with .tar.gz or .apk extensions and delete them
    for file in files:
        if file.endswith('.tar.gz') or file.endswith('.apk') or file.endswith('.gz'):
            file_path = os.path.join(current_directory, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
