import requests
from bs4 import BeautifulSoup
import re



def currency(curr_name):
    url = 'https://www.cbr.ru/currency_base/daily/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    name_of_value_list = []
    for name_of_value in soup.find_all('tr', class_= ''):
        name_of_value_list.append(name_of_value.text)
    
    currency_string = str()
    for j in name_of_value_list:
        if curr_name in j:
            currency_string += j
    if not currency_string:
        return ('Вы указали неверную валюту')
    else:        

        currency_elements = []
        temp_str = str()
        for i in currency_string:
            if i != '\n':
                temp_str +=i
            elif i == '\n':
                currency_elements.append(temp_str)
                temp_str = str()

        tmp2 = currency_elements[5]
        tmp3 = str()
        for i in tmp2:
            if i !=',':
                tmp3 +=i
            if i ==',':
                tmp3 +='.'

        value_of_currency = float(currency_elements[3])/float(tmp3)
        value_of_currency = round(value_of_currency,2)
        
        result = f"{currency_elements[4]} ({currency_elements[2]}) \nКурс к рублю {currency_elements[3]} / {tmp3}"

        return (result)