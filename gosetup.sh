#!/data/data/com.termux/files/usr/bin/bash
echo "安装将会清除所有数据, 请确认已备份重要数据"
read -p "按下回车继续" _
echo "[*] 安装依赖"
pkg install wget git -y
echo "[*] 下载文件"
<<<<<<< HEAD
rm -rf $PREFIX/tmp/飞屎OS-bate.tar.gz
wget --show-progress -q "https://请遵守开源协议-my.sharepoint.com/:u:/g/personal/xingyujie_xingyujie_onmicrosoft_com/EfqCU1iWEBtBloitHDxCTKcBYiMJ9bEiDVeAzEi6wPLSVA?e=ZdnmMV&download=1" -O $PREFIX/tmp/飞屎OS-bate.tar.gz
rm -rf ~/.飞屎OS-bate
echo "[*] 解压文件"
cd $PREFIX/../
tar -zxvf $PREFIX/tmp/飞屎OS-bate.tar.gz --recursive-unlink --preserve-permissions
echo "[*] 更新系统"
cd $PREFIX/etc/飞屎OS-bate
=======
rm -rf $PREFIX/tmp/flyos.tar.gz
wget --show-progress -q "https://xingyujie-my.sharepoint.com/:u:/g/personal/xingyujie_xingyujie_onmicrosoft_com/EfqCU1iWEBtBloitHDxCTKcBYiMJ9bEiDVeAzEi6wPLSVA?e=ZdnmMV&download=1" -O $PREFIX/tmp/flyos.tar.gz
rm -rf ~/.flyos
echo "[*] 解压文件"
cd $PREFIX/../
tar -zxvf $PREFIX/tmp/flyos.tar.gz --recursive-unlink --preserve-permissions
echo "[*] 更新系统"
cd $PREFIX/etc/flyos
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)
git pull
pip install -r requirements.txt
echo "[+] 安装完成, 请重启termux"
