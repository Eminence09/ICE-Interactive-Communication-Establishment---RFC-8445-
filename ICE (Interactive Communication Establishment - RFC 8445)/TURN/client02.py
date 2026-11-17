import socket
import threading

SERVER_IP = "10.158.86.162"  # Change to Windows LAN IP if running on another device
SERVER_PORT = 3478
MY_NAME = "client2"
PEER_NAME = "client1"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    while True:
        try:
            data, _ = sock.recvfrom(4096)
            if data.startswith(b"MSG:"):
                print(f"\n[{PEER_NAME}]: {data[4:].decode()}\nYou: ", end="")
            else:
                print(f"\n[Server]: {data.decode()}\nYou: ", end="")
        except Exception:
            break

auth_packet = f"REGISTER:{MY_NAME}:yash:123".encode()
sock.sendto(auth_packet, (SERVER_IP, SERVER_PORT))

threading.Thread(target=receive_messages, daemon=True).start()

print(f"Connected as {MY_NAME}. Type messages to send to {PEER_NAME}:")
while True:
    msg = input("You: ")
    if msg:
        relay_packet = f"RELAY:{PEER_NAME}:{msg}".encode()
        sock.sendto(relay_packet, (SERVER_IP, SERVER_PORT))
