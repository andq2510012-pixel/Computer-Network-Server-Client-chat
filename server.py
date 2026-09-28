import socket
import threading
from datetime import datetime

def receive_messages(client_socket):
    #liên tục nhận tin nhắn từ client
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8') #giải mã 
            if not message:
                break
            print(f"\n[Máy 2]: {message}")
        except:
            print("\ndisconnect.")
            break

# 
# Server
HOST = '0.0.0.0'  
PORT = 5000       

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#ipv4, TCP
server.bind((HOST, PORT))
server.listen(1)

print(f"Waiting for Client to connect{PORT}...")
client_socket, client_address = server.accept()
print(f"Connect successfully with {client_address}!")

# Bắt đầu luồng nhận tin nhắn
thread = threading.Thread(target=receive_messages, args=(client_socket,))
thread.daemon = True
thread.start()

# Vòng lặp chính để gửi tin nhắn
while True:
    try:
        msg = input()
        client_socket.send(msg.encode('utf-8'))

    except KeyboardInterrupt:
        break

while True:
    try:
        msg = input()
        now = datetime.now().strftime('%H:%M:%S')
        client_socket.send(f"[{now}] {msg}".encode('utf-8'))
    except KeyboardInterrupt:
        break