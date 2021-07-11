import requests
from bs4 import BeautifulSoup
import re


if __name__ == '__main__':
    my_res = requests.get('http://www.columbia.edu/~fdc/sample.html')

    if my_res.status_code == 200:
        h3_text = []
        html_doc = BeautifulSoup(my_res.text, features='html.parser')
        list_of_values = html_doc.find_all('h3')
        for content in list_of_values:
            h3_text.append(content.text)
            print(content.text)
        print(h3_text)
        #  предлагаю попробовать подобрать правильное регулярное выражение
        #  и решить с использованием метода findall модуля re
        #  В таком случае, импорт модуля bs4 и цикл получатся лишними =)
        h3_text_re = []
        html_doc_1 = my_res.text
        list_h3 = re.findall(r'>.+</h3>', html_doc_1)
        for elem in list_h3:
            content = elem[1:-5]
            h3_text_re.append(content)
            print(content)
        print(h3_text_re)
