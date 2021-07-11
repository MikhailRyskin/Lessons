import re

if __name__ == '__main__':
    phone_numbers = ['9999999999', '999999-999', '99999x9999', '8675432123', '865432176', '6543213458']
    phone_template = re.compile(r'[8,9]\d{9}')
    for number_id, phone in enumerate(phone_numbers):
        print(f'{number_id + 1} номер:', end=' ')
        if re.match(phone_template, phone):
            print('всё в порядке')
        else:
            print('не подходит')
