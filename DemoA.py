import socket
from PIL import Image
from io import BytesIO
def start_client(host='192.168.0.105', port=12345):
    # 创建 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 连接到服务器
        s.connect((host, port))
        # 发送截图命令
        cmd = '截图'.encode('utf-8')
        s.sendall(len(cmd).to_bytes(4, 'big'))
        s.sendall(cmd)
        # 发送数据
        # message = 'Hello, server1!'
        # 接收图片大小
        size = int.from_bytes(s.recv(4), 'big')
        img_data = b''
        while len(img_data) < size:
            part = s.recv(size - len(img_data))
            if not part:
                break
            img_data += part

            # 使用Pillow库将字节流转换为图片
            image = Image.open(BytesIO(img_data))
            # 显示图片
            image.show()

if __name__ == "__main__":
    start_client()


