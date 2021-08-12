nohup ttyd pwlogin > /dev/null 2>&1 & 
<<<<<<< HEAD
nohup python /data/data/com.termux/files/usr/etc/飞屎OS-bate/panel/server.py > /dev/null 2>&1 &   
nohup apachectl start > /dev/null 2>&1 &      
nohup python /data/data/com.termux/files/usr/etc/飞屎OS-bate/virtualmachine/web.py > /dev/null 2>&1 &
nohup nginx > /dev/null 2>&1 &
nohup php-fpm > /dev/null 2>&1 &
nohup /data/data/com.termux/files/usr/bin/http-server > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/飞屎OS-bate/phone/web.py > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/飞屎OS-bate/api/web.py > /dev/null 2>&1 &
=======
nohup python /data/data/com.termux/files/usr/etc/flyos/panel/server.py > /dev/null 2>&1 &   
nohup apachectl start > /dev/null 2>&1 &      
nohup python /data/data/com.termux/files/usr/etc/flyos/virtualmachine/web.py > /dev/null 2>&1 &
nohup nginx > /dev/null 2>&1 &
nohup php-fpm > /dev/null 2>&1 &
nohup /data/data/com.termux/files/usr/bin/http-server > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/flyos/phone/web.py > /dev/null 2>&1 &
nohup python /data/data/com.termux/files/usr/etc/flyos/api/web.py > /dev/null 2>&1 &
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
nohup sshd > /dev/null 2>&1 &
nohup code-server --bind-addr 0.0.0.0:2001 > /dev/null 2>&1 &
nohup jupyter notebook --ip='0.0.0.0' --port=2000 --NotebookApp.token='' --no-browser > /dev/null 2>&1 &
nohup termux-wake-lock > /dev/null 2>&1 &
<<<<<<< HEAD
#nohup python $飞屎OS-bate/deploylinux/web.py > /dev/null 2>&1 &
nohup python $飞屎OS-bate/panel/飞屎OS-batePanel/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
nohup 飞屎OS-batevnc > /dev/null 2>&1 &
nohup $飞屎OS-bate/webvnc/utils/novnc_proxy --listen 6081 --vnc localhost:5902 > /dev/null 2>&1 &
#下面是飞屎OS-bate Console启动
bash $飞屎OS-bate/chooseconsole.sh
=======
#nohup python $FLYOS/deploylinux/web.py > /dev/null 2>&1 &
nohup python $FLYOS/panel/FlyOSPanel/manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &
nohup flyosvnc > /dev/null 2>&1 &
nohup $FLYOS/webvnc/utils/novnc_proxy --listen 6081 --vnc localhost:5902 > /dev/null 2>&1 &
#下面是FlyOS Console启动
bash $FLYOS/chooseconsole.sh
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
