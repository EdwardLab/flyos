#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import re
import subprocess

import pywebio.input
from pywebio.output import put_text, popup, put_html
from pywebio import start_server
from pywebio.session import set_env

import termux_auth
#Tips
print("___________________")
print("FlyOS Phone Shell")
print("启动中")
#FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Phone Shell",
            auto_scroll_bottom=True
        )
    put_html("<h1>FlyOS WEB Phone Shell</h1>")
    put_text('FlyOS Phone Web Shell By:XingYuJie',
            sep=' '
        )
    pwd = pywebio.input.input("输入flyos密码:")
    if termux_auth.auth(pwd):
        while 1:
            command = pywebio.input.input("请输入AM参数加命令:")
            if re.search('[;&|<>$]', command):
                popup('检测到非法字符',
                        content="请检查命令中是否包含;&|等特殊字符"
                    )
                continue
            status, output = subprocess.getstatusoutput("am " + command)
            if status==0:
                popup('命令已执行', output)
            else:
                popup('命令执行时出现错误', output)
    else:
        put_text("密码错误，请刷新页面重试")

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=5000)
    pywebio.session.hold()
