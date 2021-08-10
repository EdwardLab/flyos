import time
import os
print("飞屎OS-bate飞聊软件--By:请遵守开源协议 Standard Edition")
print("[*]启动中")
time.sleep(1)
print("小提示:飞屎OS-bate分为两个部分:服务端和客户端，服务端用于搭建群聊，私聊服务。客户端输入服务器IP地址即可加入群组。本地搭建本地加入IP输入127.0.0.1即可")
print("您要启动:")
print("1.客户端")
print("2.服务端")
num = input("请输入编号(1或2)，按回车继续:")
if num == '1':
   os.system("python3 $飞屎OS-bate/chat/cilent.py")
if num == '2':
   os.system("python3 $飞屎OS-bate/chat/server.py")
else:
   print("请输入正确的编号，1或者2")
