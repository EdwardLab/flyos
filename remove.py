#!/usr/bin/python python3
# coding=utf-8
'''
Author: whalefall
Date: 2021-08-12 12:42:55
LastEditTime: 2021-08-12 12:55:57
Description: 一键清除飞屎OS,还你一个纯洁的termux
'''
import os
from pathlib2 import Path


FLYOS_PATH = Path.cwd()
print(f"当前屎飞os路径:{FLYOS_PATH}")

# 伪代码
if input("确定删除屎飞os?(Y/n)") == "Y":
    print("明治维新！！")
else:
    print("狗屎吧你，马上删除")
    pass
try:
    Path.unlink(FLYOS_PATH)
except PermissionError:
    print("？？？")
