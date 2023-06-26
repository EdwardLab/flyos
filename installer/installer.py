# FlyOS Installer
# FlyOS Open Source Project AGPL-3.0 LICENSE
# install.py Created by: Edward Hsing
from adb.adb import runsys, popen_sys, adb_list, device_check, get_android_version, check_root, check_data_rw, check_system_rw, get_device_architecture, get_device_storage, get_total_ram, check_internet_connection, get_kernel_version, shell, runsys_root
from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
import sys
import os
console = Console()
# CONFIG
ignore_error = False


# END CONFIG
def exit_installer():
    if ignore_error == False:
        sys.exit()
def ui():
    print("Welcome to the FlyOS Installer")
    print("""
VER 3.1 Preview
1. Run the Device Requirements Test
2. Deploy and install the FlyOS subsystem
3. View EULA
4. Device Shell
    """)
    ask = input('Enter an option: ')
    if ask == '1':
        device_test()
    if ask == '2':
        install()
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
        console.print('Sorry, your device is not detected, please reconnect the USB cable, or replace the data cable',style='red')
        exit_installer()
    if int(get_android_version()) < 7:
        console.print(f"Your Android version is not supported, current version: " + get_android_version() + ', Minimum requirement: Android 7.0+', style='bold red')
    else:
        console.print(f'[green][*] Pass[/green], your Android version: {get_android_version()} meets the requirements')
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
        console.print('Your device System partition is not writable', style='bold red')
        exit_installer()
    else:
        console.print('[green][*] Pass[/green], Your device System partition is writable')
    if get_device_architecture() == 'arm64-v8a':
        console.print('[green][*] Pass[/green], Your device architecture: arm64-v8a')
    else:
        console.print('Currently only arm64-v8a is supported. Welcome to join the development, support and maintain more architectures', style='bold red')
        exit_installer()
    if int(get_device_storage()) < 10:
        console.print('[yellow][*] Warning[/yellow], The device space is less than 10GB, there may be problems continuing to install')
    else:
        console.print('[green][*] Pass[/green], Available storage > 10GB')
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
    console.print('[green]You passed the test![/green] Now we deploy the FlyOS subsystem for you!')
    input("Press enter to continue")
    console.print('FlyOS Installer starts deploying subsystems for this device', style='green')
    # create dirs
    print("[START] STEP-1 Create FlyOS file system")
    runsys_root('mkdir /data/flyos')
    runsys_root('mkdir /data/local/flyos')
    console.print('[*] Done!', style='green')
if __name__ == '__main__':
    ui()