from socket import *

ip_port = ('127.0.0.1', 8090)
buffer_size = 1024
u_client = socket(AF_INET, SOCK_DGRAM)
print("客户端开始运行...")
while True:
    msg_send = input(">>:").strip()
    u_client.sendto(msg_send.encode('utf-8'), ip_port)
    data, addr = u_client.recvfrom(buffer_size)
    print("收到服务端的回复:", data.decode('utf-8'))

