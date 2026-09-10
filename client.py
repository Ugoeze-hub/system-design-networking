import socket
import threading
from protocol import send_message, recv_message

HOST = '127.0.0.1' #as long as it's localhost it works
PORT = 9000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((HOST, PORT))

print("Connected to server")

def receive_loop():
    while True:
        try:
            data = recv_message(client_sock)
        except ConnectionError:
            print("Disconnected from server")
            break
        print(f"Received: {data.decode()}")

receive_thread = threading.Thread(target=receive_loop, daemon=True)
receive_thread.start()

while True:
    message = input("Enter message (or 'quit'/'exit' to exit):")
    if message.lower() in ('quit', 'exit'):
        print('Connection disconnected.') 
        break
    
    # client_sock.sendall(message.encode())
    # print("Sent message")

    send_message(client_sock, message.encode())
    # response = recv_message(client_sock)   # ← wait right here, for THIS specific reply
    # print(f"Received: {response}")

client_sock.close()