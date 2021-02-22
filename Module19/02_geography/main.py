n = int(input('Кол-во стран: '))
cities_dict = {}
print('Введите страну и 3 города этой страны.')
for i in range(1, n + 1):
    country_cities = input(f'{i} страна: ').split()
    for ind in range(1, 4):
        cities_dict[country_cities[ind]] = country_cities[0]
print('Введите названия 3-х разных городов.')
for j in range(1, 4):
    city = input(f'{j} город: ')
    country = cities_dict.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')
