#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-10 19:11:49
LastEditTime: 2021-08-10 21:05:15
Description: 狗屎4
'''
import os
try:
<<<<<<< HEAD
    f = open("/data/data/com.termux/files/home/.飞屎OS-bate/admin.飞屎OS-bate")
=======
    f = open("/data/data/com.termux/files/home/.flyos/admin.flyos")
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
    f.close()
except FileNotFoundError:
    input("ERROR!RBOOT is not authorized, please authorize and try again")
    #pkill termux
    os.system("pkill bash")
    os.system("pkill sh")
    os.system("pkill zsh")
<<<<<<< HEAD
os.system("bash $飞屎OS-bate/kernel/rboot/rbootservices.sh")
=======
os.system("bash $FLYOS/kernel/rboot/rbootservices.sh")
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
# 拉的什么狗屎
# for i in range(99):
#    print("")
print()
<<<<<<< HEAD
print("飞屎OS-bate RBOOT MODE")
=======
print("FlyOS RBOOT MODE")
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
print("webshell:HTTP:7681--SSH:8022")
input("Enter to exit!!")
print("exit!!")