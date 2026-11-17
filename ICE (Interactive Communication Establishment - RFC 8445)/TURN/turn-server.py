import socket
import threading

HOST = "0.0.0.0"
PORT = 3478
VALID_CREDENTIALS = b"AUTH:yash:123"

clients = {}  # Stores {client_name: (ip, port)}
lock = threading.Lock()

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    print(f"[TURN Server] Listening on UDP {HOST}:{PORT}...")

    while True:
        data, addr = sock.recvfrom(4096)
        
        # 1. Handle Authentication & Allocation
        if data.startswith(b"REGISTER:"):
            parts = data.decode().split(":")
            if len(parts) == 4 and f"AUTH:{parts[2]}:{parts[3]}".encode() == VALID_CREDENTIALS:
                client_name = parts[1]
                with lock:
                    clients[client_name] = addr
                sock.sendto(b"ALLOCATED:OK", addr)
                print(f"[ALLOCATE] Client '{client_name}' registered from {addr}")
            else:
                sock.sendto(b"ERROR:401_UNAUTHORIZED", addr)
                print(f"[REJECTED] Failed login from {addr}")

        # 2. Handle Data Relaying between Peers
        elif data.startswith(b"RELAY:"):
            parts = data.split(b":", 2)
            if len(parts) == 3:
                target_name = parts[1].decode()
                payload = parts[2]
                
                with lock:
                    target_addr = clients.get(target_name)
                
                if target_addr:
                    # Forward packet to the destination peer
                    sock.sendto(b"MSG:" + payload, target_addr)
                    print(f"[RELAY] {addr} ---> {target_name} ({target_addr}) | {len(payload)} bytes")
                else:
                    sock.sendto(b"ERROR:PEER_OFFLINE", addr)

if __name__ == "__main__":
    start_server()
