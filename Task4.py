# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
#

import random
import os
os.system('cls')

def write_file(st):
    with open('file_Task5.txt', 'w') as data:
        data.write(st)

def rnd(): # случайный коэффициент из заданного диапазона
    return random.randint(-100,101)

def create_coeff(k): # список случайных коэффициентов
    lst = [rnd() for i in range(k+1)]
    # print(lst, '\n')
    return lst

def create_poly(lst): # полином из списка коэффициентов
    str = ''
    if len(lst) < 1:
        str = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                if lst[i] == 1:
                    str += f'x^{len(lst) - 1 - i}'
                    str += ' + '
                else:
                    str += f'{lst[i]}x^{len(lst) - 1 - i}'
                    str += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                if lst[i] == 1:
                    str += 'x'
                else:
                    str += f'{lst[i]}x'
                    if lst[i+1] != 0:
                        str += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                str += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                 str += ' = 0'
# уберём артефакты
        if lst[len(lst) - 1] == 0 and lst[len(lst) - 2] == 0:
            str = str[:-7] + ' = 0'
        str = str.replace('+ -', '- ')
        str = str.replace('-1x', '-x')
        str = str.replace('- 1x', '- x')
    return str

k = int(input("Введите натуральную степень k = "))
print('\n')

coeff = create_coeff(k)
print(create_poly(coeff), '\n')

write_file(create_poly(coeff))