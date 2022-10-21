# Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.

import os
os.system('cls')

n = int(input('Введите число: '))
print('\n')

res = []
i = 2
k = n

while i * i <= n:
    
    while n % i == 0:
        res.append(i)
        n = n // i
        #print(n)
    i = i + 1

if n > 1:
    res.append(n)

print(f'{res} --> список простых множителей числа {k}')
print('\n')