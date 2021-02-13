wget https://assets.huoyinetwork.cn/FlyOS/VM/sparc.7z
7z x sparc.7z
qemu-system-sparc -hda sparc.qcow2 -m 64 -M SS-5 -vnc :0
