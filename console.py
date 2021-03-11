#作者:邢宇杰 Xingyujie GPL-V3
#请根据协议发布，严禁违反
import os
import time
import getpass
import datetime

print("_____ _        ___  ____")
print("|  ___| |_   _ / _ \\/ ___|")
print("| |_  | | | | | | | \\___ \\.")
print("|  _| | | |_| | |_| |___) |")
print("|_|   |_|\\__, |\\___/|____/")
print("         |___/")
print("_________________________")
print("__________FlyOS__________")
#获取年月日格式的时间
date = time.strftime("%Y-%m-%d %H:%M:%S")
print("现在时间:" + date)
i = datetime.datetime.now()
PREFIX='''\n日　期：{}年{}月{}日 时　间：{} \n'''.format(i.year,i.month,i.day,time.strftime('%p %X'))
print(PREFIX)
print(f"{getpass.getuser()}欢迎使用FlyOS!")
print("欢迎使用FlyOS开源面板！")
print("By:XingYuJie Rainbow")
print("FlyOS由Microtech开发")
print("输入00查看关于")
print("输入01反馈问题")
print("1.给FlyOS 安装GNU/发行版Linux(推荐|简洁)")
print("2.Linux菜单高级部署菜单(推荐)")
print("3.软件安装器(Termux软件包)")
print("4.启动最近使用的GNU/Linux")
print("5.FlyOS Chat 飞聊聊天系统")
print("6.重新查看激活状态/重启")
print("7.更新软件源APT")
print("8.更新软件源PKG")
print("9.查看系统信息")
print("10.更改默认Shell解释器")
print("11.更改Termux密码")
print("12.FlyOS浏览器")
print("13.网站服务器面板")
print("14.重新启动FlyOS WEB Panel(已自动启动，再次启动会出问题)")
print("15.打开Aria2")
print("16.打开Aria2 WEB")
print("17.VM虚拟机")
print("18.文件管理器")
print("19.虚拟机WEB管理面板(已自动启动，再次启动会出问题)")
print("20.启动nginx WEB Server")
print("21.初始化FlyOS")
print("22.启动Xfce4图形化(端口5902)")
print("0.进入终端")
print("如需再次打开FlyOS Console，进入终端输入flyos即可")
print("####FlyOS Panel已经启动，"
        "浏览器访问http://IP:8888，"
        "WebShell请浏览器访问http://IP:4200，"
        "WEB虚拟机请访问http://IP:8002，"
        "Apache服务请访问http://IP:8080，"
        "Nginx在http://IP:8088，"
        "HTTP文件管理器在http://IP:8081，"
        "FlyOS AM调用在http://IP:5000，"
        "Termux:API调用在http://IP:5002。"
        "注意，本地访问请浏览器访问http://127.0.0.1:端口号####")
while 1:
    num = input("请输入要启动的编号，例如:1 :")
    print("正在启动项目" + num)
    if num == '1':
        os.system("python3 $FLYOS/deploylinux/deploy.py")
    elif num == '2':
        os.system("tmoe")
    elif num == '3':
        os.system("python3 $FLYOS/softwareinstall/install.py")
    elif num == '4':
        os.system("debian")
    elif num == '5':
        os.system("python3 $FLYOS/chat/chat.py")
    elif num == '6':
        os.system("python3 $FLYOS/console.py")
    elif num == '7':
        os.system("apt update")
    elif num == '8':
        os.system("pkg update")
    elif num == '9':
        os.system("screenfetch")
    elif num == '10':
        os.system("chsh")
    elif num == '11':
        print("您可以更改FlyOS的默认User密码")
        os.system("passwd")
    elif num == '12':
        website = input("欢迎使用FlyOS Browser浏览器，例如:http://www.bing.com --必应 输入网址开始浏览网页:")
        os.system("w3m " + website)
    elif num == '13':
        os.system("python3 $FLYOS/webserver/main.py")
    elif num == '14':
        os.system("sh $FLYOS/panel/server.py")
    elif num == '15':
        os.system("aria2c --enable-rpc --rpc-listen-all")
    elif num == '16':
        os.chdir('/data/data/com.termux/files/home/webui-aria2')
        os.system('node node-server.js')
    elif num == '17':
        os.system("python $FLYOS/virtualmachine/vm.py")
    elif num == '18':
        os.system("mc")
    elif num == '19':
        os.system("python $FLYOS/virtualmachine/web.py")
    elif num == '20':
        os.system("nginx")
    elif num == '21':
        os.system("python $FLYOS/.firstuse/register.py")
    elif num == '22':
        print("Xfce4图形化界面启动在IP:5902，本地连接请输入IP:127.0.0.1:5902")
        os.system("nohup flyosvnc &")
    elif num == '0':
        os.system('zsh')
    elif num == '00':
        print("关于:\n开发者创始人:Rainbow邢宇杰\n邮箱:xingyujie50@gmail.com\n当前版本:bilndv2.7")
    elif num == '01':
        print("有BUG请反馈到:xingyujie50@gmail.com")
    else:
        print("请输入选项")
