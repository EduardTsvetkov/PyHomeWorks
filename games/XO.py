# 3. Создайте программу для игры в ""Крестики-нолики"".


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
    # print("Введите количество игроков (1 или 2):")
    # while True:
    #     print("1 - игра с компьютером")
    #     print("2 - игра с другим игроком")
    #     players = input("-> ")
    #     if players == "1":
    #         pl1 = input("Введите Ваше имя: ") 
    #         pl2 = "Бот"
    #         break
    #     elif players == "2":
    pl1 = input("Введите имя первого игрока: ") 
    pl2 = input("Введите имя второго игрока: ") 
    #         break
    #     else:
    #         print("\033[31mВы ввели неправильное число!...\033[37m")
    smart = "-1"  # флаг -1, что игра с человеком
    # if players == "1":
    #     print("С каким ботом Вы будете играть?")
    #     while True:
    #         print("0 - игра с обычным ботом")
    #         print("1 - игра с 'умным' ботом")
    #         smart = input("-> ")
    #         if smart in ["0", "1"]:
    #             break
    #         print("\033[31mВы ввели неправильное число!...\033[37m")
    
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
    print("зантые - обозначены 'X' и 'O' соответственно.")
    print(f'''
    |   |   
  {b[1]} | {b[2]} | {b[3]}  
----+---+----
  {b[4]} | {b[5]} | {b[6]} 
----+---+----
  {b[7]} | {b[8]} | {b[9]} 
    |   |   
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
 
    print(f" Играют: {players[1]} (у него 'X') и {players[-1]} (у него 'O').")
 
    winner_flag = False
    simbols = {1: "X", -1: "O"}
    board = {1: "1", 2: "2", 3: "3", 
             4: "4", 5: "5", 6: "6",
             7: "7", 8: "8", 9: "9"}

    current_player = choosing_first_move(players)
    print(f"Первый ход у игрока по имени {players[current_player]} он играет {simbols[current_player]}")
    print_board(board)
    
    for _ in range(9):
        if players[0] == -1 or current_player == 1:  # ход человека
            print(f"Ход игрока по имени {players[current_player]} (играет '{simbols[current_player]}').")
            cell_num = get_int("Какую ячейку выбираем? ")

            while cell_num < 1 or cell_num > 9:
                print(f"Свободной ячейки с номером {cell_num} нет")
                cell_num = get_int("Какую ячейку выбираем? ")
        # elif current_player == -1 and players[0] == 1:  # ходит второй игрок (умный бот)
        #     get_smart_move()  # считаем умный ход бота
 
        # elif current_player == -1 and players[0] == 0:  # 0 - ходит второй игрок (обычный бот)
        #     get_dump_move()
        board[cell_num] = simbols[current_player]
        print_board(board)
        if check_win(board):
            winner_flag = True
            break
        current_player *= -1          

    if winner_flag:
        print(f"Выиграл игрок по имени {players[current_player]}")
        print("Поздравляем!!!")
    else:
        print("Боевая ничья!")
    print()

    