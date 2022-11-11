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
    elif message.text == "csv":
        file_for_export = "phone_export.csv"
        export_csv(file_for_export, contacts)
    elif message.text == "txt":
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


def export_utf(path, input_list):
    exp_file = open(path, "w", encoding="utf-8")  # файл UNICODE поля по строкам
    for contact in input_list:
        item_list = contact[:-1].split(";")
        
        for item in item_list:
                exp_file.write(item + "\n")   
        exp_file.write("\n")          
           
    exp_file.close()    
   
#-------------------------------------------------------------

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Просмотр")
    btn2 = telebot.types.KeyboardButton("Поиск")
    btn3 = telebot.types.KeyboardButton("Экспорт")
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id=message.from_user.id, text="Привет! Я, телефонный справочник.", reply_markup=markup)


@bot.message_handler(content_types=['text'])
#@bot.message_handler()
def func(message):
    global search_flag
    
    if (message.text == "Просмотр"):
        bot.send_message(chat_id=message.from_user.id, text="Просмотр контактов")
        display_contacts_list(message)
   
    elif (message.text == "Поиск"):
        search_flag = True
        bot.send_message(chat_id=message.from_user.id, text="Введите строку для поиска")
    elif search_flag:
        search_flag = False
        bot.send_message(chat_id=message.from_user.id, text=f"Ищем {message.text}")
        search_contact(message)

    elif (message.text == "Экспорт"):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("csv")
        btn2 = telebot.types.KeyboardButton("txt")
        back = telebot.types.KeyboardButton("Назад")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id=message.from_user.id, text="Укажите формат", reply_markup=markup)
    elif(message.text == "csv") or (message.text == "txt"):
        bot.send_message(chat_id=message.from_user.id, text="Экспорт данных")
        export_data(message)
    elif (message.text == "Назад"):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Просмотр")
        btn2 = telebot.types.KeyboardButton("Поиск")
        btn3 = telebot.types.KeyboardButton("Импорт")
        btn4 = telebot.types.KeyboardButton("Экспорт")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)
    else:
        bot.send_message(chat_id=message.from_user.id, text="На такую комманду я не запрограммирован..")
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = telebot.types.KeyboardButton("Просмотр")
        btn2 = telebot.types.KeyboardButton("Поиск")
        btn3 = telebot.types.KeyboardButton("Импорт")
        btn4 = telebot.types.KeyboardButton("Экспорт")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=message.from_user.id, text="Выберите действие", reply_markup=markup)
    

bot.polling(none_stop=True)
