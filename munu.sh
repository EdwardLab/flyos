
nohup bash $FLYOS/killmunu.sh 2>&1 & 
OPTION=$(whiptail --title "GNU FlyOS Boot" --menu "选择要启动的系统 4秒后自动启动FlyOS系统!" 15 60 4  "1" "FlyOS"  "2" "终端"  "3" "不启动服务的FlyOS启动(安全模式)"  "4" "关机(退出)"  3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    bash $FLYOS/$OPTION.sh
else
    bash $FLYOS/booting.sh
fi
