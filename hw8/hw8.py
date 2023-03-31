# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить 
# на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано 
# положительное целое число). Протестируем функцию на файле «article.txt»

# Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово, 
# имеющее максимальную длину (или список слов, если таковых несколько).

import codecs


def read_last(lines, file):
    data = open(file, 'r', encoding='utf8')
    s_list = data.readlines()
    if len(s_list) < lines or lines < 0:
        data.close()
        print('Неправильное количество строк...')
        return
    for i in range(-lines, 0):
        print(s_list[i])
    data.close()
    print('------------')
    return


def longest_words(file):
    data = open(file, 'r', encoding='utf8')
    s_list = data.readlines()
    data.close()
    
    max_len = len(max(s_list, key=len))

    data = open('result.txt', 'w', encoding='utf8')
    data.writelines(filter(lambda s: len(s) == max_len, s_list))
    data.close()


read_last(3, 'article.txt')
longest_words('article.txt')