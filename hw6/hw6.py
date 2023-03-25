# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random


print('Задача 30')

a1 = int(input('Первый элемент: '))
n = int(input('Количество элементов: '))
d = int(input('Коэффициент прогрессии: '))

progr = []
progr.append(a1)

for i in range(1, n):
    progr.append(a1 + i * d)

print(progr)

def fill_list_random_int(size: int, min_n: int, max_n: int) -> list[int]:
    """Функция заполняет список случайными целыми числами"""
    result = []
    for _ in range(size):
        result.append(random.randint(min_n, max_n))
    return result

print('Задача 32')

print('Заполняем массив')
size = int(input('Размер массива: '))
min_n = int(input('Минимальный элемент массива: '))
max_n = int(input('Максимальный элемент массива: '))

my_list = []
for _ in range(size):
    my_list.append(random.randint(min_n, max_n))
print(my_list)    

print('Выбираем индексы значений, попадающих в диапазон')
min_num = int(input('Минимум диапазона: '))
max_num = int(input('Максимум диапазона: '))
for i in range(size):
    if min_num <= my_list[i] <= max_num:
       print(i, end=' ')

print()