import socket
import threading
from protocol import send_message, recv_message

HOST = 'localhost'
PORT = 9000

clients = []
clients_lock = threading.Lock()  # shields clients from concurrent read/write chaos

def broadcast(message_bytes, sender_conn):
    with clients_lock:
        for client_conn in clients:
            if client_conn != sender_conn:
                send_message(client_conn, message_bytes)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    
    with clients_lock:
        clients.append(conn)
        
    while True:
        try:
            data = recv_message(conn)
            #data = conn.recv(1024)
        except ConnectionError:
            print(f"{addr} disconnected (conn: {conn})")
            break
        print(f"Received from {addr}: {data}")
        broadcast(data, conn)
        # conn.sendall(data)
        print("Echoed back")

    with clients_lock:
        clients.remove(conn)
    
    conn.close()
    
# AF_INET  uses IPv4 addresses
# SOCK_STREAM uses TCP as opposed to SOCK_DGRAM for UDP)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created:", server_sock)

# Allow the OS to reuse this address/port immediately after the program exits,
# instead of holding it in a "wait" state for a minute or two.
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print("Socket created and configured")


server_sock.bind((HOST, PORT))
server_sock.listen(5)

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        conn, addr = server_sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
except KeyboardInterrupt:
    print("\nShutting down server...")
finally:
    server_sock.close()