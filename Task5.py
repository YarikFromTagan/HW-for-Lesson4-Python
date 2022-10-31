# Заны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0

import itertools
import os
os.system('cls')

def polyToDict(poly): # полином в словарь из показателей степени и коэффициентов
    poly = poly.replace(' = 0', '')
    if poly[-1] != 'x':
        poly = poly + ' 0'
    if poly[-5] == 'x':
        poly = poly.replace(' 0', '')
    poly = '|' + poly
    poly = poly.replace(' - ', '|-')
    poly = poly.replace(' + ', '|')
    poly = poly.replace('-x^', '-1 ')
    poly = poly.replace('x^', ' ')
    poly = poly.replace('| ', '|1 ')
    poly = poly.replace('-x', '-1 1')
    poly = poly.replace('x', ' 1')
    poly = poly.replace('| ', '|')
    poly = poly.replace('|', '', 1)
    poly = poly.split('|')
    poly = [char.split(' ') for char in poly]
    tuple_poly = [tuple(int(i) for i in j) for j in poly]
    dict_poly = {tuple_poly[i][1]: tuple_poly[i][0] for i in range(0, len(tuple_poly))}
    return dict_poly

def fold_dict(dict1, dict2): # сложение значений словарей с одинаковыми ключами
    res = dict1.copy()
    for i in dict2.keys():
        if i in res.keys():
            res[i] += dict2[i]
        else:
            res[i] = dict2[i]
    #print(res, '\n')
    return res

def create_poly(tupl): # из кортежа показателей степени и коэффициентов собираем полином
    var = ['x^'] * len(tupl)
    coefs = [x[1] for x in tupl]
    degrees = [x[0] for x in tupl]
    new_pol = [[int(a), str(b), int(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))


with open('cond1.txt', 'r') as f:
    a = f.read()
print(a, '\n')
dict1 = polyToDict(a)

with open('cond2.txt', 'r') as f:
    b = f.read()
print(b, '\n')
dict2 = polyToDict(b)

sum_dict = fold_dict(dict1, dict2)
temp = sum_dict.copy()
for i in temp.keys():
    if temp[i] == 0:
        del sum_dict[i]

tupl = sorted(sum_dict.items(), key=lambda x: -x[0]) # сумму словарей в кортеж

new_poly = create_poly(tupl)
# убираем артефакты
new_poly = new_poly.replace('+ -', '- ')
new_poly = new_poly.replace('x^0', '')
new_poly = new_poly.replace('- 1x', '- x')
new_poly = new_poly.replace('+ 1x', '+ x')
new_poly = new_poly.replace('x^1', 'x')

print(new_poly, '\n')

with open('file_Task5.txt', 'w') as data:
        data.write(new_poly)
