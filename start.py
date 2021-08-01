"""flyos启动入口"""
import os

HOME = os.getenv("HOME")
FLYOS = os.getenv("FLYOS")

os.system("clear")

if not os.path.exists(HOME+"/.flyos/"): # 检测是否已经初始化
    os.system(f"python {FLYOS}/.firstuse/register.py")

os.system('clear')
os.system("bash $FLYOS/services.sh")
