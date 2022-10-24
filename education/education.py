import my_function as my
import teacher
import admin


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
    """Функция выводит на экран меню, в зависимости от категории пользователя, и возвращает его выбор"""    
    if category == 1:
        print("1. Показать ДЗ по предметам") 
        print("2. Добавить ДЗ по предметам") 
        print("3. Показать ДЗ по студентам") 
        print("4. Оценить ДЗ студента")
        print("5. ")
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

    return my.get_int("Введите номер пункта меню: ") + category * 10




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
    users_list = my.file_to_dct("users.txt", "utf-8", ";")
    user_name = users_list[login][1]
    user_category = int(users_list[login][2])
    print(f"Добро пожаловать {user_name}!\n")


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
        print("Вызов 5. ")
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
        print("Имеющиеся пользователи: ")
        users_file = open("users.txt", "r", encoding="utf-8") 
        contacts = users_file.readlines()
        if len(contacts) == 0: 
            print( "Список пользователей пустой...") 
        else: 
            admin.display_users_list(contacts)
        users_file.close()
        input("Нажмите Enter для перехода в меню...")
    elif choise == 32:
        admin.add_users()
        input("Нажмите Enter для перехода в меню...") 
    elif choise == 33:
        admin.del_user()
        input("Нажмите Enter для перехода в меню...")
    elif not (choise % 10):
        break
    else:
        print("Вы ввели несуществующий пункт меню!")




print("Всего доброго!")
print()