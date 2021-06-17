nohup ttyd pwlogin & 
nohup python /data/data/com.termux/files/usr/etc/flyos/panel/server.py &   
nohup apachectl start &      
nohup python /data/data/com.termux/files/usr/etc/flyos/virtualmachine/web.py &
nohup nginx &
nohup php-fpm &
nohup http-server &
nohup python /data/data/com.termux/files/usr/etc/flyos/phone/web.py &
nohup python /data/data/com.termux/files/usr/etc/flyos/api/web.py &
nohup sshd &
nohup jupyter notebook --ip='0.0.0.0' --port=2000 --NotebookApp.token='' --no-browser &
nohup termux-wake-lock &
nohup code-server --bind-addr 0.0.0.0:2001 &
nohup python $FLYOS/deploylinux/web.py &
nohup python $FLYOS/panel/FlyOSPanel/manage.py runserver 0.0.0.0:8000 &
nohup flyosvnc &
#下面是FlyOS Console启动
python $FLYOS/console.py
