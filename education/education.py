
def get_int(request: str) -> int:
    """Функция возвращает целое число, введенное с клавиатуры"""
    while (True):
        n = input(request)
        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)
        print('\033[31mЭто не целое число!\033[37m')


def check_access(log, pas: str) -> bool:
    """Функция проверяет соответствие логина и пароля пользователя"""
    with open('users.txt', "r", encoding="utf-8") as users_file:
        users_list = users_file.readlines() 
        for user in users_list:
            l = user.split(";")
            if log == l[0] and  pas == l[1]:
               return True
    return False


def display_menu(category: int) -> int:
    """Функция выводит на экран меню, в зависимости от категории пользователя"""    
    if category == 1:
        print("1. Показать ДЗ по предметам") 
        print("2. Добавить ДЗ по предметам") 
        print("3. Показать ДЗ по студентам") 
        print("4. Оценить ДЗ студента")
        print("5. Добавить ДЗ")
        print("6. ") 
        print("0. Выход из программы") 
    elif category == 2:
        print("1. Показать ДЗ студента") 
        print("2. Показать оценки студента") 
        print("3. Показать долги студента")
        print("4. ")
        print("5. ") 
        print("0. Выход из программы") 
    else:
        print("1. Показать пользователей") 
        print("2. Добавить пользователя") 
        print("3. Удалить пользователя")
        print("0. Выход из программы") 

    return get_int("Введите номер пункта меню: ") + category * 10




#-------------------------------------------------------
login = input("Введите Ваш логин: ")
password = input("Введите Ваш пароль: ")

flag = check_access(login, password)
attempt_counter = 3
while not flag and attempt_counter:
    print("Указанная комбинация логин/пароль отсутствует!")
    print(f"Повторите ввод (осталось попыток - {attempt_counter}).")
    login = input("Введите Ваш логин: ")
    password = input("Введите Ваш пароль: ")
    flag = check_access(login, password)
    attempt_counter -= 1
if not flag:
    print("Вы не авторизованы в программе!")
else:
    with open('users.txt', "r", encoding="utf-8") as users_file:
        users_list = users_file.readlines() 
        for user in users_list:
            l = user.split(";")
            if login == l[0]:
                user_name = l[2]
                user_category = int(l[3])
                print(f"Добро пожаловать {user_name}!\n")

print(user_name, user_category)


while flag:
    choise = display_menu(user_category)

    if choise == 11:
        print("Вызов 1. Показать ДЗ по предметам") 
    elif choise == 12:
        print("Вызов 2. Добавить ДЗ по предметам") 
    elif choise == 13:
        print("Вызов 3. Показать ДЗ по студентам") 
    elif choise == 14:
        print("Вызов 4. Оценить ДЗ студента")
    elif choise == 15:    
        print("Вызов 5. Добавить ДЗ")
    elif choise == 16:
        print("Вызов 6. ") 
    elif choise == 21:
        print("Вызов 1. Показать ДЗ студента") 
    elif choise == 22:
        print("Вызов 2. Показать оценки студента") 
    elif choise == 23:
        print("Вызов 3. Показать долги студента")
    elif choise == 24:
        print("Вызов 4. ")
    elif choise == 31:
        print("Вызов 1. Показать пользователей") 
    elif choise == 32:
        print("Вызов 2. Добавить пользователя") 
    elif choise == 33:
        print("Вызов 3. Удалить пользователя")
    elif not (choise % 10):
        break
    else:
        print("Вы ввели несуществующий пункт меню!")




print("Всего доброго!")
print()