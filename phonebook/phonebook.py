
import my_function as my
 
# creating a .txt file to store contact details 
filename = "phonebook.txt" 
myfile = open(filename, "a") 
myfile.close 
 

 
# defining search function         
def search_contact(): 
    searchname = input( "Введите фамилию, имя или номер телефона (полностью или частично): ").upper()
    myfile = open(filename, "r+") 
    contact_string = myfile.readlines() 
      
    found = False 
    for line in contact_string: 
        if searchname in line: 
            print( "Искомый контакт:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print(f"Искомый контакт '{searchname}' не найден.") 
 
 

def add_contact(): 
    lastname = input( "Введите фамилию: ").upper()
    firstname = input( "Введите имя: ").upper() 
    phone_num = input( "Введите номер телефона: ") 
    comment  = input( "Введите комментарий: ").upper()
    contact  = f"{lastname};{firstname};{phone_num};{comment}" 
    myfile = open(filename, "a") 
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
        myfile = open(filename, "r+") 
        contacts = myfile.read() 
        if len(contacts) == 0: 
            print( "Телефонная книга пуста...") 
        else: 
            print(contacts) 
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