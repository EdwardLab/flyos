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
print("FlyOS Panel")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Panel", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS WEB Panel</h1>
    """, strip_indent=4)
    put_text('FlyOS Panel By:XingYuJie', sep=' ', inline=False, scope=- 1, position=- 1)
    output.popup('欢迎使用FlyOS Panel！', '欢迎使用FlyOS WEB Panel！如果程序有Bug，请务必提交到邮箱:xingyujie50@gmail.com谢谢！程序由MicroTech Projects -- FlyOS强力驱动')
    pywebio.output.put_link("本地WEB终端", url='http://127.0.0.1:4200', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("VM虚拟机", url='http://127.0.0.1:8002', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("Apache主页", url='http://127.0.0.1:8080', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("Nginx主页", url='http://127.0.0.1:8088', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("HTTP文件服务器", url='http://127.0.0.1:8081', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("FlyOS RunShell Tool", url='http://127.0.0.1:8887', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_________系统工具__________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("FlyOS AM调用 ", url='http://127.0.0.1:5000', app=None, new_window=False, scope=- 1, position=- 1)
    put_text('_______________________', sep=' ', inline=False, scope=- 1, position=- 1)
    pywebio.output.put_link("FlyOS Termux:API调用 ", url='http://127.0.0.1:5002', app=None, new_window=False, scope=- 1, position=- 1)
    hold()
def webterminal():
    put_html('<h3>Popup Content</h3>')
    put_text('html: <br/>')
    put_buttons([('clear()', s)], onclick=clear)

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=8888)
    pywebio.session.hold()