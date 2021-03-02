input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(zip(input_list[::2], input_list[1::2]))
print('Новый список:', new_list)

new_list_1 = []
for index in range(0, len(input_list), 2):
    new_list_1.append((input_list[index], input_list[index + 1]))
print('Новый список:', new_list_1)

# зачёт!
