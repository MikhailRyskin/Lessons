import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    my_res = requests.get('http://www.columbia.edu/~fdc/sample.html')

    h3_text = []
    if my_res.status_code == 200:
        html_doc = BeautifulSoup(my_res.text, features='html.parser')
        list_of_values = html_doc.find_all('h3')
        # TODO, предлагаю попробовать подобрать правильное регулярное выражение
        #  и решить с использованием метода findall модуля re
        #  В таком случае, импорт модуля bs4 и цикл получатся лишними =)
        for content in list_of_values:
            h3_text.append(content.text)
            print(content.text)
    print(h3_text)
