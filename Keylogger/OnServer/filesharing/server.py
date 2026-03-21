import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(('0.0.0.0', 5001))
    server.listen(1)
    print('Receiver is waiting for a connection...')
    
    conn, addr = server.accept()
    print(f"connected to {addr}")
    
    with open(r'C:\ftp_files\received_file.txt', 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            
    print("File received successfully!")
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
