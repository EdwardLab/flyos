#飞屎OS Panel By:请遵守开源协议
#Use Under License GPL - V3
"""飞屎OS用户注册程序"""
import os
import sqlite3

import pywebio.input
from pywebio.output import put_html, popup, put_text
from pywebio import start_server
from pywebio.session import set_env

import termux_auth

飞屎OS_ROOT = os.getenv('飞屎OS')
HOME = os.getenv('HOME')

#Tips
print("______________________________________")
print("欢迎使用飞屎OS!")
print("请使用本机浏览器访问:http://127.0.0.1:5005 来初始化飞屎OS")
#飞屎OS 激活main
def main():
    """主方法"""
    if not os.path.exists(飞屎OS_ROOT+"/.firstuse/lock"):
        set_env(title="欢迎使用飞屎OS", auto_scroll_bottom=True)
        put_html("<h1>欢迎使用！ -- 飞屎OS 初始化向导</h1>")
        put_text('欢迎使用飞屎OS!开始初始化您的飞屎OS吧！')
        popup('Hi,There！欢迎使用飞屎OS！让我们来初始化飞屎OS吧！')
        
        password = pywebio.input.input("设置您的系统密码:", type="password")
        vpwd = pywebio.input.input("请再次输入密码验证:", type="password")
        if password != vpwd:
            popup('错误', "两次输入密码不一致，请刷新页面重试")
            return
        put_text('初始化完成！请进入termuxAPP开始体验飞屎OS吧！')
        termux_auth.change_passwd(password)
        os.mkdir(f"{HOME}/.飞屎OS")
    os.kill(os.getpid(), 9)

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=5005)
