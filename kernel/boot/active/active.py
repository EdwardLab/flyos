#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 21:09:49
LastEditTime: 2021-08-10 21:10:00
Description: 
'''
import os
print('\xe6\xa3\x80\xe6\x9f\xa5\xe7\xb3\xbb\xe7\xbb\x9f\xe6\xbf\x80\xe6\xb4\xbb')
f = open('/data/data/com.termux/files/home/.飞屎OS/active/key.fk', 'r')
i = f.read().split('-')
if not i[0]:
    print('\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7\xe6\x97\xa0\xe6\x95\x88\xef\xbc\x8c\xe5\x8f\xaf\xe5\x89\x8d\xe5\xbe\x80http://store.飞屎OSgeek.com\xe8\xb4\xad\xe4\xb9\xb0')
    os.system('python $飞屎OS/kernel/boot/active/buy.py')
    f = open('/data/data/com.termux/files/home/.飞屎OS/active/key.fk', 'r')
    i = f.read().split('-')
print('\xe6\xad\xa3\xe5\x9c\xa8\xe5\x90\xaf\xe5\x8a\xa8')
os.system('bash $飞屎OS/munu.sh')
