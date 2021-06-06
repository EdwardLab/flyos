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
    os.system("bash $FLYOS/services.sh")
elif input_ == '2':
    logging.info("启动FlyOS恢复模式")
    print("这是什么?")
    print("这是flyos的恢复模式,\n 当您的flyos无法正常启动的时候,\n 您可以尝试使用此模式恢复")
    os.system("bash")
else:
    print("错误选项")
