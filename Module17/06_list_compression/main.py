n = int(input('Введите кол-во чисел в списке: '))
origin_list = []
for i in range(1, n + 1):
    print('Ведите', i, 'число:', end=' ')
    num = input()
    origin_list.append(num)
print('Исходный список:', origin_list)
new_list = [n for n in origin_list if n != '0']
null_numbers = len(origin_list) - len(new_list)
new_list += '0' * null_numbers
print('"Сжатый" список:', new_list)
new_list = new_list[:(len(new_list) - null_numbers)]
print('Список без 0:', new_list)
