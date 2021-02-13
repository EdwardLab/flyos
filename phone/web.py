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
print("FlyOS Phone Shell")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Phone Shell", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS WEB Phone Shell</h1>
    """, strip_indent=4)
    put_text('FlyOS Phone Web Shell By:XingYuJie', sep=' ', inline=False, scope=- 1, position=- 1)
    am = pywebio.input.input("请输入AM参数加命令:")
    os.system("am " + am)
    hold()

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=5000)
    pywebio.session.hold()