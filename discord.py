import os
import asyncio
from os import system
from time import gmtime, strftime

def discord():
    system("title " + 'DISCORD PARSER')

    path = input('Введите путь к папке с логами: ')
    a = list(filter(os.path.isdir, [f'{path}/' + x for x in os.listdir(path)]))
    all_tokens = []
    for i in a:
        file = os.listdir(i)
        print(f'Open {i.replace(f"{path}/", "")}')
        if 'Discord' in file:
            filetokens = os.listdir(f'{i}/Discord')
            if 'Tokens.txt' in filetokens:
                with open(f"{i}/Discord/Tokens.txt", 'r', encoding="utf-8") as f:
                    gg = [g.replace('\r', '') for g in f.readlines()]
                    if len(gg) > 0:
                        print(f'Найдено {len(gg)} токенов')
                        all_tokens += gg
                    else:
                        print('Найдено 0 токенов')
            else:
                continue

        elif 'Other' in file:
            othres = os.listdir(f"{i}/Other")
            if 'Discord Token(s).txt' in othres:
                print(i)
                with open(f"{i}/Other/Discord Token(s).txt", 'r', encoding="utf-8",errors='ignote') as f:
                    try:
                        gg = [g.replace('\r', '') for g in f.readlines() if "Discord не установлен!" and " " and "?" not in g.replace('\r', '') and len(g.replace('\r', '').replace(',','')) == 60]
                    except Exception as e:
                        print(f'ОШИБКА {e}\n{i}')
                    else:
                        if len(gg) > 0:
                            print(f'Найдено {len(gg)} токенов')
                            all_tokens += gg
                        else:
                            print('Найдено 0 токенов')

        else:
            print('Найдено 0 токенов')
        system("title " + f'Discord parser by @racursbtw \\  Tokens: {len(all_tokens)}')





    result = list(set(all_tokens))




    if not result:
        print(f'\nФинальный результат: \nНайдено 0 токенов')
    else:
        print(f'\nРезультат с дублями: \nНайдено {len(all_tokens)} токенов ')
        with open(f'tokens.txt', 'w') as f:
            for i in result:
                f.write(i)
        print(f'Финальный результат: \nНайдено {len(result)} токенов ')
