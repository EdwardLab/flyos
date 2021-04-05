"""flyos启动入口"""
import os
import time
import sqlite3
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

print("flyos启动选项")
print("1. 启动flyos")
print("2. 启动恢复模式")
print("3秒后自动启动flyos")

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
    # 下面的代码是为了防止重复启动服务
    try:
        with open(HOME+"/.flyos/ppid", "r") as f: # 读取之前保存的父进程的pid
            FLYOS_PPID = int(f.read(16))
    except FileNotFoundError:
        with open(HOME+"/.flyos/ppid", "w") as f: # 没有保存过
            f.write("0")
        FLYOS_PPID = 0

    if os.getppid() == FLYOS_PPID: # 如果这个进程的父进程pid与之前保存的一致, 就运行console.py
        os.system(f"python {FLYOS}/console.py")
    else:
        with open(HOME+"/.flyos/ppid", "w") as f: # 如果不一样, 将父进程pid写入文件
            f.write(str(os.getppid()))
        print("运行自启动服务...")
        conn = sqlite3.connect(f'{HOME}/.flyos/service.db')
        cur = conn.cursor()
        data = cur.execute("SELECT * FROM boot WHERE status==1;")
        for i in data: # 运行开机自启动服务
            print(i[1])
            subprocess.Popen(i[1],
                    stderr=-1,
                    stdout=-1,
                    shell=True
                )
            time.sleep(0.1)
        conn.close()
        os.system(f"python {FLYOS}/console.py")
elif input_ == '2':
    print("这是什么?")
    print("这是flyos的恢复模式,"
            "当您的flyos无法正常启动的时候,"
            "您可以尝试使用此模式恢复")
    os.system("bash")
else:
    print("错误选项")
