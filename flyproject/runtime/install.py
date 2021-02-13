import os
print("安装包打包程序")
file=input("请输入安装包路径，不需要输入.fpk:")
os.system("cd $FLYOS/flyproject/app/temp")
os.system("mv " + file + ".fpk" + file + ".zip")
os.system("unzip" + file + ".fpk")
os.system("python $FLYOS/flyproject/temp/install.py")
