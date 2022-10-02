# Урок 3. Данные, функции и модули в Python
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

from random import randint

def make_choice(question: str) -> bool:
    """Возвращаем ответ на вопрос: True - если 'да', False - если 'нет'"""  
    yes_answers = ['y', 'yes', 'д', 'да']
    no_answers = ['n', 'no', 'н', 'нет']
    print(question)
    while (True):
        choice = input("Ведите y,yes,д,да если 'ДА' либо n,no,н,нет если 'НЕТ': ").lower()
        if choice in yes_answers:
            return True
        elif choice in no_answers:
            return False


def get_int(request: str) -> int:
    """Функция возвращает целое число, введенное с клавиатуры"""
    while (True):
        n = input(request)

        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)

        print('\033[31mЭто не целое число!\033[37m')


def fill_list_random_int() -> list[int]:
    """Функция заполняет список случайными целыми числами"""
    size = 0
    while size < 1:
        size = get_int('Введите размер заполняемого списка (положительное число): ')
    min_n = get_int('Введите минимальное значение элементов списка: ')
    max_n = min_n - 1
    while max_n < min_n:
        max_n = get_int(f'Введите максимальное значение элементов списка (больше {min_n}): ')
    result = []
    for _ in range(size):
        result.append(randint(min_n, max_n))
    return result


def get_sum_odd_elements(input_list: int | float) -> int | float:
    """Функция считает сумму элементов, находящихся на нечетных позициях"""
    result = 0
    n = len(input_list)
    for i in range(n):
        if i % 2:
            result += input_list[i]
    return result


def get_multiplication_elements(input_list: int | float) -> list[int | float]:
    """Функция считает произведения элементов, находящихся одинаковых позициях с концов списка"""
    result = []
    n = -(-len(input_list) // 2)  # чтоб при нечетных центральный умножить сам на себя
    for i in range(n):
            result.append(input_list[i] * input_list[-(i + 1)])
    return result


print()
while make_choice("Решаем задачу 1 (сумма элементов на нечетных позициях)? "):
    print()
    print("Заполняем список случайными целыми числами")
    first_list = fill_list_random_int()
    print(f'Сумма элементов на нечетных позициях в списке \n {first_list} равна {get_sum_odd_elements(first_list)}')
    print()        


print()
while make_choice("Решаем задачу 2 (произведение пар чисел списка)? "):
    print()
    print("Заполняем список случайными целыми числами")
    second_list = fill_list_random_int()
    print(f'Произведение элементов списка \n {second_list} -> {get_multiplication_elements(second_list)}')
    print()        


