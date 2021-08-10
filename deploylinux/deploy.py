#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 19:11:49
LastEditTime: 2021-08-10 19:55:11
Description: 
'''
"""Linux部署程序--中文版"""
import os

strr='''
Linux部署程序--中文版
By:飞屎OS-bate MicroTech 抄袭王邢宇杰(严禁删除版权，不允许修改版权)GPL-V3
请选择系统(内置常用的几个系统):
1.Ubuntu
2.Debian
3.轻量级kali
4.Kali nethunter
5.Fedora
6.CentOS
7.Arch Linux(安装完请手动运行:chmod 755 additional.sh && ./afdtitonal.sh(只需首次运行前输入))
8.Alpine
---------------------------------------
安装完成后，请输入./start-系统名.sh启动。输入0退出
'''
print(strr)
num = input("请输入编码来安装系统:")

# 修改 if 叠杀人书 -- 更改屎山代码第一天
switch={
    "1":lambda:os.system(
        "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh"
    ),
    "2":lambda:os.system(
        "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Debian/debian.sh && bash debian.sh"
    ),
    "3":lambda:os.system(
        "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Kali/kali.sh && bash kali.sh"
    ),
    "4":lambda:os.system(
        "pkg install wget openssl-tool proot -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh"
    ),
    "5":lambda:os.system(
        "pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh"
    ),
    "6":lambda:os.system(
        "pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh"
    ),
    "7":lambda:os.system(
        "pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh"
    ),
    "8":lambda:os.system(
        "pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.fastgit.org/ChenYifei21/Scripts/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh"
    ),
    "0":lambda:exit()


}

try:
    switch[num]()
except KeyError:
    print("输入的数字有误! 阿巴阿巴~~")
