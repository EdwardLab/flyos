
nohup bash $飞屎OS/killmunu.sh 2>&1 & 
OPTION=$(whiptail --title "GNU 飞屎OS Boot" --menu "选择要启动的系统 4秒后自动启动飞屎OS系统!" 15 60 4  "1" "飞屎OS"  "2" "终端"  "3" "不启动服务的飞屎OS启动(安全模式)"  "4" "关机(退出)"  3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    bash $飞屎OS/$OPTION.sh
else
    bash $飞屎OS/booting.sh
fi
