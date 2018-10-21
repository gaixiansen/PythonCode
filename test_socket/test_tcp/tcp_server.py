# coding:utf-8

import socket

# 定义常用参数
ip_port = ('127.0.0.1', 8007)
buffer_size = 1024
max_conn_size = 5
# 初始化得到socket对象
t_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 解决端口ip被占用问题
t_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定一个ip
t_server.bind(ip_port)
# 开始监听(开机)
t_server.listen(max_conn_size)
print("服务端已开机...")
# 接收连接
while True:
    print("服务端接收连接中...")
    conn, addr = t_server.accept()
    print("接收到来自客户端的连接:", addr)
    # 收发消息
    while True:
        try:
            msg_recv = conn.recv(buffer_size)
            if msg_recv.decode('utf-8') == 'quit':
                print("客户端{}请求退出".format(addr))
                conn.close()
                break
            print("收到来自客户端发来的消息：", msg_recv.decode('utf-8'))
            msg_send =msg_recv.decode('utf-8').upper()
            conn.send(msg_send.encode('utf-8'))
        except Exception as e:
            print(e)
            break










