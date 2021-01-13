n = int(input('Кол-во элементов: '))
origin_list = []
for _ in range(n):
    element = int(input('Введите элемент: '))
    origin_list.append(element)
shift = int(input('Сдвиг: '))
print('Изначальный список:', origin_list)
shift_list = []
ind = -shift
for _ in range(n):
    shift_list.append(origin_list[ind])
    ind += 1
print('Сдвинутый список: ', shift_list)
