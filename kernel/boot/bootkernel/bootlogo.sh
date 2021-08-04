
clear
termimage $FLYOS/kernel/boot/bootkernel/logo.png 
sleep 2
echo 加载FlyOS内核配置与系统检查
##RecoveryMode请去掉注释，下次将会启动到Recovery

bash $FLYOS/kernel/boot/kernelconfig/kernelconf.sh
