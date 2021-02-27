import os
print("开始安装软件包" + appname)
print("软件信息:")
print("开发者" + name)
print("版本号" + ver)
print("项目名称" + projectname)
input("来源于未知来源的FlyOS软件包，该软件包可能会伤害您的设备，您确定要安装吗？(回车继续)")
os.system("python install.py")