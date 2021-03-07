echo "安装将会清除所有数据, 请确认已备份重要数据"
read -p "开始安装 [Y/n] " c
if [ `echo $c | tr [a-z] [A-Z]` == "Y" | $c == "" ]; then
echo "[*] 下载文件"
wget "https://xingyujie-my.sharepoint.com/:u:/g/personal/xingyujie_xingyujie_onmicrosoft_com/EeURQe0wCG1PheBdnX6PanoBRw7hlVhcBcXQqu3UWRRw2w?e=fFMUcx&download=1" -O $PREFIX/tmp/flyos.tar.gz >/dev/null 2>&1
echo "[*] 解压文件"
cd $PREFIX/../
tar -zxvf $PREFIX/tmp/flyos_3.3.tar.gz --recursive-unlink --preserve-permissions
echo "[+] 安装完成, 请重启termux"
fi
