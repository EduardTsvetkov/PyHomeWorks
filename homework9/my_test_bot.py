import telebot.types
from telebot import TeleBot

bot = TeleBot('5531697465:AAGRub4W8iidGkotLZmvqTA7rlCt-nC3SQE')


def summator(text: str):
    lst = text.split()
    if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
        return str(int(lst[0]) + int(lst[1]))
    return "Это некорректный запрос!"


@bot.message_handler(commands=['log'])
def hello(msg: telebot.types.Message):
 bot.send_message(chat_id=msg.from_user.id ,
 text='Лог программы\newcoiywgecowegcouwefoyewfov')
 bot.send_document(chat_id=msg.from_user.id , document=open('TestBot.log', 'rb'))
 
 
@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    file == bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
 
 
@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Справка")
 
 
@bot.message_handler(commands=['summator'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=sum_items, message=msg)
 
 
def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))
 
 
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f"Вы ввели: {msg.text}")
 

bot.polling()
