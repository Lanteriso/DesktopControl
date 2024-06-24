import socket
import threading
import cv2
from PIL import ImageGrab

def capture_screen_and_send(client_socket):
    while True:
        screen = ImageGrab.grab()
        img_np = np.array(screen)
        _, buffer = cv2.imencode('.jpg', cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB), [int(cv2.IMWRITE_JPEG_QUALITY), 50])
        client_socket.send(buffer.tobytes())

def receive_commands(client_socket):
    while True:
        command = client_socket.recv(1024).decode('utf-8')
        if command == 'quit':
            break
        # 根据接收到的命令执行相应操作，例如移动鼠标、点击等

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.0.105', 5000))

t1 = threading.Thread(target=capture_screen_and_send, args=(client_socket,))
t2 = threading.Thread(target=receive_commands, args=(client_socket,))

t1.start()
t2.start()

t1.join()
t2.join()

client_socket.close()
