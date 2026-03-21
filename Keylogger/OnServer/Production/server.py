import socket 

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(('0.0.0.0', 5001))
    server.listen(5)
    print('Receiver is waiting for a connection...')
    
    conn, addr = server.accept()
    print(f"connected to {addr}")
    # received_bytes = ""
    
    while True:
        with open(r'C:\\ftp_files\\received_file.txt', 'wb') as f:
            data = conn.recv(1024)
            # print("Data received successfully!")
            f.write(data)
            break
                # bytes_2_str = str(data)
            # if not data:
            #     break
                # print(type(bytes_2_str))
                # f.write(received_bytes)
            # break 
    print("File received successfully!")
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
