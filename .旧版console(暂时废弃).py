import os
import time
print("FlyOS For Termux Console")
print("MicroTech Software Group GPL-V3")
print("[*]启动FlyOS面板")
time.sleep(2)
print("[*]Done!")
print("FlyOS主菜单")
print("1.安装GNU/Linux(例如Debian,Ubuntu)")
print("2.部署Kali nethunter(完整版)")
print("3.启动FlyOS桌面环境(默认XFCE)")
print("4.部署Ubuntu20.10")
num = input("请输入程序编号:")
#判断用户输入
if num == '1':
  os.system("sh deploylinux.sh")
elif num == '2':
  os.system("sh deploylinux.sh")
elif num == '3':
  os.system("sh deploylinux.sh")
elif num == '4':
  os.system("sh deploylinux.sh")
elif num == '5':
  os.system("sh deploylinux.sh")
elif num == '6':
  os.system("sh deploylinux.sh")
elif num == '7':
  os.system("sh deploylinux.sh")
else:
  print("请输入正确的编号！")