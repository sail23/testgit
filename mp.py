import socket
from threading import Thread 

ADDRESS = ('127.0.0.1',8712)

g_socket_server = None

g_conn_pool = []

def init():
    """
    初始化服务端
    """
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)
    print("服务器端已启动，等待客户端连接。。。")

def accept_client():
    """
    接受新连接
    """
    while True:
        client,_=g_socket_server.accept()
        g_conn_pool.append(client)
        thread = thread(target=message_handle,args=(client,))
        thread.setDaemon(True)
        thread.start()
def message_handle(client):
    """
    消息处理
    """
    client.sendall("连接服务器成功".encode(encoding="utf8"))
    while True:
        bytes = client.recv(1024)
        print("客户端消息：",bytes.decode(encoding="utf8"))
        if len(bytes)== 0:
            client.close()
            g_conn_pool.remove(client)
            print("有一个客户端下线了")
            break
if __name__ == '__main__':
    init()
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    while True:
        cmd = input("""-----------------------
        输入1：查看当前在线人数
        输入2：给指定客户端发送消息
        输入3：关闭服务端
        """)
        if cmd =="1":
            print("-----------------")
            print("当前在线人数：",len(g_conn_pool))
        elif cmd =='2':
            print("-----------------")
            index,msg = input("请输入“索引,消息”的形式：").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding="utf8"))
        elif cmd=="3":
            exit()

