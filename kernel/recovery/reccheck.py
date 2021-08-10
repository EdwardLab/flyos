import os
try:
    f = open("/data/data/com.termux/files/home/.飞屎OS-bate/admin.飞屎OS-bate")
    f.close()
except FileNotFoundError:
    input("ERROR!RBOOT is not authorized, please authorize and try again")
    #pkill termux
    os.system("pkill bash")
    os.system("pkill sh")
    os.system("pkill zsh")