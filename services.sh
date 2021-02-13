echo [*]Starting FlyOS Services
shellinaboxd --disable-ssl --background
nohup python $FLYOS/panel/server.py &
nohup python $FLYOS/panel/shell.py &
apachectl start
nohup python $FLYOS/virtualmachine/web.py &
nohup nginx &
nohup php-fpm &
nohup http-server &
nohup python $FLYOS/phone/web.py &
nohup python $FLYOS/api/web.py &
sshd
echo [*]Done!