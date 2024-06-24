import socket

class EchoClient:
    def __init__(self, host='192.168.0.105', port=12345):
        self.host = host
        self.port = port
        self.client_socket = None



    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def send(self, message):
        self.client_socket.sendall(message.encode('utf-8'))

    def on_key_event(self,event):
        print(event.name)
        self.send(event.name)
        if event.event_type == 'down' and event.name == 'alt+a':
            print('Alt+A 组合键被按下了。')
            self.send('截图')

    def receive(self):
        return self.client_socket.recv(1024).decode('utf-8')

    def close(self):
        self.client_socket.close()

    def __del__(self):
        print("客户端对象销毁。")

if __name__ == '__main__':
    import keyboard

    #input("按 Enter 启动客户端...")

    # 客户端连接和通信
    client = EchoClient()
    client.connect()
    client.send("你好，服务器！")
    keyboard.on_press(client.on_key_event)
    # 保持程序运行，以便监听快捷键
    keyboard.wait('esc')  # 按Esc键退出程序

    #print("收到服务器的回声：", client.receive())
    #client.close()

