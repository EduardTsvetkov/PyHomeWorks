import telebot.types
from telebot import TeleBot

bot = TeleBot('5531697465:AAGRub4W8iidGkotLZmvqTA7rlCt-nC3SQE')


def is_number(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка числом"""
    inp_str.replace(".", "", 1)
    if inp_str.isdigit() or (inp_str[0] == '-' and inp_str[1:].isdigit()):
        return True
    return False


def is_complex(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка комплексным числом"""
    if inp_str[-1] != "i":
        return False
    l = inp_str.replace("i", "").split("+")
    if len(l) == 2 and is_number(l[0]) and is_number(l[1]):
        return True
    else:
        return False

    
def is_math_operation(inp_str: str) -> bool:
    """Функция проверяет, является ли полученная строка матеметическим оператором"""
    operators = ["+", "-", "*", "/"]
    if inp_str in operators:
        return True
    return False


def check_elements(inp_str: str) -> str:
    result = ''
    complex_list = []
    inp_list = inp_str.split()
    if len(inp_list) != 3 or not is_math_operation(inp_list[1]):
        return "Неправильный формат ввода данных. Для получения справки введите /help"
    if is_number(inp_list[0]) and is_number(inp_list[2]):
        result = calc_rational_elements(inp_list)
        return result   
    elif is_complex(inp_list[0]) and is_complex(inp_list[2]):
        complex_list.append(inp_list[0].replace("i", "").split("+"))
        complex_list.append(inp_list[1])
        complex_list.append(inp_list[2].replace("i", "").split("+"))
        result = calc_complex_elements(complex_list)
        return result
    else:    
        return "2. Вы ввели неправильную задачу. Для получения справки введите /help"


def calc_rational_elements(inp_list: list) -> str:
    """Функция считает пример и возвращает результат"""
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

    return f"{a} {inp_list[1]} {b} = {str(result)}"


def calc_complex_elements(inp_list: list) -> str:
    """Функция считает пример и возвращает результат"""
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
    return s.replace(".0+", "+").replace("+-", "-").replace(".0i", "i")



@bot.message_handler(commands=["start"])
def start(msg, res=False):
    start_text = "Я бот-калькулятор. Напиши мне задачу \n(число, пробел, оператор, пробел, число): "
    """Функция, обрабатывающая команду /start"""
    bot.send_message(chat_id=msg.from_user.id, text=start_text)


@bot.message_handler(commands=['help'])
def help_command(msg: telebot.types.Message):
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
    bot.send_message(chat_id=msg.from_user.id, text=help_text)


# @bot.message_handler()
# def calc(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
#     bot.register_next_step_handler(callback=calc_items, message=msg)
 
 
# def calc_items(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=calc_elements(msg.text))


@bot.message_handler()
def calc(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=check_elements(msg.text))

bot.polling()