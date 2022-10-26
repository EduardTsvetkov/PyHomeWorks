 
import my_function as my

def display_hw_list(input_list: list):
    """Функция выводит список заданий"""
    print("{:>3} {:3} {:15} {:3} {:25}".format("№", " | ", "Предмет", " | ", "Задание"))
    print("-" * 60)
    for s in input_list:
        l = s[:-1].split(";")
        print("{:>3} {:3} {:15} {:3} {:25}".format(l[0], " | ", l[1], " | ", l[2]))


def write_hw_list(input_list):
    myfile = open("hw.txt", "a", encoding="utf-8") 
    for s in input_list:
        if ";" not in s:
            continue
        myfile.write(s) 
    myfile.close()    
    print(f"Задания добавлены!")   


def add_hw(): 
    d = my.file_to_dct("hw.txt", "utf-8", ";")
    n = 0
    for key in d:
        if int(key) > n:
            n = int(key)
    n += 1
    result = []
    while True:
        print(f"Введите новое задание (№ {n}): ")
        subject = input( "предмет: ").upper()
        homework = input( "задание: ").upper()
        result.append(f"{n};{subject};{homework}\n") 
        if not my.make_choice("Добавим еще одного пользователя? "):
            break
        n += 1
    write_hw_list(result)


def display_scores_list(input_list: list):
    """Функция выводит список оценок"""
    hw_dct = my.file_to_dct("hw.txt", "utf-8", ";")
    print("{:>3} {:3} {:15} {:3} {:30} {:3} {:^5}".format("ДЗ", " | ", "Предмет", " | ",
                                               "Задание", " | ", "Оценка"))
    print("-" * 70)
    for s in input_list:
        l = s[:-1].split(";")
        l.append(hw_dct[l[0]][0])
        l.append(hw_dct[l[0]][1])
#        print(l)
        print("{:>3} {:3} {:15} {:3} {:30} {:3} {:^5}".format(l[0], " | ", l[3], " | ", l[4], " | ", l[2]))



def display_debts_list(input_list: list):
    """Функция выводит список оценок"""
    print("{:>3} {:3} {:15} {:3} {:30} {:3} {:25}".format("ДЗ", " | ", "Предмет", " | ",
                                                            "Задание", " | ", "Студент"))
    print("-" * 80)
    for s in input_list:
        l = s.split(";")
        print("{:>3} {:3} {:15} {:3} {:30} {:3} {:25}".format(l[0], " | ", l[1], " | ", 
                                                               l[2], " | ", l[4]))

def get_debts():
    hw_dct = my.file_to_dct("hw.txt", "utf-8", ";")
    users_dct = my.file_to_dct("users.txt", "utf-8", ";")
    students_dct = {}
    for key in users_dct:
        if users_dct[key][2] == "2":
            students_dct[key] = users_dct[key]

    result = []
    scores_file = open("scores.txt", "r", encoding="utf-8") 
    scores_list = scores_file.readlines()
    scores_file.close()
    for hw_key, hw_value in hw_dct.items():
        for students_key, students_value in students_dct.items():
            flag = True
            for s in scores_list:
                if f"{hw_key};{students_key}" in s:
                    flag = False
                    break
            if flag:
                result.append(f"{hw_key};{hw_value[0]};{hw_value[1]};{students_key};{students_value[1]}")
    
    display_debts_list(result)


def get_student_debts(name):
    hw_dct = my.file_to_dct("hw.txt", "utf-8", ";")
    users_dct = my.file_to_dct("users.txt", "utf-8", ";")
    
    for key in users_dct:
        if users_dct[key][2] != "2":
            continue
        if users_dct[key][1] == name: 
            login = key
            break
    else:
        print(f"Студента с именем {name} нет!")
        return (None, None)

    result = []
    debts_hw = []
    scores_file = open("scores.txt", "r", encoding="utf-8") 
    scores_list = scores_file.readlines()
    scores_file.close()
    for hw_key, hw_value in hw_dct.items():
        flag = True
        for s in scores_list:
            if f"{hw_key};{login}" in s:
                flag = False
                break
        if flag:
            result.append(f"{hw_key};{hw_value[0]};{hw_value[1]};{login};{name}")
            debts_hw.append(hw_key)
    
    display_debts_list(result)
    return (login, debts_hw)


def put_rating():
    student_name = input("Введите фамилию и имя студента: ").upper()
    student_login, hw_debts = get_student_debts(student_name)
    if student_login is None:
        return
    while True:
        hw = input("Введите номер ДЗ: ")
        if hw in hw_debts:
            break
        else:
            print("Такого задания без оценки нет.")
    while True:
        score = input("Введите оценку (от 1 до 5): ")
        if score in ["1", "2", "3", "4", "5"]:
            break

    s = f"{hw};{student_login};{score}\n"
    myfile = open("scores.txt", "a", encoding="utf-8") 
    myfile.write(s) 
    myfile.close()     
    print("Оценка поставлена.")
    get_student_scores(student_login)


def get_student_scores(login):
    scores_file = open("scores.txt", "r", encoding="utf-8") 
    scores = scores_file.readlines()
    scores_file.close()
    result = []
    for s in scores:
        if login in s:
            result.append(s)
    
    display_scores_list(result)

