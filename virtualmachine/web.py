"""
飞屎OS-bate Panel By:请遵守开源协议
Use Under License GPL - V3
"""
import os
import subprocess
import asyncio
import pywebio.input
from pywebio.output import popup, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env
import termux_auth
import re

print("___________________")
print("飞屎OS-bate Virtual Machine")
print("启动中")


class Main:
    """飞屎OS-bate WEB Panel main"""
    def __init__(self):
        env = os.getenv('飞屎OS-bate')
        if env is None:
            env = '.'
        self.__path = os.path.abspath(env + '/virtualmachine')
        if not os.path.exists(os.path.abspath(self.__path + "/vms")):
            os.mkdir(os.path.abspath(self.__path + "/vms"))
        set_env(title="飞屎OS-bate Virtual Machine", auto_scroll_bottom=True)
        put_html("<h1>飞屎OS-bate WEB Virtual Machine</h1>")
        put_text("飞屎OS-bate Virtual Machine By:请遵守开源协议", sep=" ")
        popup(
            "欢迎使用飞屎OS-bate 飞屎OS-bate Virtual Machine！",
            "欢迎使用飞屎OS-bate Virtual Machine。"
            "开始创建您的虚拟机吧！"
            "程序由MicroTech Projects -- 飞屎OS-bate强力驱动",
        )
        pwd = pywebio.input.input("输入飞屎OS-bate密码:")
        if termux_auth.auth(pwd):
            self.__run()
        else:
            popup("密码错误，请刷新页面重试")

    @staticmethod
    async def get_result(cmd):
        """
        params:
            cmd - 要执行的命令
        """
        if re.search('[;&|<>$]', cmd):
            popup('检测到非法字符', content="请检查命令中是否包含;&|等特殊字符, 并刷新重试")
            return
        popen = subprocess.Popen(cmd,
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 text=True)
        while True:
            buff = popen.stdout.readline()
            if buff:
                put_text(buff)
            elif popen.poll() is not None:
                break

    def __run(self):
        num = pywebio.input.select(options=[
            ("运行虚拟机", 1, True),
            ("运行模板", 2, False),
            ("创建虚拟机", 3, False),
        ])
        if num == 1:
            run_type = pywebio.input.radio(options=[("新建临时",
                                                     "1"), ("运行已保存的配置文件",
                                                            "2")])
            if run_type == "1":
                qemu = self.create()
                asyncio.run(self.get_result(qemu))
                popup(
                    "恭喜，虚拟机成功创建，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可"
                )
            elif run_type == "2":
                options = []
                dirs = os.listdir("{}/vms".format(self.__path))
                for path in dirs:
                    options.append((path[:5], path[:5]))
                conf = pywebio.input.select("选择创建的虚拟机名称", options=options)
                os.environ["conf"] = str(conf)
                run = "bash {}/vms/$conf.conf".format(self.__path)
                asyncio.run(self.get_result(run))
                popup(
                    "恭喜，虚拟机成功运行，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可"
                )
        elif num == 2:
            print(
                "模板VNC端口都为:5900，没有图形将从串口输出，内存分配视Guest机系统而定，请确保有500MB左右的剩余储存空间")
            template_num = pywebio.input.select(options=[
                ("Windows", "1", True),
                ("SunOS", "2", False),
                ("HelenOS", "3", False),
            ])

            if template_num == "1":
                template_type = pywebio.input.radio(
                    options=[("Windows95", "1"), ("WindowsXP", "2")])

                os.environ["w"] = str(template_type)
                sh_name = "Windows"
                asyncio.run(
                    self.get_result("sh {}/templates/".format(self.__path) +
                                    sh_name + ".sh"))
                # cd $飞屎OS-bate/virtualmachine && sh 2.sh
                popup(
                    "恭喜，模板成功运行，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可")
            elif template_num == "2":
                template_type = pywebio.input.radio(
                    options=[("SunOS4.13", "1"), ("SunOS4.14",
                                                  "2"), ("Solaris2.4", "3")])
                os.environ["sp"] = str(template_type)
                sh_name = "3"
                asyncio.run(self.get_result("sh templates/" + sh_name + ".sh"))
                popup(
                    "恭喜，模板成功运行，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可")

            elif template_num == "3":
                archi = pywebio.input.radio(options=[("i386", "1"), ("arm",
                                                                     "2")])
                sh_name = "4"
                os.environ["h"] = str(archi)
                asyncio.run(
                    self.get_result("sh {}/templates/".format(self.__path) +
                                    sh_name + ".sh"))
                popup(
                    "恭喜，模板成功运行，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可")

        elif num == 3:
            qemu = self.create()
            name = pywebio.input.input("虚拟机名称:")
            os.environ["qemu"] = str(qemu)
            os.environ["vm"] = str(name)
            save = "echo $qemu; echo $vm; echo $qemu > %s/vms/${vm}.conf " % self.__path
            asyncio.run(self.get_result(save))
            popup("恭喜，虚拟机成功保存，请在网上或应用市场下载vncviewer，打开+点击右下角，名称随便取，点击列表名称连接即可")

    @staticmethod
    def __get_cdrom():
        cdrom_num = pywebio.input.input("请输入虚拟光盘的个数",
                                        type=pywebio.input.NUMBER,
                                        value=1)
        cdroms = ""
        for i in range(cdrom_num):
            cdrom_info = dict(
                pywebio.input.input_group("光盘{}信息".format(i + 1), [
                    pywebio.input.input("虚拟机光盘镜像的绝对路径", name="cdrom_path"),
                ]))
            try:
                if not cdrom_info["cdrom_path"]:
                    popup("光盘路径为空！")
                else:
                    cdroms += " -cdrom {} ".format(
                        os.path.abspath(cdrom_info["disk_path"]))
            except KeyError:
                popup("输入出错！")
        return cdroms

    @staticmethod
    def __get_disk():
        disk_num = pywebio.input.input("请输入虚拟磁盘的个数",
                                       type=pywebio.input.NUMBER,
                                       value=1)
        disks = ""
        for i in range(disk_num):
            disk_info = dict(
                pywebio.input.input_group(
                    "虚拟磁盘{}信息".format(i + 1),
                    [
                        pywebio.input.input("虚拟机磁盘镜像的绝对路径", name="disk_path"),
                        pywebio.input.select(
                            "虚拟磁盘镜像格式",
                            [
                                ("RAW(IMG, ISO)", "raw"),
                                ("QCOW", "qcow"),
                                ("VHD（Windows）", "vhd"),
                            ],
                            name="disk_format",
                        ),
                    ],
                ))
            try:
                if not disk_info["disk_path"]:
                    popup("磁盘路径为空！")
                else:
                    disks += " -drive file={},if=virtio,format={},id=drive-virtio-disk{} ".format(
                        os.path.abspath(disk_info["disk_path"]),
                        disk_info["disk_format"],
                        i,
                    )
            except KeyError:
                popup("输入出错！")
        return disks

    def create(self):
        """
        创建虚拟机函数，返回虚拟机运行命令
        """
        command = pywebio.input.select(
            label="请选择qemu的命令",
            options=[
                ("qemu-system-i386 （x86）", "qemu-system-i386 "),
                ("qemu-system-x86_64 （amd64）", "qemu-system-x86_64 "),
                ("qemu-system-arm （arm32）", "qemu-system-arm"),
                ("qemu-system-aarch64 （arm64）", "qemu-system-aarch64 "),
            ],
        )
        cdrom = self.__get_cdrom()
        disk = self.__get_disk()

        memory = pywebio.input.input(
            "请输入虚拟机内存(不建议太大),Windows 95/98建议512以下，NT/XP建议768，Windows7/8建议1G左右 :"
        )
        network = pywebio.input.input("请输入网卡型号(建议rtl8139):")
        vnc = pywebio.input.input("输入VNC端口号(建议0):")
        vga = pywebio.input.input("显卡型号，NT系建议vmware，Windowz95/98建议cirrus:")
        extra = pywebio.input.input("额外参数，没有留空:")
        # 判断是否有额外参数，否则添加
        if not extra:
            extra = ""
        else:
            extra = " " + extra

        # 判断是否有网卡，否则提供默认
        if not network:
            network = "rtl8139"

        # 判断是否自定义内存大小，否则使用默认128
        if not memory:
            memory = "128"

        # 判断是否有显卡类型，否则使用默认的vmware
        if not vga:
            vga = "vmware"

        # 判断是否有自定义vnc端口，否则使用默认的0
        if not vnc:
            vnc = "0"

        memory = " -m " + memory
        network = " -net user -net nic,model=" + network
        vga = " -vga " + vga
        vnc = " -vnc :" + vnc
        result = (command + cdrom + disk + memory + network + vga + vnc +
                  extra)
        popup("确认配置: " "要执行的命令" f"{result}")
        print(result)

        return result


# Server Port 关于服务器的配置信息
if __name__ == "__main__":
    start_server(Main, debug=True, host="0.0.0.0", port=8002)
    pywebio.session.hold()
