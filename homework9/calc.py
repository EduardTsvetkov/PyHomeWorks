from datetime import datetime

import telebot.types
from telebot import TeleBot

bot = TeleBot('5531697465:AAGRub4W8iidGkotLZmvqTA7rlCt-nC3SQE')

with open("log.txt", "w", encoding='utf-8') as file:  # перезаписываем лог
    file.write(f'{datetime.now()}; бот запущен\n')

def write_log(inp_str: str):
    dt_now = datetime.now()
    with open("log.txt", "a", encoding='utf-8') as file:
        file.write(f'{dt_now}; {inp_str}\n')
    

def is_number(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка числом"""
    write_log(f'is_number получила {inp_str}')
    inp_str.replace(".", "", 1)
    if inp_str.isdigit() or (inp_str[0] == '-' and inp_str[1:].isdigit()):
        write_log('is_number результат True')
        return True
    write_log('is_number результат False')
    return False


def is_complex(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка комплексным числом"""
    write_log(f'is_complex получила {inp_str}')
    if inp_str[-1] != "i":
        write_log('is_complex результат False')
        return False
    l = inp_str.replace("i", "").split("+")
    if len(l) == 2 and is_number(l[0]) and is_number(l[1]):
        write_log('is_complex результат True')
        return True
    else:
        write_log('is_complex результат False')
        return False

    
def is_math_operation(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка матеметическим оператором"""
    write_log(f'is_math_operation получила {inp_str}')
    operators = ["+", "-", "*", "/"]
    if inp_str in operators:
        write_log('is_math_operation результат True')
        return True
    write_log('is_math_operation результат False')
    return False


def check_elements(inp_str: str) -> str:
    write_log(f'check_elements получила {inp_str}')
    result = ''
    complex_list = []
    inp_list = inp_str.split()
    if len(inp_list) != 3 or not is_math_operation(inp_list[1]):
        write_log('check_elements сообщает о неправильном формате')
        return "Неправильный формат ввода данных. Для получения справки введите /help"
    if is_number(inp_list[0]) and is_number(inp_list[2]):
        write_log(f'check_elements подсчет рациональных элементов {inp_list}')
        result = calc_rational_elements(inp_list)
        write_log(f'check_elements возврат рациональных вычислений {inp_list}')
        return result   
    elif is_complex(inp_list[0]) and is_complex(inp_list[2]):
        complex_list.append(inp_list[0].replace("i", "").split("+"))
        complex_list.append(inp_list[1])
        complex_list.append(inp_list[2].replace("i", "").split("+"))
        write_log(f'check_elements подсчет комплексных элементов {complex_list}')
        result = calc_complex_elements(complex_list)
        write_log(f'check_elements возврат комплексных вычислений {inp_list}')
        return result
    else:
        write_log('check_elements сообщает о неправильной задаче')    
        return "Вы ввели неправильную задачу. Для получения справки введите /help"


def calc_rational_elements(inp_list: list) -> str:
    """Функция считает пример и возвращает результат"""
    write_log(f'calc_rational_elements получено для подсчета {inp_list}')
    result = ''
    a, b = float(inp_list[0]), float(inp_list[2])
    if inp_list[1] == "+":
        result = a + b
    elif inp_list[1] == "-":
        result = a - b
    elif inp_list[1] == "*":
        result = a * b
    elif inp_list[1] == "/":
        result = a / b
    write_log(f'calc_rational_elements результат подсчета {result}')
    return f"{a} {inp_list[1]} {b} = {str(result)}"


def calc_complex_elements(inp_list: list) -> str:
    """Функция считает пример с комплексными числами и возвращает результат"""
    write_log(f'calc_complex_elements получено для подсчета {inp_list}')
    result = ''
    a, b = float(inp_list[0][0]), float(inp_list[0][1])
    c, d = float(inp_list[2][0]), float(inp_list[2][1])
    if inp_list[1] == "+":
        result = f"{a + c}+{b + d}i"
    elif inp_list[1] == "-":
        result = f"{a - c}+{b - d}i"
    elif inp_list[1] == "*":
        result = f"{a * c - b * d}+{a * d + b * c}i"
    elif inp_list[1] == "/":
        result = f"{(a * c + b * d) / (c**2 + d**2)}+{(c * b - a * d) / (c**2 + d**2)}i"
    s = f"{a}+{b}i {inp_list[1]} {c}+{d}i = {result}"
    write_log(f'calc_complex_elements результат подсчета {s}')
    return s.replace(".0+", "+").replace("+-", "-").replace(".0i", "i")


@bot.message_handler(commands=["start"])
def start(msg, res=False):
    write_log(f'@bot.message_handler(commands=["start"]) получено сообщение {msg.text}')
    start_text = "Я бот-калькулятор. Для получения справки введите /help "
    """Функция, обрабатывающая команду /start"""
    write_log('@bot.message_handler(commands=["start"]) отправлено приветственное сообщение')
    bot.send_message(chat_id=msg.from_user.id, text=start_text)


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
    write_log(f"@bot.message_handler(commands=['help']) получено сообщение {msg.text}")
    help_text = """
    Бот производит сложение, вычитание, умножение и деление двух чисел.
    Для этого операторы и знак операции указываются через пробел, например:
        2 + 2
        3.2 - 1.75
        -8 / -2
        2.5 * -3
    Комплексные числа указываются в формате a+bi (без пробелов), например:
        5+7i - 3+2i   
    """
    write_log("@bot.message_handler(commands=['help']) отправлено сообщение со справкой")
    bot.send_message(chat_id=msg.from_user.id, text=help_text)


# @bot.message_handler()
# def calc(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
#     bot.register_next_step_handler(callback=calc_items, message=msg)
 
 
# def calc_items(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=calc_elements(msg.text))


@bot.message_handler()
def calc(msg: telebot.types.Message):
    write_log(f'@bot.message_handler() получено сообщение {msg.text}')
    result = check_elements(msg.text)
    write_log(f'@bot.message_handler() отправлено сообщение {result}')
    bot.send_message(chat_id=msg.from_user.id, text=result)

bot.polling()