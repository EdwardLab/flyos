CONTAINERROOT="/container/userspace"
mount --bind /dev $CONTAINERROOT/dev
mount --bind /sys $CONTAINERROOT/sys
mount --bind /proc $CONTAINERROOT/proc
mount -t devpts devpts $CONTAINERROOT/dev/pts
mount -t tmpfs -o size=256M tmpfs $CONTAINERROOT/dev/shm
mount --bind /sdcard $CONTAINERROOT/sdcard
mount --bind /flyos $CONTAINERROOT/flyos
mount --bind /flyosext $CONTAINERROOT/flyosext
mount --bind /usr/local/flyos/bin $CONTAINERROOT/usr/local/flyos/bin
mount --bind / $CONTAINERROOT/flyosroot