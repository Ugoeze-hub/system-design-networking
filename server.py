import socket
from protocol import send_message, recv_message

HOST = 'localhost'
PORT = 9000

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

conn, addr = server_sock.accept()
print(f"Connected by {addr}")

while True:
    try:
        data = recv_message(conn)
        #data = conn.recv(1024)
    except ConnectionError:
        print("Client disconnected")
        break
    print(f"Received: {data}")
    send_message(conn, data)
    # conn.sendall(data)
    print("Echoed back")

conn.close()
server_sock.close()