
nohup bash $飞屎OS/.services.sh & 
#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=25)); do
        sleep 0.3
        echo $i
    done
} | whiptail --gauge "飞屎OS正在启动" 6 60 0
bash $飞屎OS/services.sh