 
# print("Вызов 4. Оценить ДЗ студента")
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

# доделать
def display_scores_list(input_list: list):
    """Функция выводит список оценок"""
    print("{:>3} {:3} {:15} {:3} {:25}".format("№", " | ", "Предмет", " | ",
                                                            "Задание"))
    print("-" * 60)
    for s in input_list:
        l = s[:-1].split(";")
        print("{:>3} {:3} {:15} {:3} {:25}".format(l[0], " | ", l[1], " | ", l[2]))



def display_debts_list(input_list: list):
    """Функция выводит список оценок"""
    print("{:>3} {:3} {:15} {:3} {:25} {:3} {:25}".format("ДЗ", " | ", "Предмет", " | ",
                                                            "Задание", " | ", "Студент"))
    print("-" * 75)
    for s in input_list:
        l = s.split(";")
        print("{:>3} {:3} {:15} {:3} {:25} {:3} {:25}".format(l[0], " | ", l[1], " | ", 
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
        return

    result = []
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
    
    display_debts_list(result)
    return login


def put_rating():
    student_name = input("Введите фамилию и имя студента: ").upper()
    student_login = get_student_debts(student_name)
    if student_login is None:
        return
    hw = input("Введите номер ДЗ: ")
    score = input("Введите оценку (от 1 до 5): ")
    s = f"{hw};{student_login};{score}\n"
    myfile = open("scores.txt", "a", encoding="utf-8") 
    myfile.write(s) 
    myfile.close()   

