
import emojis as em
from random import randint, random

 
def make_choice(question: str) -> bool:  # определяем выполнять (повторять) задачу или переходить к следующей    print(question)
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
 
def choosing_players() -> tuple:
    """Функция возвращает кортеж с флагом (кто играет) и списком игроков"""
    pl1 = input("Введите имя первого игрока: ") 
    pl2 = input("Введите имя второго игрока: ") 
    smart = "-1"  # флаг -1, что игра с человеком
    result = (int(smart), pl1, pl2)
    return result
 
def choosing_first_move(pls: tuple) -> int:
    """Функция возвращает"""
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


def print_board(b: dict):
    print("Свободные ячейки обозначены цифрами,")
    print(f"занятые - обозначены {em.encode(':negative_squared_cross_mark:')} и {em.encode(':o2:')} соответственно.")
    print(f'''
     |     |   
 {b[1]}  | {b[2]}  | {b[3]}  
-----+-----+-----
 {b[4]}  | {b[5]}  | {b[6]} 
-----+-----+-----
 {b[7]}  | {b[8]}  | {b[9]} 
     |     |   
''')
      
 
def check_win(d: dict) -> bool:
    win_combin = ["123", "456", "789",
               "147", "258", "369",
               "159", "357"]
    for s in win_combin:
        if d[int(s[0])] == d[int(s[1])] == d[int(s[2])]:
            return True
    return False


print()
while make_choice("Поиграем в 'Крестики-нолики'? "):
    
    print()
    players = choosing_players()   # у первого игрока индекс 1, у второго индекс -1
                                   # индекс 0 определяет с кем игра (-1 - с человеком, 0 - простой бот, 1 - умный бот)
 
    print(f" Играют: {players[1]} (у него {em.encode(':negative_squared_cross_mark:')})")
    print(f"         {players[-1]} (у него {em.encode(':o2:')} ).")
 
    winner_flag = False
    simbols = {1: em.encode(':negative_squared_cross_mark:').strip(), -1: em.encode(':o2:') + ' '}
    board = {1: em.encode(':one:') + ' ', 2: em.encode(':two:') + ' ', 3: em.encode(':three:'), 
             4: em.encode(':four:') + ' ', 5: em.encode(':five:') + ' ', 6: em.encode(':six:'),
             7: em.encode(':seven:') + ' ', 8: em.encode(':eight:') + ' ', 9: em.encode(':nine:')}

    current_player = choosing_first_move(players)
    print(f"Первый ход у игрока по имени {players[current_player]} он играет {simbols[current_player]}")
    print_board(board)
    
    for _ in range(9):
        if players[0] == -1 or current_player == 1:  # ход человека
            print(f"Ход игрока по имени {players[current_player]} (играет '{simbols[current_player]}').")
            cell_num = get_int("Какую ячейку выбираем? ")

            while cell_num < 1 or cell_num > 9 or board[cell_num] == simbols[1] or board[cell_num] == simbols[-1]:
                print(f"Свободной ячейки с номером {cell_num} нет")
                cell_num = get_int("Какую ячейку выбираем? ")
        board[cell_num] = simbols[current_player]
        print_board(board)
        if check_win(board):
            winner_flag = True
            break
        current_player *= -1          

    if winner_flag:
        print(f"Выиграл игрок по имени {players[current_player]}!!!")
        print("Поздравляем!!!")
        print(em.encode(':trophy:'))
    else:
        print("Боевая ничья!")
    print()

    