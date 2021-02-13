import os
#try:
#    f =open('/sdcard/.FlyOS/Keys/fpro.fk')
#    f.close()
#except FileNotFoundError:
#    os.system("python3 $FLYOS/.firstuse/firstrun.py")

try:
    f =open('/data/data/com.termux/files/usr/etc/flyos/.firstuse/lock')
    f.close()
except FileNotFoundError:
    os.system("python3 $FLYOS/.firstuse/register.py")

p = open('/data/data/com.termux/files/usr/etc/flyos/database/password.db','r')
password = p.read()
inputpass = input("请输入开机密码:")
if inputpass == password:
  os.system("sh $FLYOS/start.sh")
else:
  os.system("python $FLYOS/logout.py")