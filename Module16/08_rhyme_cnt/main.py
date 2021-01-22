people_num = int(input('Кол-во человек: '))
people_list = list(range(1, people_num + 1))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек')

start_poz = 1
while len(people_list) > 1:
    print('\nТекущий круг людей:', people_list)
    print('Начало счёта с номера', people_list[start_poz - 1])
    choice_man = start_poz + (number - 1)
    curr_size = len(people_list)
    while choice_man > curr_size:
        choice_man = choice_man - curr_size
    print('Выбывает человек под номером', people_list[choice_man - 1])
    people_list.remove(people_list[choice_man - 1])
    curr_size = len(people_list)
    start_poz = choice_man
    while start_poz > curr_size:
        start_poz -= curr_size
print('\nОстался человек под номером', *people_list)
