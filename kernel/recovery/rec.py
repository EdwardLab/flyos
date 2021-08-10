import os
import time
os.system("clear")
print("")
print("飞屎OS-bate Recovery")
print("Booting To Recovery...")
time.sleep(3)
os.system("clear")
print("_____ _        ___  ____")
print("|  ___| |_   _ / _ \\/ ___|")
print("| |_  | | | | | | | \\___ \\.")
print("|  _| | | |_| | |_| |___) |")
print("|_|   |_|\\__, |\\___/|____/")
print("         |___/")
print("__________________________")
print("飞屎OS-bate Recovery恢复/工程模式")
print("VER 1.1 KERNEL VERSION")
print("中文版VER_RELEASES")
print("1.重新安装飞屎OS-bate")
print("2.进入终端")
print("3.重启到RBOOT(RemoteBootTerminal))")
print("4.重启到Recovery")
print("5.快速更新飞屎OS-bate")
print("6.卸载飞屎OS-bate")
print("7.重启到系统")
num = input("请输入编号来启动项目:")
if num == '1':
    os.system("curl http://飞屎OS-bategeek.com/gosetup.sh | bash")
if num == '2':
    os.system("python $飞屎OS-bate/kernel/recovery/reccheck.py")
    os.system("bash")
elif num == '3':
    os.system("python $飞屎OS-bate/kernel/rboot/rboot.py")
elif num == '4':
    os.system("python $飞屎OS-bate/kernel/recovery/rec.py")
elif num == '5':
    os.system("cd $飞屎OS-bate && git pull")
elif num == '6':
    os.system("termux-reset")
elif num == '7':
    os.system("python $飞屎OS-bate/kernel/boot/active/active.py")
else:
    print("输入不正确")
