#!/bin/bash
while true; do
    OPTION=$(
        whiptail \
            --backtitle "FlyOS GUI Console" \
            --title "FlyOS 开源面板" \
            --menu "请使用触摸屏或方向键+回车键进行操作" 0 50 0 \
            00 "查看关于" \
            01 "反馈问题" \
            02 "快速更新" \
            03 "切换更新通道" \
            04 "完整更新" \
            1 "给FlyOS 安装GNU/发行版Linux(推荐|简洁)" \
            2 "Linux菜单高级部署菜单(推荐)" \
            3 "软件安装器(Termux软件包)" \
            4 "启动最近使用的GNU/Linux" \
            5 "FlyOS Chat 飞聊聊天系统" \
            6 "重新查看激活状态/重启" \
            7 "更新软件源APT" \
            8 "更新软件源PKG" \
            9 "查看系统信息" \
            10 "更改默认Shell解释器" \
            11 "更改Termux密码" \
            12 "FlyOS浏览器" \
            13 "网站服务器面板" \
            14 "重新启动FlyOS WEB Panel(已自动启动，再次启动会出问题)" \
            15 "打开Aria2" \
            16 "打开Aria2 WEB" \
            17 "VM虚拟机" \
            18 "文件管理器" \
            19 "虚拟机WEB管理面板(已自动启动，再次启动会出问题)" \
            20 "启动nginx WEB Server" \
            21 "初始化FlyOS" \
            22 "启动Xfce4图形化(端口5902)" \
            23 "启动Minecraft-pocketmine服务器" \
            24 "退出" \
            3>&1 1>&2 2>&3
    )
    case $OPTION in
    1) python3 "$FLYOS"/deploylinux/deploy.py ;;
    2) tmoe ;;
    3) python3 "$FLYOS"/softwareinstall/install.py ;;
    4) debian ;;
    5) python3 "$FLYOS"/chat/chat.py ;;
    6) python3 "$FLYOS"/console.py ;;
    7) apt update ;;
    8) pkg update ;;
    9) screenfetch ;;
    10) chsh ;;
    11)
        whiptail --msgbox '您可以更改FlyOS的默认User密码' 0 50
        passwd
        ;;
    12)
        website=$(whiptail --inputbox '欢迎使用FlyOS Browser浏览器，例如:http://www.bing.com --必应 输入网址开始浏览网页:' 0 50)
        w3m "$website"
        ;;
    13) python3 "$FLYOS"/webserver/main.py ;;
    14) python3 "$FLYOS"/panel/server.py ;;
    15) aria2c --enable-rpc --rpc-listen-all ;;
    16)
        cd /data/data/com.termux/files/home/webui-aria2 || whiptail --msgbox "cd出现了问题" 0 50
        node node-server.js
        ;;
    17) bash "$FLYOS"/virtualmachine/vm.sh ;;
    18) mc ;;
    19) python "$FLYOS"/virtualmachine/web.py ;;
    20) nginx ;;
    21) python "$FLYOS"/.firstuse/register.py ;;
    22)
        whiptail --msgbox 'Xfce4图形化界面启动在IP:5902，本地连接请输入IP:127.0.0.1:5902' 0 50
        nohup flyosvnc &
        ;;
    23) bash "$FLYOS"/mc/start.sh ;;
    0) zsh ;;
    00)
        whiptail --msgbox "关于:
开发者创始人:Rainbow邢宇杰
邮箱:xingyujie50@gmail.com" 0 0
        ;;
    01) whiptail --msgbox "有BUG请反馈到:xingyujie50@gmail.com" 0 50 ;;

    02)
        if (whiptail --yesno '将会进行快速更新
快速更新有可能会出现问题，但不会删除用户数据' 0 50); then
            cd "$FLYOS" || whiptail --msgbox "cd出现了问题" 0 50
            git reset --hard
            git pull
            pip install -r requirements.txt
            cd "$HOME" || whiptail --msgbox "cd出现了问题" 0 50
        else
            whiptail --msgbox "取消" 0 50
        fi
        ;;
    03)
        cd "$FLYOS" || whiptail --msgbox "cd出现了问题" 0 50
        while true; do
            case $(
                whiptail \
                    --menu "请选择要执行的操作" 0 50 0 \
                    1 "切换到稳定版" \
                    2 "切换到preview" \
                    3 "切换到beta" \
                    4 "切换到dev(unstable, 更新最快)" \
                    5 "退出" \
                    3>&1 1>&2 2>&3
            ) in
            1) git checkout master ;;
            2) git checkout preview ;;
            3) git checkout beta ;;
            4) git checkout dev ;;
            5) break ;;
            *) break ;;
            esac
        done
        ;;
    04)
        if (whiptail --yesno '注意：
完整更新将会删除所有用户数据
真的要继续吗' 0 50); then
            curl flyosgeek.com/gosetup.sh | bash
        else
            whiptail --msgbox "取消" 0 50
        fi
        ;;
    24)
        break
        ;;
    *) break ;;
    esac
done
