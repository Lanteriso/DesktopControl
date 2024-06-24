import socket
from PIL import ImageGrab  # 需要安装Pillow库
from io import BytesIO
import pydirectinput
def send_screenshot(conn):
    # 截取屏幕
    screenshot = ImageGrab.grab()
    # 将图片转换为字节流
    buffer = BytesIO()
    screenshot.save(buffer, format='PNG')
    img_str = buffer.getvalue()

    # 发送图片数据
    conn.sendall(len(img_str).to_bytes(4, 'big'))  # 发送图片大小
    conn.sendall(img_str)

class EchoServer:
    def __init__(self, host='192.168.0.105', port=12345):
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
                client_socket.sendall('Hello')
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

    def startA(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("服务器启动，等待连接...")
        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"{addr}:{data.decode()}")
                    if data.decode() == 'a':
                        send_screenshot(client_socket)
                    else:
                        pydirectinput.press(data.decode())
        except KeyboardInterrupt:
            print("服务器关闭。")
        finally:
            print("服务器关闭2。")
            self.server_socket.close()
    def __del__(self):
        print("服务器对象销毁。")

if __name__ == '__main__':
    import threading

    # 启动服务器
    server = EchoServer()
    server_thread = threading.Thread(target=server.startA)
    server_thread.start()
    server_thread.join()
    # 等待服务器启动
    #input("按 Enter 启动客户端...")
