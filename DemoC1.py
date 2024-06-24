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

    def 截图啊(self):
        from PIL import Image
        from io import BytesIO
        # 发送截图命令
        cmd = '截图'.encode('utf-8')
        # s.sendall(len(cmd).to_bytes(4, 'big'))
        self.send(cmd)

        # 接收图片大小
        size_bytes = self.client_socket.recv(4)
        if len(size_bytes) != 4:
            print("接收到的图片大小信息不完整")
            return

        size = int.from_bytes(size_bytes, 'big')
        img_data = b''

        # 确保接收到完整的图片数据
        while len(img_data) < size:
            part = self.client_socket.recv(size - len(img_data))
            if not part:
                print("图片数据接收不完整.")
                break
            img_data += part

        if len(img_data) == size:
            # 使用Pillow库将字节流转换为图片
            try:
                image = Image.open(BytesIO(img_data))
                # 显示图片
                image.show()
            except IOError as e:
                print(f"无法显示图片: {e}")
        else:
            print("接收到的图片数据不完整")

    def on_key_event(self,event):
        print(event.name)
        self.send(event.name)
        if event.event_type == 'down' and event.name == '截图':
            print('Alt+A 组合键被按下了。')
            self.client_socket.sendall('截图')
        elif event.name == 'esc':
            self.close()
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

