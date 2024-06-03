from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

def main():
    server = socket(family=AF_INET,type=SOCK_STREAM) # 创建socket
    server.bind(('0.0.0.0',6788))
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        client,addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()


from threading import Thread,Lock
from json import dumps


# 
def main1():
    client = socket()
    client.connect(('0.0.0.0',6787))
    print(client.recv(1024).decode('utf-8'))
    client.close()

    # 自定义线程类
    class FileTransferHandle(Thread):
        def __init__(self,client):
            super().__init__()
            # 针对client开线程
            self.__client = client
        def run(self):
            my_dict = {}   
            my_dict['filename'] = 'guido.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.__client.send(json_str.encode('utf-8'))
            self.__client.close()


# 使用套接字开启服务监听