#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 19:11:49
LastEditTime: 2021-08-12 12:02:19
Description: 
'''
#飞屎OS-bate Panel By:请遵守开源协议
#Use Under License GPL - V3
import re
import subprocess

import pywebio.input
from pywebio import start_server
from pywebio.output import put_html, popup, put_text
from pywebio.session import set_env

import termux_auth

#Tips
print("___________________")
print("飞屎OS-bate Device API")
print("启动中")
#飞屎OS-bate WEB Panel main
def main():
    set_env(title="飞屎OS-bate Devices API Tool", auto_scroll_bottom=True)
    put_html("<h1>飞屎OS-bate Devices API Tool</h1>")
    pwd = pywebio.input.input("输入飞屎OS-bate密码: ")
print("FlyOS Device API")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Devices API Tool", auto_scroll_bottom=True)
    put_html("<h1>FlyOS Devices API Tool</h1>")
    pwd = pywebio.input.input("输入flyos密码: ")
    if termux_auth.auth(pwd):
        while 1:
            api = pywebio.input.input("输入api调用接口:")
            if re.search('[;&|<>$]', api):
                popup('检测到非法字符',
                        content="请检查命令中是否包含;&|等特殊字符"
                    )
                continue
            status, output = subprocess.getstatusoutput(f'termux-{api}')
            if status==0:
                popup('命令已执行', output)
            else:
                popup('执行时出现错误', output)
    else:
        put_text("密码错误, 请刷新页面重试")

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=5002)
    pywebio.session.hold()
