import os
os.system("bash $FLYOS/kernel/reboot/rbootservices.sh")
for i in range(99):
   print("")
print("FlyOS RBOOT MODE")
print("webshell:HTTP:7681--SSH:8022")
input("Enter to exit!!")
print("exit!!")