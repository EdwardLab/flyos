<<<<<<< HEAD
#nohup bash $飞屎OS-bate/killconsolechoose.sh 2>&1 &
if (whiptail --title "选择启动面板" --yes-button "标准的Console" --no-button "直观的Console"  --yesno "飞屎OS-bate自带两个面板，标准面板功能丰富，适合经常使用Linux的人使用，他更加方便，但不是很美观。直观的Console功能没标准丰富，对于经常使用Windows的人非常友好，但是不是很方便，直观的Console更加漂亮，并且支持触屏。请根据自己的情况选择面板，建议都尝试一下! " 10 60) then
    clear
    python $飞屎OS-bate/console.py
else
    bash $飞屎OS-bate/console.sh
=======
#nohup bash $FLYOS/killconsolechoose.sh 2>&1 &
if (whiptail --title "选择启动面板" --yes-button "标准的Console" --no-button "直观的Console"  --yesno "FlyOS自带两个面板，标准面板功能丰富，适合经常使用Linux的人使用，他更加方便，但不是很美观。直观的Console功能没标准丰富，对于经常使用Windows的人非常友好，但是不是很方便，直观的Console更加漂亮，并且支持触屏。请根据自己的情况选择面板，建议都尝试一下! " 10 60) then
    clear
    python $FLYOS/console.py
else
    bash $FLYOS/console.sh
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
fi