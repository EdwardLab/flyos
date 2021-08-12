<<<<<<< HEAD
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
=======
"""flyos启动入口"""
import os

HOME = os.getenv("HOME")
FLYOS = os.getenv("FLYOS")

os.system("clear")

if not os.path.exists(HOME+"/.flyos/"): # 检测是否已经初始化
    os.system(f"python {FLYOS}/.firstuse/register.py")

os.system('clear')
os.system("python $FLYOS/update.py")
os.system("bash $FLYOS/kernel/boot/bootkernel/bootlogo.sh")
#/data/data/com.termux/files/usr/etc/flyos/kernel/boot/bootkernel/
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
