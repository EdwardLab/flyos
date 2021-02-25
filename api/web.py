#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import os
import re
import time

import pywebio.input
from pywebio.output import *
from pywebio import *
from pywebio.session import set_env
#下面的import是表单
from functools import partial

import termux_auth

#Tips
print("___________________")
print("FlyOS Device API")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Devices API Tool", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS Devices API Tool</h1>
    """, strip_indent=4)
    pwd = pywebio.input.input("输入flyos密码: ")
    if termux_auth.auth(pwd):
        while 1:
            api = pywebio.input.input("输入api调用接口:")
            if re.search('[;&|<>$]', api):
                popup('检测到非法字符', content="请检查命令中是否包含;&|等特殊字符")
                continue
            os.system(f'termux-{api}')
    else:
        put_text("密码错误, 请刷新页面重试")
        return 
    hold()
#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=5002)
    pywebio.session.hold()
