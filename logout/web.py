#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import pywebio.input
from pywebio.output import *
from pywebio import *
import logging
import string
import os
from pywebio.session import set_env
#下面的import是表单
from functools import partial
#Tips
print("______________________________________")
print("FlyOS Logout")
print("开发者工具")
print("请使用本机浏览器访问:http://127.0.0.1:4888 来远程注销FlyOS")
#FlyOS 激活main
def main():
    os.system("exit")
    hold()

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=4888)
    pywebio.session.hold()