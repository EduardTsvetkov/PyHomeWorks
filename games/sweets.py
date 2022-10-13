# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""


from random import randint, random
from tkinter import Y


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
    """Функция возвращает целое число, введенное с клавиатуры"""
    while (True):
        n = input(request)
 
        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)
 
        print('\033[31mЭто не целое число!\033[37m')
 
def choosing_players():
    print("Введите количество игроков (1 или 2):")
    while True:
        print("1 - игра с компьютером")
        print("2 - игра с другим игроком")
        players = input("-> ")
        if players == "1":
            pl1 = input("Введите Ваше имя: ") 
            pl2 = "Бот"
            break
        elif players == "2":
            pl1 = input("Введите имя первого игрока: ") 
            pl2 = input("Введите имя второго игрока: ") 
            break
        else:
            print("\033[31mВы ввели неправильное число!...\033[37m")
    smart = "-1"  # флаг, что игра не с ботом
    if players == "1":
        print("С каким ботом Вы будете играть?")
        while True:
            print("0 - игра с обычным ботом")
            print("1 - игра с 'умным' ботом")
            smart = input("-> ")
            if smart in ["0", "1"]:
                break
            print("\033[31mВы ввели неправильное число!...\033[37m")
    
    result = (int(smart), pl1, pl2)
    return result


def choosing_first_move(pls: tuple) -> int:
    print("Выберите игрока с правом первого хода (введите 1, 2 или 3):")
    while True:
        print(f"1 - первым ходит {pls[1]}")
        print(f"2 - первым ходит {pls[-1]}")
        print(f"3 - случайный вбор")
        result = input("-> ")
        if result in ["1", "2", "3"]:
            break
        print("\033[31mВы ввели неправильное число!...\033[37m")
    if result == "1":
        return 1
    elif result == "2":
        return -1
    else:
        if randint(-1, 1) < 0:
            return -1
        else:    
            return 1
    return int(result)    


def smart_move(total_, max_: int) -> int:
    if total_ <= max_:
        return total_
    result = total_ % (max_ + 1)
    if result:
        return result
    return randint(1, max_) 

 
print()
while make_choice("Поиграем в конфетки? "):
    print()
    total_sweets = 85
    max_sweets = 28
    players = choosing_players()  # у первого игрока индекс 1, у второго индекс -1

    print(players)
    input()

    print(f" Играют: {players[1]} и {players[-1]}")

    current_player = choosing_first_move(players)
    print(f"Первый ход у игрока по имени {players[current_player]}")
    print(f"На столе лежат конфеты - {total_sweets} шт.")
    print(f"За один ход можно взять не более {max_sweets} конфет.")
    get_sweets = 0
    while total_sweets > 0:
        if players[0] == -1 or current_player == 1:
            print(f"Ход игрока по имени {players[current_player]}.")
            get_sweets = get_int("Сколько Вы берёте конфет? ")
            while get_sweets > min(total_sweets, max_sweets):
                print(f"Число должно быть от 1 до {min(total_sweets, max_sweets)}")
                get_sweets = get_int("Сколько Вы берёте конфет? ")
        elif current_player == -1 and players[0] == 1:  # ходит второй игрок (умный бот)
            get_sweets = smart_move(total_sweets, max_sweets)  # считаем умный ход бота

        elif current_player == -1 and players[0] == 0:  # 0 - ходит второй игрок (обычный бот)
            if total_sweets <= max_sweets:  # если игрок тормоз, то забираем всё... :-)
                get_sweets = total_sweets
            else:
                get_sweets = randint(1, max_sweets)  


        total_sweets -= get_sweets
        print(f"{players[current_player]} взял {get_sweets} кофет.")
        print(f"На столе осталось {total_sweets} конфет.")  
        print()

        current_player *= -1          
        
    print(f"Выиграл игрок по имени {players[current_player * -1]}")
    print()

print()
