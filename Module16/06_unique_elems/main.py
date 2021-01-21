list_1 = []
for _ in range(3):
    num = int(input('Число из первого списка: '))
    list_1.append(num)
print('Первый список:', list_1)
list_2 = []
for _ in range(7):
    num = int(input('Число из второго списка: '))
    list_2.append(num)
print('Второй список:', list_2)

list_1.extend(list_2)
ind = 0
while ind < len(list_1):
    curr_num = list_1[ind]
    count = list_1.count(curr_num)
    for _ in range(count - 1):
        list_1.remove(curr_num)
    ind += 1

print('\nНовый первый список с уникальными элементами:', list_1)
