import socket
import threading
import cv2
from PIL import ImageGrab
import time
def capture_and_send_screen(client_socket):
    while True:
        # 捕获屏幕图像，指定分辨率
        screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        _, buffer = cv2.imencode('.jpg', screen, [int(cv2.IMWRITE_JPEG_QUALITY), 10])
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

    # 等待线程结束
    thread.join()

if __name__ == "__main__":
    main()