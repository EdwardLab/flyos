#作者:请遵守开源协议 GPL-V3
#请根据协议发布，严禁违反
"""飞屎OS主程序"""
import os
import time
import getpass
import datetime
import subprocess
import socket
import requests
import termux_auth
#ip获取
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))
ip=s.getsockname()[0]
HOME = os.getenv("HOME")
username=getpass.getuser()


os.system("clear")

#print("_____ _        ___  ____")
#print("|  ___| |_   _ / _ \\/ ___|")
#print("| |_  | | | | | | | \\___ \\.")
#print("|  _| | | |_| | |_| |___) |")
#print("|_|   |_|\\__, |\\___/|____/")
#print("         |___/")
os.system("toilet -f mono12 -F gay 飞屎OS")
print("__________________________")
print("________飞屎OS v4.8________")
#获取年月日格式的时间
date = time.strftime("%Y-%m-%d %H:%M:%S")
print("现在时间:" + date)
i = datetime.datetime.now()
PREFIX='''\n日　期：{}年{}月{}日 时　间：{} \n'''.format(i.year,i.month,i.day,time.strftime('%p %X'))
print(PREFIX)
print(f"{getpass.getuser()}欢迎使用飞屎OS!")

try:
    print(requests.get("http://飞屎OSgeek.com/notices.txt").content.decode("utf-8"))
except Exception:
    print("获取公告失败")

print("欢迎使用飞屎OS开源面板！")
print("By:请遵守开源协议 抄袭王邢宇杰")
print("飞屎OS由Microtech开发")
print("输入00查看关于")
print("输入01反馈问题")
print("输入02快速更新")
print("输入03切换更新通道")
print("输入04完整更新")
print("1.给飞屎OS 安装GNU/发行版Linux(推荐|简洁)")
print("2.Linux菜单高级部署菜单(推荐)")
print("3.软件安装器(Termux软件包)")
print("4.启动最近使用的GNU/Linux")
print("5.飞屎OS Chat 飞聊聊天系统")
print("6.重新查看激活状态/重启")
print("7.更新软件源APT")
print("8.更新软件源PKG")
print("9.查看系统信息")
print("10.更改默认Shell解释器")
print("11.更改Termux密码")
print("12.飞屎OS浏览器")
print("13.网站服务器面板")
print("14.重新启动飞屎OS WEB Panel(已自动启动，再次启动会出问题)")
print("15.打开Aria2")
print("16.打开Aria2 WEB")
print("17.VM虚拟机")
print("18.文件管理器")
print("19.虚拟机WEB管理面板(已自动启动，再次启动会出问题)")
print("20.启动nginx WEB Server")
print("21.初始化飞屎OS")
print("22.启动Xfce4图形化(端口5902)")
print("23.启动pocketmine Minecraft基岩服务器")
print("24.启动Nukkitx Minecraft基岩服务器")
print("0.进入终端")
print("如需再次打开飞屎OS Console，进入终端输入飞屎OS即可")
print("####飞屎OS Panel已经启动，请使用手机网络浏览器或者其他设备访问http://" + ip + ":8888，VNC桌面环境请使用VNC客户端连接到" + ip + ":5902")
print("!!序号使用帮助:请在下面🚀后输入要启动的编号，例如1")
while 1:
    print(f"👉👉👉👉👉👉👉👉{getpass.getuser()}🌈")
    os.system("pwd")
    num = input("✈️ " + date + "🚀🚀🚀 >>> ")
    #print("正在启动项目或命令" + num)
    try:
        int(num)
    except:
        os.system(num)
    if num == '1':
        os.system("python3 $飞屎OS/deploylinux/deploy.py")
    elif num == '2':
        os.system("tmoe")
    elif num == '3':
        os.system("python3 $飞屎OS/softwareinstall/install.py")
    elif num == '4':
        os.system("debian")
    elif num == '5':
        os.system("python3 $飞屎OS/chat/chat.py")
    elif num == '6':
        os.system("python3 $飞屎OS/console.py")
    elif num == '7':
        os.system("apt update")
    elif num == '8':
        os.system("pkg update")
    elif num == '9':
        os.system("screenfetch")
    elif num == '10':
        os.system("chsh")
    elif num == '11':
        print("您可以更改飞屎OS的默认User密码")
        os.system("passwd")
    elif num == '12':
        website = input("欢迎使用飞屎OS Browser浏览器，例如:http://www.bing.com --必应 输入网址开始浏览网页:")
        os.system("w3m " + website)
    elif num == '13':
        os.system("python3 $飞屎OS/webserver/main.py")
    elif num == '14':
        os.system("python3 $飞屎OS/panel/server.py")
    elif num == '15':
        os.system("aria2c --enable-rpc --rpc-listen-all")
    elif num == '16':
        os.chdir('/data/data/com.termux/files/home/webui-aria2')
        os.system('node node-server.js')
    elif num == '17':
        os.system("bash $飞屎OS/virtualmachine/vm.sh")
    elif num == '18':
        os.system("mc")
    elif num == '19':
        os.system("python $飞屎OS/virtualmachine/web.py")
    elif num == '20':
        os.system("nginx")
    elif num == '21':
        os.system("python $飞屎OS/.firstuse/register.py")
    elif num == '22':
        print("Xfce4图形化界面启动在IP:5902，本地连接请输入IP:127.0.0.1:5902")
        os.system("nohup 飞屎OSvnc &")
    elif num == '23':
        os.system("bash $飞屎OS/mc/PHP/start.sh")
    elif num == '24':
        os.system("python $飞屎OS/mc/JAVAPE/cr.py")
    elif num == '0':
        os.system('zsh')
    elif num == '00':
        print("关于:\n开发者创始人:抄袭王邢宇杰邢宇杰\n邮箱:110github@gmail.com")
    elif num == '01':
        print("有BUG请反馈到:110github@gmail.com")
    elif num == '02':
        print("将会进行快速更新")
        print("快速更新有可能会出现问题，但不会删除用户数据")
        input_ = input("继续吗 [y/N] ")
        if input_ == 'y':
            os.chdir(os.getenv('飞屎OS'))
            os.system('git reset --hard')
            os.system('git pull')
            os.system('pip install -r requirements.txt')
            os.chdir(os.getenv('HOME'))
            print("完成")
        else:
            print("取消")
    elif num == '03':
        os.chdir(os.getenv('飞屎OS'))
        print("输入1切换到稳定版")
        print("输入2切换到preview版")
        print("输入3切换到beta版")
        print("输入4切换到dev版(不稳定, 更新最快)")
        print("输入q返回主菜单")
        while 1:
            input_ = input(">>> ")
            if input_ == '1':
                os.system('git checkout master')
            elif input_ == '2':
                os.system('git checkout preview')
            elif input_ == '3':
                os.system('git checkout beta')
            elif input_ == '4':
                os.system('git checkout dev')
            elif input_ == 'q':
                break
            else:
                print("无效输入")
    elif num == '04':
        print("注意:")
        print("完整更新将会删除所有用户数据")
        if input("真的要继续吗? [y/N] ") == 'y':
            os.system("curl 飞屎OSgeek.com/gosetup.sh|bash")
        else:
            print("取消操作")
    else:
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        print("")
        #可以写每次运行完命令显示的内容
