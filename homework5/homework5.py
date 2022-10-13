
# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""

# 3. Создайте программу для игры в ""Крестики-нолики"".

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Входные и выходные данные хранятся в отдельных текстовых файлах.


import my_function as my
 
def string_cleaning(inp_text, inp_str: str) -> str:
    """Функция удаляет из текста слова, содержащую указанный набор символов"""
    my_list = inp_text.split()
    # l = []
    # for x in my_list:
    #     if inp_str not in x:
    #         l.append(x)
    # result = ' '.join(l)
 
    result = ' '.join(list(filter(lambda x: inp_str not in x, my_list)))
    return result
 
def coding_word_RLE(inp_word: str) -> str:
    """Функция возвращает закодированное RLE слово или строку"""
    result = ''
    saved_c = ''
    count = 1
 
    if not inp_word: 
        return ""
    elif len(inp_word) == 1:
        return "1" + inp_word
 
    for c in inp_word:
        if c == saved_c:
            count += 1
        else:
            if saved_c:
                while count > 9:
                    result += "9" + saved_c
                    count -= 9
                result += str(count % 9) + saved_c
            saved_c = c    
            count = 1
            
    while count > 9:
        result += "9" + saved_c
        count -= 9
    result += str(count % 9) + saved_c
 
    return result
 
def decoding_word_RLE(inp_word: str) -> str:
    """Функция возвращает раскодированное RLE слово или строку"""
    result = ""
    l = []
    if not inp_word: 
        return ""
    elif len(inp_word) == 2:
        return inp_word[1] * int(inp_word[0])
 
    for i in range(1, len(inp_word), 2):
        l.append(inp_word[i] * int(inp_word[i - 1]))
 
    result = ''.join(l) 
    return result   
 
print()
while my.make_choice("Решаем задачу 1 (удаление слов из текста),"):
    print()
    input_file = open("input_text.txt", "r")
    my_text = input_file.read()
    input_file.close()
    
    print("Исходный текст (из файла input_text.txt): ")
    print(my_text)
 
    outp_text = string_cleaning(my_text, "abc")
    
    print()
    print("Текст без слов с 'abc' (записан в файл output_text.txt)")
    print(outp_text)
 
    output_file = open("output_text.txt", "w")
    output_file.write(outp_text)
    output_file.close()
 
    print()
print()
 
print()
while my.make_choice("Решаем задачу 4 (RLE)? "):
    print()
    inp_string = "aaadsdfbbbb  x erttyuuu   seeeeeeeeeeeeeeeeeeee z qwertttttttttt"
    coded_string = coding_word_RLE(inp_string)
    print("Исходная строка:")
    print(inp_string)
    print("Закодированая строка:")
    print(coded_string)
    print("Раскодированная строка:")
    print(decoding_word_RLE(coded_string))
    print()
print()