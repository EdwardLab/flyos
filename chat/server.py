#server.py
import socket
import logging

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建socket对象

    addr = ('127.0.0.1', 9999)
    s.bind(addr)  # 绑定地址和端口

    logging.info('UDP Server on %s:%s...', addr[0], addr[1])

    user = {}  # 存放字典{addr:name}
    while True:
        try:
            data, addr = s.recvfrom(1024)  # 等待接收客户端消息存放在2个变量data和addr里
            if not addr in user:  # 如果addr不在user字典里则执行以下代码
                for address in user:  # 从user遍历数据出来address
                    s.sendto(data + ' 进入聊天室...'.encode('utf-8'), address)  # 发送user字典的data和address到客户端
                user[addr] = data.decode('utf-8')  # 接收的消息解码成utf-8并存在字典user里,键名定义为addr
                continue  # 如果addr在user字典里，跳过本次循环

            if 'EXIT'.lower() in data.decode('utf-8'):#如果EXIT在发送的data里
                name = user[addr]   #user字典addr键对应的值赋值给变量name
                user.pop(addr)      #删除user里的addr
                for address in user:    #从user取出address
                    s.sendto((name + ' 离开了聊天室...').encode(), address)     #发送name和address到客户端
            else:   
                print('"%s" from %s:%s' %(data.decode('utf-8'), addr[0], addr[1]))  
                for address in user:    #从user遍历出address
                    if address != addr:  #address不等于addr时间执行下面的代码
                        s.sendto(data, address)     #发送data和address到客户端

        except ConnectionResetError:
            logging.warning('Someone left unexcept.')

if __name__ == '__main__':
    main()
