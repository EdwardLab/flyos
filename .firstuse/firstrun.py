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
print("激活FlyOS")
print("亲爱的用户您好:本机FlyOS尚未激活！")
print("请使用本机浏览器访问:http://127.0.0.1:5001 来激活FlyOS系统")
#FlyOS 激活main
def main():
    set_env(title="FlyOS初始化向导", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS 初始化向导</h1>
    """, strip_indent=4)
    put_text('欢迎使用FlyOS!开始设置您的FlyOS吧！', sep=' ', inline=False, scope=- 1, position=- 1)
    output.popup('Hi,There!Welcome To Use FlyOS,Now activate your system.')
    put_text('您好，您的FlyOS尚未激活，请根据以下提示来激活您的FlyOS系统', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("1.首先进入FlyOS激活官网获取设备密钥(点此进入)", url='http://flyos.club', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("2.下载FlyOS激活系统(点此下载)，然后安装打开，输入密钥并激活", url='https://assets.huoyinetwork.cn/Flyos/Activate/FlyOS_Activate_Pro_1.5.apk', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    put_text('3.完全退出并重新打开Termux', sep=' ', inline=False, scope=- 1, position=- 1)
    hold()

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=5001)
    pywebio.session.hold()