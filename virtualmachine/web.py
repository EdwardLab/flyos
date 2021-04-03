# FlyOS Panel By:XingYuJie
# Use Under License GPL - V3
import os

import pywebio.input
from pywebio.output import popup, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env

print("___________________")
print("FlyOS Virtual Machine")
print("启动中")


# FlyOS WEB Panel main
def main():
    set_env(title="FlyOS Virtual Machine", auto_scroll_bottom=True)
    put_html("<h1>FlyOS WEB Virtual Machine</h1>")
    put_text('FlyOS Virtual Machine By:XingYuJie', sep=' ')
    popup(
        '欢迎使用FlyOS FlyOS Virtual Machine！', '欢迎使用FlyOS Virtual Machine。'
        '开始创建您的虚拟机吧！'
        '程序由MicroTech Projects -- FlyOS强力驱动')
    num = pywebio.input.select(options=[
        ('运行虚拟机', 1, True),
        ('运行模板', 2, False),
        ('创建虚拟机', 3, False),
    ])

    def create():
        cpu = pywebio.input.select(options=[
            ('Intel 32', 'i386'),
            ('AMD 64', 'x86_64'),
            ('ARM 32', 'arm'),
            ('ARM 64', 'aarch64')
        ])
        cdrom = pywebio.input.input("安装光盘路径，没有留空:")
        fd = pywebio.input.input("安装软盘路径，没有留空:")
        path = pywebio.input.input("请输入虚拟机磁盘镜像1完整绝对路径:")
        pp = pywebio.input.input("请输入磁盘二绝对路径，没有留空:")
        ppp = pywebio.input.input("请输入磁盘三绝对路径，没有留空:")
        memory = pywebio.input.input(
            "请输入虚拟机内存(不建议太大),Windows 95/98建议512以下，NT/XP建议768，Windows7/8建议1G左右 :"
        )
        network = pywebio.input.input("请输入网卡型号(建议rtl8139):")
        vnc = pywebio.input.input("输入VNC端口号(建议0):")
        vga = pywebio.input.input("显卡型号，NT系建议vmware，Windowz95/98建议cirrus:")
        extra = pywebio.input.input("额外参数，没有留空:")
        uefi = pywebio.input.radio(label='是否使用UEFI引导', options=[
                                   ('是', ' --boot uefi '), ('否', '')])
        popup("确认配置: "
              f"架构:{cpu}"
              f"路径:{path};{pp};{ppp}"
              f"内存:{memory}"
              f"网络:{network}"
              f"显卡型号:{vga}"
              f"VNC端口号:{vnc}"
              f"额外参数{extra}")
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
        if not path:
            popup("正准备启动测试用镜像")
            path = ""
            fd = " -fda test.img"
        else:
            path = " -hda " + path
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
        q = (cpu + uefi + fd + cdrom + path + pp +
             ppp + memory + network + vga + vnc + extra)
        return q

    if num == 1:
        nw = pywebio.input.radio(options=[("新建临时", '1'), ("运行已保存的配置文件", '2')])
        if nw == '1':
            qemu = create()
            os.system(qemu)
        elif nw == '2':
            conf = pywebio.input.input("您创建的虚拟机的名称:")
            os.environ['conf'] = str(conf)
            sh = "bash vms/$conf.conf"
            os.system(sh)
    elif num == 2:
        vm = "cd $FlyOS/virtualmachine "
        print("模板VNC端口都为:5900，没有图形将从串口输出，内存分配视Guest机系统而定，请确保有500MB左右的剩余储存空间")
        se = pywebio.input.select(
            options=[
                ('Windows', '1', True),
                ('SunOS', '2', False),
                ('HelenOS', '3', False),
            ]
        )
        if se == '1':
            w = pywebio.input.radio(
                options=[
                    ("Windows95", '1'),
                    ("WindowsXP", '2')
                ]
            )

            os.environ['w'] = str(w)
            n = "Windows"
            os.system(vm + '&& sh templates/' + n + '.sh')
            # cd $FLYOS/virtualmachine && sh 2.sh
        elif se == '2':
            sp = pywebio.input.radio(options=[("SunOS4.13", '1'),
                                              ("SunOS4.14", '2'),
                                              ('Solaris2.4', '3')])
            os.environ['sp'] = str(sp)
            n = "3"
            os.system(vm + '&& sh templates/' + n + '.sh')
        elif se == '3':
            archi = pywebio.input.input("1.i386 2.arm")
            n = '4'
            os.environ['h'] = str(archi)
            os.system(vm + '&& sh templates/' + n + '.sh')

    elif num == 3:
        qemu = create()
        name = pywebio.input.input("虚拟机名称:")
        os.environ['qemu'] = str(qemu)
        os.environ['vm'] = str(name)
        save = "echo $qemu;echo $vm ;echo $qemu > ${vm}.conf "
        os.system(save)
        popup("保存完成")


# Server Port 关于服务器的配置信息
if __name__ == '__main__':
    start_server(main, debug=True, host='0.0.0.0', port=8002)
    pywebio.session.hold()
