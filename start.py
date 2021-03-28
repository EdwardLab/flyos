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

def bsod(stdscr, error):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
    stdscr.clear()
    stdscr.addstr(0, 0, "flyos启动时出现了一些错误")
    stdscr.addstr(1, 0, "将会在5秒后重新启动flyos")
    stdscr.addstr(2, 0, "启动flyos时请不要乱动您的设备")
    stdscr.addstr(3, 0, "如果此问题重复出现, 请反馈至交流群")
    stdscr.addstr(4, 0, "你也可以尝试通过恢复模式修复问题")
    stdscr.addstr(6, 0, f"有关问题的详细信息: {error}")
    stdscr.refresh()
    time.sleep(5)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.bkgd(' ', curses.color_pair(1))
    os.system("clear")
    print("启动flyos...")
    time.sleep(1)
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
            "按下回车键启动flyos\n",
            stdscr
            )
    printMsg(3,
            (curses.COLS-19)//2,
            "按下r键启动恢复模式\n",
            stdscr
            )
    try:
        while 1:
            key = stdscr.getkey()
            if key == 'r':
                stdscr.clear()
                printMsg(0, 0, "正在启动恢复模式...", stdscr)
                recovery_mode=1
                time.sleep(1)
                curses.endwin()
                return
            elif key == '\n':
                break

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
        subprocess.Popen(i[1],
                stderr=-1,
                stdout=-1,
                shell=True
                )
        printMsg(curses.LINES-2,
                12,
                "="*(quantity*(i[0]+1)),
                stdscr
                )
        printMsg(i[0]+2,
                0,
                i[1],
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
    while 1:
        try:
            curses.wrapper(main)
        except Exception as e:
            curses.wrapper(lambda scr: bsod(scr, e))
        else:
            break
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
