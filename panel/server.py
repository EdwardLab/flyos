# 飞屎OS Panel By:请遵守开源协议
# Use Under License GPL - V3
import socket

import pywebio.input
from pywebio.output import popup, put_link, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env

print("______________________________________")
print("飞屎OS Panel")
print("启动中")
# 飞屎OS WEB Panel main


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def main():
    set_env(title="飞屎OS Panel",
            auto_scroll_bottom=True
            )
    put_html("<h1>飞屎OS WEB Panel</h1>")
    put_text('飞屎OS Panel By:请遵守开源协议',
             sep=' '
             )
    popup('欢迎使用飞屎OS Panel！',
          '欢迎使用飞屎OS WEB Panel！'
          '如果程序有Bug，'
          '请务必提交到邮箱:110github@gmail.com谢谢！'
          '程序由Python-pywebio强力驱动'
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
    put_link("飞屎OS桌面环境",
             url=f'http://{get_host_ip()}:6081/vnc.html'
             )
    put_text('_________系统工具__________',
             sep=' '
             )
    put_link("飞屎OS AM调用 ",
             url=f'http://{get_host_ip()}:5000'
             )
    put_text('_______________________',
             sep=' '
             )
    put_link("飞屎OS Termux:API调用 ",
             url=f'http://{get_host_ip()}:5002'
             )


if __name__ == '__main__':
    # print(get_host_ip())
    start_server(main, debug=True, host='0.0.0.0', port=8888)
    pywebio.session.hold()
