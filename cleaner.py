import os
from os import system
import shutil
def clean():
    system("title " + 'LOGS CLEANER')
    folder_path = input('Введите папку с логами для чистки: ')
    ext = ['.vdf', '.bak', '.bat', '.png', '.jpeg', '.jpg', '.ico', '.gif', '.svg', '.mp3', '.mp4', '.py', '.avi', '.pdf', '.wav', '.mkv', '.mpg', '.mov', '.3gp', '.js', '.exe', '.rar', '.zip', '.7z', '.cab', '.dll', '.sys', '.msc', '.lnk', '.scr', '.bin', '.url', '.cmd', '.vbs', '.jar', '.jse', '.chm', '.iso', '.torrent', '.tmp', '.php', '.apk', '.ahk', '.scr', '.cab', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pot', '.potx', '.pps', 'ppsx', '.rtf', '.odt']

    def delete_files_with_extensions(folder_path, extensions):
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file_path.endswith(ext) for ext in extensions):
                    os.remove(file_path)
    delete_files_with_extensions(folder_path, ext)
