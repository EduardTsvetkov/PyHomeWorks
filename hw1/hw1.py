# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no



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


def get_sum_digit(n: int) -> int:
    """Функция принимает число в виде строки и возвращает сумму его цифр"""
    result = 0
    chars_list = list(str(n))
    for c in chars_list:
        if c.isdigit():
            result += int(c)

    return result


def paper_crane(s: int) -> int:
    """Функция возвращает x, решение уравнения 6x=s"""
    n = int(s)
    if n % 6 == 0:
        return n // 6    
    else:
        return -1  


def check_chocolate(choco: list[int]) -> bool:
    """Функция проверяет, можно ли одним разломом отломить нужное количество кубиков"""
    if choco[0] * choco[1] > choco[2] and (choco[2] % choco[0] == 0 or choco[2] % choco[1] == 0):
        return True
    return False


#------------------------------------------------------
print()
while make_choice("Выполняем задачу 2 (сумма цифр)? "):
    print()
    num = get_int("Введите число: ")
    sum_digit = get_sum_digit(num)
    print(f'В числе {num} сумма цифр {sum_digit}')
    print()

#------------------------------------------------------
print()
while make_choice("Выполняем задачу 4 (журавлики)? "):
    print()
    num = get_int("Введите количество сделанных журавликов: ")
    cranes = paper_crane(num)
    
    if cranes == -1:
        print(f'С числом {num} задача не решается')
    else:    
        print(f'Петя и Серёжа сделали журавликов по {cranes} ,')
        print(f'а Катя {cranes * 4}.')
    print()

#------------------------------------------------------
print()
while make_choice("Выполняем задачу 6 (счастливый билет)? "):
    print()
    num = input("Введите номер билета (шестизначное число): ")
    if len(num) != 6:
        print('Вы ввели не 6 цифр!')
        continue
    
    if get_sum_digit(int(num[0:3])) == get_sum_digit(int(num[3:6])):
        print(f'Билет {num} "счастливый"')
    else:
        print(f'Билет {num} не "счастливый"')
    print()


#------------------------------------------------------
print()
while make_choice("Выполняем задачу 8 (шоколад)? "):
    print()
    print('Введите размер шоколоадки (в кубиках):')
    n = get_int('Ширина ')
    m = get_int('Высота ')
    k = get_int('Сколько отломить? ')

    if check_chocolate([n, m, k]):
        print(f'От шоколадки {n}х{m} можно отломать {k} кубиков')
    else:
        print(f'От шоколадки {n}х{m} нельзя отломать {k} кубиков')
    print()
