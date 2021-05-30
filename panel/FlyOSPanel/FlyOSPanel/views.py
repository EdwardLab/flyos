from django.shortcuts import render
import os 
def uname(request):
    disk = os.popen("df -h").read()
    return render(disk, 'index.html', {"disk": disk})
def panel(request):
    context          = {}
    import os
    linux = os.popen("uname").read()
    return render(request, 'index.html', {"linux": linux})
    

   