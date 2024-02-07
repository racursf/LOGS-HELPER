import os
import shutil
import random
import string

def cookies_parser():
    
    def find_and_move_cookies_folder(source_dir, destination_dir):
        if not os.path.isdir(source_dir):
            print(f"Папки {source_dir} не существует.")
            return
        
        if not os.path.isdir(destination_dir):
            print(f"Папки {destination_dir} не существует.")
            return
        
        for root, dirs, files in os.walk(source_dir):
            for dir_name in dirs:
                if dir_name.lower() == "cookies":
                    cookies_dir = os.path.join(root, dir_name)
                    for file_name in os.listdir(cookies_dir):
                        source_path = os.path.join(cookies_dir, file_name)
                        file_name_without_ext, ext = os.path.splitext(file_name)
                        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                        destination_file_name = f"{file_name_without_ext}{suffix}{ext}"
                        destination_path = os.path.join(destination_dir, destination_file_name)
                        shutil.move(source_path, destination_path)
                        print(f"Файл {file_name} перемещен в {destination_file_name}")

    source_folder = input(r'Введите папку с логами: ')
    destination_folder = input(r'Введите папку для сохранения всех куков с логов: ')
    find_and_move_cookies_folder(source_folder, destination_folder)
