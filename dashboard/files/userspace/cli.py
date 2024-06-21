import argparse
import os
CONTAINERROOT = '/container/userspace'
def mount_userspace():
    os.system("nohup bash /flyos/files/userspace/start.sh >> /flyos/logs/userspace_start.log 2>&1 &")
def umount_userspace():
   os.system("nohup bash /flyos/files/userspace/stop.sh >> /flyos/logs/userspace_stop.log 2>&1 &")
def userspace_execute(cmd=''):
    if not cmd:
        cmd = '/usr/bin/login'
    try:
        os.system(f'chroot /container/userspace /bin/bash -c "source /etc/profile;  {cmd}"')
    except FileNotFoundError as e:
        print(e)

def userspace_start():
    try:
        mount_userspace()
        print('Userspace started.')
    except FileNotFoundError as e:
        print(e)

def userspace_stop():
    try:
        umount_userspace()
        print('Userspace stopped.')
    except FileNotFoundError as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='CLI for managing userspace container')
    parser.add_argument('action', choices=['login', 'start', 'stop', 'cmd'],
                        help='Action to perform on the container')
    parser.add_argument('--cmd', help='Command to execute within the container')

    args, unknown = parser.parse_known_args()

    if args.action == 'login':
        userspace_execute()
    elif args.action == 'start':
        userspace_start()
    elif args.action == 'stop':
        userspace_stop()
    elif args.action == 'cmd':
        cmd = ' '.join([args.cmd] + unknown)
        userspace_execute(cmd)

if __name__ == "__main__":
    main()
