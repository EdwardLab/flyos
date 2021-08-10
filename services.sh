nohup ttyd pwlogin > /dev/null 2>&1 & 
nohup python /data/data/com.termux/files/usr/etc/飞屎OS/panel/server.py > /dev/null 2>&1 &   
nohup apachectl start > /dev/null 2>&1 &      
nohup python /data/data/com.termux/files/usr/etc/飞屎OS/virtualmachine/web.py > /dev/null 2>&1 &
nohup nginx > /dev/null 2>&1 &
nohup php-fpm > /dev/null 2>&1 &
nohup /data/data/com.termux/files/usr/bin/http-server > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/飞屎OS/phone/web.py > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/飞屎OS/api/web.py > /dev/null 2>&1 &
nohup sshd > /dev/null 2>&1 &
nohup code-server --bind-addr 0.0.0.0:2001 > /dev/null 2>&1 &
nohup jupyter notebook --ip='0.0.0.0' --port=2000 --NotebookApp.token='' --no-browser > /dev/null 2>&1 &
nohup termux-wake-lock > /dev/null 2>&1 &
#nohup python $飞屎OS/deploylinux/web.py > /dev/null 2>&1 &
nohup python $飞屎OS/panel/飞屎OSPanel/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
nohup 飞屎OSvnc > /dev/null 2>&1 &
nohup $飞屎OS/webvnc/utils/novnc_proxy --listen 6081 --vnc localhost:5902 > /dev/null 2>&1 &
#下面是飞屎OS Console启动
bash $飞屎OS/chooseconsole.sh