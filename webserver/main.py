#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 19:11:50
LastEditTime: 2021-08-10 21:00:51
Description: 屎山2
'''
import os
print("飞屎OS-bate网站服务器管理中心")
print("By:飞屎OS-bate Group GPL-V3")
print("默认使用:Apache WEB服务器 默认支持PHP+Apache+Mysql")
print("面板功能列表:")
print("1.启动Apache服务")
print("2.停止Apache服务")
print("3.重启Apache服务")
print("4.切换到网站根目录")
print("5.启动mysql服务(错误不要管)")
print("6.查看mysql进程号")
print("7.停止mysql服务")
print("8.查看默认mysql用户名密码和修改root密码")
print("9.查看root登录方法")
print("10.远程登录数据库方法")
print("回车退出")
num = input("请输入编号:")
if num == '1':
    os.system("apachectl start")
elif num == '2':
    os.system("apachectl stop")
elif num == '3':
    os.system("apachectl restart")
elif num == '4':
    print("默认路径在:/data/data/com.termux/files/usr/share/apache2/default-site/")
    os.chdir("/data/data/com.termux/files/usr/share/apache2/default-site/")
elif num == '5':
    os.system("nohup mysqld &")
elif num == '6':
    os.system("ps aux|grep mysql")
elif num == '7':
    os.system("kill -9 `pgrep mysql`")
elif num == '8':
    print("默认mysql用户名为Termux，密码为空，使用mysql -u $(whoami)来登录")
    print("修改Root密码步奏:")
    print("""
  # 登录 Termux 用户
mysql -u $(whoami)

# 修改 root 密码的 SQL语句
use mysql;
set password for 'root'@'localhost' = password('你设置的密码');

# 刷新权限 并退出
flush privileges;
quit; 
""")
elif num == '9':
    print("""
mysql -u root -p
Enter password: xxxxx（这里输入你的密码)
  """)
elif num == '10':
    print("""
登录到root mysql账户
执行:
grant all on *.* to root@'%' identified by 'P@ssw0rd' with grant option;
flush privileges;
即可
  """)
else:
    print("退出")
