from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

# Define the directory where files will be uploaded (must exist)
UPLOAD_DIR = r"C:\ftp_files"  # Change to your desired path

# Create the authorizer (handles user authentication)
authorizer = DummyAuthorizer()
authorizer.add_user("yashbanait", "yash@6123", UPLOAD_DIR, perm="elradfmw")  # Permissions: e=change dir, l=list, r=read, a=append, d=delete, f=rename, m=make dir, w=write

# Create the handler
handler = FTPHandler
handler.authorizer = authorizer

# Create and start the server
server = FTPServer(("10.26.87.162", 21), handler)  # Listens on all interfaces (use System B's IP if needed), port 21
print(f"FTP server started on port 21. Upload directory: {UPLOAD_DIR}")
server.serve_forever()