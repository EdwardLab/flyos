import subprocess
import getpass
import sys

sys.path.append('/flyos')
from tools import check_password
def execute_adb_shell():
    try:
        while True:
            print("Login to Android Shell")
            password = getpass.getpass("FlyOS Password: ")
            if check_password(password):
                print("Welcome to Android Shell")
                adb_command = f"adb shell"
                subprocess.run(adb_command, shell=True)
            if password == '':
                print("please provide a password")
                continue
            else:
                print("Incorrect password (Use the login password of FlyOS Dashboard)")
        
    except KeyboardInterrupt:
        execute_adb_shell()
    except MemoryError:
        print("MemoryError, retry")
    except Exception as e:
        print(f"Error :{e}")
        execute_adb_shell()
        
if __name__ == "__main__":
    execute_adb_shell()
