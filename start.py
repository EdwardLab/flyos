"""飞屎OS启动入口"""
import os

HOME = os.getenv("HOME")
飞屎OS = os.getenv("飞屎OS")

os.system("clear")

if not os.path.exists(HOME+"/.飞屎OS/"): # 检测是否已经初始化
    os.system(f"python {飞屎OS}/.firstuse/register.py")

os.system('clear')
os.system("python $飞屎OS/update.py")
os.system("bash $飞屎OS/kernel/boot/bootkernel/bootlogo.sh")
#/data/data/com.termux/files/usr/etc/飞屎OS/kernel/boot/bootkernel/