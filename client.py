import socket
import threading

# Cấu hình kết nối tới Server
SERVER_IP = '10.50.84.139'  # <--- THAY BẰNG IP V4 CỦA MÁY HOST SERVER
PORT = 5000

nickname = input("Nhập biệt danh của bạn: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def receive():
    """Lắng nghe tin nhắn từ Server"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(f"[Máy 1]: {message}")
        except:
            print("Đã xảy ra lỗi hoặc mất kết nối tới Server!")
            client.close()
            break

def write():
    """Gửi tin nhắn lên Server"""
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

# Chạy đa luồng để vừa nhận vừa gửi tin nhắn cùng lúc
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()