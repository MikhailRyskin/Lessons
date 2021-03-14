def all_numbers(number):
    if number > 1:
        all_numbers(number - 1)
    print(number, end=' ')


my_number = int(input('Введите число: '))
all_numbers(my_number)

# зачёт!
# зачёт!
