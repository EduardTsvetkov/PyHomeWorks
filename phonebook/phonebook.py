
import my_function as my
 

filename = "phonebook.txt" 
myfile = open(filename, "a", encoding="utf-8") 
myfile.close 
 

def display_contacts_list(input_list):
    print("{0:>25} {1:>15} {2:>15}".format("Фамилия Имя |", "Телефон |", "Описание"))
    print("-" * 59)
    for s in input_list:
        l = s[:-1].split(";")
        print("{0:>25} {1:>15} {2:>15}".format(f"{l[0]} {l[1]} |", f"{l[2]} |", l[3]))


def search_contact(): 
    searchname = input( "Введите фамилию, имя или номер телефона (полностью или частично): ").upper()
    myfile = open(filename, "r", encoding="utf-8") 
    contacts_list = myfile.readlines() 
      
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
    lastname = input( "Введите фамилию: ").upper()
    firstname = input( "Введите имя: ").upper() 
    phone_num = input( "Введите номер телефона: ") 
    comment  = input( "Введите комментарий: ").upper()
    contact  = f"{lastname};{firstname};{phone_num};{comment}\n" 
    myfile = open(filename, "a", encoding="utf-8") 
    myfile.write(contact) 
    print(f"Контакт {lastname} {firstname} добавлен!") 
 


print("ТЕЛЕФОННАЯ КНИГА")
while True:
    print( "Меню") 
    print("1. Показать контакты") 
    print("2. Добавить контакт") 
    print("3. Экспорт")
    print("4. Импорт")
    print("5. Поиск контакта") 
    print("6. Выход") 
    choice = my.get_int("Введите номер пункта меню: ") 
    if choice == 1: 
        print("Имеющиеся контакты: ")
        myfile = open(filename, "r+", encoding="utf-8") 
        contacts = myfile.readlines()
        if len(contacts) == 0: 
            print( "Телефонная книга пуста...") 
        else: 
            display_contacts_list(contacts)
        myfile.close 
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 2: 
        add_contact() 
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 3:
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 4:
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 5: 
        search_contact() 
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 6: 
        break
    else: 
        print("Вы выбрали несуществующий пункт меню.") 
        input("Нажмите Enter для перехода в меню...") 


print("ВСЕГО ДОБРОГО!!!") 
print  ()