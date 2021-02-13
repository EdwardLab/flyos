import os
import time
print("FlyOS虚拟机面板")
print("__________________")
print("欢迎使用FlyOS虚拟机")
print("功能:")
print("1.创建虚拟机")
print("2.运行模板")
print("回车退出")
print("其他功能施工中...")
num = input("请选择功能|输入编号:")
if num == '1':
  print("开始创建虚拟机")
  name = input("请输入虚拟机的名称:")
  cpu = input("请输入架构，例如i386架构:")
  path = input("请输入虚拟机磁盘镜像完整绝对路径:")
  memory = input("请输入虚拟机内存(不建议太大):")
  network = input("请输入网卡驱动(建议rtl8139):")
  vga = input("请输入显卡驱动(建议vmware):")
  vnc = input("输入VNC端口号(建议0):")
  print("确认配置: 架构:" + cpu + "路径:" + path + "内存:" + memory + "网络:" + network + "显卡:" + vga + "VNC端口号:" + vnc)
  input("回车开始启动")
  qemu = "qemu-system-" + cpu + " -hda " + path + " -m " + memory + " -device " + network + " -vga " + vga + " -vnc :" + vnc
  os.system(qemu)
if num == '2':
    print("模板VNC端口都为:0，没有图形将从串口输出，内存分配视Guest机系统而定，请确保有500MB左右的剩余储存空间")
    se = input("1.Windows 2.SunOS 3.HelenOS 4.退出")
    vm = "cd ~/../usr/etc/flyos/virtualmachine;"
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
