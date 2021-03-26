import os
import time
import json
import curses
import subprocess

HOME = os.getenv("HOME")
FLYOS = os.getenv("FLYOS")

recovery_mode = 0

def printMsg(y, x, msg, scr):
    scr.addstr(y, x, msg)
    scr.refresh()
    time.sleep(0.1)

def main(stdscr):
    global recovery_mode
    curses.halfdelay(30)
    curses.curs_set(0)
    front_white = (curses.COLS-17)//2
    behind_white = curses.COLS-front_white-17
    stdscr.addstr(0,
            0,
            " "*front_white+"flyos启动引导程序"+" "*behind_white,
            curses.A_REVERSE
            )
    printMsg(1,
            (curses.COLS-19)//2,
            "将在3秒钟后启动flyos\n",
            stdscr
            )
    printMsg(2,
            (curses.COLS-19)//2,
            "按下任意键启动flyos\n",
            stdscr
            )
    printMsg(3,
            (curses.COLS-19)//2,
            "按下r键启动恢复模式\n",
            stdscr
            )
    try:
        key = stdscr.getkey()
        if key == 'r':
            stdscr.clear()
            printMsg(0, 0, "正在启动恢复模式...", stdscr)
            recovery_mode=1
            time.sleep(1)
            curses.endwin()
            return

    except curses.error:
        pass
    stdscr.clear()
    printMsg(0, 0, "flyos启动中...", stdscr)
    printMsg(1, 0, "运行自启动服务...", stdscr)
    printMsg(curses.LINES-2,
            0,
            "启动进度: ["+" "*(curses.COLS-12)+"]",
            stdscr
            )
    with open(HOME+"/.flyos/boot.json") as f:
        data = json.load(f)
    tasks_len = len(data["boot"])
    quantity = (curses.COLS-12)//tasks_len
    for i in enumerate(data["boot"]):
        subprocess.getoutput(i[1])
        printMsg(curses.LINES-2,
                12,
                "="*(quantity*(i[0]+1)),
                stdscr
                )
    time.sleep(0.1)
    with open(HOME+"/.flyos/ppid", "w") as f:
        f.write(str(os.getppid()))
    curses.endwin()

if not os.path.exists(HOME+"/.flyos/"):
    os.system(f"python {FLYOS}/.firstuse/register.py")

try:
    with open(HOME+"/.flyos/ppid", "r") as f:
        flyos_ppid = f.read(10)
except:
    with open(HOME+"/.flyos/ppid", "w") as f:
        f.write("0")
        flyos_ppid = 0
if str(os.getppid()) == flyos_ppid:
    os.system(f"python {FLYOS}/console.py")
else:
    curses.wrapper(main)
    if recovery_mode:
        os.system("clear")
        os.chdir(HOME)
        print("这是什么?")
        print("这是flyos的恢复模式,"
                "当您的flyos无法正常启动的时候,"
                "您可以尝试使用此模式恢复")
        os.system("bash")
        exit()
    os.system(f"python {FLYOS}/console.py")
