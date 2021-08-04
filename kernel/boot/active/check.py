#python -m py_compile 文件
import os
import requests
print("激活FlyOS!")
while 1:
    i=input("请输入密钥:")
    #i是密钥内容
    i=i.split("-")

    URL = 'http://store.flyosgeek.com/active/key.php?key=' + '-'.join(i)
    res = requests.get(URL)
    if res.text == 'n':
      print("密钥作废(已被使用)或者格式不正确，请检查!")
    elif res.text == 'y':
      break
print("序列号正确，写入中")
f = open( '/data/data/com.termux/files/home/.flyos/active/key.fk', 'w' )
f.write("-".join(i))
f.close()
os.system("bash $FLYOS/munu.sh")