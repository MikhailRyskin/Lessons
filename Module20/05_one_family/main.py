people = {
    ('Иванова', 'Кира'): 50,
    ('Петров', 'Иван'): 40,
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Петрова', 'Ольга'): 38,
    ('Сидоров', 'Павел'): 10,
    }
total_age = 0
inp_surname = input('Введите фамилию: ').title()
inp_fem_surname = inp_surname + 'а'
for surname_name, age in people.items():
    surname = surname_name[0]
    if surname == inp_surname or surname == inp_fem_surname:
        total_age += age
print('Общий возраст: ', total_age)

# TODO, пожалуйста добавьте вывод ФИО и возвраста людей, чьи фамилии были указаны во вводе пользователя.