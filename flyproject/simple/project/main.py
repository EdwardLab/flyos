#FlyOS环境检查
try:
    f =open('/data/data/com.termux/files/usr/etc/flyos/.flyos/check')
    f.close()
except FileNotFoundError:
    print("运行出错！未知的环境！非FlyOS运行时！")
#界面设计 simple UI 标题不应太长，否则无法正常显示
print("_____________________________________")
print("标题--一个简单的例子程序 SimpleUI")
print("_____________________________________")
#提行代码
print("")
#跳转到核心文件代码
import os
os.system("python index.py")
