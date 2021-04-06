import random


random_exceptions = [ValueError, ZeroDivisionError, FileNotFoundError, TypeError, IndexError]
lucky_number = 0

with open('numbers.txt', 'w') as file:
    while lucky_number < 777:
        user_number = int(input('Введите число: '))
        lucky_number += user_number
        dice = random.randint(1, 13)
        if dice == 13:
            raise random.choice(random_exceptions)
        file.write(f'{str(user_number)}\n')  # TODO, str лишнее, т.к. используем f-строки =)
print(f'Удалось набрать {lucky_number}!!!')

# TODO, предлагаю попробовать создать функцию, внутри которой будем вызывать исключения
#  или возвращать рандомное число и запускать её в основном цикле.
#  Ошибку необходимо вызывать внутри этой функции.
#  В таком случае, стоит ловить ошибки внутри основного цикла.
