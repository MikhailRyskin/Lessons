def super_zip(data1, data2):
    data1_list = list(data1)
    data2_list = list(data2)
    zip_list = [(data1_list[ind], data2_list[ind]) for ind in range(min(len(data1_list), len(data2_list)))]
    return zip_list


data_1 = 'abcde'
data_2 = (9, 8, 7, 6, 5, 4, 3)
data_3 = {32, 34, 36, 38, 40, 42, 44}
data_4 = [1, 2, 3, 4, 5, 6]
data_5 = {'Иванов': 22, 'Петров': 33}

zip_list_1 = super_zip(data_1, data_2)
print(*zip_list_1)
zip_list_2 = super_zip(data_3, data_4)
print(*zip_list_2)
zip_list_3 = super_zip(data_5, data_2)
print(*zip_list_3)
