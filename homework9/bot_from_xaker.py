
import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('5531697465:AAGRub4W8iidGkotLZmvqTA7rlCt-nC3SQE')


# @bot.message_handler(commands=["start"])
# def start(m, res=False):
#     """Функция, обрабатывающая команду /start"""
#     bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     """Получение сообщений от юзера и отправка его же"""
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)