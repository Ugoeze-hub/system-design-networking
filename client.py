import socket

HOST = '127.0.0.1' #as long as it's localhost it works
PORT = 9000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((HOST, PORT))

print("Connected to server")

client_sock.sendall(b"hello server")
print("Sent message")

response = client_sock.recv(1024)
print(f"Received: {response}")

client_sock.close()