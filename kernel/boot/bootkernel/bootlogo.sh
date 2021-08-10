
clear
termimage $飞屎OS/kernel/boot/bootkernel/logo.png 
sleep 2
echo 加载飞屎OS内核配置与系统检查
##RecoveryMode请去掉注释，下次将会启动到Recovery

bash $飞屎OS/kernel/boot/kernelconfig/kernelconf.sh
