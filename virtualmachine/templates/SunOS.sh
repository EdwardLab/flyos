if [ ! -d "sunos" ];then
	mkdir sunos
fi
cd sunos
if [ $sp -eq 1 ]; then
if [ ! -f "sparc.7z" ]; then 
	wget http://d.ixcmstudio.cn:21188/doc/飞屎OS-bate/VM/sparc.7z
fi
	7z x -aos sparc.7z
	qemu-system-sparc -hda sparc.qcow2 -m 64 -M SS-5 -vnc :0 
elif [ $sp -eq 2 ];then
	if [ ! -f "sunos4.14.7z" ]; then
	wget http://d.ixcmstudio.cn:21188/doc/飞屎OS-bate/VM/sunos4.14.7z
	fi
	7z x -aos sunos4.14.7z
	qemu-system-sparc -m 64 -M SS-5 -vnc :0 -hda sol.qcow2 
else
	if [ ! -f "solaris2.4.7z"];then
	wget http://d.ixcmstudio.cn:21188/doc/飞屎OS-bate/VM/solaris2.4.7z
	fi
	7z x -aos solaris2.4.7z
    echo "虚拟机启动"
	qemu-system-i386 -hda sol.vmdk -vnc :0 -m 256
fi
if [ $? -ne 0 ]
	echo "错误请检查"
fi