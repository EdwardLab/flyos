#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 21:13:42
LastEditTime: 2021-08-10 21:13:43
Description: 
'''
#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
import os
import time
import datetime
import getpass
import socket
os.system('clear')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
print('OOOPS\xe4\xbd\xa0\xe6\xb2\xa1\xe6\x9c\x89\xe6\xbf\x80\xe6\xb4\xbb!')
print('\xe4\xba\x86\xe8\xa7\xa3飞屎OS-bate\xe5\xae\x8c\xe6\x95\xb4\xe7\x89\x88\xe7\x9a\x84\xe9\xad\x85\xe5\x8a\x9b\xef\xbc\x9f')
print('飞屎OS-bate Console\xe6\x9c\x89\xe9\x99\x90\xe5\x88\xb6\xe5\x8a\x9f\xe8\x83\xbd\xe7\x9a\x84\xe9\xa2\x84\xe8\xa7\x88:')
os.system('toilet -f mono12 -F gay 飞屎OS-bate')
print('__________________________')
print('________飞屎OS-bate vx.xx________')
date = time.strftime('%Y-%m-%d %H:%M:%S')
print('\xe7\x8e\xb0\xe5\x9c\xa8\xe6\x97\xb6\xe9\x97\xb4:' + date)
i = datetime.datetime.now()
PREFIX = '\n\xe6\x97\xa5\xe3\x80\x80\xe6\x9c\x9f\xef\xbc\x9a{}\xe5\xb9\xb4{}\xe6\x9c\x88{}\xe6\x97\xa5 \xe6\x97\xb6\xe3\x80\x80\xe9\x97\xb4\xef\xbc\x9a{} \n'.format(i.year, i.month, i.day, time.strftime('%p %X'))
print(PREFIX)
print(f'''{getpass.getuser()}\xe6\xac\xa2\xe8\xbf\x8e\xe4\xbd\xbf\xe7\x94\xa8飞屎OS-bate!''')
# WARNING: Decompyle incomplete

