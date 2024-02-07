import subprocess
import os
from os import system
from discord import discord
from termcolor import colored
from cookies import cookies_parser
from cleaner import clean

system("title " + 'LOGS HELPER by racurs') #Титульник

#Начальные слова
print(colored('Добро пожаловать в скрипт-помощник в работе с логами!', 'green'))
print(colored('Если у Вас будут какие-то вопросы или советы, можете обращаться в тг бота: @racursbtw_bot или в ЛС на форуме', 'magenta'))

#Функция менюшки
def menu():
    print('''
1. Быстрое удаление логов. 
2. Парсер токенов Discord.
3. Парсер cookies с логов.
4. Чистка логов от мусора.
''')
    
#Вывод меню и запрос цифры
menu()
inp = input('Выберите один из пунктов для работы: ')
folder_logs = r''

#Фун быстрого удаления 
def dell():
    try:
        subprocess.run(f'rmdir /q /s "{folder_logs}"', shell=True)
        print("Команда выполнена успешно.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")



#Если 1, то быстрое удаление логов
if inp == '1':
    os.system('cls') #os.system('cls') для чистки консоли
    print(colored("Данная утилита ускоряет удаление папки с логами.", 'yellow'))
    print(colored("Отдельная благодарнсоть: https://zelenka.guru/topchek/", 'green'))
    print(colored("\nP.S. Проверяйте удаляемую папку, т.к. она удалится без подтверждения и безвозвратно!", 'red'))
    print('\nВведите папку для быстрого удаления:')
    folder_logs = input()
    dell()

#Если 2, парсим дс.
elif inp == '2':
    os.system('cls')
    print(colored("Данная утилита парсит токены discord с логов.\nСамописный софт, который работает с несколькими стиллерами\n", 'green'))
    discord()

#Если 3, парсим куки
elif inp == '3':
    os.system('cls')
    print(colored("Данная утилита парсит ВСЕ куки с логов в указанную Вами папку.\n", 'green'))
    print(colored("P.S. Скрипт именно перемещает куки в указанную папку, а не копирует их!\n", 'red'))
    cookies_parser()

#Если 4, клининг 
elif inp == '4':
    os.system('cls')
    print(colored("Данная утилита предназначена для чистки логов от мусора.", 'green'))
    print(colored("А точнее, скрипт удаляет мусорные расширения из логов, по типу: .exe .rar .bat и тд\n", 'green'))
    clean()

#Сворачиваемся
input('\nРабота завершена. Нажмите любую клавишу для закрытия.')