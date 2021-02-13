wget https://assets.huoyinetwork.cn/Flyos/VM/arm32Helen.boot
echo "虚拟机启动"
qemu-system-arm -M integratorcp -kernel arm32Helen.boot -vnc :0
