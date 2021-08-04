#python -m py_compile 文件
import os
print("检查系统激活")
#i=input("请输入密钥:")
#i是密钥内容
f = open( '/data/data/com.termux/files/home/.flyos/active/key.fk', 'r' )
i=f.read().split("-")
if not i[0]:
  print("序列号无效，可前往http://store.flyosgeek.com购买")
  os.system("python $FLYOS/kernel/boot/active/buy.py")
  f = open( '/data/data/com.termux/files/home/.flyos/active/key.fk', 'r' )
  i=f.read().split("-")
for _ in i:
    if int(_) % 6 != 0:
        print("序列号无效，可前往http://store.flyosgeek.com购买")
        os.system("python $FLYOS/kernel/boot/active/buy.py")
       
        print("非FlyOS激活序列号，请检查或联系管理员!!")

print("正在启动")
os.system("bash $FLYOS/munu.sh")