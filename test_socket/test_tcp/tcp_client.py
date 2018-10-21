# coding:utf-8

import socket

# 定义常用参数
ip_port = ('127.0.0.1', 8007)
buffer_size = 1024
# 初始化得到一个socket对象
t_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 连接服务端
t_client.connect(ip_port)
# 收发消息
while True:
    msg = input('>>:').strip()
    t_client.send(msg.encode('utf-8'))
    if msg == 'quit':
        break
    elif not msg:
        print("input empty,please input again")
        continue
    msg_recv = t_client.recv(buffer_size)
    print("收到来自服务端的回复:", msg_recv.decode('utf-8'))
t_client.close()