import os
import time
os.system("clear")
print("")
while 1:
num = input("")
if num == '1':
    os.system("curl http://flyosgeek.com/gosetup.sh | bash")
if num == '2':
    os.system("bash")
elif num == '3':
    os.system("python $FLYOS/kernel/rboot/rboot.py")
elif num == '4':
    os.system("python $FLYOS/kernel/recovery/rec.py")
elif num == '5':
    os.system("cd $FLYOS && git pull")
elif num == '6':
    os.system("termux-reset")
elif num == '7':
    os.system("python $FLYOS/kernel/boot/active/active.py")
else:
    print("")
