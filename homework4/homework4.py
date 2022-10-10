# 1 Вычислить число π c заданной точностью d
# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]

# 3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.


import my_function as my
from random import randint


def get_pi(k: int) -> float:
    """Функция вычисляет число pi с заданным количеством знаков после запятой"""
    pi_ = 4
    n = 1
    delta = 1
    precision = 10**(-k)
    while True:
        delta = ((1 / (2 * n + 1))*(-1)**n) * 4
        if abs(delta) < precision:
            break

        pi_ = pi_ + delta
        n += 1

    return round(pi_, k)


def get_prime_devisors(n: int) -> list[int]:
    result = []
    i = 2
    while n > 1:
        if n % i:
            i += 1
        else:
            result.append(i)
            n //= i
    return result        


def get_polinom(n: int) -> str:
    member_list = []
    for i in range(n, -1, -1):
        k = randint(-100, 100)
        if i == n:
            member_list.append(f"{k}*x^{i} ")
            continue
        
        if k > 0:
            member_list.append("+ ")
        elif k < 0:
            member_list.append("- ")
        else:
            continue
        if i == 0:
            member_list.append(f"{abs(k)} ")
        else:
            member_list.append(f"{abs(k)}*x^{i} ")
        
    member_list.append("= 0")
    return ''.join(member_list)


print()
while my.make_choice("Решаем задачу 1 (вычисление числа pi)? "):
    d = 11
    print("Введите точность расчетов (число знаков после запятой): ")
    print("(при числах, больших 7 - считает долго...)")
    while d < 1 or d > 10:
        d = my.get_int("(введите целое число от 1 до 10): ")
    print(f"Число pi с точностью до {d} знаков после запятой:")
    print(get_pi(d))
    print()
print()


print()
while my.make_choice("Решаем задачу 2 (список простых множителей)? "):
    num = abs(my.get_int("Введите целое число: "))
    devisors = get_prime_devisors(num)
    print(f"Простые делители числа {num}:")
    print(devisors)
    print()
print()


print()
while my.make_choice("Решаем задачу 4 (многочлен)? "):
    
    degree = abs(my.get_int("Введите степень первого многочлена (положительное целое число): "))
    polinom1 = get_polinom(degree)
    file1 = open("polinom1.txt", "w")
    file1.write(polinom1)
    file1.close()
        
    print(f"{polinom1} сохранен в файл 'polinom1.txt'")
    
    degree = abs(my.get_int("Введите степень первого многочлена (положительное целое число): "))
    polinom2 = get_polinom(degree)
    file2 = open("polinom2.txt", "w")
    file2.write(polinom2)
    file2.close()
    print(f"{polinom2} сохранен в файл 'polinom2.txt'")