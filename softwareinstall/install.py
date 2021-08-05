import os

print("FlyOS Package Installer")
print("FlyOS 软件包安装器 By:Microtech Software Group")
print("请输入您要安装的软件包在哪个管理器(如果不懂，都可以尝试)")
print("1.PKG(apt) 2.pip")
num = input("请输入编号:")
packages = input("请输入要安装的软件包，例如vim(多个软件包直接可以用空格隔开，例如:vim ):")
if num == '1':
    os.system(f"pkg in {packages}")
if num == '2':
    os.system(f"pip install {packages}")
else:
    print("错误的选项!")