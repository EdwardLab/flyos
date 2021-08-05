#!/bin/bash
#Tarprogressbar.sh
#一个用来显示tar解压缩某文件时进度条的脚本

FILE="test.tar.gz"

TOTAL_SIZE=0
for FILE_SIZE in $(tar tvvf $FILE | awk '{print $3}'); do
    if [ "$FILE_SIZE" = "${FILE_SIZE//[^0-9]/}" ]; then 
        TOTAL_SIZE=$((TOTAL_SIZE+FILE_SIZE))
    fi
done

TMPFIFO=/tmp/tmpfifo &> /dev/null
if [[  -f $TMPFIFO ]];then
:
else
    mkfifo $TMPFIFO &> /dev/null
fi

(
TOTAL_FILE_SIZE_UNZIP=0
{
p=1
while read line
do
    FILE_SIZE_UNZIP=$(echo $line | awk '{print $3}')
    ((TOTAL_FILE_SIZE_UNZIP=$TOTAL_FILE_SIZE_UNZIP+$FILE_SIZE_UNZIP))
    echo $((TOTAL_FILE_SIZE_UNZIP*100/TOTAL_SIZE))
done<$TMPFIFO
rm -rf $TMPFIFO
echo 100
} | whiptail --gauge "Extracting $FILE..." 6 60 0
) &
B_PID=$!

tar zxvvf  $FILE -C /opt >$TMPFIFO 2>/dev/null 
wait $B_PID
echo " unzip ended successfully. "
