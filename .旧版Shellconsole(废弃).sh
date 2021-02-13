#!/bin/bash
OPTION=$(whiptail --title "FlyOS Manager (Termux)" --menu "FlyOS管理器-中文版 By:MicroTech Software Group -----请选择您的选项(手机支持触屏选择)" 15 60 5 \
"1" "安装GNU/发行版Linux" \
"2" "Linux菜单高级部署菜单(推荐)" \
"3" "软件安装器" \
"4" "打开最近使用的Linux" \
"5" "FlyOS Chat 飞聊" 4>&1 1>&2 2>&3 3>&4)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    sh /data/data/com.termux/files/home/flyosbin/$OPTION.sh
else
    echo "您已取消"
fi