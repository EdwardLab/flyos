nohup ttyd pwlogin > /dev/null 2>&1 & 
nohup python /data/data/com.termux/files/usr/etc/flyos/panel/server.py > /dev/null 2>&1 &   
nohup apachectl start > /dev/null 2>&1 &      
nohup python /data/data/com.termux/files/usr/etc/flyos/virtualmachine/web.py > /dev/null 2>&1 &
nohup nginx > /dev/null 2>&1 &
nohup php-fpm > /dev/null 2>&1 &
nohup /data/data/com.termux/files/usr/bin/http-server > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/flyos/phone/web.py > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/flyos/api/web.py > /dev/null 2>&1 &
nohup sshd > /dev/null 2>&1 &
nohup code-server --bind-addr 0.0.0.0:2001 > /dev/null 2>&1 &
nohup jupyter notebook --ip='0.0.0.0' --port=2000 --NotebookApp.token='' --no-browser > /dev/null 2>&1 &
nohup termux-wake-lock > /dev/null 2>&1 &
#nohup python $FLYOS/deploylinux/web.py > /dev/null 2>&1 &
nohup python $FLYOS/panel/FlyOSPanel/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
nohup flyosvnc > /dev/null 2>&1 &
nohup $FLYOS/webvnc/utils/novnc_proxy --listen 6081 --vnc localhost:5902 > /dev/null 2>&1 &
#下面是FlyOS Console启动
bash $FLYOS/chooseconsole.sh