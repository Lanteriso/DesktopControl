import socket
import threading
import cv2
import numpy as np
from PIL import ImageGrab

def capture_and_send_screen(client_socket):
    while True:
        # 捕获屏幕图像
        screen = ImageGrab.grab()
        # 将PIL图像转换为numpy数组
        screen_np = np.array(screen)
        # 将图像转换为BGR格式
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
        # 编码图像为JPEG格式
        _, buffer = cv2.imencode('.jpg', screen_bgr)
        # 将编码后的图像数据发送给客户端
        client_socket.send(buffer.tobytes())

def main():
    # 创建socket对象并绑定到端口
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.0.105', 5000))
    server_socket.listen(1)
    print("等待客户端连接...")

    # 接受客户端的连接
    client_socket, addr = server_socket.accept()
    print(f"已连接: {addr}")

    # 创建线程来捕获并发送屏幕图像
    thread = threading.Thread(target=capture_and_send_screen, args=(client_socket,))
    thread.start()

    # 这里可以添加更多的控制逻辑，比如接收移动鼠标或键盘输入的指令

    # 等待线程结束
    thread.join()

if __name__ == "__main__":
    main()