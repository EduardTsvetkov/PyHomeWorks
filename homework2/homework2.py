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



def make_choice(question: str) -> bool:  # определяем выполнять (повторять) задачу или переходить к следующей    print(question)
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
    while (True):
        n = input(request)

        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)

        print('\033[31mЭто не целое число!\033[37m')


def get_sum_digit(n: str) -> int:
    result = 0
    chars_list = list(n)    
    for c in chars_list:
        if c.isdigit():
            result += int(c)
    return result      
    

def factorial(n: int) -> int:  # вспомним рекурсию :-)
    if n == 1:
        return n
    else: 
        return n * factorial(n - 1)


def check_sum_elements(list_of_number: list[int | float]) -> int | float:
    result = 0 
    for n in list_of_number:
        result += n
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
    n_factorial = get_int('Введите целое число: ')
    factorial_list = [factorial(i) for i in range(1, n_factorial + 1)]
    print(factorial_list)
    print()


print()
while make_choice("Выполняем задачу 3 (сумма элементов последовательности)? "):
    elements = get_int('Введите целое число элементов: ')
    my_list = [(1 + 1 / i)**i for i in range(1, elements + 1)]
    sum_elements = check_sum_elements(my_list)
    print("В списке")
    print(my_list)
    print(f'Сумма элементов приблизительно равна {round(sum_elements, 3)}')
    print()