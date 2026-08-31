import socket

HOST = 'localhost'
PORT = 9000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((HOST, PORT))

print("Connected to server")

client_sock.close()