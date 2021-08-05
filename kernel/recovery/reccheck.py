import os
try:
    f = open("/data/data/com.termux/files/home/.flyos/admin.flyos")
    f.close()
except FileNotFoundError:
    input("ERROR!RBOOT is not authorized, please authorize and try again")
    #pkill termux
    os.system("pkill bash")
    os.system("pkill sh")
    os.system("pkill zsh")