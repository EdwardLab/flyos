from django.shortcuts import render
import os 

def panel(request):
    context          = {}
    import os
    disk = os.popen("df -h /storage/emulated").read()
    linux = os.popen("uname -a").read()
    username = os.popen("whoami").read()
    screenfetch = os.popen("screenfetch").read()
    return render(request, 'index.html', {"disk":disk,"linux":linux,"username":username,"screenfetch":screenfetch})
    

   