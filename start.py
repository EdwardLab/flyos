"""飞屎OS-bate启动入口"""
import os

HOME = os.getenv("HOME")
飞屎OS-bate = os.getenv("飞屎OS-bate")

os.system("clear")

if not os.path.exists(HOME+"/.飞屎OS-bate/"): # 检测是否已经初始化
    os.system(f"python {飞屎OS-bate}/.firstuse/register.py")

os.system('clear')
os.system("python $飞屎OS-bate/update.py")
os.system("bash $飞屎OS-bate/kernel/boot/bootkernel/bootlogo.sh")
#/data/data/com.termux/files/usr/etc/飞屎OS-bate/kernel/boot/bootkernel/