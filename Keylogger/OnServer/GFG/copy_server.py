import socket

if __name__ == '__main__':
    # Defining Socket
    host = '127.0.0.1'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    # Establishing Connections
    print('Initiating clients')
    
    conn, addr = sock.accept()

    print('Connected with client')

    data = conn.recv(1024).decode()
    print(data)
    
    # Creating a new file at server end and writing the data
    
    filename = 'output.txt'
    
    fo = open(filename, "w")
    fo.write(data)

    print()
    print('Receiving file from client')
    print()
    print('Received successfully! New filename is:', filename)
    fo.close()
    
    # Cosing all Connections
    sock.close()