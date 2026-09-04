import socket
from protocol import send_message, recv_message

HOST = '127.0.0.1' #as long as it's localhost it works
PORT = 9000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((HOST, PORT))

print("Connected to server")

while True:
    message = input("Enter message (or 'quit'/'exit' to exit):")
    if message.lower() in ('quit', 'exit'):
        print('Connection disconnected.') 
        break
    
    # client_sock.sendall(message.encode())
    # print("Sent message")

    send_message(client_sock, message.encode())
    response = recv_message(client_sock)
    print(f"Received: {response}")
    

client_sock.close()