

import my_function as my


#     Задание 1 Напишите программу, которая принимает на вход вещественное число # и показывает сумму его цифр.
# Пример: 6782 -> 23      0,56 -> 11
def get_sum_digit(n: str) -> int:
    """Функция принимает число в виде строки и возвращает сумму его цифр"""
    # result = 0
    # chars_list = list(n)
    # for c in chars_list:
    #     if c.isdigit():
    #         result += int(c)

    result = sum(map(int, filter(lambda x: x.isdigit(), list(n))))  # заменил цикл на лямбду с фильтром и мапом

    return result



#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def get_sum_odd_elements(input_list: int | float) -> int | float:
    """Функция считает сумму элементов, находящихся на нечетных позициях"""
    result = 0
    # n = len(input_list)
    # for i in range(n):
    #     if i % 2:
    #         result += input_list[i]

    for i, num in enumerate(input_list):  # enumerate для номера позиции
        if i % 2:
            result += num

    return result

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def string_cleaning(inp_text, inp_str: str) -> str:
    """Функция удаляет из текста слова, содержащую указанный набор символов"""
    my_list = inp_text.split()
    # temp_list = []
    # for s in my_list:
    #     if inp_str not in s:
    #         temp_list.append(s)
    # result = ' '.join(temp_list)     

    result = ' '.join(list(filter(lambda x: inp_str not in x, my_list)))  # заменил цикл на лямбду с фильтром
    return result


def difference_fractional_part(input_list: list[float], prec: int) -> float:
    """Функция считает разность между максимальной и минимальной дробной частью"""

    # min_fract = round(input_list[0] - int(input_list[0]), prec)
    # max_fract = min_fract
    # for n in input_list:
    #     fract = round(n - int(n), prec)
    #     if fract > max_fract:
    #         max_fract = fract
    #     elif fract < min_fract:
    #         min_fract = fract   

    temp_list = [round(n - int(n), prec) for n in input_list]  # в одну строку

    return round(max(temp_list) - min(temp_list), prec)



print()
while my.make_choice("Выполняем задачу (сумма цифр числа)? "):
    print()
    num = input("Введите число: ")
    sum_digit = get_sum_digit(num)
    print(f'В числе {num} сумма цифр {sum_digit}')
    print()
print()    


print()
while my.make_choice("Решаем задачу (сумма элементов на нечетных позициях)? "):
    print()
    print("Заполняем список случайными целыми числами")
#    first_list = my.fill_list_random_int()
    first_list = [2, 3, 5, 9, 3]
    print(f'Сумма элементов на нечетных позициях в списке \n {first_list} равна {get_sum_odd_elements(first_list)}')
    print()
print()
    

print()
while my.make_choice("Решаем задачу (удаление слов из текста),"):
    print()
    input_file = open("input_text.txt", "r")
    my_text = input_file.read()
    input_file.close()
    
    print("Исходный текст (из файла input_text.txt): ")
    print(my_text)
 
    outp_text = string_cleaning(my_text, "abc")
    
    print()
    print("Текст без слов с 'abc' (записан в файл output_text.txt)")
    print(outp_text)
 
    output_file = open("output_text.txt", "w")
    output_file.write(outp_text)
    output_file.close()
 
    print()
print()


print()
while my.make_choice("Решаем задачу 3 (разность дробных частей вещественных элементов)? "):
    print()
    print("Заполняем список случайными вещественными числами")
    precision = 0
    while precision < 1:
        precision = my.get_int('Введите число знаков после запятой (больше 0) : ')
    third_list = my.fill_list_random_float(precision)
   
    print(f'В списке \n {third_list} \nразница меду дробными частями равна {difference_fractional_part(third_list, precision)}')
    print()
 
print()