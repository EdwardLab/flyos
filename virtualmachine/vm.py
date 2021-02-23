import os
import time
print("FlyOS虚拟机面板")
print("__________________")
print("欢迎使用FlyOS虚拟机")
print("功能:")
print("1.运行虚拟机")
print("2.运行模板")
print("3.创建虚拟机")
print("回车退出")
print("其他功能施工中...")
num = input("请选择功能|输入编号:")
def create():
        print("开始创建虚拟机")
        cpu = input("请输入架构，例如i386架构:")
        cdrom = input("安装光盘路径，没有回车:")
        fd = input("安装软盘路径，没有留空:")
        path = input("请输入虚拟机磁盘镜像1完整绝对路径:")
        pp =  input("请输入磁盘二绝对路径，没有回车:")
        ppp = input("请输入磁盘三绝对路径，没有回车:")

        memory = input("请输入虚拟机内存(不建议太大),Windows 95/98建议512以下，NT/XP建议768，Windows7/8建议1G左右 :")
        network = input("请输入网卡型号(建议rtl8139):")
        vnc = input("输入VNC端口号(建议0):")
        vga = input("显卡型号，NT系建议vmware，Windowz95/98建议cirrus:")
        extra = input("额外参数，没有留空:")
        print("确认配置: 架构:" + cpu + "路径:" + path + ";" + pp + ";" + ppp + "内存:" + memory + "网络:" + network + "显卡:" + vga + "VNC端口号:" + vnc + "额外参数" + extra)
        if not fd:
            fd = ""
        else:
            fd = " -fda " + fd
        if not cdrom:
            cdrom = ""
        else:
            cdrom = " -cdrom " + cdrom
        if not pp:
            pp = ""
        else:
            pp = " -hdb " + pp
        if not ppp:
            ppp = ""
        else:
            ppp = " -hdc " + ppp
        if not extra:
            extra = ""
        else:
            extra = " " + extra
        if not path :
            print("正准备启动测试用镜像")
            path = ""
            fd = " -fda test.img"
        else:
            path = " -hda "+ path
        if not cpu:
            cpu = "i386"
        if not network:
            network = "rtl8139"
        if not memory:
            memory = "128"
        if not vga:
            vga = "vmware"
        if not vnc:
            vnc = "0"
        cpu = "qemu-system-" + cpu
        memory = " -m " + memory
        network = " -net user -net nic,model=" + network
        vga = " -vga " + vga
        vnc = " -vnc :" + vnc
        q = cpu +  fd  + cdrom + path +pp + ppp + memory + network + vga + vnc + extra
        return q
if num == '1' :
    nw = input("1.新建临时 2.运行已保存的配置文件")
    if nw == '1' :
        qemu = create()
        input("回车开始启动")
        os.system(qemu)
    elif nw == '2' :
        conf = input("您创建的虚拟机的名称:")
        os.environ['conf']=str(conf)
        sh = "bash $conf.conf"
        os.system(sh)
if num == '2':
    vm = "cd /data/data/com.termux/files/us    r/etc/flyos/virtualmachine "
    print("模板VNC端口都为:5900，没有图形将从串口输出，内存分配视Guest机系统而定，请确保有500MB左右的剩余储存空间")
    se = input("1.Windows 2.SunOS 3.HelenOS 4.退出")
    if se == '1':
        w = input("1.Windows95 2.WindowsXP")
        os.environ['w']=str(w)
        n = "2"
        os.system(vm + 'sh ' +n + '.sh' )
    elif se == '2':
        sp = input("1.SunOS4.13 2. SunOS4.14 3.Solaris2.4")
        os.environ['sp']=str(sp)
        n = "3"
        os.system(vm + 'sh ' + n + '.sh')
    elif se == '3' :
        archi = input("1.i386 2.arm")
        n = '4'
        os.environ['h']=str(archi)
        os.system(vm + 'sh ' + n + '.sh')
    elif se == '4' :
        exit()
elif num == '3' :
    qemu = create()
    name = input("虚拟机名称:")
    os.environ['qemu']=str(qemu)
    os.environ['vm']=str(name)
    save = "echo $qemu;echo $vm ;echo $qemu > ${vm}.conf "
    os.system(save)
    print("保存完成")
