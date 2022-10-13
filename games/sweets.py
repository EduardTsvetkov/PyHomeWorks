# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""
 
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
 
def choosing_players():
    print("Введите количество игроков (1 или 2):")
    while True:
        print("1 - игра с компьютером")
        print("2 - игра с другим игроком")
        players = input("-> ")
        if players == "1":
            pl1 = input("Введите Ваше имя: ") 
            pl2 = "Компьютер"
            break
        elif players == "2":
            pl1 = input("Введите имя первого игрока: ") 
            pl2 = input("Введите имя второго игрока: ") 
            break
        else:
            print("\033[31mВы ввели неправильное число!...\033[37m")
 
    if players == 1:
        print("С каким компьютером Вы будете играть?")
    while True:
        print("0 - игра с обычным ботом")
        print("1 - игра с 'умным' ботом")
        smart = input("-> ")
        if smart in ["0", "1"]:
            break
        print("\033[31mВы ввели неправильное число!...\033[37m")
 
    result = (int(smart), pl1, pl2)
    return result




 
print()
while make_choice("Поиграем в конфетки? "):
    print()
    total_sweets = 2021
    max_sweets = 28
    players = choosing_players()
 
    print(players[1], players[-1], ["smart" if players[0] else "no smart"])
 
    print()