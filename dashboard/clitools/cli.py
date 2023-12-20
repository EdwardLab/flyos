from rich import print
from rich.text import Text
from rich.console import Console
from rich.markdown import Markdown
import os
import sys
import getpass
from werkzeug.security import generate_password_hash
console = Console()
console.print("Welcome to FlyOS CLI Tools", style='bold green')
print("This tool can help you manage and maintain your FlyOS subsystem")
import cmd
sys.path.append('/flyos')
from tools import check_password
def login_flyoscli_shell():
    try:
        while True:
            print("Login to FlyOS CLI Tools\n")
            password = getpass.getpass("FlyOS Password: ")
            if check_password(password):
                flycmd = FlyOSCmd()
                flycmd.cmdloop("Welcome to the FlyOS CLI Tools")
            if password == '':
                print("please provide a password")
                continue
            else:
                print("Incorrect password (Use the login password of FlyOS Dashboard)")
        
    except KeyboardInterrupt:
        login_flyoscli_shell()
    except MemoryError:
        print("MemoryError, retry")
    except Exception as e:
        print(f"Error :{e}")
        login_flyoscli_shell()

class FlyOSCmd(cmd.Cmd):
    prompt = "flyos > "

    def do_passwd(self, line):
        """Change Linux User Password"""
        os.system("passwd")

    def do_flypasswd(self, line):
        """Change FlyOS Login (Dashboard) Password"""
        passwd = getpass.getpass("New FlyOS password: ")
        passwd_check = getpass.getpass("Retype new password: ")
        if passwd != passwd_check:
            print("Password do not match, Please try again")
            print("Password unchanged")
            return True
        hashpwd = generate_password_hash(passwd)
        
        file_path = '/flyos/files/pwd.conf'
        try:
            with open(file_path, 'w') as pwd_file:
                pwd_file.write(hashpwd)
            print("Password changed")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def do_quit(self, line):
        """Exit the application."""
        print("Quit!")
        return True

if __name__ == "__main__":
    login_flyoscli_shell()