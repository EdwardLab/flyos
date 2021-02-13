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
print("___________________")
print("FlyOS Device API")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Devices API Tool", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS Devices API Tool</h1>
    """, strip_indent=4)
    api = pywebio.input.input("输入api调用接口:")
    termux = "termux-" + api
    os.system(termux)
    print("继续使用请刷新页面")
    hold()
#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=5002)
    pywebio.session.hold()