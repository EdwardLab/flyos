"""
FlyOS Panel By:XingYuJie
Use Under License GPL - V3
"""
import asyncio
import os
import subprocess

import pywebio.input
from pywebio import start_server
from pywebio.output import popup, put_text, put_html
from pywebio.session import set_env
import tarfile
print("Linux部署程序--中文版")
print("By:FlyOS MicroTech XingYuJie(严禁删除版权，不允许修改版权)GPL-V3")


async def get_result(cmd):
    """
    params:
        cmd - 要执行的命令
    """
    popen = subprocess.Popen(cmd,
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             text=True,
                             cwd=path)
    while True:
        buff = popen.stdout.readline()
        if buff:
            put_text(buff)
        elif popen.poll() is not None:
            break


def main():
    set_env(title="Linux  部署程序--中文版", auto_scroll_bottom=True)
    put_html("<h1>FlyOS Linux Deploy</h1>")
    put_text("By:FlyOS MicroTech XingYuJie(严禁删除版权，不允许修改版权)GPL-V3", sep=" ")
    popup(
        "欢迎使用Linux部署程序--中文版",
        "欢迎使用Linux部署程序--中文版。"
        "开始部署你的Linux吧！"
        "程序由MicroTech Projects -- FlyOS强力驱动",
    )
    Main()


class Main:
    """FlyOS WEB Panel main"""

    def __init__(self):
        global path
        self.path = path
        self.__run()

    async def join(self):
        """进入 Linux 系统"""
        options = []
        dirs = os.listdir("{}/cmd".format(self.path))
        for vm_path in dirs:
            options.append((vm_path, vm_path))
        linux = pywebio.input.select("选择创建的Linux名称", options=options)
        popup('打开Linux', '请在终端输入 `$FLYOS/deploylinux/cmd/{}` 打开 Linux'.format(linux))

    async def delete(self):
        """删除一个 Linux 系统"""
        options = []
        dirs = os.listdir("{}/cmd".format(self.path))
        for vm_path in dirs:
            options.append((vm_path, vm_path))
        linux = pywebio.input.select("选择创建的Linux名称", options=options)
        subprocess.call([
            'rm -rf {path}/rootfs/{linux}'.format(path=self.path,
                                                  linux=linux)
        ],
            cwd=self.path)

    def __run(self):
        n = pywebio.input.select('请选择你要执行的操作',
                                 options=[
                                     ("安装Linux", 1, True),
                                     ("进入Linux", 2),
                                 ])
        if n == 1:
            GetLinux()
        elif n == 2:
            asyncio.run(self.join())
        elif n == 3:
            asyncio.run(self.delete())


class GetLinux:
    def __init__(self):
        name = pywebio.input.input('请输入该系统的名字')
        command = pywebio.input.radio('请选择要用的命令',
                                      [('PRoot(无root下使用)', 'proot -r ', True),
                                       ('chroot(有root建议使用)', 'chroot ')])
        arch = subprocess.getoutput('dpkg --print-architecture')
        num = pywebio.input.select('请选择你要安装的系统',
                                   options=[
                                       ("Ubuntu", 1, True),
                                       ("CentOS", 2),
                                       ("Kali", 3),
                                   ])
        if num == 1:
            asyncio.run(self.get_ubuntu(name, arch, command))
        elif num == 2:
            asyncio.run(self.get_centos(name, arch, command))
        elif num == 3:
            asyncio.run(self.get_kali(name, arch, command))

    @staticmethod
    async def get_ubuntu(name, arch, command):
        """获取ubuntu rootfs并写入运行文件"""
        version = pywebio.input.select('请选择版本号',
                                       options=[
                                           ("20.04", "20.04.2", True),
                                           ("20.10", "20.10"),
                                           ("21.04", "21.04"),
                                       ])
        if arch in ('aarch64', 'armel'):
            arch = 'arm64'
        elif arch in ('x86_64', 'x64', 'amd64'):
            arch = 'amd64'
        rootfs_url = (
            "https://mirrors.bfsu.edu.cn/ubuntu-cdimage/ubuntu-base/releases/"
            "{ver}/release/ubuntu-base-{ver}-base-{arch}.tar.gz").format(
            ver=version, arch=arch)
        await GetLinux.get_rootfs(rootfs_url, name, 'gz', command)

    @staticmethod
    async def get_centos(name, arch, command):
        """获取centos rootfs并写入运行文件"""
        if arch in ('aarch64', 'armel'):
            arch = 'arm64'
        elif arch in ('x86_64', 'x64', 'amd64'):
            arch = 'amd64'
        elif arch in ('x86', 'i386'):
            arch = 'i386'
        rootfs_url = (
            "https://gitee.com/xingyujie_pro/Anlinux-Resources/tree/master/Rootfs/"
            "CentOS/{arch}/centos-rootfs-{arch}.tar.xz").format(arch=arch)
        await GetLinux.get_rootfs(rootfs_url, name, 'xz', command)

    @staticmethod
    async def get_kali(name, arch, command):
        """获取kali rootfs并写入运行文件"""
        if arch in ('aarch64', 'armel'):
            arch = 'arm64'
        elif arch in ('x86_64', 'x64', 'amd64'):
            arch = 'amd64'
        elif arch in ('x86', 'i386'):
            arch = 'i386'
        rootfs_url = (
            "https://gitee.com/xingyujie_pro/Anlinux-Resources/tree/master/Rootfs/"
            "Kali/{arch}/kali-rootfs-{arch}.tar.xz").format(arch=arch)
        await GetLinux.get_rootfs(rootfs_url, name, 'xz', command)

    @staticmethod
    async def get_rootfs(rootfs_url, name, ext, command):
        popup('正在下载rootfs……')
        await get_result('wget {} -O deploylinux/rootfs/{}.tar.{}'.format(
            rootfs_url, name, ext))
        popup('正在解压rootfs……')
        path = os.path.abspath('deploylinux/rootfs/{}/'.format(name))
        os.makedirs(path)
        fs = tarfile.open('deploylinux/rootfs/{name}.tar.{ext}'.format(name=name, ext=ext))
        fs.extractall(path=path)
        # await get_result(
        #     'tar x{type}vf rootfs/{name}.tar.{ext} -C rootfs/{name}'.format(type='J' if ext == 'xz' else 'gz',
        #                                                                     )
        popup('正在清理……')
        await get_result('rm -f rootfs/{}.tar.{}'.format(name, ext))
        popup('正在创建配置……')
        conf_template = '''
        if [ -z $1 ]; then
            {command} rootfs/{name}/ /bin/bash
        else
        {command} rootfs/{name}/ /bin/sh -c $1
        fi
        '''
        await get_result(
            'echo {cmd} > cmd/{name} && chmod +x cmd/{name}'.format(
                cmd=conf_template.format(command=command, name=name), name=name))


# Server Port 关于服务器的配置信息
if __name__ == "__main__":
    env = os.getenv('FLYOS')
    if env is None:
        env = '.'
    path = os.path.abspath(env + '/deploylinux')
    if not os.path.exists(os.path.abspath(path + "/rootfs")):
        os.mkdir(os.path.abspath(path + "/rootfs"))
    if not os.path.exists(os.path.abspath(path + "/cmd")):
        os.mkdir(os.path.abspath(path + "/cmd"))
    start_server(main, debug=True, host="0.0.0.0", port=2002)
    pywebio.session.hold()
