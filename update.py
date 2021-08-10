import os
#快速更新补全依赖


try:
    f = open("/data/data/com.termux/files/home/.飞屎OS/active/key.fk")
    f.close()
except FileNotFoundError:
    os.system("mkdir -p /data/data/com.termux/files/home/.飞屎OS/active/ && cd /data/data/com.termux/files/home/.飞屎OS/active/ && touch key.fk && chmod 777 /data/data/com.termux/files/home/.飞屎OS/active/key.fk")
    print("Finished")