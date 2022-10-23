
def get_int(request: str) -> int:
    """Функция возвращает целое число, введенное с клавиатуры"""
    while (True):
        n = input(request)
        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)
        print('\033[31mЭто не целое число!\033[37m')


def check_access(log, pas: str) -> bool:
    """Функция проверяет соответствие логина и пароля пользователя"""
    if log == "admin" and  pas == "admin":
        return True
    return False


def display_menu(category: int) -> int:
    """Функция выводит на экран меню, в зависимости от категории пользователя"""    
    if category == 1:
        print("1. Показать ДЗ по предметам") 
        print("2. Добавить ДЗ по предметам") 
        print("2. Показать ДЗ по студентам") 
        print("3. Оценить ДЗ студента")
        print("4. Добавить ДЗ")
        print("5. ") 
        print("6. Выход из программы") 
    elif category == 2:
        print("1. Показать ДЗ студента") 
        print("2. Показать оценки студента") 
        print("3. Показать долги студента")
        print("4. ")
        print("5. ") 
        print("6. Выход из программы") 
    else:
        print("1. Показать пользователей") 
        print("2. Добавить пользователя") 
        print("3. Удалить пользователя")
        print("6. Выход из программы") 

    return get_int("Введите номер пункта меню: ") 




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
    print("Добро пожаловать {}!\n")

while flag:
    if display_menu(3) == 6:
        break




print("Всего доброго!")