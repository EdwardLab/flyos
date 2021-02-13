import os
print("Linux部署程序--中文版")
print("By:FlyOS MicroTech Rainbow(严禁删除版权，不允许修改版权)GPL-V3")
print("请选择系统(内置常用的几个系统):")
print("1.Ubuntu")
print("2.Debian")
print("3.轻量级kali")
print("4.Kali nethunter")
print("5.Fedora")
print("6.CentOS")
print("7.Arch Linux(安装完请手动运行:chmod 755 additional.sh && ./afdtitonal.sh(只需首次运行前输入))")
print("8.Alpine")
print("---------------------------------------")
print("如果嫌速度太慢，可以选择使用国光码云脚本，也可以梯子，输入00即可安装国光脚本")
print("安装完成后，请输入./start-系统名.sh启动。输入0退出")
num = input("请输入编码来安装系统:")
if num == '1':
   os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")
if num == '2':
   os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh && bash debian.sh")
if num == '3':
   os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh")
if num == '4':
   os.system("pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh && bash nethunter.sh")
if num == '5':
   os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh && bash fedora.sh")
if num == '6':
   os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh && bash centos.sh")
if num == '7':
   os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Arch/armhf/arch.sh && bash arch.sh")
if num == '8':
   os.system("pkg install wget openssl-tool proot tar -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Alpine/alpine.sh && bash alpine.sh")
if num == '00':
   os.system("git clone https://github.com/sqlsec/termux-install-linux && cd termux-install-linux && python termux-linux-install.py")
if num == '66':
   os.system("wget https://gitee.com/mo2/linux/raw/2/2 && sh 2")
if num == '0':
   exit(())
else:
    print("输入错误，请检查！")