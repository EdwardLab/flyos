import os
#FlyOS 信息存储文件
#您可以在这里编写您的程序信息
#信息中不允许出现空格
appname='exmaple_simple_project'
#软件名称
ver='1'
#软件版本
projectname='MicroTech_FlyOS'
#项目名称
name='xingyujie'
#请不要更改以下参数！！！否则无法安装！
import os
print("开始安装软件包" + appname)
print("软件信息:")
print("开发者" + name)
print("版本号" + ver)
print("项目名称" + projectname)
input("来源于未知来源的FlyOS软件包，该软件包可能会伤害您的设备，您确定要安装吗？(回车继续)")
os.system("python install.py")