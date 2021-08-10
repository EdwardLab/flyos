#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 19:11:50
LastEditTime: 2021-08-10 20:34:55
Description: 
'''
# 飞屎OS Panel By:请遵守开源协议
# Use Under License GPL - V3
import re
import subprocess

import pywebio.input
from pywebio.output import put_text, popup, put_html
from pywebio import start_server
from pywebio.session import set_env

import termux_auth
# Tips
print("___________________")
print("飞屎OS Phone Shell")
print("启动中")
# 飞屎OS WEB Panel main


def main():
    set_env(title="飞屎OS Phone Shell",
            auto_scroll_bottom=True
            )
    put_html("<h1>飞屎OS WEB Phone Shell</h1>")
    put_text('飞屎OS Phone Web Shell By:请遵守开源协议',
             sep=' '
             )
    pwd = pywebio.input.input("输入飞屎OS密码:")
    if termux_auth.auth(pwd):
        while 1:
            command = pywebio.input.input("请输入AM参数加命令:")
            if re.search('[;&|<>$]', command):
                popup('检测到非法字符',
                      content="请检查命令中是否包含;&|等特殊字符"
                      )
                continue
            status, output = subprocess.getstatusoutput("am " + command)
            if status == 0:
                popup('命令已执行', output)
            else:
                popup('命令执行时出现错误', output)
    else:
        put_text("密码错误，请刷新页面重试")


# Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=5000)
    pywebio.session.hold()
