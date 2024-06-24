
import socket
import sys
from PIL import ImageGrab  # 需要安装Pillow库
from io import BytesIO

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

def start_server(host='192.168.0.105', port=12345):
    # 创建 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 绑定地址和端口
        s.bind((host, port))
        # 开始监听
        s.listen()
        print(f"Server started, listening on {host}:{port}")

        while True:
            # 接受连接
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # 接收数据
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    # 发送数据
                    #conn.sendall(data)
                    send_screenshot(conn)

if __name__ == "__main__":
    start_server()