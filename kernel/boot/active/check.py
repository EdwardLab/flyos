#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 21:14:40
LastEditTime: 2021-08-10 21:17:01
Description: 
'''
import os
import requests
<<<<<<< HEAD
print('\xe6\xbf\x80\xe6\xb4\xbb飞屎OS-bate!')
i = input('\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xaf\x86\xe9\x92\xa5:')
i = i.split('-')
# 目前不能访问
URL = 'http://store.飞屎OS-bategeek.com/active/key.php?key=' + '-'.join(i)
=======
print('\xe6\xbf\x80\xe6\xb4\xbbFlyOS!')
i = input('\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xaf\x86\xe9\x92\xa5:')
i = i.split('-')
# 目前不能访问
URL = 'http://store.flyosgeek.com/active/key.php?key=' + '-'.join(i)
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
res = requests.get(URL)
# if res.text == 'n':
#     print('\xe5\xaf\x86\xe9\x92\xa5\xe4\xbd\x9c\xe5\xba\x9f(\xe5\xb7\xb2\xe8\xa2\xab\xe4\xbd\xbf\xe7\x94\xa8)\xe6\x88\x96\xe8\x80\x85\xe6\xa0\xbc\xe5\xbc\x8f\xe4\xb8\x8d\xe6\xad\xa3\xe7\xa1\xae\xef\xbc\x8c\xe8\xaf\xb7\xe6\xa3\x80\xe6\x9f\xa5!')
#     # continue #????
# if res.text == 'y':
#     pass

print('\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7\xe6\xad\xa3\xe7\xa1\xae\xef\xbc\x8c\xe5\x86\x99\xe5\x85\xa5\xe4\xb8\xad')
# 什么垃圾验证？？？？
<<<<<<< HEAD
f = open('/data/data/com.termux/files/home/.飞屎OS-bate/active/key.fk', 'w')
f.write('-'.join(i))
f.close()
os.system('bash $飞屎OS-bate/munu.sh')
=======
f = open('/data/data/com.termux/files/home/.flyos/active/key.fk', 'w')
f.write('-'.join(i))
f.close()
os.system('bash $FLYOS/munu.sh')
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)

