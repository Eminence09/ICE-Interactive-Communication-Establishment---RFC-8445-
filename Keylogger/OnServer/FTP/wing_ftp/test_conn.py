import ftplib
FTP_HOST = "127.0.0.1"  # Replace with actual
FTP_USER = "yashbanait"
FTP_PASS = "yash@6123"
try:
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    print("Connected successfully")
    ftp.quit()
except Exception as e:
    print(f"Error: {e}")