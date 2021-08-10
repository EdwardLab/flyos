from django.shortcuts import render
import os 
import socket
import urllib.request
def panel(request):
    context          = {}
    import os
    disk = os.popen("df -h /storage/emulated").read()
    linux = os.popen("uname -a").read()
    username = os.popen("whoami").read()
    screenfetch = os.popen("screenfetch").read()
    #ip获取
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip=s.getsockname()[0]
    #公告获取
    RES = urllib.request.urlopen("http://飞屎OSgeek.com/notices.txt")
    print("\n公告:")
    notice = RES.read().decode('utf-8')
    RES.close()
    return render(request, 'index.html', {"disk":disk,"linux":linux,"username":username,"screenfetch":screenfetch,"ip":ip,"notice":notice})
    

   