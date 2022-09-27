import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
max_data_size = 1024

print(f"Connection to the server {HOST_IP}, port {HOST_PORT}")
print()

while True:

    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
        print("Connected to the server")
        break

    except ConnectionRefusedError:
        print("Error: the connection is not possible. Reconnection...")
        time.sleep(4)

while True:
    data_received = s.recv(max_data_size)
    if not data_received:
        break
    print("Mesaj : ", data_received.decode())
    text_sent = input("You: ")
    s.sendall(text_sent.encode())


s.close()
