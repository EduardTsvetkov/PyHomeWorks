from genericpath import exists
import os.path
import my_function as my
 

filename = "phonebook.txt" 
myfile = open(filename, "a", encoding="utf-8") 
myfile.close()
 

def display_contacts_list(input_list):
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


# набросок... необходимо сделать контроль (добавление, дубли), отчет
# проверку наличия \n
def import_data():
    print("Выберите формат данных: csv (данные в одной строке, разделители ';', кодировка Windows)")
    print("Выберите формат данных: txt (данные по строкам, разделители пустая строка, кодировка UTF-8)")
    data_format = 0
    file_type = "csv"
    while data_format < 1 or data_format > 2:
        data_format = my.get_int("Введите 1 для csv, 2 для txt: ")
    
    if data_format == 2:
        file_type = "txt"
    
    file_for_import = ""
    while not os.path.exists(file_for_import):
        file_for_import = input(f"Введите имя файла {file_type}: ")

    if data_format == 1:
        import_csv(file_for_import)
    elif data_format == 2:
        import_utf(file_for_import)


def export_data(input_list):
    print("Выберите формат данных: csv (данные в одной строке, разделители ';', кодировка Windows)")
    print("Выберите формат данных: txt (данные по строкам, разделители пустая строка, кодировка UTF-8)")
    data_format = 0
    file_type = "csv"
    while data_format < 1 or data_format > 2:
        data_format = my.get_int("Введите 1 для csv, 2 для txt: ")
    
    if data_format == 2:
        file_type = "txt"
    
    file_for_export = input(f"Введите имя файла {file_type}: ")

    if data_format == 1:
        export_csv(file_for_export, input_list)
    elif data_format == 2:
        export_utf(file_for_export, input_list)

def import_csv(path):  
    import_file = open(path, "r", encoding="cp1251")  # файл из Excel (csv c разделителями ";")
    import_list = import_file.readlines() 
    import_file.close()
    display_contacts_list(import_list)
    if my.make_choice("Импортируем указанные данные?: "):
        write_contacts_list(import_list)
        print("Импорт данных выполнен!")
    else:
        print("Импортирование данных отменено!")

def import_utf(path): 
    result = []
    import_file = open(path, "r", encoding="utf-8")  # файл UNICODE поля по строкам
    import_list = import_file.readlines() 
    import_file.close()
    ind = 0
    import_contact = ["","","",""]
    for s in import_list:
        if s == "\n":
            result.append(';'.join(import_contact) + "\n")
            import_contact = ["","","",""]
            ind = 0
        else:
            import_contact[ind] = s[:-1]
            ind += 1
    result.append(';'.join(import_contact) + "\n")

    display_contacts_list(result)
    if my.make_choice("Импортируем указанные данные?: "):
        write_contacts_list(result)
        print("Импорт данных выполнен!")
    else:
        print("Импортирование данных отменено!")


def export_csv(path, input_list):
    exp_file = open(path, "w", encoding="cp1251")  # для Excel (csv c разделителями ";")
    for s in input_list:
        exp_file.write(s) 
    exp_file.close()    
    print(f"Контакты экспортированы!")     


def export_utf(path, input_list):
    exp_file = open(path, "w", encoding="utf-8")  # файл UNICODE поля по строкам
    for contact in input_list:
        item_list = contact[:-1].split(";")
        
        for item in item_list:
                exp_file.write(item + "\n")   
        exp_file.write("\n")          
           
    exp_file.close()    
    print(f"Контакты экспортированы!")     


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
        myfile.close()
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 2: 
        add_contact() 
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 3:
        myfile = open(filename, "r+", encoding="utf-8") 
        contacts = myfile.readlines()
        if len(contacts) == 0: 
            print( "Телефонная книга пуста...") 
        else: 
            export_data(contacts)
        myfile.close()
        input("Нажмите Enter для перехода в меню...") 
    elif choice == 4:
        import_data()
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