import os
from hashlib import md5
#try:
#    f =open('/sdcard/.FlyOS/Keys/fpro.fk')
#    f.close()
#except FileNotFoundError:
#    os.system("python3 $FLYOS/.firstuse/firstrun.py")

if os.path.exists('/data/data/com.termux/files/usr/etc/flyos/.firstuse/lock') == False:
    os.system("python3 $FLYOS/.firstuse/register.py")

p = open('/data/data/com.termux/files/usr/etc/flyos/database/password.db','r')
password = p.read()
inputpass = input("请输入开机密码:")
inputpass = str(inputpass)
md5_obj = md5()
md5_obj.update(inputpass.encode())
inputpass = md5_obj.hexdigest()
print(inputpass)
print(inputpass)
if inputpass == password:
  os.system("sh $FLYOS/start.sh")
else:
  os.system("python $FLYOS/logout.py")
