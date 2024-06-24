import socket
import cv2
from PIL import ImageGrab
import numpy as np

# 设置服务端的IP地址和端口号
server_ip = '192.168.0.105'  # 请替换为服务端的局域网IP
server_port = 5000

# 创建socket对象并绑定IP地址和端口号
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

# 开始监听连接
server_socket.listen(1)
print("等待客户端连接...")

# 接受客户端连接
client_socket, addr = server_socket.accept()
print(f"已连接: {addr}")

# 定义接收屏幕图像的函数
def receive_screen():
    while True:
        # 捕获屏幕图像
        screen = ImageGrab.grab()
        # 将图像转换为numpy数组
        screen_np = np.array(screen)
        # 将图像编码为字节流
        _, buffer = cv2.imencode('.jpg', cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB), [int(cv2.IMWRITE_JPEG_QUALITY), 50])
        # 发送字节流
        client_socket.send(buffer.tobytes())

# 开始接收屏幕图像的循环
receive_screen()

# 关闭连接
client_socket.close()
server_socket.close()