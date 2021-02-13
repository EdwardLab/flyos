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
print("FlyOS Virtual Machine")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Virtual Machine", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>FlyOS WEB Virtual Machine</h1>
    """, strip_indent=4)
    put_text('FlyOS Virtual Machine By:XingYuJie', sep=' ', inline=False, scope=- 1, position=- 1)
    output.popup('欢迎使用FlyOS FlyOS Virtual Machine！', '欢迎使用FlyOS Virtual Machine。开始创建您的虚拟机吧！程序由MicroTech Projects -- FlyOS强力驱动')
  
    name = pywebio.input.input("请输入虚拟机的名称:")
    cpu = pywebio.input.input("请输入架构，例如i386架构:")
    path = pywebio.input.input("请输入虚拟机磁盘镜像完整绝对路径:")
    memory = pywebio.input.input("请输入虚拟机内存(不建议太大):")
    network = pywebio.input.input("请输入网卡驱动(建议rtl8139):")
    vga = pywebio.input.input("请输入显卡驱动(建议vmware):")
    vnc = pywebio.input.input("输入VNC端口号(建议0):")
  
    qemu = "qemu-system-" + cpu + " -hda " + path + " -m " + memory + " -device " + network + " -vga " + vga + " -vnc :" + vnc
    os.system(qemu)
    hold()
def webterminal():
    put_html('<h3>Popup Content</h3>')
    put_text('html: <br/>')
    put_buttons([('clear()', s)], onclick=clear)

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=8002)
    pywebio.session.hold()