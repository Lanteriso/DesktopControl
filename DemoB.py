import socket
import threading
import cv2

def receive_screen(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        frame = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Remote Desktop', frame)

def send_commands(client_socket):
    # 这里可以根据用户的操作发送控制命令到客户端.
    pass

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.105', 5000))
server_socket.listen()

client_socket, addr = server_socket.accept()
print(f'Connected by {addr}')

t1 = threading.Thread(target=receive_screen, args=(client_socket,))
t2 = threading.Thread(target=send_commands, args=(client_socket,))

t1.start()
t2.start()

t1.join()
t2.join()

server_socket.close()
cv2.destroyAllWindows()