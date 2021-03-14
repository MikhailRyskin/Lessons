def fibonacci(number):
    if number == 1 or number == 2:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)


my_number = int(input('Введите позицию числа в ряде Фибоначчи: '))

print('Число:', fibonacci(my_number))

# зачёт!
