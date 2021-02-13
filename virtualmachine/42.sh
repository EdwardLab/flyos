wget https://assets.huoyinetwork.cn/Flyos/VM/helenos.7z
7z x helenos.7z
qemu-system-i386 -hda helen.img -m 256 -vnc :0
