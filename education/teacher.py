# print("Вызов 1. Показать ДЗ по предметам") 
# print("Вызов 2. Добавить ДЗ по предметам") 
# print("Вызов 3. Показать ДЗ по студентам") 
# print("Вызов 4. Оценить ДЗ студента")


def display_users_list(input_list):
    print("{0:>25} {1:>15} {2:>15}".format("Фамилия Имя |", "Телефон |", "Описание"))
    print("-" * 59)
    for s in input_list:
        l = s[:-1].split(";")
        print("{0:>25} {1:>15} {2:>15}".format(f"{l[0]} {l[1]} |", f"{l[2]} |", l[3]))


def write_contacts_list(input_list):
    myfile = open(filename, "a", encoding="utf-8") 
    for s in input_list:
        if ";" not in s:
            continue
        myfile.write(s.upper()) 
    myfile.close()    
    print(f"Контакт(ы) добавлен(ы)!")     


def search_contact(): 
    searchname = input( "Введите фамилию, имя или номер телефона (полностью или частично): ").upper()
    myfile = open(filename, "r", encoding="utf-8") 
    contacts_list = myfile.readlines() 
    myfile.close()      
    
    found = []
    for line in contacts_list: 
        if searchname in line: 
            found.append(line)
            
    if len(found):
        print(f"Контакты, содержащие {searchname}: ") 
        display_contacts_list(found)   
    else:
        print(f"Искомый текст '{searchname}' не найден.") 
  

def add_contact(): 
    result = []
    while True:
        print("Введите данные нового контакта")
        lastname = input( "фамилия: ").upper()
        firstname = input( "имя: ").upper() 
        phone_num = ""
        while not phone_num.isdigit(): 
            phone_num = input( "номер телефона (только цифры, без +, (), -): ") 
        comment  = input( "комментарий: ")
        result.append(f"{lastname};{firstname};{phone_num};{comment}\n") 
        if not my.make_choice("Добавим еще один контакт? "):
            break
    write_contacts_list(result)