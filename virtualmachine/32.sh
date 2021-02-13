wget https://assets.huoyinetwork.cn/Flyos/VM/sunos4.14.7z
7z x sunos4.14.7z
qemu-system-sparc -hda sparc.qcow2 -m 64 -M SS-5 -vnc :0
