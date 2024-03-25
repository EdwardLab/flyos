# FlyOS Installer
# FlyOS Open Source Project AGPL-3.0 LICENSE
# install.py Created by: Edward Hsing
from adb import *
from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
import sys
import os
from files.tools import *
import gdown
import webbrowser
import time
import wget
console = Console()
# CONFIG
ignore_error = False
version = '1.00.00'

# END CONFIG
def check_version():
    try:
        response = requests.get('https://info.flyos.us/installer_ver')
        if response.status_code == 200:
            online_version = response.text.strip()
            print("FlyOS Installer version:", online_version)
            if online_version > version:
                print("Your FlyOS Installer is not the latest version, please update to the latest version and try again.")
                sys.exit()
        else:
            print("Failed to retrieve online version information. Please check your internet connection and try again.")
    except Exception as e:
        print("An error occurred:", e)
check_version()

def exit_installer():
    if ignore_error == False:
        sys.exit()
def ui():
    try:
        flyos_ver = requests.get('https://info.flyos.us/latest_ver')
        if flyos_ver.status_code == 200:
            flyos_ver = flyos_ver.text.strip()
        else:
            print("Failed to retrieve online version information. Please check your internet connection and try again.")
    except Exception as e:
        print("An error occurred:", e)
    print("Welcome to the FlyOS Installer")
    print(f"""
Latest FlyOS Version: {flyos_ver}
1. Run the Device Requirements Test
2. Deploy and install the FlyOS subsystem
3. Uninstall and remove FlyOS
4. Device Shell
    """)
    ask = input('Enter an option: ')
    if ask == '1':
        device_test()
    if ask == '2':
        install()
    if ask == '3':
        uninstall()
    if ask == '4':
        device_shell()
    
def device_test():
    ui_main_text = Markdown(
'''
# Enable developer mode (if enabled, please ignore)
To enable Developer Options and activate USB debugging, follow these simple steps: Go to your device Settings menu, tap on "About phone" or "About device," and locate the "Build number" or "Build version" entry. Tap on it repeatedly, around seven times, until you receive a confirmation message indicating that you are now a developer. Return to the main settings menu and find "Developer Options" or "Developer settings." In the Developer Options menu, toggle the switch next to "USB debugging" to enable it. Connect your device to a computer using a USB cable, and when prompted on your device, tap on "Allow" to grant permission for USB debugging.
''')
    console.print(ui_main_text)
    input('Enter to continue')
    print("Check your device")
    print(adb_list())
    if device_check() == False:
        console.print('Sorry, your device is not detected, please reconnect the USB cable, replace the data cable, Or check if USB debugging is enabled',style='red')
        exit_installer()
    if int(get_android_version()) < 7:
        console.print(f"Your Android version is not supported, current version: " + get_android_version() + ', Minimum requirement: Android 7.0+', style='bold red')
    else:
        console.print(f'[green][*] Pass[/green], your Android version: {get_android_version()}')
    if check_root() == False:
        console.print(f'Your device does not have root permission, please root the device and try again (such as Magisk)', style='bold red')
        exit_installer()
    else:
        if 'Usage' in popen_sys('su -v'):
            su_ver = ''
        else:
            su_ver = ', SU Version: ' + popen_sys('su -v')
        console.print(f'[green][*] Pass[/green], Your device is [green]rooted[/green]' + su_ver, end='')
    if check_data_rw() == False:
        console.print('Your device Data partition is not writable', style='bold red')
        exit_installer()
    else:
        console.print('[green][*] Pass[/green], Your device Data partition is writable')
    if check_system_rw() == False:
        console.print('Your device System partition maybe not writable, You can still install FlyOS, but some features may not be available, it is recommended that the system partition be writable', style='bold yellow')
    else:
        console.print('[green][*] Pass[/green], Your device System partition is writable')
    if get_device_architecture() == 'arm64-v8a':
        console.print('[green][*] Pass[/green], Your device architecture: arm64-v8a')
    else:
        console.print('Currently only arm64-v8a is supported. Welcome to join the development, support and maintain more architectures', style='bold red')
        exit_installer()
    if int(get_device_storage()) < 20:
        console.print('[yellow][*] Warning[/yellow], The device space is less than 20GB, there may be problems continuing to install')
    elif int(get_device_storage()) < 18:
        console.print('The device space is less than 18GB, Unable to continue installing FlyOS', style='bold red')
    else:
        console.print('[green][*] Pass[/green], Available storage > 20GB')
    if int(get_total_ram()) < 3:
        console.print('[yellow][*] Warning[/yellow], Your device memory is less than 3GB, there may be problems continuing to install')
    else:
        console.print('[green][*] Pass[/green], Device RAM >= 3GB')
    if check_internet_connection() == False:
        console.print('Your device does not have internet access', style='bold red')
        exit_installer()
    else:
        console.print('[green][*] Pass[/green], Your device is connected to the Internet')
    devinfo_report_title = Markdown(
f"""
# Device Information Report
##### This report is provided for reference purposes only and may not be entirely accurate or representative.
"""
    )
    console.print(devinfo_report_title)
    #devinfo get
    android_version = get_android_version()
    kernel_version = get_kernel_version()
    architecture = get_device_architecture()
    storage = get_device_storage()
    ram = get_total_ram()

    console.print(
        f"""
[bold green]Device Information Report[/bold green]
[bold]Android Version:[/bold] [blue]{android_version}[/blue]
[bold]Kernel Information:[/bold] [blue]{kernel_version}[/blue]
[bold]Arch:[/bold] [blue]{architecture}[/blue]
[bold]Available Storage:[/bold] [blue]{storage} GB[/blue]
[bold]RAM:[/bold] [blue]{ram} GB[/blue]
        """
    )
    if ignore_error == False:
        console.print('[bold green]Congratulations! This device meets the minimum requirements for running FlyOS, and you can install FlyOS now![/bold green]')
def device_shell():
    shell()
def install():
    console.print('Before installation, [bold]you [red]must[/red] check the device requirements[/bold], and you must meet the minimum device installation requirements before you can install FlyOS')
    input("Press enter to check device requirements")
    device_test()
    console.print('[green]You passed the test![/green] Now start installing FlyOS')
    input("Press enter to continue install, or press Ctrl+C to exit")
    print("Initialize and mount file system")
    init_install()
    time.sleep(8)
    console.print('[*] Done Initialize!', style='green')
    console.print('FlyOS Installer starts deploying subsystems for this device', style='green')
    console.print('[bold] Just answer a few simple questions and the installer will start working automatically! [/bold]')
    console.print('Which server do you want to download FlyOS rootfs from?')
    console.print('''

1. Google Server (Recommended & Fast)
2. FlyOS Server (Unstable, In development)
3. Custom Server (Input URL)
4. Download rootfs from Google Drive in Browser (Open in Browser & Download)
5. Choose rootfs file from local (Type rootfs path)
    ''')
    ask = input('Enter an option: ')
    if ask == '1':
        if os.path.exists("rootfs.tar.gz"):
            response = input("rootfs.tar.gz already exists. Do you want to skip downloading it? (y/n) (y = skip): ")
            if response.lower() == 'n':
                clear_env()
                down_url = get_server_data('https://raw.githubusercontent.com/xingyujie/flyos_info/main/gd_latest')
                print('Downloading from Google Server...')
                output = "rootfs.tar.gz"
                gdown.download(down_url, output, quiet=False, fuzzy=True)
                rootfs_filename = output
                rootfs_path = output
            if response.lower() == 'y':
                rootfs_filename = "rootfs.tar.gz"
                rootfs_path = "rootfs.tar.gz"
        else:
            rootfs_path = "rootfs.tar.gz"
            down_url = get_server_data('https://raw.githubusercontent.com/xingyujie/flyos_info/main/gd_latest')
            print('Downloading from Google Server...')
            output = "rootfs.tar.gz"
            gdown.download(down_url, output, quiet=False, fuzzy=True)
            rootfs_filename = output
            rootfs_path = output

    elif ask == '2':
        if os.path.exists("rootfs.tar.gz"):
            response = input("rootfs.tar.gz already exists. Do you want to skip downloading it? (y/n) (y = skip): ")
            if response.lower() == 'n':
                down_url = get_server_data('https://raw.githubusercontent.com/xingyujie/flyos_info/main/flyos_server_latest')
                wget.download(down_url, 'rootfs.tar.gz')
                rootfs_path = 'rootfs.tar.gz'
            else:
                rootfs_filename = "rootfs.tar.gz"
                rootfs_path = "rootfs.tar.gz"

    elif ask == '3':
        if os.path.exists("rootfs.tar.gz"):
            response = input("rootfs.tar.gz already exists. Do you want to skip downloading it? (y/n) (y = skip): ")
            if response.lower() == 'n':
                down_url = input('Enter the URL: ')
                wget.download(down_url, 'rootfs.tar.gz')
                rootfs_filename = "rootfs.tar.gz"
                rootfs_path = 'rootfs.tar.gz'
            elif response.lower() == 'y':
                rootfs_filename = "rootfs.tar.gz"
                rootfs_path = "rootfs.tar.gz"
            else:
                console.print('[red]Invalid option[/red]')
                exit_installer()
        else:
            down_url = input('Enter the URL: ')
            wget.download(down_url, 'rootfs.tar.gz')
            rootfs_filename = "rootfs.tar.gz"
            rootfs_path = 'rootfs.tar.gz'

    elif ask == '4':
        webbrowser.open('https://drive.google.com/drive/folders/1JGg0Vxcdtu6fIN6oMFCbQu-AUOjzw3LE?usp=sharing')
        rootfs_path = input('Enter the rootfs file path: ')
        rootfs_filename = os.path.basename(rootfs_path)
    elif ask == '5':
        rootfs_path = input('Enter the rootfs file path: ')
        rootfs_filename = os.path.basename(rootfs_path)
    else:
        console.print('[red]Invalid option[/red]')
        exit_installer()
    console.print('Which server do you want to download FlyOS Container Tools from?')
    console.print('''
1. SourceForge Server (Recommended & Fast)       
2. Choose rootfs file from local (Type tar.gz file path)
    ''')
    ask = input('Enter an option: ')
    if ask == '1':
        down_url = get_server_data('https://raw.githubusercontent.com/xingyujie/flyos_info/main/tools_sf_latest')
        wget.download(down_url, 'tools.tar.gz')
        print()
        tools_path = 'tools.tar.gz'
        tools_filename = 'tools.tar.gz'
    elif ask == '2':
        tools_path = input('Enter the tools file path: ')
        tools_filename = os.path.basename(tools_path)
    else:
        console.print('[red]Invalid option[/red]')
        exit_installer()
    console.print('Which server do you want to download FlyOS Manager from?')
    console.print('''
1. SourceForge Server (Recommended & Fast)
2. Choose rootfs file from local (Type apk file path)
    ''')  
    ask = input('Enter an option: ')
    if ask == '1':
        down_url = get_server_data('https://raw.githubusercontent.com/xingyujie/flyos_info/main/manager_sf_latest')
        wget.download(down_url, 'manager.apk')
        print()
        manager_path = 'manager.apk'
        manager_filename = 'manager.apk'
    elif ask == '2':
        manager_path = input('Enter the manager file path: ')
        manager_filename = os.path.basename(manager_path)
    else:
        console.print('[red]Invalid option[/red]')
        exit_installer()
    if input('Do you want to Install FlyOS Manager to System Partition? (System partition must be writeable) (y/n) ') == 'y':
        install_manager_system = True
    else:
        install_manager_system = False

    print("[START] STEP-1 Create and copy basic FlyOS files and Install Container Tools")
    runsys_root('mkdir /data/flyos')
    runsys_root('mkdir -p /data/local/flyos/rootfs')
    os.system('adb push ' + tools_path + ' /sdcard')
    runsys_root(f'tar -zxvf /sdcard/{tools_filename} -C /data/flyos')
    runsys_root('chmod +x /data/flyos/bin/*')
    runsys_root('chmod +x /data/flyos/*')
    runsys_root(f'rm -rf /sdcard/{tools_filename}')
    console.print('[*] Done STEP-1!', style='green')
    print("[START] STEP-2 Copy and Install rootfs")
    os.system('adb push ' + rootfs_path + ' /sdcard')
    runsys_root(f'tar -zxvf /sdcard/{rootfs_filename} -C /data/local/flyos/rootfs/')
    runsys_root(f'rm -rf /sdcard/{rootfs_filename}')
    console.print('[*] Done STEP-2!', style='green')
    print("[START] STEP-3 Copy and Install FlyOS Manager")
    adb_install(manager_path)
    if install_manager_system == True:
        runsys_root('mkdir /system/app/FlyOSManager')
        os.system('adb push ' + manager_path + ' /sdcard')
        runsys_root(f'mv /sdcard/{manager_filename} /system/app/FlyOSManager/FlyOSManager.apk')
    console.print('[*] Done STEP-3!', style='green')
    console.print('[*] STEP-4 Set up system environment and update FlyOS software', style='green')
    os.system("adb shell sh /data/flyos/bin/flyos -c 'apt update'")
    os.system("adb shell sh /data/flyos/bin/flyos -c 'apt upgrade -y'")
    console.print('[*] Done STEP-4!', style='green')
    clear_env()
    console.print('Almost Done! Do you want to reboot your device before start FlyOS? for final installation (Recommended), If not, please manually restart your device before start FlyOS for the first time (y/n)')
    if input('Enter an option: ') == 'y':
        runsys_root('svc power reboot')
        console.print('You can start FlyOS after reboot!', style='green')
    else:
        console.print('Please manually restart your device before start FlyOS for the first time', style='green')
    console.print('Installation completed! Enjoy FlyOS! A Linux Subsystem for your Android device! Visit: http://127.0.0.1:5000 on your device after started FlyOS on FlyOS Manager', style='green')
def uninstall():
    print("Checking Device")
    print(adb_list())
    if device_check() == False:
        console.print('Sorry, your device is not detected, please reconnect the USB cable, replace the data cable, Or check if USB debugging is enabled',style='red')
        exit_installer()
    if popen_sys('[ -d /data/flyos ] && echo "True" || echo "False"') == "False":
        console.print('FlyOS is not installed on your device, Exiting', style='red')
        exit_installer()
    console.print('Do you really want to uninstall and remove FlyOS from your device? This action CAN NOT undone', style='yellow')
    input('Enter to continue')
    console.print('All data in FlyOS will be removed and lost, including applications, files, user data, and configurations. Please back up your data before uninstalling and removing.', style='yellow')
    input('Enter to continue')
    console.print('WARNING: Please DO NOT use your device during uninstalling, and DO NOT disconnect the USB cable during the uninstall process, otherwise it may cause damage to your device, Even damage the Android system·', style='yellow')
    input('Enter to continue')
    console.print('Again, do you really want to uninstall and remove FlyOS from your device? This action CAN NOT undone(y/n)', style='yellow')
    if input('Enter an option: ') == 'y':
        console.print('Please make sure FlyOS has compeltely stopped and exited before uninstall, If you are not sure, Please reboot your device before uninsall', style='yellow')
        if input('Enter "yes" to reboot device (make sure FlyOS subsystem has compeltely stopped), Enter "no" to continue without reboot: ') == 'yes':
            runsys_root('svc power reboot')
            console.print('Please wait for the device to restart, once device restarted, then press Enter', style='yellow')
            input('Enter to continue uninstall')
    # Uninstall part
        console.print('Uninstalling FlyOS subsystem... Please wait', style='yellow')
        runsys_root('rm -rf /data/flyos')
        runsys_root('rm -rf /data/local/flyos')
        runsys_root('pm uninstall org.flyos.manager')
        runsys_root('rm -rf /system/app/FlyOSManager')
        console.print('FlyOS has been uninstalled and removed from your device', style='green')
    else:
        sys.exit()
if __name__ == '__main__':
    ui()