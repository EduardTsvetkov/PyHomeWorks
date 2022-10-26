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
        print("1. Показать ДЗ") 
        print("2. Добавить ДЗ") 
        print("3. Показать долги студентов") 
        print("4. Оценить ДЗ студента")
        print("0. Выход из программы") 
    elif category == 2:
        print("1. Показать ДЗ") 
        print("2. Показать оценки студента") 
        print("3. Показать долги студента")
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
        print()
        print("Имеющиеся задания: ")
        hw_file = open("hw.txt", "r", encoding="utf-8") 
        hw = hw_file.readlines()
        if len(hw) == 0: 
            print( "Список заданий пустой...") 
        else: 
            teacher.display_hw_list(hw)
        hw_file.close()
        print()
        input("Нажмите Enter для перехода в меню...")
    elif choise == 12:
        print()
        teacher.add_hw()
        input("Нажмите Enter для перехода в меню...")  
    elif choise == 13:
        teacher.get_debts()
        input("Нажмите Enter для перехода в меню...")  
    elif choise == 14:
        teacher.put_rating()
        print()
        input("Нажмите Enter для перехода в меню...") 

    elif choise == 21:
        print()
        print("Имеющиеся задания: ")
        hw_file = open("hw.txt", "r", encoding="utf-8") 
        hw = hw_file.readlines()
        if len(hw) == 0: 
            print( "Список заданий пустой...") 
        else: 
            teacher.display_hw_list(hw)
        hw_file.close()
        print()
        input("Нажмите Enter для перехода в меню...") 
    elif choise == 22:
        print()
        print(f"Оценки студента {user_name}:\n")
        teacher.get_student_scores(login)
        print()
        input("Нажмите Enter для перехода в меню...") 
    elif choise == 23:
        print()
        teacher.get_student_debts(user_name)
        print()
        input("Нажмите Enter для перехода в меню...")
        
    elif choise == 31:
        print()
        print("Имеющиеся пользователи: ")
        users_file = open("users.txt", "r", encoding="utf-8") 
        contacts = users_file.readlines()
        if len(contacts) == 0: 
            print( "Список пользователей пустой...") 
        else: 
            admin.display_users_list(contacts)
        users_file.close()
        print()
        input("Нажмите Enter для перехода в меню...")
    elif choise == 32:
        print()
        admin.add_users()
        print()
        input("Нажмите Enter для перехода в меню...") 
    elif choise == 33:
        print()
        admin.del_user()
        print()
        input("Нажмите Enter для перехода в меню...")
    elif not (choise % 10):
        break
    else:
        print()
        print("Вы ввели несуществующий пункт меню!")
        print()
print() 
print("Всего доброго!")
print()