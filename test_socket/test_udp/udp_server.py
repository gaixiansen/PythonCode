# coding:utf-8

from socket import *

ip_port = ('127.0.0.1', 8090)
buffer_size = 1024
u_server = socket(AF_INET, SOCK_DGRAM)
u_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
u_server.bind(ip_port)
print("服务端开始运行...")
while True:
    data, addr = u_server.recvfrom(buffer_size)
    print("收到来自客户端的消息:", data.decode('utf-8'))
    msg_send = data.decode('utf-8').upper()
    u_server.sendto(msg_send.encode('utf-8'), addr)
