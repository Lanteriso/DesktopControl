import socket

def start_client(host='192.168.0.105', port=12345):
    # 创建 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到服务器
        s.connect((host, port))
        print("Connected to server")

        # 发送数据
        message = 'Hello, server!'
        s.sendall(message.encode())

        # 接收数据
        data = s.recv(1024)
        print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_client()