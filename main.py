import subprocess
import os
from os import system
from discord import discord
from cookies import cookies_parser
from cleaner import clean
from descriptions import *

def main():
    system("title " + 'LOGS HELPER by racurs') #Титульник
    total = ''
    folder_logs = r''

    while total != '0': #костыль на бэк в меню

        #Начальные слова
        print(hello1+hello2)

        #Функ меню
        def menu():
            print('''
    1. Быстрое удаление логов. 
    2. Парсер токенов Discord.
    3. Парсер cookies с логов.
    4. Чистка логов от мусора.

    0. Выход.
        ''') 
        #Вывод меню и запрос цифры
        menu()
        inp = input('Выберите один из пунктов для работы: ')
        

        #Функ быстрого удаления 
        def dell():
            subprocess.run(f'rmdir /q /s "{folder_logs}"', shell=True)

        #Выбор после завершения утилиты
        def choise():
            if total == '1':
                os.system('cls')
            else:
                exit()


        #Если 1, то быстрое удаление логов
        if inp == '1':
            os.system('cls') #os.system('cls') для чистки консоли
            print(del1 + del2 + del3)
            folder_logs = input('\nВведите папку для быстрого удаления: ')
            dell()
            total = input(finish)
            choise()


        #Если 2, парсим дс.
        elif inp == '2':
            os.system('cls')
            print(ds)
            discord()
            total = input(finish)
            choise()


        #Если 3, парсим куки
        elif inp == '3':
            os.system('cls')
            print(pars1 + pars2)
            cookies_parser()
            total = input(finish)
            choise()


        #Если 4, клининг 
        elif inp == '4':
            os.system('cls')
            print(cln1 + cln2)
            clean()
            total = input(finish)
            choise()

        #Если 0, exit()
        elif inp == '0':
            exit()

if __name__ == "__main__":
    main()