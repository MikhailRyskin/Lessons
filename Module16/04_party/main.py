def if_exist(guest, guests_list):
    for element in guests_list:
        if element == guest:
            return True
    return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    action = input('Гость пришел или ушел? ')
    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    elif action == 'ушел':
        guest = input('Имя гостя: ')
        if if_exist(guest, guests):
            print('Пока,', guest, '!')
            guests.remove(guest)
        else:
            print('Нет такого гостя.')
    elif action == 'пришел':
        guest = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', guest, '!')
            guests.append(guest)
        else:
            print('Прости,', guest, ', но мест нет.')
    else:
        print('Неверный ввод!')

# зачёт!
