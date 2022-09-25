# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.


# Цвета: \033[32m - зеленый, \033[37m - белый, \033[31m - красный


def MakeСhoice(question):  # определяем выполнять (повторять) задачу или переходить к следующей    print(question)
    yes_answers = ['y', 'yes', 'д', 'да', 'lf', 'нуы', 'l']
    no_answers = ['n', 'no', 'н', 'нет', 'ytn', 'тщ', 'т']
    print(question)
    while (True):
        choice = input("Ведите y,yes,д,да если 'ДА' либо n,no,н,нет если 'НЕТ': ").lower()
        if choice in yes_answers:
            return True
        elif choice in no_answers:
            return False
        

def GetIntInResponce(request):
    while (True):
        n = input(request)

        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)

        print('\033[31mЭто не целое число!\033[37m')
        

def GetDayNumber():
    flag = True
    while flag:
        a = GetIntInResponce("Введите число от 1 до 7: ")
        
        if a < 1 or a > 7:
            print("\033[31m Это не число от 1 до 7 \033[37m")
        else: 
            flag = False
    return a


def WhatDay(number):  # сообщаем что за день :-)
    if number == 1:
        return "Понедельник - отходим после выходных."
    elif number == 2:
        return "Вторник - готовимся к работе."
    elif number == 3:
        return "Среда - работаем."
    elif number == 4:
        return "Четверг - отходим после работы."
    elif number == 5:
        return "Пятница - готовимся к выходным."
    elif number == 6:
        return "Суббота - первый выходной!"
    elif number == 7:
        return "Воскресенье - второй выходной!"
    else:
        return "Что-то не так..."


def GetKvadrantNumber():
    flag = True
    while flag:
        a = GetIntInResponce("Введите номер квадранта (от 1 до 4): ")
        
        if a < 1 or a > 4:
            print("\033[31mЭто не число от 1 до 4\033[37m")
        else: 
            flag = False
    return a


# def GetBooleanData():
#     while True:
#         b = GetIntInResponce("Введите 1 (True) или 0 (False): ")        
#         if b == 1:
#             return True
#         elif b == 0:
#             return False
#         else:
#             print("Это не 0 и не 1.")
         
    
print()
while MakeСhoice('1. Решаем задачу про дни недели? '):
    print()
    day_number = GetDayNumber()
    print('\033[32m', WhatDay(day_number))
    print('\033[37m')

print()
while MakeСhoice('2. Решаем задачу про проверку истинности? '):
    print()
    # print("Введите x")
    # x = GetBooleanData()
    # print()
    # print("Введите y")
    # y = GetBooleanData()
    # print()
    # print("Введите z")
    # z = GetBooleanData()
    # print()
    # print('x =', x, 'y =', y, 'z =', z)
    # print()
    # if not (x or y or z) == (not x and not y and not z):
    #     print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это True')
    # else:
    #     print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} - это False')
    # print()

    print('Проверка всех возможных вариантов')
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]: 
                if not (x or y or z) == (not x and not y and not z):
                    print(f'\033[32m ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  -  это True \033[37m')
                else:
                    print(f'\033[31m ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  -  это False \033[37m')
    print()
print()   

while MakeСhoice('3. Решаем задачу квадрант по координатам?'):
    print()
    X = 0
    Y = 0
    while not X:  # Если X = 0, то повторяем ввод
        X = GetIntInResponce('Введите координату X (целое число, отличное от 0): ')
    while not Y:  # Если Y = 0, то повторяем ввод
        Y = GetIntInResponce('Введите координату Y (целое число, отличное от 0): ')

    if X > 0:
        if Y > 0:
            print(f'\033[32m Точка с координатами ({X};{Y}) находится в I квадранте.')
        else:
            print(f'\033[32m Точка с координатами ({X};{Y}) находится в IV квадранте.')
    else: 
        if Y > 0:
            print(f'\033[32m Точка с координатами ({X};{Y}) находится в II квадранте.')
        else:
            print(f'\033[32m Точка с координатами ({X};{Y}) находится в III квадранте.')   
    print('\033[37m')
print()               

while MakeСhoice('4. Решаем задачу координаты по квадранту?'):
    print()
    kvadrant = GetKvadrantNumber()
    if kvadrant == 1:
        print(f'\033[32m В {kvadrant} квадранте у точек X > 0 и Y > 0')
    elif kvadrant == 2:
        print(f'\033[32m В {kvadrant} квадранте у точек X < 0, а Y > 0')
    elif kvadrant == 3:
        print(f'\033[32m В {kvadrant} квадранте у точек X < 0 и Y < 0')
    else:
        print(f'\033[32m В {kvadrant} квадранте у точек X > 0, а Y < 0')
    print('\033[37m')
print()

while (MakeСhoice('5. Решаем задачу расстояние между точками?')):
    print()
    print('Введите координаты точки A:')
    a_X = GetIntInResponce('Введите координату X (целое число): ')
    a_Y = GetIntInResponce('Введите координату Y (целое число): ')
    print('Введите координаты точки B:')
    b_X = GetIntInResponce('Введите координату X (целое число): ')
    b_Y = GetIntInResponce('Введите координату Y (целое число): ')

    distance = round(((a_X - b_X)**2 + (a_Y - b_Y)**2)**0.5, 2)
    print(f'\033[32m Расстояние между точками A({a_X};{a_Y}) и B({b_X};{b_Y}) равно {distance}')
    print('\033[37m')
print()