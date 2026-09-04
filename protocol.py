import struct

def recv_exact(sock, num_bytes):
    buffer = b''
    while len(buffer) < num_bytes:
        chunk = sock.recv(num_bytes - len(buffer))
        if not chunk:
            raise ConnectionError("Socket closed before expected bytes were received")
        buffer += chunk
    return buffer

def send_message(sock, message_bytes):
    length_prefix = struct.pack('!I', len(message_bytes))
    sock.sendall(length_prefix)
    sock.sendall(message_bytes)
    
def recv_message(sock):
    length_prefix = recv_exact(sock, 4)
    message_length = struct.unpack('!I', length_prefix)[0]
    message_bytes = recv_exact(sock, message_length)
    return message_bytes