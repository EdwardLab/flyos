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
    f = open("/data/data/com.termux/files/home/.flyos/admin.flyos")
    f.close()
except FileNotFoundError:
    input("ERROR!RBOOT is not authorized, please authorize and try again")
    #pkill termux
    os.system("pkill bash")
    os.system("pkill sh")
    os.system("pkill zsh")
os.system("bash $FLYOS/kernel/rboot/rbootservices.sh")
# 拉的什么狗屎
# for i in range(99):
#    print("")
print()
print("FlyOS RBOOT MODE")
print("webshell:HTTP:7681--SSH:8022")
input("Enter to exit!!")
print("exit!!")