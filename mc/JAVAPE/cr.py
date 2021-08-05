import os
import subprocess
results = v_return_status=os.system("java -version")
results = "results=%.1d" % results
if not results == 1 :
    print("检测到您未安装JAVA，正在为您安装")
    os.system("apt install openjdk-17")
else:
    print("正在为您启动Nukkit服务器...")
    print("查看可用版本使用/version")
    os.system("java -Xms1G -Xmx1G -jar nukkit-1.0-SNAPSHOT.jar")
