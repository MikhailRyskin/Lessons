import requests
from bs4 import BeautifulSoup
import re


if __name__ == '__main__':
    my_res = requests.get('http://www.columbia.edu/~fdc/sample.html')

    if my_res.status_code == 200:
        # h3_text = []
        #         # html_doc = BeautifulSoup(my_res.text, features='html.parser')
        #         # list_of_values = html_doc.find_all('h3')
        #         # for content in list_of_values:
        #         #     h3_text.append(content.text)
        #         #     print(content.text)
        #         # print(h3_text)
        #  предлагаю попробовать подобрать правильное регулярное выражение
        #  и решить с использованием метода findall модуля re
        #  В таком случае, импорт модуля bs4 и цикл получатся лишними =)
        html_doc_1 = my_res.text
        list_h3 = re.findall(r'>(.+)</h3>', html_doc_1)
        print(list_h3)


#  пожалуйста, обратите внимание, цикл со списком h3_text и срезами получился лишним.
#  Стоит подобрать регулярное выражение таким образом, чтобы findall вернул нам список нужных значений.
#  Остальной код предлагаю из решения убрать =)