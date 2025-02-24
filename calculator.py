import os
import time

def clea():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check():
    print('By d3f4ult')
    print('By d3f4ult')
    print('By d3f4ult')
    input('\n\nPress enter!')
    clea()

    vibr = input('1. Посчитать по курсу\n2. Прибавить комку\n99. Выход\n        >> ')

    if vibr == '1':
        kyrs = float(input('Введите курс на 1кк виртов >> '))
        chislo = float(input('Введите количество валюты (В КК) >> '))
        itog = kyrs * chislo
        clea()
        print(f'{chislo}КК - {itog} Рублей')
        time.sleep(5)
        clea()
        check()
    elif vibr == '2':
        chislo = float(input('Введите количество валюты (В КК) >> '))
        numberl = chislo * 1000000
        itog = numberl * 1.08
        itorrl = itog / 1000000
        clea()
        print(f'{chislo}КК с комиссией равно {itorrl}КК')
        time.sleep(5)
        clea()
        check()
    elif vibr == '99':
        print('Выход из программы.')
    else:
        clea()
        print('Некорректный выбор.')
        time.sleep(5)
        clea()
        check()

check()
