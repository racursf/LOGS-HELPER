import os
from os import system
from tqdm import tqdm, tqdm_gui
from extensions import extension
def clean():
    system("title " + 'LOGS CLEANER')
    folder_path = input('Введите папку с логами для чистки: ')
    ext = extension

    def delete_files_with_extensions(folder_path, extensions):
        deleted_files = 0
        with tqdm(total=len(extensions), desc="Удаление файлов", unit=' files') as pbar:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if any(file_path.endswith(ext) for ext in extensions):
                        os.remove(file_path)
                        deleted_files += 1
                        pbar.update(1)
        print(f"Удалено {deleted_files} файлов.")

    delete_files_with_extensions(folder_path, ext)