"""
FlyOS Panel By:XingYuJie
Use Under License GPL - V3
"""
import os
import subprocess
import asyncio
import pywebio.input
from pywebio.output import popup, put_text, put_html
from pywebio import start_server
from pywebio.session import set_env

print("Linux部署程序--中文版")
print("By:FlyOS MicroTech nullptr(严禁删除版权，不允许修改版权)GPL-V3")


class Main:
    """FlyOS WEB Panel main"""
    def __init__(self):
        env = os.getenv('FLYOS')
        if env is None:
            env = '.'
        self.__path = os.path.abspath(env + '/deploylinux')
        if not os.path.exists(os.path.abspath(self.__path + "/rootfs")):
            os.mkdir(os.path.abspath(self.__path + "/rootfs"))
        if not os.path.exists(os.path.abspath(self.__path + "/cmd")):
            os.mkdir(os.path.abspath(self.__path + "/cmd"))
        set_env(title="Linux部署程序--中文版", auto_scroll_bottom=True)
        put_html("<h1>FlyOS WEB Virtual Machine</h1>")
        put_text("By:FlyOS MicroTech nullptr(严禁删除版权，不允许修改版权)GPL-V3", sep=" ")
        popup(
            "欢迎使用Linux部署程序--中文版",
            "欢迎使用Linux部署程序--中文版。"
            "开始部署你的Linux吧！"
            "程序由MicroTech Projects -- FlyOS强力驱动",
        )
        self.__run()

    @staticmethod
    async def get_result(cmd):
        """
        params:
            cmd - 要执行的命令
        """
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
        num = pywebio.input.select('请选择你要安装的系统',
                                   options=[
                                       ("Ubuntu", 1, True),
                                       ("CentOS", 2),
                                       ("Arch", 3),
                                   ])
        if num == 1:
            asyncio.run(self.get_ubuntu())
        elif num == 2:
            asyncio.run(self.get_centos())

        elif num == 3:
            self.get_arch()

    async def get_ubuntu(self):
        """获取ubuntu rootfs并写入运行文件"""
        name = pywebio.input.input('请输入该系统的名字')
        command = pywebio.input.radio('请选择要用的命令',
                                      [('proot(无root下使用)', 'proot ', True),
                                       ('chroot(有root建议使用)', 'chroot ')])
        version = pywebio.input.select('请选择版本号',
                                       options=[
                                           ("20.04", "20.04.2", True),
                                           ("20.10", "20.10"),
                                           ("21.04", "21.04"),
                                       ])
        arch = subprocess.getoutput(['dpkg', '--print-architecture'])
        if arch in ('aarch64', 'armel'):
            arch = 'arm64'
        elif arch in ('x86_64', 'x64', 'amd64'):
            arch = 'amd64'
        rootfs_url = (
            "https://mirrors.bfsu.edu.cn/ubuntu-cdimage/ubuntu-base/releases/"
            "{ver}/release/ubuntu-base-{ver}.2-base-{arch}.tar.gz").format(
                ver=version, arch=arch)
        popup('正在下载rootfs……')
        await self.get_result('wget {} -O rootfs/{}.tar.gz'.format(
            rootfs_url, name))
        popup('正在解压rootfs……')
        await self.get_result('tar xzvf rootfs/{}.tar.gz'.format(name))
        popup('正在清理……')
        await self.get_result('rm -f rootfs/{}.tar.gz'.format(name))
        popup('正在创建配置……')
        await self.get_result(
            'echo {cmd} > cmd/{name} && chmod +x cmd/{name}'.format(
                cmd=(command + 'rootfs/{}'.format(name)), name=name))

    async def get_centos(self):
        """获取centos rootfs并写入运行文件"""
        name = pywebio.input.input('请输入该系统的名字')
        command = pywebio.input.radio('请选择要用的命令',
                                      [('proot(无root下使用)', 'proot ', True),
                                       ('chroot(有root建议使用)', 'chroot ')])
        arch = subprocess.getoutput('dpkg --print-architecture')
        if arch in ('aarch64', 'armel'):
            arch = 'arm64'
        elif arch in ('x86_64', 'x64', 'amd64'):
            arch = 'amd64'
        elif arch in ('x86', 'i386'):
            arch = 'i386'
        rootfs_url = (
            "https://gitee.com/xingyujie_pro/Anlinux-Resources/tree/master/Rootfs/"
            "CentOS/{arch}/centos-rootfs-{arch}.tar.xz").format(arch=arch)
        popup('正在下载rootfs……')
        await self.get_result('wget {} -O rootfs/{}.tar.xz'.format(
            rootfs_url, name))
        popup('正在解压rootfs……')
        await self.get_result('tar xJvf rootfs/{}.tar.xz'.format(name))
        popup('正在清理……')
        await self.get_result('rm -f rootfs/{}.tar.xz'.format(name))
        popup('正在创建配置……')
        await self.get_result(
            'echo {cmd} > cmd/{name} && chmod +x cmd/{name}'.format(
                cmd=(command + 'rootfs/{}'.format(name)), name=name))

    def get_arch(self):
        """获取arch rootfs并写入运行文件"""


# Server Port 关于服务器的配置信息
if __name__ == "__main__":
    start_server(Main, debug=True, host="0.0.0.0", port=2002)
    pywebio.session.hold()
