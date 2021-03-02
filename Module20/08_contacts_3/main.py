phone_book = {}
while True:
    choice = int(input('Выберите действие: 1 - добавить контакт, 2 - поиск человека по фамилии, 3 - выход: '))
    if choice == 3:
        print('Выход')
        break
    elif choice == 1:
        surname = input('Введите фамилию: ').title()
        name = input('Введите имя: ').title()
        person = (surname, name)
        if person not in phone_book:
            phone_number = int(input('Введите номер телефона: '))
            phone_book[person] = phone_number
        else:
            print('Контакт уже есть в книге')
        print(phone_book)
    elif choice == 2:
        surname = input('Введите фамилию: ').title()
        number_found = 0
        for person, phone_number in phone_book.items():
            if surname == person[0]:
                print(person, phone_number)
                number_found += 1
        if number_found == 0:
            print('Такой фамилии нет в телефонной книге')
    else:
        print('Неверное действие!')

# зачёт!
