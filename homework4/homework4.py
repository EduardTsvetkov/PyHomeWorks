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
    """Функция возвращает простые делители числа"""
    result = []
    i = 2
    while n > 1:
        if n % i:
            i += 1
        else:
            result.append(i)
            n //= i
    return result        


def search_single_elements(input_list: list[int]) -> list[int]:
    """Функция исчет в списке элементы в единственном числе и возвращает их список"""
    elements_dct = {}
    for n in input_list:
        if n not in elements_dct:
            elements_dct[n] = input_list.count(n)
    result = []        
    for d in elements_dct:
        if elements_dct[d] == 1:
            result.append(d)
           
    return sorted(result) 


def fill_dict_random_int(max_key: int, min_rand = -99, max_rand = 99) -> dict:
    """Функция заполняет словарь (key от 0 до max_key) случайными целыми числами"""
    result = {}
    for k in range(max_key + 1):
        result[k] = randint(min_rand, max_rand)
    
    return result


def get_polinom_koeff(s: str) -> dict:
    """Функция возвращает словарь коэффициентов многочлена для каждой степени"""
    s = s.replace("+ ", "")
    s = s.replace("- ", "-")
    s = s.replace(" = 0", "")
    s = s + "*x^0"
    result = {}
    for x in s.split():
        member = x.split("*x^")
        result[int(member[1])] = int(member[0])
 
    return result 


def sum_dict_values(d1: dict, d2: dict) -> dict:
    """Функция суммирует значения двух словарей по соответствующим ключам"""
    result = d1.copy()
    for k in d2:
        if d1.get(k) is None:
            result[k] = d2[k]
        else:
            result[k] = d1[k] + d2[k]
 
    return result
 
def polinom_from_dict(input_d: dict) -> str:
    """Фунция возвращает строку с многочленом, коэффициенты которого в словаре"""
    max_degree = max(input_d.keys())
    member_list = []
    for i in range(max_degree, -1, -1):
        k = input_d[i]
        if i == max_degree:
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
    print()
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
    print()
    num = abs(my.get_int("Введите целое число: "))
    devisors = get_prime_devisors(num)
    print(f"Простые делители числа {num}:")
    print(devisors)
    print()
print()


print()
while my.make_choice("Решаем задачу 3 (поиск единственных элементов)? "):
    print()
    first_list = my.fill_list_random_int()
    single_list = search_single_elements(first_list)
    print(f"В списке: {first_list}")
    print(f"в единственном экземпляре: {single_list}")
    print()
print()


print()
while my.make_choice("Решаем задачу 4 (многочлен)? "):
    print()
    print("Создаем два многочлена и сохраняем в файлы (для следующего задания).")
    degree1 = abs(my.get_int("Введите степень первого многочлена (положительное целое число): "))
    polinom1 = polinom_from_dict(fill_dict_random_int(degree1, -9, 9))
    file1 = open("polinom1.txt", "w")
    file1.write(polinom1)
    file1.close()
    print(f"{polinom1} -> сохранен в файл 'polinom1.txt'")
    
    degree2 = abs(my.get_int("Введите степень второго многочлена (положительное целое число): "))
    polinom2 = polinom_from_dict(fill_dict_random_int(degree2, -9, 9))
    file2 = open("polinom2.txt", "w")
    file2.write(polinom2)
    file2.close()
    print(f"{polinom2} -> сохранен в файл 'polinom2.txt'")
    print()
print()


print()
while my.make_choice("Решаем задачу 5 (сложение многочленов)? "):
    print()
    print("Берем из файлов (созданных в предыдущем задании) многочлены")
    print("и суммируем их.")
    file1 = open("polinom1.txt", "r")
    polinom_1 = file1.read()
    file1.close()
    file2 = open("polinom2.txt", "r")
    polinom_2 = file2.read()
    file2.close()
    
    print("Сумма многочленов:")
    print(polinom_1)
    koef_1 = get_polinom_koeff(polinom_1)
    print(polinom_2)
    koef_2 = get_polinom_koeff(polinom_2)
    print("равна")
    
    sum_koeff = sum_dict_values(koef_1, koef_2)
    print(polinom_from_dict(sum_koeff))
    print()
print()
