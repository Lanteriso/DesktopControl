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

    def receive(self):
        return self.client_socket.recv(1024).decode('utf-8')

    def close(self):
        self.client_socket.close()

    def __del__(self):
        print("客户端对象销毁。")