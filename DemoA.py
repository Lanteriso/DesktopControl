import socket
import cv2
import numpy as np
def receive_and_display_image(server_ip):
    # 创建socket对象并连接到服务端
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(0.5)  # 设置非阻塞模式
    client_socket.connect((server_ip, 5000))

    while True:
        # 接收图像数据
        data = b''
        while len(data) < 4000000:  # 假设JPEG图像数据不会超过4MB
            packet = client_socket.recv(1080)
            if not packet:
                break
            data += packet

        # 使用cv2.imdecode尝试解码图像
        nparr = np.frombuffer(data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # 检查frame是否解码成功
        if frame is not None:
            # 显示图像
            cv2.imshow('B', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("无法解码图像数据。")

    # 清理
    client_socket.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    server_ip = '192.168.0.105'  # 替换为B电脑的实际IP地址
    receive_and_display_image(server_ip)