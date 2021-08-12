if [ ! -d "helen" ]; then
	mkdir helen
fi
cd helen
if [ $h -eq 1 ];then
if [ ! -f "helen.7z" ]; then
	wget http://d.ixcmstudio.cn:21188/doc/FlyOS/VM/helenos.7z
fi
7z x  -aos helenos.7z
echo "镜像来自镜连"
echo "虚拟机启动"
qemu-system-i386 -hda arm.qcow2 -m 256 -vnc :0
if [ $? -ne 0 ]; then
	echo “错误请检查”
fi
else
if [ ! -f "arm32.boot" ]; then
	wget http://d.ixcmstudio.cn:21188/doc/FlyOS/VM/arm32Helen.boot
fi
echo "虚拟机启动"
qemu-system-arm -M integratorcp -kernel arm32Helen.boot -vnc :0 
if [ $? -ne 0 ]; then
	echo “启动失败，检查报错”
fi
fi