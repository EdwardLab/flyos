
nohup bash $FLYOS/.services.sh & 
#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=25)); do
        sleep 0.3
        echo $i
    done
} | whiptail --gauge "FlyOS正在启动" 6 60 0
python $FLYOS/console.py