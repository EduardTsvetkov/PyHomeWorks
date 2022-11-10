from genericpath import exists
import os.path
import my_function as my
from telebot import TeleBot
import telebot.types

bot = TeleBot('5531697465:AAGRub4W8iidGkotLZmvqTA7rlCt-nC3SQE')

filename = "phonebook.txt" 
myfile = open(filename, "a", encoding="utf-8") 
myfile.close()

search_flag = False
export_flag = False





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


  


def write_contacts_list(input_list):
    myfile = open(filename, "a", encoding="utf-8") 
    for s in input_list:
        if ";" not in s:
            continue
        myfile.write(s.upper()) 
    myfile.close()    
    print(f"Контакт(ы) добавлен(ы)!") 


#------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Просмотр")
    btn2 = telebot.types.KeyboardButton("Поиск")
    btn3 = telebot.types.KeyboardButton("Импорт")
    btn4 = telebot.types.KeyboardButton("Экспорт")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id=message.from_user.id, text="Привет! Я, телефонный справочник.", reply_markup=markup)


#@bot.message_handler(content_types=['text'])
@bot.message_handler()
def func(message):
    global search_flag
    
    if (message.text == "Просмотр"):
        bot.send_message(chat_id=message.from_user.id, text="Просмотр контактов")
        bot.register_next_step_handler(callback=display_contacts_list, message=message)
   
    elif (message.text == "Поиск"):
        search_flag = True
        bot.send_message(chat_id=message.from_user.id, text="Введите строку для поиска")
    elif search_flag:
        search_flag = False
        bot.send_message(chat_id=message.from_user.id, text=f"Ищем {message.text}")
        bot.register_next_step_handler(callback=search_contact, message=message)

    elif (message.text == "Экспорт"):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Формат csv")
        btn2 = telebot.types.KeyboardButton("Формат txt")
        back = telebot.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id=message.from_user.id, text="Укажите формат", reply_markup=markup)
    elif(message.text == "Формат csv") or (message.text == "Формат txt"):
        bot.send_message(chat_id=message.from_user.id, text="Экспорт данных")
        bot.register_next_step_handler(callback=export_data, message=message)
    elif (message.text == "Назад"):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Просмотр")
        btn2 = telebot.types.KeyboardButton("Поиск")
        btn3 = telebot.types.KeyboardButton("Импорт")
        btn4 = telebot.types.KeyboardButton("Экспорт")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)
    elif (message.text == "Импорт"):    
        bot.send_message(chat_id=message.from_user.id, text="тут будет импорт")
    else:
        bot.send_message(chat_id=message.from_user.id, text="На такую комманду я не запрограммирован..")
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Просмотр")
        btn2 = telebot.types.KeyboardButton("Поиск")
        btn3 = telebot.types.KeyboardButton("Импорт")
        btn4 = telebot.types.KeyboardButton("Экспорт")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)




def display_contacts_list(message: telebot.types.Message):
    global search_flag
    bot.send_message(chat_id=message.from_user.id, text="Имеющиеся контакты")

    myfile = open(filename, "r+", encoding="utf-8") 
    contacts = myfile.readlines()
    myfile.close()
    if len(contacts) == 0: 
        print( "Телефонная книга пуста...")
    else:
        bot.send_message(chat_id=message.from_user.id, text="Фамилия Имя; Телефон; Описание")   
    
        for s in contacts:
            l = s[:-1].split(";")
            bot.send_message(chat_id=message.from_user.id, text=f"{l[0]} {l[1]}  {l[2]}  {l[3]}")
    search_flag = False
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Просмотр")
    btn2 = telebot.types.KeyboardButton("Поиск")
    btn3 = telebot.types.KeyboardButton("Импорт")
    btn4 = telebot.types.KeyboardButton("Экспорт")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)


def search_contact(message: telebot.types.Message): 
    searchname = message.text.upper()
    myfile = open(filename, "r", encoding="utf-8") 
    contacts_list = myfile.readlines() 
    myfile.close()      
    
    found = []
    for line in contacts_list: 
        if searchname in line: 
            found.append(line)
            
    if len(found):
        bot.send_message(chat_id=message.from_user.id, text=f"Контакты, содержащие {searchname}: ") 
        for s in found:
            l = s[:-1].split(";")
            bot.send_message(chat_id=message.from_user.id, text=f"{l[0]} {l[1]}  {l[2]}  {l[3]}")   
    else:
        bot.send_message(chat_id=message.from_user.id, text=f"Искомый текст '{searchname}' не найден.") 
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Просмотр")
    btn2 = telebot.types.KeyboardButton("Поиск")
    btn3 = telebot.types.KeyboardButton("Импорт")
    btn4 = telebot.types.KeyboardButton("Экспорт")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)


def export_data(message: telebot.types.Message):
    myfile = open(filename, "r+", encoding="utf-8")
    contacts = myfile.readlines()
    if len(contacts) == 0:
        bot.send_message(chat_id=message.from_user.id, text="Телефонная книга пуста...")
    elif message.text == "Формат csv":
        file_for_export = "phone_export.csv"
        export_csv(file_for_export, contacts)
    elif message.text == "Формат txt":
        file_for_export = "phone_export.txt"
        export_utf(file_for_export, contacts)  
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Просмотр")
    btn2 = telebot.types.KeyboardButton("Поиск")
    btn3 = telebot.types.KeyboardButton("Импорт")
    btn4 = telebot.types.KeyboardButton("Экспорт")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_document(chat_id=message.from_user.id, document=open(file_for_export, 'rb'))
    bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)


def export_csv(path, input_list):
    exp_file = open(path, "w", encoding="cp1251")  # для Excel (csv c разделителями ";")
    for s in input_list:
        exp_file.write(s) 
    exp_file.close()    
#    print(f"Контакты экспортированы!")     


def export_utf(path, input_list):
    exp_file = open(path, "w", encoding="utf-8")  # файл UNICODE поля по строкам
    for contact in input_list:
        item_list = contact[:-1].split(";")
        
        for item in item_list:
                exp_file.write(item + "\n")   
        exp_file.write("\n")          
           
    exp_file.close()    
#    print(f"Контакты экспортированы!")   






bot.polling(none_stop=True)

# print("ТЕЛЕФОННАЯ КНИГА")
# while True:
#     print( "Меню") 
#     print("1. Показать контакты") 
#     print("2. Добавить контакт") 
#     print("3. Экспорт")
#     print("4. Импорт")
#     print("5. Поиск контакта") 
#     print("6. Выход") 
#     choice = my.get_int("Введите номер пункта меню: ") 
#     if choice == 1: 
#         print("Имеющиеся контакты: ")
#         myfile = open(filename, "r+", encoding="utf-8") 
#         contacts = myfile.readlines()
#         if len(contacts) == 0: 
#             print( "Телефонная книга пуста...") 
#         else: 
#             display_contacts_list(contacts)
#         myfile.close()
#         input("Нажмите Enter для перехода в меню...") 
#     elif choice == 2: 
#         add_contact() 
#         input("Нажмите Enter для перехода в меню...") 
#     elif choice == 3:
#         myfile = open(filename, "r+", encoding="utf-8") 
#         contacts = myfile.readlines()
#         if len(contacts) == 0: 
#             print( "Телефонная книга пуста...") 
#         else: 
#             export_data(contacts)
#         myfile.close()
#         input("Нажмите Enter для перехода в меню...") 
#     elif choice == 4:
#         import_data()
#         input("Нажмите Enter для перехода в меню...") 
#     elif choice == 5: 
#         search_contact() 
#         input("Нажмите Enter для перехода в меню...") 
#     elif choice == 6: 
#         break
#     else: 
#         print("Вы выбрали несуществующий пункт меню.") 
#         input("Нажмите Enter для перехода в меню...") 


# print("ВСЕГО ДОБРОГО!!!") 
# print  ()