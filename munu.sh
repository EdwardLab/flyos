
<<<<<<< HEAD
nohup bash $飞屎OS-bate/killmunu.sh 2>&1 & 
OPTION=$(whiptail --title "GNU 飞屎OS-bate Boot" --menu "选择要启动的系统 4秒后自动启动飞屎OS-bate系统!" 15 60 4  "1" "飞屎OS-bate"  "2" "终端"  "3" "不启动服务的飞屎OS-bate启动(安全模式)"  "4" "关机(退出)"  3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    bash $飞屎OS-bate/$OPTION.sh
else
    bash $飞屎OS-bate/booting.sh
=======
nohup bash $FLYOS/killmunu.sh 2>&1 & 
OPTION=$(whiptail --title "GNU FlyOS Boot" --menu "选择要启动的系统 4秒后自动启动FlyOS系统!" 15 60 4  "1" "FlyOS"  "2" "终端"  "3" "不启动服务的FlyOS启动(安全模式)"  "4" "关机(退出)"  3>&1 1>&2 2>&3)

exitstatus=$?
if [ $exitstatus = 0 ]; then
    bash $FLYOS/$OPTION.sh
else
    bash $FLYOS/booting.sh
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
fi
