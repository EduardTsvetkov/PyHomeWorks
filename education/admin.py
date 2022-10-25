import my_function as my


def display_users_list(input_list: list):
    """Функция выводит список пользователей"""
    print("{:10} {:3} {:10} {:3} {:25} {:3} {:15}".format("Логин", " | ", "Пароль", " | ",
                                                            "Фамилия Имя", " | ",  "Категория"))
    print("-" * 70)
    for s in input_list:
        s.replace("\n", "")
        l = s[:-1].split(";")
        if l[3] == "1":
            l[3] = "Преподаватель"
        if l[3] == "2":
            l[3] = "Студент"    
        if l[3] == "3":
            l[3] = "Администратор"
        print("{:10} {:3} {:10} {:3} {:25} {:3} {:15}".format(l[0], " | ", l[1], " | ", 
                                                                l[2], " | ", l[3]))


def write_users_list(input_list):
    myfile = open("users.txt", "a", encoding="utf-8") 
    for s in input_list:
        if ";" not in s:
            continue
        myfile.write(s) 
    myfile.close()    
    print(f"Пользователи добавлены!")   


def add_users(): 
    d = my.file_to_dct("users.txt", "utf-8", ";")
    result = []
    print("Введите данные нового пользователя")
    while True:
        while True:
            login = input( "логин: ")
            if login in d:
                print("Такой логин существует.")
            else:
                break
        password = input( "пароль: ")
        lastname = input( "фамилия: ").upper()
        firstname = input( "имя: ").upper() 
        user_category = ""
        print("Категория: 1 - преподаватель")
        print("           2 - студент")
        print("           3 - администратор")
        while user_category not in ["1", "2", "3"]: 
            user_category = input( "категория (от 1 до 3): ") 
        
        result.append(f"{login};{password};{lastname} {firstname};{user_category}\n") 
        if not my.make_choice("Добавим еще одного пользователя? "):
            break
    write_users_list(result)                                                               


def del_user():
    login = input("Введите логин пользователя, которого хотите удалить: ")
    d = my.file_to_dct("users.txt", "utf-8", ";")
    if login in d:
        user_name = d[login][1]
        if my.make_choice(f"Вы действительно хотите удалить {user_name}? "):
            del d[login]
            print(f"Пользователь {user_name} удален!")
            my.dct_to_file("users.txt", "w", "utf-8",";", d)
    else:
        print(f"Пользователя с логином {login} не существует!")
