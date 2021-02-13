import time
import os
print("FlyOS飞聊软件--By:XingYuJie Standard Edition")
print("[*]启动中")
time.sleep(1)
print("小提示:FlyOS分为两个部分:服务端和客户端，服务端用于搭建群聊，私聊服务。客户端输入服务器IP地址即可加入群组。本地搭建本地加入IP输入127.0.0.1即可")
print("您要启动:")
print("1.客户端")
print("2.服务端")
num = input("请输入编号(1或2)，按回车继续:")
if num == '1':
   os.system("python3 $FLYOS/chat/cilent.py")
if num == '2':
   os.system("python3 $FLYOS/chat/server.py")
else:
   print("请输入正确的编号，1或者2")
