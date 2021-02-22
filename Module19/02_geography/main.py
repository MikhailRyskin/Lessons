number_countries = int(input('Кол-во стран: '))  #
cities_dict = {}
print('Введите страну и 3 города этой страны.')
# Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i", "n" и "j" не отражают =)
#  исправил названия переменных

for country_index in range(1, number_countries + 1):
    country_cities = input(f'{country_index} страна: ').split()
    for ind in range(1, 4):
        cities_dict[country_cities[ind]] = country_cities[0]
print('Введите названия 3-х разных городов.')
for city_index in range(1, 4):
    city = input(f'{city_index} город: ')
    country = cities_dict.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')

# зачёт!
