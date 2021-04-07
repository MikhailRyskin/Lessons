import random


def random_result():
    input_number = int(input('Введите число: '))
    dice = random.randint(1, 13)
    if dice == 3:
        raise random.choice(random_exceptions)
    else:
        return input_number


random_exceptions = [ValueError('ValueError'), ZeroDivisionError('ZeroDivisionError'),
                     FileNotFoundError('FileNotFoundError'), TypeError('TypeError'), IndexError('IndexError')]
lucky_number = 0

with open('numbers.txt', 'w') as file:
    while lucky_number < 777:
        try:
            user_number = random_result()
            lucky_number += user_number
            file.write(f'{user_number}\n')  # str лишнее, т.к. используем f-строки =)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError, IndexError) as exc:
            print('выпала случайная ошибка:', exc)
print(f'Удалось набрать {lucky_number}!!!')

#  предлагаю попробовать создать функцию, внутри которой будем вызывать исключения
#  или возвращать рандомное число и запускать её в основном цикле.
#  Ошибку необходимо вызывать внутри этой функции.
#  В таком случае, стоит ловить ошибки внутри основного цикла.

# зачёт!
