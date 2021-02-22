max_num = int(input('Введите максимальное число: '))
possible_numbers = set()
while True:
    proposed_numbers = set()
    answer_str = input('Нужное число есть среди вот этих чисел: ').title()
    if answer_str == 'Помогите!':
        break
    else:
        proposed_numbers = set(answer_str.split())
        answer = input('Ответ Артёма: ').title()
        if answer == 'Да':
            possible_numbers.update(proposed_numbers)
        elif answer == 'Нет':
            possible_numbers.difference_update(proposed_numbers)
print('Артём мог загадать следующие числа:', *possible_numbers)

# зачёт!
