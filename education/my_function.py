from random import randint, uniform

def make_choice(question: str) -> bool:
    """Возвращаем ответ на вопрос: True - если 'да', False - если 'нет'"""  
    yes_answers = ['y', 'yes', 'д', 'да']
    no_answers = ['n', 'no', 'н', 'нет']
    print(question)
    while (True):
        choice = input("Ведите y,yes,д,да если 'ДА' либо n,no,н,нет если 'НЕТ': ").lower()
        if choice in yes_answers:
            return True
        elif choice in no_answers:
            return False


def get_int(request: str) -> int:
    """Функция возвращает целое число, введенное с клавиатуры"""
    while (True):
        n = input(request)
 
        if n != '' and (n.isdigit() or (n[0] == '-' and n[1:].isdigit())):
            return int(n)
 
        print('\033[31mЭто не целое число!\033[37m')


def fill_list_random_int() -> list[int]:
    """Функция заполняет список случайными целыми числами"""
    size = 0
    while size < 1:
        size = get_int('Введите размер заполняемого списка (больше 0): ')
    min_n = get_int('Введите минимальное значение элементов списка: ')
    max_n = min_n - 1
    while max_n < min_n:
        max_n = get_int(f'Введите максимальное значение элементов списка (больше {min_n}): ')
    result = []
    for _ in range(size):
        result.append(randint(min_n, max_n))
    return result


def fill_list_random_float(prec: int) -> list[float]:
    """Функция заполняет список случайными вещественными числами"""
    size = 0
    while size < 1:
        size = get_int('Введите размер заполняемого списка (больше 0): ')
    min_n = get_int('Введите минимальное значение элементов списка: ')
    max_n = min_n - 1
    while max_n < min_n:
        max_n = get_int(f'Введите максимальное значение элементов списка (больше {min_n}): ')
    result = []
    for _ in range(size):
        result.append(round(uniform(min_n, max_n), prec))
    return result


def file_to_dct(path: str, cp: str, sep: str) -> dict:
    """Функция читает файл с разделителями в словарь:
    первое значение идет в ключ, следующие в список"""
    result = {}
    with open(path, "r", encoding=cp) as f:
        for line in f:
            items = line.replace("\n", "").split(sep)
            result[items[0]] = items[1:]

    return result        


def dct_to_file(path: str, mode: str, cp: str, sep: str, input_dct: dict):
    """Функция читает файл с разделителями в словарь:
    первое значение идет в ключ, следующие в список"""
    result = ""
    with open(path, mode, encoding=cp) as f:
        for key, value in input_dct.items():
            result = f"{key}{sep}{sep.join(value)}\n"
            f.write(result)

        