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
    put_text('FlyOS RunShellTool By:XingYuJie', sep=' ', inline=False, scope=- 1, position=- 1)
   
    runshell = pywebio.input.input("Shell终端命令执行，请输入要执行的命令(会在后台执行):", lstrip=True)
    fastrun = pywebio.input.input("FlyOS快速运行程序(已在FlyOS环境下):")
    #启动FlyOSfastrun
    os.system("python $FLYOS" + fastrun)
    #结束Fastrun
    hold()
    print("你输入的命令(结果在下方): %s" % runshell)
    #使用runshell
    os.system(runshell)
    hold()
def webterminal():
    put_html('<h3>Popup Content</h3>')
    put_text('html: <br/>')
    put_buttons([('clear()', s)], onclick=clear)

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=8887)
    pywebio.session.hold()