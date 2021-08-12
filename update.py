import os
#快速更新补全依赖


try:
<<<<<<< HEAD
    f = open("/data/data/com.termux/files/home/.飞屎OS-bate/active/key.fk")
    f.close()
except FileNotFoundError:
    os.system("mkdir -p /data/data/com.termux/files/home/.飞屎OS-bate/active/ && cd /data/data/com.termux/files/home/.飞屎OS-bate/active/ && touch key.fk && chmod 777 /data/data/com.termux/files/home/.飞屎OS-bate/active/key.fk")
=======
    f = open("/data/data/com.termux/files/home/.flyos/active/key.fk")
    f.close()
except FileNotFoundError:
    os.system("mkdir -p /data/data/com.termux/files/home/.flyos/active/ && cd /data/data/com.termux/files/home/.flyos/active/ && touch key.fk && chmod 777 /data/data/com.termux/files/home/.flyos/active/key.fk")
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
    print("Finished")