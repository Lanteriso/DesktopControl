import socket
from PIL import Image
from io import BytesIO
def start_client(host='192.168.0.105', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # 发送截图命令
        cmd = '截图'.encode('utf-8')
        # s.sendall(len(cmd).to_bytes(4, 'big'))
        s.sendall(cmd)

        # 接收图片大小
        size_bytes = s.recv(4)
        if len(size_bytes) != 4:
            print("接收到的图片大小信息不完整")
            return

        size = int.from_bytes(size_bytes, 'big')
        img_data = b''

        # 确保接收到完整的图片数据
        while len(img_data) < size:
            part = s.recv(size - len(img_data))
            if not part:
                print("图片数据接收不完整.")
                break
            img_data += part

        if len(img_data) == size:
            # 使用Pillow库将字节流转换为图片
            try:
                image = Image.open(BytesIO(img_data))
                # 显示图片
                image.show()
            except IOError as e:
                print(f"无法显示图片: {e}")
        else:
            print("接收到的图片数据不完整")

if __name__ == "__main__":
    start_client()


