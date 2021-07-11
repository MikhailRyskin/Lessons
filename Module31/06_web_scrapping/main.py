import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    my_res = requests.get('http://www.columbia.edu/~fdc/sample.html')

    h3_text = []
    if my_res.status_code == 200:
        html_doc = BeautifulSoup(my_res.text, features='html.parser')
        list_of_values = html_doc.find_all('h3')
        for content in list_of_values:
            h3_text.append(content.text)
            print(content.text)
    print(h3_text)
