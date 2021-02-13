
#if (whiptail --title "FlyOS FBoot" --yes-button "FlyOS Console" --no-button "终端"  --yesno "快速启动，选择要启动的选项(终端不启动FlyOS服务)" 10 60) then
    python3 $FLYOS/console.py
#else
#    echo "进入终端..."
#fi
