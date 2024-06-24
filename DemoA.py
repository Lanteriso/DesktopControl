import socket
import cv2
import numpy as np

# 设置服务端的IP地址和端口号
server_ip = '192.168.0.105'  # 请替换为服务端的局域网IP
server_port = 5000

# 创建socket对象并连接到服务端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# 定义显示屏幕图像的函数
def display_screen():
    while True:
        # 接收屏幕图像的字节流
        data = client_socket.recv(1024)
        # 如果没有数据，说明连接已断开
        if not data:
            break
        # 将字节流解码为图像
        frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        # 显示图像
        cv2.imshow('Remote Desktop', frame)
        # 按'q'退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 开始显示屏幕图像的循环
display_screen()

# 关闭连接
client_socket.close()
cv2.destroyAllWindows()