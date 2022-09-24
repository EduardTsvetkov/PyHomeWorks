# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from urllib import request


def MakeСhoice(question):  # определяем выполнять (повторять) задачу или переходить к следующей    print(question)
    yes_answers = ['y', 'yes', 'д', 'да']
    no_answers = ['n', 'no', 'н', 'нет']
    print(question)
    while (True):
        print("Ведите y, yes, д, да если 'ДА' либо n, no, н, нет если 'НЕТ': ")
        choice = input().lower()
        if choice in yes_answers:
            return True
        elif choice in no_answers:
            return False
        

def GetIntInResponce(request):
    while (True):
        n = input(request)
        if n.isdigit() or (n[0] == '-' and n[1:].isdigit()):
            return int(n)

        print("Это не целое число!")
        


def GetDayNumber():
    flag = True
    while flag:
        a = GetIntInResponce("Введите число от 1 до 7: ")
        
        if a < 1 or a > 7:
            print("Это не число от 1 до 7")
        else: 
            flag = False
    return a


def WhatDay(number):  # сообщаем что за день :-)
    if number == 1:
        return "Первый день недели - отходим после выходных."
    elif number == 2:
        return "Второй день недели - готовимся к работе."
    elif number == 3:
        return "Третий день недели - работаем."
    elif number == 4:
        return "Четвертый день недели - отходим после работы."
    elif number == 5:
        return "Пятый день недели - готовимся к выходным."
    elif number == 6:
        return "Шестой день недели - первый выходной!"
    elif number == 7:
        return "Седьмой день недели (а у кого-то первый) - второй выходной!"
    else:
        return "Что-то не так..."


def GetBooleanData():
    while True:
        b = GetIntInResponce("Введите 1 (True) или 0 (False): ")
        
        if b == 1:
            return True
        elif b == 0:
            return False
        else:
            print("Это не 0 и не 1.")
         
    
print()
while MakeСhoice('Решаем задачу про дни недели? '):
    day_number = GetDayNumber()
    print(WhatDay(day_number))
    print()

print()
while MakeСhoice('Решаем задачу про проверку истинности? '):
    print("Введите x")
    x = GetBooleanData()
    print()
    print("Введите y")
    y = GetBooleanData()
    print()
    print("Введите z")
    z = GetBooleanData()
    print()
    print('x =', x, 'y =', y, 'z =', z)
    print()
    if not (x or y or z) == (not x and not y and not z):
        print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это True')
    else:
        print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это False')
    print()

    print('Проверка всех возможных вариантов')
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2): 
                if not (x or y or z) == (not x and not y and not z):
                    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это True')
                else:
                    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это False')
    print()
    