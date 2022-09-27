import socket

HOST_IP = "127.0.01"
HOST_PORT = 32000
max_data_size = 1024

s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting the connection on {HOST_IP}, port {HOST_PORT}...")
connection_socket, customer_adress = s.accept()
print(f"Connection etablished with {customer_adress}")

while True:
    text_sent = input("You: ")
    connection_socket.sendall(text_sent.encode())
    data_received = connection_socket.recv(max_data_size)
    if not data_received:
        break
    print("Mesaj : ", data_received.decode())


s.close()
connection_socket.close()