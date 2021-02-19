if [ $w -eq 1 ];then
if [ ! -d "95" ]; then
mkdir 95
fi
cd 95
if [ ! -f "win95.7z" ]; then
wget https://assets.huoyinetwork.cn/Flyos/VM/win95.7z
fi
7z x -aos win95.7z
echo "虚拟机启动，镜像来自镜连"
qemu-system-i386 -m 256 -hda win95.img -soundhw sb16 -vnc :0
else
	if [ ! -d "xp" ];then
		mkdir xp
	fi
	cd xp
	if [ ! -f "xp.zip" ];then
		wget https://assets.huoyinetwork.cn/Flyos/VM/xp.zip
	fi
	echo "镜像来自ixcm工作室的阳光XP第八版"
	unzip -n xp.zip
    echo "虚拟机启动"
	qemu-system-i386 -smp 2 -m 512 -net user -net nic,model=rtl8139 -hda 8.vmdk -vnc :0
fi
if [ $? -ne 0 ];then
	echo "错误请检查"
fi
