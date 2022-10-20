# Задайте последовательность цифр. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import os
os.system("cls")

lst = list(input('---> '))
print('\n')
r_lst = lst.copy()
for i in range(len(lst)):
     lst[i] = int(lst[i])

lst.sort()

res = []
k = None
for i in range(len(lst)-1):
    if lst[i] != lst[i+1] and lst[i] != k:
        res.append(lst[i])
    else:
        k = lst[i]
if lst[-1] != lst[-2]:
    res.append(lst[-1])

print(f"{''.join(r_lst)} -> {res}")
print('\n')
