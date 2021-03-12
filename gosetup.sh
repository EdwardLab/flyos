#!/data/data/com.termux/files/usr/bin/bash
echo "安装将会清除所有数据, 请确认已备份重要数据"
read -p "按下回车继续" _
echo "[*] 安装依赖"
pkg install wget -y
echo "[*] 下载文件"
rm -rf $PREFIX/tmp/flyos.tar.gz
wget --show-progress -q "http://d.ixcmstudio.cn:21188/doc/FlyOS/3.3/flyos_3.3.tar.gz" -O $PREFIX/tmp/flyos.tar.gz
echo "[*] 解压文件"
cd $PREFIX/../
tar -zxvf $PREFIX/tmp/flyos.tar.gz --recursive-unlink --preserve-permissions
echo "[+] 安装完成, 请重启termux"
