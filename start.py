"""flyos启动入口"""
import os
import time
import logging
import sqlite3
import threading
import subprocess

try:
    import func_timeout
except:
    os.chdir(os.getenv("FLYOS"))
    os.system("pip install -r $FLYOS/requirements.txt")
    os.chdir(os.getenv("HOME"))

HOME = os.getenv("HOME")
FLYOS = os.getenv("FLYOS")
WIDTH = os.get_terminal_size().columns

logging.basicConfig(filename=f"{HOME}/.flyos/boot.log", level=logging.INFO, format="[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y/%d/%m %I:%M:%S")

os.system("clear")

if not os.path.exists(HOME+"/.flyos/"): # 检测是否已经初始化
    os.system(f"python {FLYOS}/.firstuse/register.py")

print("flyos启动选项\n 1. 启动flyos\n 2. 启动恢复模式\n 3秒后自动启动flyos")

@func_timeout.func_set_timeout(3)
def get_input():
    """获取用户输入"""
    return input(">>> ")

try:
    input_ = get_input()
except func_timeout.exceptions.FunctionTimedOut:
    input_ = '1'

if input_ == '1':
    os.system('clear')
    logging.info("启动FlyOS")
    # 下面的代码是为了防止重复启动服务
    try:
        logging.info("读取父进程pid")
        with open(HOME+"/.flyos/ppid", "r") as f: # 读取之前保存的父进程的pid
            FLYOS_PPID = int(f.read(16))
            logging.info(f"成功读取到父进程pid:{FLYOS_PPID}")
    except FileNotFoundError:
        logging.warning("未能成功读取父进程pid")
        with open(HOME+"/.flyos/ppid", "w") as f: # 没有保存过
            f.write("0")
        FLYOS_PPID = 0
    if os.getppid() == FLYOS_PPID: # 如果这个进程的父进程pid与之前保存的一致, 就运行console.py
        logging.info("自启动项已经启动")
        logging.info("运行FlyOS主程序")
        os.system(f"python {FLYOS}/console.py")
    else:
        
        os.system("bash $FLYOS/services.sh")
elif input_ == '2':
    logging.info("启动FlyOS恢复模式")
    print("这是什么?")
    print("这是flyos的恢复模式,\n 当您的flyos无法正常启动的时候,\n 您可以尝试使用此模式恢复")
    os.system("bash")
else:
    print("错误选项")
