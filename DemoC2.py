import socket

class EchoServer:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("服务器启动，等待连接...")

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"接收到来自 {addr} 的连接")
                client_socket.sendall(b'欢迎连接服务器！')
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    client_socket.sendall(data)  # 回声
                client_socket.close()
        except KeyboardInterrupt:
            print("服务器关闭。")
        finally:
            self.server_socket.close()

    def __del__(self):
        print("服务器对象销毁。")

if __name__ == '__main__':
    import threading

    # 启动服务器
    server = EchoServer()
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # 等待服务器启动
    input("按 Enter 启动客户端...")