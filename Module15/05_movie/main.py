films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
fav_films = []
my_film = input('Введите название фильма (или "end"): ')
while my_film != 'end':
    not_film = True
    for film in films:
        if my_film == film:
            fav_films.append(my_film)
            print('Фильм добвлен в список любимых.')
            not_film = False
            break
    if not_film:
        print('Этого фильма нет на сайте.')
    my_film = input('Введите название фильма (или "end"): ')
print('Список любимых фильмов:', fav_films)
