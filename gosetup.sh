echo "安装将会清除所有数据, 请确认已备份重要数据"
read -p "开始安装 [Y/n] " c
if [ $c == "Y" -o $c == "y" ]; then
echo "[*] 安装依赖"
pkg in wget -y
echo "[*] 下载文件"
wget --show-progress -q "https://xingyujie-my.sharepoint.com/:u:/g/personal/xingyujie_xingyujie_onmicrosoft_com/EeURQe0wCG1PheBdnX6PanoBRw7hlVhcBcXQqu3UWRRw2w?e=fFMUcx&download=1" -O $PREFIX/tmp/flyos.tar.gz
echo "[*] 解压文件"
cd $PREFIX/../
tar -zxvf $PREFIX/tmp/flyos.tar.gz --recursive-unlink --preserve-permissions
echo "[+] 安装完成, 请重启termux"
fi
