#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import socket

import pywebio.input
from pywebio.output import popup, put_link, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env

print("______________________________________")
print("FlyOS Panel")
print("启动中")
#FlyOS WEB Panel main
def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def main():
    set_env(title="FlyOS Panel",
            auto_scroll_bottom=True
        )
    put_html("<h1>FlyOS WEB Panel</h1>")
    put_text('FlyOS Panel By:XingYuJie',
            sep=' '
        )
    popup('欢迎使用FlyOS Panel！',
            '欢迎使用FlyOS WEB Panel！'
            '如果程序有Bug，'
            '请务必提交到邮箱:xingyujie50@gmail.com谢谢！'
            '程序由MicroTech Projects -- FlyOS强力驱动'
        )
    put_link("web终端",
            url=f'http://{get_host_ip()}:7681'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("VM虚拟机",
            url=f'http://{get_host_ip()}:8002'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("vscode",
            url=f'http://{get_host_ip()}:2001'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("Apache主页",
            url=f'http://{get_host_ip()}:8080'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("Nginx主页",
            url=f'http://{get_host_ip()}:8088'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("HTTP文件服务器",
            url=f'http://{get_host_ip()}:8081'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("jupyter notebook",
            url=f'http://{get_host_ip()}:2000'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("FlyOS桌面环境",
            url=f'http://{get_host_ip()}:6081/vnc.html'
        )
    put_text('_________系统工具__________',
            sep=' '
        )
    put_link("FlyOS AM调用 ",
            url=f'http://{get_host_ip()}:5000'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("FlyOS Termux:API调用 ",
            url=f'http://{get_host_ip()}:5002'
            )

if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=8888)
    pywebio.session.hold()
