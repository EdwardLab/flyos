#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import pywebio.input
from pywebio.output import popup, put_link, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env

print("______________________________________")
print("FlyOS Panel")
print("启动中")
#FlyOS WEB Panel main
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
    put_link("本地WEB终端",
            url='http://127.0.0.1:4200'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("VM虚拟机",
            url='http://127.0.0.1:8002'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("Apache主页",
            url='http://127.0.0.1:8080'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("Nginx主页",
            url='http://127.0.0.1:8088'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("HTTP文件服务器",
            url='http://127.0.0.1:8081'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("FlyOS RunShell Tool",
            url='http://127.0.0.1:8887'
        )
    put_text('_________系统工具__________',
            sep=' '
        )
    put_link("FlyOS AM调用 ",
            url='http://127.0.0.1:5000'
        )
    put_text('_______________________',
            sep=' '
        )
    put_link("FlyOS Termux:API调用 ",
            url='http://127.0.0.1:5002'
            )

if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=8888)
    pywebio.session.hold()
