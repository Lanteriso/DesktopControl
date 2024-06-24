import socket

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
                    conn.sendall(data)

if __name__ == "__main__":
    start_server()