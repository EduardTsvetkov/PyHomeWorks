#     Задание 1 Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Задание 2 Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

# Задание 5 Реализуйте алгоритм перемешивания списка.

import random


def make_choice(question: str) -> bool:
    """Возвращаем ответ на вопрос: True - если 'да', False - если 'нет'"""  
    yes_answers = ['y', 'yes', 'д', 'да', 'lf', 'нуы', 'l']
    no_answers = ['n', 'no', 'н', 'нет', 'ytn', 'тщ', 'т']
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


def get_sum_digit(n: str) -> int:
    """Функция принимает число в виде строки и возвращает сумму его цифр"""
    result = 0
    chars_list = list(n)
    for c in chars_list:
        if c.isdigit():
            result += int(c)
    return result


def factorial(n: int) -> int:  # вспомним рекурсию :-)
    """Функция возвращает факториал числа"""
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def check_sum_elements(list_of_number: list[int | float]) -> int | float:
    """Функция возвращает сумму элементов списка чисел"""
    result = 0
    for n in list_of_number:
        result += n
    return result


def fill_list_random_int(size: int, min_n: int, max_n: int) -> list[int]:
    """Функция заполняет список случайными целыми числами"""
    result = []
    for _ in range(size):
        result.append(random.randint(min_n, max_n))
    return result


def fill_list(limit: int) -> list[int]:
    """Функция заполняет список целыми числами с шагом 1"""
    result = [i for i in range(-limit, limit + 1)]
    return result


def mixing_list(inp_list: list[int | float | str]) -> list[int | float | str]:
    """Функция перемешивает список"""
    result = [n for n in inp_list]  # иначе меняет исходный список :-(
    l = len(result)
    for _ in range(1000):
        i = random.randrange(0, l)
        j = random.randrange(0, l)
        result[i], result[j] = result[j], result[i]
    return result


print()
while make_choice("Выполняем задачу 1 (сумма цифр)? "):
    print()
    num = input("Введите число: ")
    sum_digit = get_sum_digit(num)
    print(f'В числе {num} сумма цифр {sum_digit}')
    print()


print()
while make_choice("Выполняем задачу 2 (факториалы)? "):
    print()
    n_factorial = get_int('Введите целое число: ')
    factorial_list = [factorial(i) for i in range(1, n_factorial + 1)]
    print(factorial_list)
    print()


print()
while make_choice("Выполняем задачу 3 (сумма элементов последовательности)? "):
    print()
    elements = get_int('Введите целое число (количество элементов): ')
    my_list = [(1 + 1 / i) ** i for i in range(1, elements + 1)]
    sum_elements = check_sum_elements(my_list)
    print("В списке")
    print(my_list)
    print(f'Сумма элементов приблизительно равна {round(sum_elements, 3)}')
    print()


print()
while make_choice("Выполняем задачу 4 (умножение элементов списка)? "):
    print()
    N = get_int("Введите целое число N (список от -N до N): ")
    list1 = fill_list(N)
    list_size = N * 2 + 1
    print('Введите номера элементов для перемножения')
    num1 = -1
    num2 = -1
    while num1 < 0 or num1 > list_size:
        num1 = get_int(f"Введите первый номер (от 1 до {list_size}): ")
    while num2 < 0 or num2 > list_size: 
        num2 = get_int(f"Введите второй номер (от 1 до {list_size}): ")

    print('В списке')
    print(list1)
    print(f'умножение элемента №{num1} ( {list1[num1 - 1]} ) на элемент №{num2} ( {list1[num2 - 1]} ) '
          f'даёт {list1[num1 - 1] * list1[num2 - 1]}')
    print()

print()
while make_choice("Выполняем задачу 5 (перемешивание списка)? "):
    print()
    size = get_int('Введите размер заполняемого массива: ')
    min_element = get_int('Введите минимальное значение элементов массива: ')
    max_element = min_element - 1
    while max_element < min_element:
        max_element = get_int(f'Введите максимальное значение элементов массива (больше {min_element}): ')
    input_list = fill_list_random_int(size, min_element, max_element)
    output_list = mixing_list(input_list)
    print('Исходный список:')
    print(input_list)
    print('Перемешаный список:')
    print(output_list)
    print()
    