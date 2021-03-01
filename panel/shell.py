#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import os

import pywebio.input
from pywebio.output import put_html, put_text
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
    put_text('FlyOS RunShellTool By:XingYuJie',
            sep=' '
        )
    runshell = pywebio.input.input(
            "Shell终端命令执行"
            "请输入要执行的命令(会在后台执行):"
            )
    fastrun = pywebio.input.input("FlyOS快速运行程序(已在FlyOS环境下):")
    #启动FlyOSfastrun
    os.system("python $FLYOS" + fastrun)
    print("你输入的命令(结果在下方): %s" % runshell)
    #使用runshell
    os.system(runshell)

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=8887)
    pywebio.session.hold()
