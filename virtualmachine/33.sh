wget https://assets.huoyinetwork.cn/Flyos/VM/solaris2.4.7z
7z x solaris2.4.7z
qemu-system-i386 -hda sol.vmdk -m 256 -vnc :0
