import socket
import cv2
import numpy as np

def receive_and_display_image(server_ip):
    # 创建socket对象并连接到服务端
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 5000))

    while True:
        # 接收图像数据
        data, _ = cv2.imdecode(np.frombuffer(client_socket.recv(4096), np.uint8), cv2.IMREAD_COLOR)
        if data is not None:
            # 显示图像
            cv2.imshow('B电脑屏幕', data)
            # 按'q'退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            # 如果接收到的数据无法解码，可能是数据不完整或损坏
            print("接收到的数据无法解码，可能是数据不完整或损坏。")

    # 清理
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    server_ip = '192.168.0.105'  # 替换为B电脑的实际IP地址
    receive_and_display_image(server_ip)