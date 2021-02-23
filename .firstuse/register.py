#FlyOS Panel By:XingYuJie
#Use Under License GPL - V3
import pywebio.input
from pywebio.output import *
from pywebio import *
import logging
import string
import os
from hashlib import md5
from pywebio.session import set_env
#下面的import是表单
from functools import partial
#Tips
print("______________________________________")
print("欢迎使用FlyOS!")
print("请使用本机浏览器访问:http://127.0.0.1:5005 来初始化FlyOS")
#FlyOS 激活main
def main():
    set_env(title="欢迎使用FlyOS", auto_scroll_bottom=True)
    put_markdown(r"""
    <h1>欢迎使用！ -- FlyOS 初始化向导</h1>
    """, strip_indent=4)
    put_text('欢迎使用FlyOS!开始初始化您的FlyOS吧！', sep=' ', inline=False, scope=- 1, position=- 1)
    output.popup('Hi,There！欢迎使用FlyOS！让我们来初始化FlyOS吧！')
    name = pywebio.input.input("请输入您的个人姓名/团队或公司名称来注册FlyOS:")
    password = pywebio.input.input("设置您的系统开机密码(如果您的设备被root，密码将不安全):", type="password")
    put_text('初始化完成！请进入termuxAPP开始体验FlyOS吧！', sep=' ', inline=False, scope=- 1, position=- 1)
    f = open('/data/data/com.termux/files/usr/etc/flyos/database/name.db', 'w')
    f.write(name)
    f.close()
    pggg = str(password)
    pggg = pggg
    md5_obj = md5()
    md5_obj.update(pggg.encode())
    pggg = md5_obj.hexdigest()
    print(pggg)
    f = open('/data/data/com.termux/files/usr/etc/flyos/database/password.db', 'w')
    f.write(pggg)
    f.close()
    os.system("touch $FLYOS/.firstuse/lock")
    os.system("flyos")
    
    hold()

#Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, port=5005)
    pywebio.session.hold()
