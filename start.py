from os.path import exists
from os import getenv, system
from getpass import getpass

import termux_auth

FLYOS_ROOT = getenv('FLYOS')

if exists(f'{FLYOS_ROOT}/.firstuse/lock'): # 检查是否已经注册
    with open(f'{FLYOS_ROOT}/database/password.db','r') as f: # 打开密码存放文件
        password = f.readline() # 读取密码
    
    while 1:
        inputpass = getpass("请输入开机密码: ") # 读取输入的密码

        if termux_auth.auth(inputpass): # 验证密码是否正确
            system(f"python {FLYOS_ROOT}/console.py")
            exit()
        else:
            print("密码错误")
else:
    system("python3 $FLYOS/.firstuse/register.py")
