from werkzeug.security import generate_password_hash
passwd = 'flyos'
hashpwd = generate_password_hash(passwd)
file_path = '/flyos/files/pwd.conf'
try:
    with open(file_path, 'w') as pwd_file:
        pwd_file.write(hashpwd)
        print("Password changed")
except Exception as e:
        print(f"Error writing to file: {e}")